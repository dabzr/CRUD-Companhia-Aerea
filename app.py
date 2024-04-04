from flask import Flask, jsonify, render_template, request, redirect, flash, session, url_for
from flask_session import Session
from .infra.repository import aeroporto_repository as aeroporto, assento_repository as assento, aviao_repository as aviao, passageiro_repository as passageiro, ticket_repository as ticket, user_repository as usuario, voos_repository as voo
from .infra.configs.connection import DBConnectionHandler
from sqlalchemy import MetaData
from sqlalchemy.orm import class_mapper
from functools import reduce
import json
app = Flask(__name__)
app.secret_key = "testando"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
feedback_message=""

def sqlalchemy_to_json(obj):
    # Obter os atributos do objeto
    attributes = obj.__dict__.copy()

    # Remover atributos que não são colunas do banco de dados
    mapper = class_mapper(obj.__class__)
    column_names = [column.key for column in mapper.columns]
    for attr in list(attributes.keys()):
        if attr not in column_names:
            del attributes[attr]

    # Converter o dicionário em JSON
    return json.dumps(attributes)

@app.route("/", methods=["GET", "POST"])
def login():
    global feedback_message
    session.clear()
    if request.method == "POST":
        if request.form["submit_button"] == "register_button":
            return render_template("register.html")
        if request.form["submit_button"] == "login_button":
            user = request.form.get("name").lower().strip()
            repo = usuario.UserRepository()
            users = repo.select()
            usuarioobj = list(filter(lambda x: x.user == user, users))[0]
            senha = request.form.get("password")
            if not usuarioobj or not usuario.verify_password(usuarioobj, senha):
                return render_template("index.html", feedback_message="Usuário ou senha inválidos.")
            if usuarioobj.user == "root":
                session["name"] = usuarioobj.user
                return redirect("/root")
            #return render_template("próxima página")

    return render_template("index.html", feedback_message=feedback_message)

@app.route("/register", methods=["GET", "POST"])
def register():
    global feedback_message
    usuario = request.form.get("name").lower().strip()
    senha = request.form.get("password")
    confirmar_senha = request.form.get("confirm_password")
    if not usuario or not senha:
        return render_template("register.html", error_message="Usuários e senhas não podem ser vazios")
    if senha == confirmar_senha:
        repo = UserRepository()
        repo.insert(usuario, senha)
        feedback_message = "Conta criada com sucesso!"
        return redirect("/")
    return render_template("register.html", error_message="As senhas precisam ser iguais")

@app.route("/root", methods=["GET", "POST"])
def root():
    tables = ['aeroporto', 'assento', 'aviao', 'passageiro', 'usuario', 'ticket', 'voo']
    table_repository = {'aeroporto':aeroporto.AeroportoRepository(),
                           'aviao': aviao.AviaoRepository(),
                            'assento': assento.AssentoRepository(),
                           'passageiro': passageiro.PassageiroRepository(),
                           'usuario': usuario.UserRepository(),
                           'ticket': ticket.TicketRepository(),
                           'voo': voo.VooRepository(),
                            }
    if request.method == "POST":
        if "ver" in request.form["submit_button"] or "adicionar" in request.form["submit_button"]:
            session['elemento'] = request.form["submit_button"]
            session['popupDisplay'] = 'block'
            lista_objects = [item for item in table_repository[request.form["submit_button"].split("_")[1]].select()]
            lista = [item.__dict__.copy() for item in lista_objects]
            session['lista'] = lista
            return redirect("/popup")
    if session.get("name") != "root":
        #db = DBConnectionHandler()
        #metadata = MetaData()
        #metadata.reflect(bind=db.get_engine())
        #listafoda = list(metadata.tables.keys())
        #tabelaaquiseria = metadata.tables.values()
        return render_template("root.html", elementos=tables)
    return redirect("/")

@app.route("/popup", methods=["GET", "POST"])
def popup():
    flash(session.get('elemento').split("_")[0])
    title = session.get('elemento').split("_")[0].capitalize()
    title += " " + session.get('elemento').split("_")[1].capitalize()
    flash(title)
    return redirect(url_for("root"))

if __name__ == '__main__':
    app.run(debug=True)


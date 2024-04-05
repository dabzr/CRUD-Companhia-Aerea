from flask import Flask, jsonify, render_template, request, redirect, flash, session, url_for
from flask_session import Session
from .forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

import json
app = Flask(__name__)
app.config["SECRET_KEY"] = "9e4976770668bf1ce6786245c1208161"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:senha@localhost:3306/dbaereo'
db = SQLAlchemy(app)
from .infra.repository.user_repository import UserRepository
from .infra.entities import Aeroporto, Assento, Aviao, Passageiro, Ticket, Usuario, Voo
with app.app_context():
    db.create_all()
Session(app)
feedback_message=""

@app.route("/", methods=["GET", "POST"])
def login():
    global feedback_message
    form = LoginForm()
    session.clear()
    if request.method == "POST":
        if form.submit_login.data:
            user = form.username.data.lower().strip()
            userObj = Usuario.Usuario.query.filter_by(user=user).first()
            senha = form.password.data.strip()
            if not userObj or not usuario.verify_password(userObj, senha):
                return render_template("index.html", feedback_message="Usuário ou senha inválidos.", form=form)
            if userObj.user == "root":
                session["name"] = userObj.user
                return redirect("/root")
            #return render_template("próxima página")
        if request.form["submit_button"] == "register":
            return redirect("/register")

    return render_template("index.html", feedback_message=feedback_message, form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    global feedback_message
    form = RegistrationForm()
    if request.method == "POST":
        user = form.username.data.lower().strip()
        senha = form.password.data.strip()
        confirmar_senha = form.confirm_password.data.strip()
        if not user or not senha:
            return render_template("register.html", error_message="Usuários e senhas não podem ser vazios", form=form)
        if senha == confirmar_senha:
            usuario = 
            Usuario.Usuario(user=user, senha=senha)
            db.session.add(usuario)
            db.session.commit()
            feedback_message = "Conta criada com sucesso!"
            return redirect("/")
    return render_template("register.html", error_message="As senhas precisam ser iguais", form=form)

@app.route("/root", methods=["GET", "POST"])
def root():

    if request.method == "POST":
        if "ver" in request.form["submit_button"] or "adicionar" in request.form["submit_button"]:
            session['elemento'] = request.form["submit_button"]
            session['popupDisplay'] = 'block'
            #lista_objects = [item for item in table_repository[request.form["submit_button"].split("_")[1]].select()]
            #lista = [item.__dict__.copy() for item in lista_objects]
            #session['lista'] = lista
            return redirect("/popup")
        if "insert" in request.form["submit_button"]:
            titulo = list(request.form.items())[-1][-1].split()[-1].lower()
            args = []
            lista_higienizada = list(session.get('lista')[0].keys())
            abc = []
            for i in lista_higienizada:
                if "instance" not in i and i != "id":
                    abc.append(i)
            lista_higienizada = abc
            for key in lista_higienizada:
                args.append(request.form.get(key))
            #table_repository[titulo].insert(*args)
    if session.get("name") == "root":
        #db = DBConnectionHandler()
        #metadata = MetaData()
        #metadata.reflect(bind=db.get_engine())
        #listafoda = list(metadata.tables.keys())
        #tabelaaquiseria = metadata.tables.items()
        #for i in tabelaaquiseria:
        #    print(i)
        #print(listafoda)
        #print(tabelaaquiseria)
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


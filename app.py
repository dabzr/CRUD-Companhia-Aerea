from flask import Flask, jsonify, render_template, request, redirect, flash, session
from flask_session import Session
from .infra.repository.user_repository import UserRepository, verify_password
from .infra.repository.aeroporto_repository import AeroportoRepository
from .infra.configs.connection import DBConnectionHandler
from sqlalchemy import MetaData
from functools import reduce
#from infra.repository.password import verify_password
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
feedback_message=""

@app.route("/", methods=["GET", "POST"])
def login():
    global feedback_message
    session.clear()
    if request.method == "POST":
        if request.form["submit_button"] == "register_button":
            return render_template("register.html")
        if request.form["submit_button"] == "login_button":
            user = request.form.get("name").lower().strip()
            repo = UserRepository()
            users = repo.select()
            usuario = list(filter(lambda x: x.user == user, users))[0]
            senha = request.form.get("password")
            if not usuario or not verify_password(usuario, senha):
                return render_template("index.html", feedback_message="Usuário ou senha inválidos.")
            if usuario.user == "root":
                session["name"] = usuario.user
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
    if session.get("name") == "root":
        db = DBConnectionHandler()
        metadata = MetaData()
        metadata.reflect(bind=db.get_engine())
        listafoda = list(metadata.tables.keys())
        tabelaaquiseria = metadata.tables.values()
        print(tabelaaquiseria)
        listafoda = ['aeroporto', 'assento', 'aviao', 'passageiro', 'usuario', 'ticket', 'voo']
        listaMAISquefoda={'aeroporto':AeroportoRepository()}
        print(listaMAISquefoda)
        return render_template("root.html")
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, jsonify, render_template, request, redirect, flash
from .infra.repository.user_repository import UserRepository, verify_password
from .infra.configs.connection import DBConnectionHandler
from sqlalchemy import MetaData
#from infra.repository.password import verify_password
app = Flask(__name__)

feedback_message=""

@app.route("/", methods=["GET", "POST"])
def login():
    global feedback_message
    if request.method == "POST":
        if request.form["submit_button"] == "register_button":
            return render_template("register.html")
        elif request.form["submit_button"] == "login_button":
            #pesquisar no banco de dados pelo usuário
            #caso exista
                #if user == root:
                    #return render_template
                #return render_template("próxima página")
            return render_template("index.html", feedback_message="Usuário ou senha inválidos")
    return render_template("index.html", feedback_message=feedback_message)

@app.route("/register", methods=["GET", "POST"])
def register():
    global feedback_message
    usuario = request.form.get("name")
    senha = request.form.get("password")
    confirmar_senha = request.form.get("confirm_password")
    #Lembrar de fazer as outras confirmações relacionadas a criação de conta ex: senha não nula, usuário não nulo...
    if senha == confirmar_senha:
        #repo = UserRepository()
        #repo.insert(usuario, senha)
        feedback_message = "Conta criada com sucesso!"
        return redirect("/")
    return render_template("register.html", error_message="As senhas precisam ser iguais")

@app.route("/root", methods=["GET", "POST"])
def root(): 
    return render_template("root.html")

if __name__ == '__main__':
    app.run(debug=True)


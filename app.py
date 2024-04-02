from flask import Flask, jsonify, render_template, request
from .infra.repository.user_repository import UserRepository, verify_password
#from infra.repository.password import verify_password
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["submit_button"] == "register_button":
            return render_template("register.html")
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    usuario = request.form.get("name")
    senha = request.form.get("password")
    confirmar_senha = request.form.get("confirm_password")
    if senha == confirmar_senha:
        repo = UserRepository()
        repo.insert(usuario, senha)
        return render_template("register.html")
    return render_template("register.html", error_message="As senhas precisam ser iguais")
    
if __name__ == '__main__':
    app.run(debug=True)


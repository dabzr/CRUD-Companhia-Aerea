from flask import Flask, jsonify, render_template, request
from infra.repository.user_repository import UserRepository
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    usuario = request.form.get("name")
    senha = request.form.get("input_password")
    repo = UserRepository(usuario, senha)
    # return render_template("index.html")



if __name__ == "__main__":
    teste = "opaaaa"
    senha_teste = "oo"
    repo = UserRepository()
    repo.insert(teste, senha_teste)
    print(repo.select())

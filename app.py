from flask import Flask, jsonify, render_template, request
from .infra.repository.user_repository import UserRepository, verify_password
#from infra.repository.password import verify_password
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    usuario = request.form.get("name")
    senha = request.form.get("input_password")
    repo = UserRepository()
    repo.insert(usuario, senha)
    return "hello world"

if __name__ == '__main__':
    app.run(debug=True)


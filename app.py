from flask import Flask, jsonify, render_template, request
from .infra.repository.user_repository import UserRepository, verify_password
#from infra.repository.password import verify_password
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("name")
        senha = request.form.get("input_password")
        repo = UserRepository()
        repo.insert(usuario, senha)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)


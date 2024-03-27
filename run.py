from infra.entities.Usuario import Usuario

cond = input("Você deseja logar ou criar usuário?[1/2] ")
user = input("Digite seu usuário: ")
senha = input("Digite sua senha:")
if(cond != 1):
    print("Criando usuário...")
    usuario = Usuario(user, senha)
else:



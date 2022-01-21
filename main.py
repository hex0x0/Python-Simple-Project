import mysql.connector


db = mysql.connector.connect(
    host="",
    user="lucas",
    password="12345",
    db="erp",
    charset="utf8mb4"
)

"""
cursor = db.cursor()

cursor.execute("SELECT * FROM cadastros")

ret = cursor.fetchall()

print(ret)
"""


def logarCadastrar(decisao):
    usuarioExistente = 0
    autenticado = False
    usuarioMaster = False

    if decisao == 1:
        nome=input("Digite seu nome:")
        senha=input("Digite sua senha:")

        for linha in ret:
            if nome == linha[0] and senha == linha[1]:
                if linha[2] == 1:
                    usuarioMaster = False
                elif linha[2] == 2:
                    usuarioMaster = True
                autenticado = True
            else:
                autenticado = False

        if not autenticado:
            print("Email ou senha errados")
    elif decisao == 2:
        print("Faca seu cadastro ")
        nome = input("Digite seu nome: ")
        senha = input("Digite sua senha: ")

        for linha in ret:
            if nome == linha[0] and senha == linha[1]:
                usuarioExistente = 1
        if usuarioExistente == 1:
            print("Usuário já está cadastrado!")
        elif usuarioExistente == 0:
            try:
                with db.cursor() as c:
                    c.execute('INSERT INTO cadastros(nome, senha, nivel) values(%s, %s, %s)', (nome, senha, 1))
                    db.commit()
                    print("Usuario cadastrado com sucesso!")
            except:
                print("Erro ao inserir os dados")

    return autenticado, usuarioMaster




autentico = False


while not autentico:
    decisao = int(input("(1) - Logar ou (2) - Cadastrar: "))
    try:
        with db.cursor() as c:
            c.execute("SELECT * FROM cadastros")
            ret = c.fetchall()

    except:
        print('Erro ao conectar no banco de dados')

    autentico, usuarioSupremo = logarCadastrar(decisao)



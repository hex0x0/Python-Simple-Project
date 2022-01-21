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
                print(linha[0] + "  - " +  linha[1] +  " - " + '{}'.format(linha[2]))
                if linha[2] == 1:
                    usuarioMaster = False
                elif linha[2] == 2:
                    usuarioMaster = True
                autenticado = True
                break
            else:
                autenticado = False

        if not autenticado:
            print("Email ou senha errados")
        else:
            print("Autenticado com sucesso")
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

def cadastrarProdutos():
    nome = input("Digite o nome do produto: ")
    ingredientes = input("Digite o ingrediente dos produtos: ")
    grupo = input("Digite o grupo deste produto: ")
    preco = float(input("Digite o preco do produto: "))

    """
        try pra tratar os erros decorrentes da conexão com o banco
    """
    try:
        with db.cursor() as c:
            c.execute("INSERT INTO produtos (nome, ingredientes, grupo, preco) values(%s, %s, %s, %s)", (nome, ingredientes, grupo, preco))
            db.commit()
            print("Produto cadastrado com sucesso!")
    except:
        print("Erro ao cadastrar produtos")

def listarProdutos():
    produtos = []

    try:
        with db.cursor() as c:
            c.execute("SELECT * from produtos")
            produtosCadastrados = c.fetchall()
    except:
        print("Erro ao conectar com o banco")

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

if autentico:
    print("Bem vindo!")

    """
    usuarioSupremo = True
    Cadastra apenas se for admin do banco
    """
    decisaoUsuario = 1


    while decisaoUsuario != 0:
        decisaoUsuario = int(input("Sair (0) ------ Cadastrar Produtos (1) : "))


        if decisaoUsuario == 1:
            cadastrarProdutos()

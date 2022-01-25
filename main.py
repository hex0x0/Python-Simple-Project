import mysql.connector
import matplotlib.pyplot as plt

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


    for p in produtosCadastrados:
        produtos.append(p)

    if len(produtos) != 0:
        for i in range(0, len(produtos)):
            print(produtos[i])
    else:
        print("Não existem produtos")

def excluirProduto():
    idDeletar=int(input("Digite o id do produto a ser deletado: "))

    try:
        with db.cursor() as c:
            c.execute("DELETE FROM produtos where id = {}".format(idDeletar))

    except:
        print("Erro ao conectar com o banco")

def listarPedidos():
    pedidos = []
    decision = 0

    while decision != 2:
        pedidos.clear()

        try:
            with db.cursor() as c:
                c.execute("SELECT * FROM pedidos")
                listaPedidos = c.fetchall()
        except:
            print("Conexao abortada")

def gerarRelatorios():
    nomeProdutos  = []
    nomeProdutos.clear()

    try:
        with db.cursor() as c:
            c.execute("SELECT * FROM produtos")
            produtos = c.fetchall()
    except:
        print("Erro ao fazer consulta")


    try:
        with db.cursor() as c:
            c.execute("SELECT * FROM estatisticavendido")
            vendidos = c.fetchall()
            print(vendidos)
    except:
        print("Erro ao fazer consulta")

    state = int(input("Digite 0 para sair, 1 para pesquisar por nome e 2 para pesquisar por grupo: "))

    if state == 1:
        dc = int(input("Digite um para pesquisar por preco e 2 por quantidade unitaria: "))
        if dc == 1:
            for i in produtos:
                nomeProdutos.append(i[1])

            print(nomeProdutos)
            valores = []
            valores.clear()

            for h in range(0, len(nomeProdutos)):
                somaValor = -1
                for i in vendidos:
                    if i[1] == nomeProdutos[h]:
                        somaValor+=i[3]

                if somaValor == -1:
                    valores.append(0)
                elif somaValor > 0:
                    valores.append(somaValor + 1)
        plt.plot(nomeProdutos, valores)
        plt.ylabel('Quantidade vendida em reais')
        plt.xlabel('Produtos')
        plt.show()



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
        decisaoUsuario = int(input("Sair (0) ------ Cadastrar Produtos (1) ---- Listar Produtos(2)  --- Gerar estatistica (3): "))


        if decisaoUsuario == 1:
            cadastrarProdutos()
        elif decisaoUsuario == 2:
            listarProdutos()

            deletar = int(input("Digite (1) Excluir produto ou (2) Sair: "))

            if deletar == 1:
                excluirProduto()
        elif decisaoUsuario == 3:
            gerarRelatorios()
import csv

# Função para carregar usuários do arquivo CSV
def carregar_usuarios():
    usuarios = {}
    with open('usuarios.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            usuarios[row['id']] = row
    return usuarios

# Função para salvar usuários no arquivo CSV
def salvar_usuarios(usuarios):
    with open('usuarios.csv', 'w', newline='') as file:
        fieldnames = ['id', 'nome', 'tipo', 'senha']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for user in usuarios.values():
            writer.writerow(user)

# Função para adicionar um novo usuário
def adicionar_usuario(usuarios, id, nome, tipo, senha):
    if id in usuarios:
        print("ID já existe!")
    else:
        usuarios[id] = {'id': id, 'nome': nome, 'tipo': tipo, 'senha': senha}
        salvar_usuarios(usuarios)

# Função para listar todos os usuários
def listar_usuarios(usuarios):
    for user in usuarios.values():
        print(user)

# Função para atualizar um usuário existente
def atualizar_usuario(usuarios, id, nome=None, tipo=None, senha=None):
    if id in usuarios:
        if nome:
            usuarios[id]['nome'] = nome
        if tipo:
            usuarios[id]['tipo'] = tipo
        if senha:
            usuarios[id]['senha'] = senha
        salvar_usuarios(usuarios)
    else:
        print("Usuário não encontrado!")

# Função para remover um usuário
def remover_usuario(usuarios, id):
    if id in usuarios:
        del usuarios[id]
        salvar_usuarios(usuarios)
    else:
        print("Usuário não encontrado!")

# Função para carregar produtos do arquivo CSV
def carregar_produtos():
    produtos = []
    with open('produtos.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            produtos.append(row)
    return produtos

# Função para salvar produtos no arquivo CSV
def salvar_produtos(produtos):
    with open('produtos.csv', 'w', newline='') as file:
        fieldnames = ['id', 'nome', 'autor', 'preco', 'quantidade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for produto in produtos:
            writer.writerow(produto)

# Função para adicionar um novo produto
def adicionar_produto(produtos, id, nome, autor, preco, quantidade):
    for produto in produtos:
        if produto['id'] == id:
            print("ID já existe!")
            return
    produtos.append({'id': id, 'nome': nome, 'autor': autor, 'preco': preco, 'quantidade': quantidade})
    salvar_produtos(produtos)

# Função para listar todos os produtos
def listar_produtos(produtos):
    for produto in produtos:
        print(produto)

# Função para atualizar um produto existente
def atualizar_produto(produtos, id, nome=None, autor=None, preco=None, quantidade=None):
    for produto in produtos:
        if produto['id'] == id:
            if nome:
                produto['nome'] = nome
            if autor:
                produto['autor'] = autor
            if preco:
                produto['preco'] = preco
            if quantidade:
                produto['quantidade'] = quantidade
            salvar_produtos(produtos)
            return
    print("Produto não encontrado!")

# Função para remover um produto
def remover_produto(produtos, id):
    for produto in produtos:
        if produto['id'] == id:
            produtos.remove(produto)
            salvar_produtos(produtos)
            return
    print("Produto não encontrado!")

# Função para buscar um produto pelo ID ou nome
def buscar_produto(produtos, chave):
    for produto in produtos:
        if produto['id'] == chave or produto['nome'] == chave:
            print(produto)
            return
    print("Produto não encontrado!")

# Função para ordenar produtos por nome
def ordenar_produtos_por_nome(produtos):
    produtos_ordenados = sorted(produtos, key=lambda x: x['nome'])
    for produto in produtos_ordenados:
        print(produto)

# Função para ordenar produtos por preço
def ordenar_produtos_por_preco(produtos):
    produtos_ordenados = sorted(produtos, key=lambda x: float(x['preco']))
    for produto in produtos_ordenados:
        print(produto)

# Exemplo de uso
usuarios = carregar_usuarios()
produtos = carregar_produtos()

# Loop principal do menu de opções
while True:
    # Exibir menu de opções
    print("\nMenu de Opções:")
    print("1 - Adicionar um usuário")
    print("2 - Listar usuários")
    print("3 - Atualizar um usuário")
    print("4 - Remover um usuário")
    print("5 - Adicionar um produto")
    print("6 - Atualizar um produto")
    print("7 - Remover um produto")
    print("8 - Buscar um produto")
    print("9 - Ordenar produtos por nome")
    print("10 - Ordenar produtos por preço")
    print("0 - Sair")
    
    # Ler a escolha do usuário
    acao = input("Qual ação deseja fazer? ")

    if acao == "0":
        break
    elif acao == "1":
        # Adicionar um novo usuário
        while True:
            id = input("Qual o ID? ")
            if id.isdigit() and id not in usuarios:
                break
            print("ID inválido ou já existe. Por favor, tente novamente.")
        
        nome = input("Qual o nome? ")
        
        while True:
            tipo = input("Qual o tipo (Gerente, Funcionário, Cliente)? ")
            if tipo in ["Gerente", "Funcionário", "Cliente"]:
                break
            print("Tipo inválido. Por favor, escolha entre Gerente, Funcionário ou Cliente.")
        
        senha = input("Qual a senha? ")
        adicionar_usuario(usuarios, id, nome, tipo, senha)
    elif acao == "2":
        # Listar todos os usuários
        listar_usuarios(usuarios)
    elif acao == "3":
        # Atualizar um usuário existente
        id = input("Qual o ID do usuário a atualizar? ")
        nome = input("Novo nome (ou enter para manter o atual): ")
        tipo = input("Novo tipo (ou enter para manter o atual): ")
        senha = input("Nova senha (ou enter para manter a atual): ")
        atualizar_usuario(usuarios, id, nome if nome else None, tipo if tipo else None, senha if senha else None)
    elif acao == "4":
        # Remover um usuário
        id = input("Qual o ID do usuário a remover? ")
        remover_usuario(usuarios, id)
    elif acao == "5":
        # Adicionar um novo produto
        id = input("Qual o ID? ")
        nome = input("Qual o nome? ")
        autor = input("Qual o autor? ")
        preco = input("Qual o preço? ")
        quantidade = input("Qual a quantidade? ")
        adicionar_produto(produtos, id, nome, autor, preco, quantidade)
    elif acao == "6":
        # Atualizar um produto existente
        id = input("Qual o ID do produto a atualizar? ")
        nome = input("Novo nome (ou enter para manter o atual): ")
        autor = input("Novo autor (ou enter para manter o atual): ")
        preco = input("Novo preço (ou enter para manter o atual): ")
        quantidade = input("Nova quantidade (ou enter para manter a atual): ")
        atualizar_produto(produtos, id, nome if nome else None, autor if autor else None, preco if preco else None, quantidade if quantidade else None)
    elif acao == "7":
        # Remover um produto
        id = input("Qual o ID do produto a remover? ")
        remover_produto(produtos, id)
    elif acao == "8":
        # Buscar um produto pelo ID ou nome
        chave = input("Buscar por ID ou nome: ")
        buscar_produto(produtos, chave)
    elif acao == "9":
        # Ordenar produtos por nome
        ordenar_produtos_por_nome(produtos)
    elif acao == "10":
        # Ordenar produtos por preço
        ordenar_produtos_por_preco(produtos)
    else:
        print("Ação inválida! Tente novamente.")

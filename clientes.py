# Importar os módulos necessários:
# - csv: para manipulação de arquivos .csv (armazenar os dados dos clientes)
# - os: para verificar se o arqquivo já existe

import csv
import os


def verificar_dados(nome, cpf, telefone, email):
    erros = []

    if not nome.replace(" ", "").isalpha():
        erros.append("O nome deve conter apenas letras e espaços.")

    if not cpf.isdigit() or len(cpf) !=11:
        erros.append("O CPF deve conter exatamente 11 números.")

    if not telefone.isdigit():
        erros.append("O telefone deve conter apenas números.")

    if "@" not in email or "." not in email.split("@")[-1]:
        erros.append("O e-mail parece inválido.")

    return erros

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# =================================
# Função responsável por cadastrar um novo cliente
# =================================
def cadastrar_clientes():
    print("\n 📋 Cadastro de Cliente") # Título de seção de cadastro

    # Solicita as informações do cliente
    nome = input("Nome completo: ")             # Nome do Cliente
    cpf = input("CPF: ")                         #CPF do Cliente
    telefone = input("Telefone: ")               # Telefone do Cliente
    email = input("E-mail: ")                    # E-mail do Cliente


    erros = verificar_dados(nome, cpf, telefone, email)

    if erros:
        print("\n❌ Forram encontrados os seguintes erros: ")
        for erro in erros:
            input("\n 🔁 Pressione Enter para tentar novamente....")
    else:
        # Abre (ou cria, se não existir) o arquivo clientes.csv no modo append (adicionar)
        #newline='' evita linhas em branco extras no Windows
        # encoding='utf-8' garante a leitura correta dos caracteres
        arquivo_existe = os.path.isfile("clientes.csv")
    with open("clientes.csv", mode="a", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        if not arquivo_existe:
            writer.writerow(["Nome", "CPF", "Telefone", "Email"])
        writer.writerow([nome, cpf, telefone, email])

        # Mensagem de sucesso após o cadastro
        print("\n✅ Cliente cadastrado com sucesso!")
        input("\n🔙 Pressione Enter para voltar...")


# =====================================
# Função responsável por listar os clientes cadastrados
# =====================================
def listar_clientes():
    limpar_tela()
    print("\n📂 Lista de Clientes:\n") # Título da seção de listagem


    # Verifica se o arquivo clientes.csv existe
    if not os.path.exists('clientes.csv'):
        print("Nenhum cliente cadastrado ainda.") # Mensagem caso o arquivo não exista
        input("\n 🔙 Pressione Enter para voltar ao menu...")
        return # Sai da função
        
    # Abre o arquivo em modo leitura
    with open('clientes.csv', mode='r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo) # Cria um objeto para ler o arquivo
        # Percorre todas as linhas do arquivo, exibindo cada cliente
        for i, linha in enumerate(leitor, start=1): # i é índice (começa em 1), linha é uma lista com os dados
            nome, cpf, telefone, email = linha #Desempacota os dados da linha
            print(f"{i}. Nome: {nome} | CPF: {cpf} | Telefone: {telefone} | E-mail: {email}") # Exibe os dados formatados

    input("\n 🔙 Pressione Enter para voltar ao menu...")
    

    #Menu simples para testar as  funções
def menu_clientes():    
    while True: 
        limpar_tela()
        print("\n=== MENU DE CLIENTES ===")
        print("1 - Cadastrar novo cliente")
        print("2 - Listar clientes cadastrados")
        print("3 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_clientes()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            print("Carregando...")
            break 
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar")
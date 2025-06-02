# Importar os módulos necessários:
# - csv: para manipulação de arquivos .csv (armazenar os dados dos clientes)
# - os: para verificar se o arqquivo já existe

import csv
import os
import time


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

def cpf_ja_cadastrado(cpf):
    if not os.path.exists('clientes.csv'):
        return False # Arquivo ainda não existe, então não tem nenhum CPF
    
    with open("clientes.csv", mode="r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor, None) # Pular o cabeçalho
        for linha in leitor:
            if linha[1] == cpf: # CPF é o segundo campo (indice 1)
                return True
    return False
# =================================
# Função responsável por cadastrar um novo cliente
# =================================
def cadastrar_clientes():
    while True:
        limpar_tela()
        cpf = input("CPF: ")

        if cpf_ja_cadastrado(cpf):
            limpar_tela()
            print("\n⚠️ Usuário já cadastrado!")
            time.sleep(3) # Espera 3 segundos
            continue # Volta para o inicio do loop, pedindo CPF de novo

        nome = input("Nome completo: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")

        erros = verificar_dados(nome, cpf, telefone, email)

        if erros:
            print("\n❌ Foram encontrados os seguintes erros:")
            for erro in erros:
                print(f"- {erro}")
            input("\n 🔁 Pressione Enter para tentar novamente...")
            return  # OK, está dentro da função

        if cpf_ja_cadastrado(cpf):
            print("\n⚠️ Este CPF já está cadastrado no sistema")
            input("\n 🔁 Pressione Enter para tentar novamente...")
            return  # OK, dentro da função

        arquivo_existe = os.path.isfile("clientes.csv")
        with open("clientes.csv", mode="a", newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)
            if not arquivo_existe:
                writer.writerow(["Nome", "CPF", "Telefone", "Email"])
            writer.writerow([nome, cpf, telefone, email])

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
        next(leitor, None)# Ignora o Cabeçalho

        contador = 0
        # Percorre todas as linhas do arquivo, exibindo cada cliente
        for i, linha in enumerate(leitor, start=1): # i é índice (começa em 1), linha é uma lista com os dados
            if len(linha) != 4:
                continue # Ignora linhas incompletas
            nome, cpf, telefone, email = linha #Desempacota os dados da linha
            print(f"{i}. Nome: {nome} | CPF: {cpf} | Telefone: {telefone} | E-mail: {email}") # Exibe os dados formatados
            contador += 1

            if contador == 0:
                print("Nennhum cliente Válido encontrado.")

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
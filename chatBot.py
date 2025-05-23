# Criando um chatbot simples

# Função para o setor de Atendimento
def atendimento():
    print("\n📞 Atendimento")  # Exibe o título do setor
    print("1 - Falar com atendente")
    print("2 - Realizar compra online")
    print("3 - Voltar ao menu principal")

    escolha = input("Escolha uma opção: ")  # Captura a escolha do usuário

    if escolha == "1":
        print("Bot: Você está sendo direcionado a um atendente de nossas unidades...")
    elif escolha == "2":
        print("Bot: Escolha uma das categorias abaixo....")
    elif escolha == "3":
        menu_principal()  # Volta ao menu principal
    else:
        print("Opção inválida! Tente novamente.")
        atendimento()  # Reinicia a função para nova escolha do usuário


# Função para o setor de Entrega
def entrega():
    print("\n🚚 Entrega")  # Exibe o título do setor
    print("1 - Acompanhe sua entrega")
    print("2 - Voltar ao menu principal")

    escolha = input("Escolha uma opção: ")  # Captura a escolha do usuário

    if escolha == "1":
        print("Bot: Um link para acompanhar sua entrega será enviado em instantes.")
    elif escolha == "2":
        menu_principal()  # Volta ao menu principal
    else:
        print("Opção inválida! Tente novamente.")
        entrega()  # Reinicia a função para nova escolha do usuário


# Função para o setor de Reclamações
def reclamacoes():
    print("\n⚠️ Reclamações")  # Exibe o título do setor
    print("1 - Reclamações sobre mercadoria")
    print("2 - Reclamações sobre a entrega")
    print("3 - Voltar ao menu principal")

    escolha = input("Escolha uma opção: ")  # Captura a escolha do usuário

    if escolha == "1":
        print("Bot: Você será redirecionado ao nosso canal de reclamações. Por favor, descreva com detalhes seu problema.")
    elif escolha == "2":
        print("Bot: Você será redirecionado ao nosso canal de reclamações. Por favor, descreva com detalhes seu problema.")
    elif escolha == "3":
        menu_principal()  # Volta ao menu principal
    else:
        print("Opção inválida! Tente novamente.")
        reclamacoes()  # Reinicia a função para nova escolha do usuário


# Função que exibe o menu principal
def menu_principal():
    print("\n🤖 Bem-vindo ao chat!")
    print("Qual setor deseja falar com a gente?")
    print("1 - Atendimento")
    print("2 - Entrega")
    print("3 - Reclamações")
    print("4 - Sair")

    escolha = input("Digite o número do setor desejado: ")

    if escolha == "1":
        atendimento()  # Chama a função Atendimento
    elif escolha == "2":
        entrega()  # Chama a função Entrega
    elif escolha == "3":
        reclamacoes()  # Chama a função Reclamações
    elif escolha == "4":
        print("Bot: Até mais! 👋")  # Mensagem de despedida
    else:
        print("Opção inválida, tente novamente.")
        menu_principal()  # Reinicia o menu principal


# Inicia o chatbot executando o menu principal
menu_principal()

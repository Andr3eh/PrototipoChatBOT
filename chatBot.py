# Criando um chatbot simples

#Funcao para o setor de Suporte
def suporte_tecnico():
    print("\n🔧 Suporte Técnico")#Exibe o título do setor
    print("1 - Meu computador não liga")
    print("2 - Problema com a Internet")
    print("3 - Voltar ao menu principal")#Opção para voltar ao menu

    escolha = input("Escolha uma opção: ")#Captura a escolha

    if escolha == "1":
        print("Bot: Verifique se o cabo de energia está conectado")
    elif escolha == "2":
        print("Bot: Reinicie seu roteador e tente novamente")
    elif escolha == "3":
        menu_principal()#Volta ao menu principal
    else: 
        print("Opção inválida! Tente novamente.")
        suporte_tecnico() #Reinicia a função nova escolha do usuario

    #Funçao para p setor Financeiro
    def financeiro():
        print("\n💰 Financeiro")
        print("1 - Ver fatura")
        print("2 - Forma de pagamento")
        print("3 - Voltar ao menu principal")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("Bot: Sua fatura esta disponivel no aplicativo.")
        elif escolha == "2":
            print("Bot: Aceitamos cartões de crédito, débito e PIX")
        elif escolha == "3":
            menu_principal()   
        else:
            print("Opção inválida! Tente novamente.")
            financeiro() 

    def vendas():
        print("\n Vendas")
        print("1 - Produtos disponíveis")
        print("2 - Promoções atuais")
        print("3 - Voltar ao menu principal")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("Bot: Temos diversos produtos ao disponiveis. Acesse nosso site!")
        elif escolha == "2":
            print("Bot: Temos descontos especiais esse mês!")
        elif escolha == "3":
            menu_principal()
        else:
            print("Opção inválida! Tente novamente.")
            vendas()    

#Exibe uma mensagem inicial antes de iniciar o chatbot

def menu_principal():
    print("\n 🤖 Bem-vindo ao chat....")
    print("Qual um setor deseja falar: ...")
    print("1° Suporte Técnico")
    print("2° Financeiro")
    print("3° Vendas")
    print("4° Sair")

    escolha = input("Digite o numero do setor desejado:")

    if escolha == "1":
        print("Voce escolheu Suporte Técnico, Como posso te ajudar?...")
    elif escolha == "2":
        print("Você escolheu financeiro. Qual sua duvida?")
    elif escolha == "3":
        print("Voce escolheu Comercial. Gostaria de saber mais sobre nossos produtos?")
    elif escolha == "4":
        print("Bot: Até mais!")
    else:
        print("Opção inválida, tente novamente")
    menu_principal()

#Dicionario de resposta pré-definidas

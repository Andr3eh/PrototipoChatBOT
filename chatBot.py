# Criando um chatbot simples

# Importando o módulo 'os' para execultar comandos do sistema operacional, como limpar tela
import os

# Importando o módulo 'os' para execultar comandos do sistema operacional, como limpar tela
import time

from clientes import menu_clientes # Importando o Menu clientes

from medicamentos import listar_medicamentos # Dicionário com os remédios


# Função para limpar a tela do terminal
def limpar_tela():
    #Se o sistema for Windows, usa 'cls', senão usa 'clear' (Linux ou Mac)
    os.system('cls' if os.name == 'nt' else 'clear')




# Função para exibir mensagens do bot de forma padronizada
def exibir_mensagem(texto):
    print(f"\nBot: {texto}")# Exibe o texto com o prefixo "Bot:" em uma nova liha

# Função para o setor de Atendimento
def atendimento():
    while True: #Matem o usúario no menu de atendimento até ele escolher sair
        limpar_tela() # Limpa a tela a caba exibição do menu, para manter a interface limpa
        print("\n📞 Atendimento")  # Exibe o título do setor
        print("1 - Falar com atendente") # Opção 1
        print("2 - Realizar compra online") # Opção 2
        print("3 - Voltar ao menu principal") # Opção 3

        escolha = input("Escolha uma opção: ")  # Captura a escolha do usuário
        
        #Verifica qual foi a escolha do usúario
        if escolha == "1":
            print("Bot: Você está sendo direcionado a um atendente de nossas unidades...")# Resposta para opção 1 
        elif escolha == "2":
            listar_medicamentos() # Resposta para opção 2
        elif escolha == "3":
            menu_principal()  # Volta ao menu principal
        else:
            limpar_tela() #Limpa a tela antes de mostrar a mensagem de erro
            exibir_mensagem("Opção inválida, tente novamente.")# Trata entrada inválida
            time.sleep(2)
            


# Função para o setor de Entrega
def entrega():
    while True: #Matem o usúario no menu de entrega até ele escolher sair
        limpar_tela() # Limpa a tela a caba exibição do menu, para manter a interface limpa
        print("\n🚚 Entrega")  # Exibe o título do setor
        print("1 - Acompanhe sua entrega")# Opção 1
        print("2 - Voltar ao menu principal")#O pção 1

        escolha = input("Escolha uma opção: ")  # Captura a escolha do usuário

        if escolha == "1":
            print("Bot: Um link para acompanhar sua entrega será enviado em instantes.")#Resposta para opção 1
        elif escolha == "2":
            menu_principal()  # Volta ao menu principal
        else:
            limpar_tela() #Limpa a tela antes de mostrar a mensagem de erro
            exibir_mensagem("Opção inválida, tente novamente.")# Trata entrada inválida
            time.sleep(2)
            


# Função para o setor de Reclamações
def reclamacoes():
    limpar_tela() # Limpa a tela a caba exibição do menu, para manter a interface limpa
    print("\n⚠️ Reclamações")  # Exibe o título do setor
    print("1 - Reclamações sobre mercadoria")# Opção 1
    print("2 - Reclamações sobre a entrega")# Opção 2
    print("3 - Voltar ao menu principal")# Opção 3

    escolha = input("Escolha uma opção: ")  # Captura a escolha do usuário

    if escolha == "1":
        print("Bot: Você será redirecionado ao nosso canal de reclamações. Por favor, descreva com detalhes seu problema.")#Resposta para opção 1
    elif escolha == "2":
        print("Bot: Você será redirecionado ao nosso canal de reclamações. Por favor, descreva com detalhes seu problema.")#Resposta para opção 1
    elif escolha == "3":
        menu_principal()  # Volta ao menu principal
    else:
            limpar_tela() #Limpa a tela antes de mostrar a mensagem de erro
            exibir_mensagem("Opção inválida, tente novamente.")# Trata entrada inválida
            time.sleep(2)
        

# Função que exibe o menu principal
def menu_principal():
    while True: #Matem o usúario no menu de atendimento até ele escolher sair
        limpar_tela() # Limpa a tela a caba exibição do menu, para manter a interface limpa

        print("\n🤖 Bem-vindo ao chat da Farmácia Viva+!")# Saudação do chatbot
        print("1 - Atendimento")# Opção para ir ao menu de atendimento
        print("2 - Cadastro")# Opção para ir ao menu de cadastro
        print("3 - Entrega")# Opção para ir ao menu de entrega
        print("4 - Reclamações")# Opção para ir ao menu de reclamações
        print("5 - Sair")# Opção para encerrar o atendimento

        escolha = input("Digite o número do setor desejado: ")# Captura a escolha do usuário

        if escolha == "1":
            atendimento()  # Chama a função Atendimento
        elif escolha == "2":
            menu_clientes()  # Chama o menu de cadastro
        elif escolha == "3":
            entrega()  # Chama a função Entrega
        elif escolha == "4":
            reclamacoes()  # Chama a função Reclamações
        elif escolha == "5":
            print("Bot: Até mais! 👋")  # Mensagem de despedida
            break # Encerra o laço, saindo do programa
        else:
            limpar_tela() #Limpa a tela antes de mostrar a mensagem de erro
            exibir_mensagem("Opção inválida, tente novamente.")# Trata entrada inválida
            time.sleep(2)
            


# Inicia o chatbot executando o menu principal
if __name__ == "__main__":
    menu_principal()

# Criando um chatbot simples

# Importando o módulo 'os' para execultar comandos do sistema operacional, como limpar tela
import os

# Importando o módulo 'os' para execultar comandos do sistema operacional, como limpar tela
import time

from clientes import menu_clientes # Importando o Menu clientes

from medicamentos import listar_medicamentos # Dicionário com os remédios

import random # para gerar prazos aleatórios

# Dicionário global para armazenar prazos por CEP
prazos_por_regiao = {}
prazos_por_cep = {}

def consultar_prazo_entrega():
    while True:
        cep = input("Digite seu CEP para estimar o prazo de entrega:").strip()

        # Validação do CEP
        if len(cep) < 2 or not cep.isdigit():
            print("Bot: CEP inválido. Por favor, digite pelo menos os dois primeiros dígitos do CEP.")
            continue

        prefixo_cep = cep[:2]  # Pega os dois primeiros dígitos do CEP

        # Se o prefixo já tem um prazo definido, usa o mesmo
        if prefixo_cep in prazos_por_regiao:
            prazo = prazos_por_regiao[prefixo_cep]
        else:
            if prefixo_cep in ["11", "12", "13", "14", "15", "16", "17", "18", "19"]:  # Estado de SP
                prazo = random.randint(2, 5)
            else:  # Fora de SP (outros estados)
                prazo = 30
            prazos_por_regiao[prefixo_cep] = prazo  # Salva para manter consistência futura

        print(f"\nBot: O prazo estimado para o CEP {cep} é de {prazo} dias úteis.")
        while True: 
            opcao = input("\nDeseja consultar outro CEP? (1 - Sim / 2 - Voltar ao menu): ").strip()
            if opcao == "1":
                break # Voltar ao início do while principal para consulatr
            elif opcao == "2":
                return # sai da função e volta ao menu
            else:
                print("Opção inválida. Por favor, digite 1 ou 2.")
        # Pergunta se deseja continuar outro
       
# Função para limpar a tela do terminal
def limpar_tela():
    #Se o sistema for Windows, usa 'cls', senão usa 'clear' (Linux ou Mac)
    os.system('cls' if os.name == 'nt' else 'clear')




# Função para exibir mensagens do bot de forma padronizada
def exibir_mensagem(texto):
    print(f"\nBot: {texto}")# Exibe o texto com o prefixo "Bot:" em uma nova liha

# Função para o setor de Atendimento
def atendimento():
    tempo_total = 60      # tempo total em segundos (1 minuto)
    intervalo = 0.5       # tempo entre pontos (em segundos)
    max_pontos = 5        # número máximo de pontos antes de reiniciar

    while True:
        limpar_tela()
        print("\n📞 Atendimento")
        print("1 - Falar com atendente")
        print("2 - Realizar compra online")
        print("3 - Voltar ao menu principal")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("Bot: Você está sendo direcionado a um atendente de nossas unidades...")
            inicio = time.time()
            pontos = 1
            while time.time() - inicio < tempo_total:
                texto = "Bot: Conectando com uma atendente" + "." * pontos + " " * (max_pontos - pontos)
                print(texto, end="\r", flush=True)
                time.sleep(intervalo)
                pontos += 1
                if pontos > max_pontos:
                    pontos = 1
            print("\nBot: Todos os nossos atendentes estão ocupados no momento. Por favor, tente novamente mais tarde.")
            input("\nPressione ENTER para voltar ao menu...")

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
        print("2 - Consultar prazo de entrega")# Opção 2
        print("3 - Alterar endereço de entrega")# Opção 2
        print("4 - Reagendar entrega")# Opção 2
        print("5 - Voltar ao menu principal")#Opção 5

        escolha = input("\n\nEscolha uma opção: ")  # Captura a escolha do usuário

        if escolha == "1":
            print("Bot: Um link para acompanhar sua entrega será enviado em instantes.")#Resposta para opção 1
        elif escolha == "2":
            consultar_prazo_entrega()
            input("\n\nPressione ENTER para voltar ao menu...")
        elif escolha == "3":
            novo_endereco = input("\nDigite o novo endereço completo: ")
            print(f"\nBot: Endereço atualizado para:\n{novo_endereco}")
            input("\n\nPressione ENTER para voltar ao menu...")
        elif escolha == "4":
            print("\nBot: Escolha uma nova data para entrega:")
            print("\n2 - Em 2 dias")
            print("\n3 - Em 3 dias")
            nova_data = input("Opção: ")
            print("\nBot: Entrega reagendada com sucesso.")
            input("\nPressione ENTER para voltar ao menu...")
        elif escolha == "5":
            return  # Volta ao menu principal
        else:
            limpar_tela() #Limpa a tela antes de mostrar a mensagem de erro
            exibir_mensagem("Opção inválida, tente novamente.")# Trata entrada inválida
            time.sleep(2)
            


# Função para o setor de Reclamações
def reclamacoes():
    while True:
        limpar_tela()
        print("\n⚠️ Reclamações")
        print("1 - Reclamações sobre mercadoria")
        print("2 - Reclamações sobre a entrega")
        print("3 - Voltar ao menu principal")

        escolha = input("Escolha uma opção: ")

        if escolha in ["1", "2"]:
            tipo = "Mercadoria" if escolha == "1" else "Entrega"
            print(f"\nBot: Você escolheu reclamação sobre {tipo}.")
            reclamacao = input("Por favor, digite sua reclamação: ")

            # Salvar reclamação em arquivo de texto
            with open("reclamacoes.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"Tipo: {tipo}\n")
                arquivo.write(f"Reclamação: {reclamacao}\n")
                arquivo.write("="*40 + "\n")

            print("\nBot: Obrigado! Sua reclamação foi registrada com sucesso.")
            input("\nPressione ENTER para voltar ao menu...")
            return  # volta ao menu principal
        elif escolha == "3":
            return  # volta ao menu principal
        else:
            limpar_tela()
            exibir_mensagem("Opção inválida, tente novamente.")
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

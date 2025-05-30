medicamentos = {
    "paracetamol": {
        "nome": "Paracetamol 500mg",
        "descricao": "Analgésico e antitérmico para dores leves.",
        "preco": 5.99,
        "estoque": 80
    },
    "dipirona":{
        "nome": "Dipirona 1g",
        "descricao": "Alívio de dores e febres.",
        "preco": 4.50,
        "estoque": 60
    }
}

# Importando o módulo 'os' para execultar comandos do sistema operacional, como limpar tela
import time

import os


# Função para exibir mensagens do bot de forma padronizada
def exibir_mensagem(texto):
    print(f"\nBot: {texto}")# Exibe o texto com o prefixo "Bot:" em uma nova liha


def limpar_tela():
    #Se o sistema for Windows, usa 'cls', senão usa 'clear' (Linux ou Mac)
    os.system('cls' if os.name == 'nt' else 'clear')

def listar_medicamentos():
    while True:
        limpar_tela()
        print("\n 🛒 Lista de Medicamentos Disponíveis:\n")

        for idx, chave in enumerate(medicamentos, start=1):
            print(f"{idx} - {medicamentos[chave]['nome']} - R$ {medicamentos[chave]['preco']:2f}")


        print(f"{len(medicamentos)+1} - Voltar ao menu anterior")

        escolha = input("\nDigite o número do medicamento que deseja visualizar: ")

        try:
            escolha = int(escolha)
            if 1 <= escolha <= len(medicamentos):
                chave_selecionada = list(medicamentos.key())[escolha - 1]
                produto = medicamentos[chave_selecionada]
                limpar_tela()
                print(f"\n💊{produto['nome']}")
                print(f"Descrição: {produto['descricao']}")
                print(f"Preço: R$ {produto['preco']:.2f}")
                print(f"Estoque disponível: {produto['estoque']} unidades")
                input("\nPressione ENTER para continuar navegando.")
            elif escolha == len(medicamentos) + 1:
                break
            else:
                exibir_mensagem("Opção inválida.")
                time.sleep(2)
        except ValueError:
            exibir_mensagem("Por favor, digite um número válido.")
            time.sleep(2)
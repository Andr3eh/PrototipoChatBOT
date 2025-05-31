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
    },
    "ibuprofeno": {
    "nome": "Ibuprofeno 600mg",
    "descricao": "Anti-inflamatório e analgésico para dores musculares e febre.",
    "preco": 6.75,
    "estoque": 50
    },
    "amoxicilina": {
        "nome": "Amoxicilina 500mg",
        "descricao": "Antibiótico para infecções bacterianas.",
        "preco": 12.90,
        "estoque": 30
    },
    "loratadina": {
        "nome": "Loratadina 10mg",
        "descricao": "Antialérgico para rinite, urticária e alergias em geral.",
        "preco": 4.99,
        "estoque": 45
    },
    "omeprazol": {
        "nome": "Omeprazol 20mg",
        "descricao": "Protetor gástrico para azia e refluxo.",
        "preco": 3.40,
        "estoque": 60
    },
    "nimesulida": {
        "nome": "Nimesulida 100mg",
        "descricao": "Analgésico e anti-inflamatório para dores e febres.",
        "preco": 5.50,
        "estoque": 40
    },
    "azitromicina": {
        "nome": "Azitromicina 500mg",
        "descricao": "Antibiótico de amplo espectro.",
        "preco": 14.90,
        "estoque": 25
    },
    "losartana": {
        "nome": "Losartana 50mg",
        "descricao": "Controlador de pressão arterial.",
        "preco": 8.25,
        "estoque": 70
    },
    "metformina": {
        "nome": "Metformina 850mg",
        "descricao": "Medicamento para controle do diabetes tipo 2.",
        "preco": 9.10,
        "estoque": 55
    },
    "cetoprofeno": {
        "nome": "Cetoprofeno 100mg",
        "descricao": "Anti-inflamatório para dores articulares e musculares.",
        "preco": 6.30,
        "estoque": 35
    },
    "bromoprida": {
        "nome": "Bromoprida 10mg",
        "descricao": "Medicamento para enjoo e refluxo.",
        "preco": 4.20,
        "estoque": 40
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
            print(f"{idx} - {medicamentos[chave]['nome']} - R$ {medicamentos[chave]['preco']:.2f}")

        print(f"{len(medicamentos)+1} - Voltar ao menu anterior")

        escolha = input("\nDigite o número do medicamento que deseja visualizar: ")

        try:
            escolha = int(escolha)
            if 1 <= escolha <= len(medicamentos):
                chave_selecionada = list(medicamentos.keys())[escolha - 1]
                produto = medicamentos[chave_selecionada]
                limpar_tela()
                print(f"\n💊 {produto['nome']}")
                print(f"Descrição: {produto['descricao']}")
                print(f"Preço: R$ {produto['preco']:.2f}")
                print(f"Estoque disponível: {produto['estoque']} unidades")

                while True:
                    print("\n1 - Voltar para lista de medicamentos")
                    print("2 - Voltar ao menu principal")
                    escolha_detalhe = input("Escolha uma opção: ")
                    if escolha_detalhe == "1":
                        break  # volta para a lista
                    elif escolha_detalhe == "2":
                        return  # volta ao menu principal
                    else:
                        exibir_mensagem("Opção inválida.")
                        time.sleep(2)
            elif escolha == len(medicamentos) + 1:
                return  # voltar ao menu anterior
            else:
                exibir_mensagem("Opção inválida.")
                time.sleep(2)

        except ValueError:
            exibir_mensagem("Digite apenas números válidos.")
            time.sleep(2)

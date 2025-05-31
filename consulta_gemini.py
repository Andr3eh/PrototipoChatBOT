import requests
import json

API_KEY = "AIzaSyCOZEx8IcYyohbLtLVU-E4PIJQYDEhfiSwI"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

def perguntar_gemini_menu(entrada_usuario):
    prompt = (
        "Você é um assistente que responde as opções do menu abaixo:\n\n"
        "1 - Falar com atendente\n"
        "2 - Realizar compra online\n"
        "3 - Voltar ao menu principal\n\n"
        "Se o usuário digitar \"1\", responda: \"Você está sendo direcionado a um atendente de nossas unidades...\"\n"
        "Se digitar \"2\", responda: \"Aqui você pode realizar sua compra online. Em breve, funcionalidade disponível!\"\n"
        "Se digitar \"3\", responda: \"Voltando ao menu principal.\"\n"
        "Se digitar qualquer outra coisa, responda: \"Opção inválida, tente novamente.\"\n\n"
        f"Usuário: {entrada_usuario}"
    )

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        resposta = response.json()
        texto_gerado = resposta['candidates'][0]['content']['parts'][0]['text']
        return texto_gerado.strip()
    else:
        return f"Erro na requisição: {response.status_code} - {response.text}"

if __name__ == "__main__":
    while True:
        entrada = input("Escolha uma opção do menu: ")
        if entrada.lower() in ["sair", "exit", "quit"]:
            print("Encerrando o chat. Até mais!")
            break

        resposta = perguntar_gemini_menu(entrada)
        print("Bot:", resposta)

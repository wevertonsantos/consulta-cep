import requests,json

def main():
    while True:
        escolha_usuario = input("Digite o CEP que deseja consultar: ")
        if len(escolha_usuario) == 8:
            url = f"https://viacep.com.br/ws/{escolha_usuario}/json"
            response = json.loads(requests.get(url).text)
            print(response)
            break
        else:
            print("O CEP deve conter 8 dígitos")

main()
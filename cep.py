import requests,json

def main():
    while True:
        cep = input("Digite o CEP que deseja consultar: ")
        if len(cep) == 8:
            url = f"https://viacep.com.br/ws/{cep}/json"
            response = json.loads(requests.get(url).text)
            print(response)
            break
        else:
            print("O CEP deve conter 8 dígitos")

main()
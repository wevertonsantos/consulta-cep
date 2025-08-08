import requests

def main():
    while True:
        escolha_usuario = input("Digite o CEP que deseja consultar: ")
        if len(escolha_usuario) == 8:
            response = requests.get(f"https://viacep.com.br/ws/{escolha_usuario}/json").text
            print(response)
            break
        else:
            print("O CEP deve conter 8 dígitos")

main()
import requests,json

def main():
    while True:
        cep = input("Digite o CEP que deseja consultar: ")
        if len(cep) == 8 and cep.isdigit():
            url = f"https://viacep.com.br/ws/{cep}/json"
            response_json = json.loads(requests.get(url).text)
            if len(response_json) == 1:
                print(f"CEP: {cep} não existe, informe outro.")
                continue
            else:
                logradouro = response_json['logradouro']
                complemento = response_json['complemento']
                bairro = response_json['bairro']
                localidade = response_json['localidade']
                estado = response_json['uf']
                print(f"Nome da rua: {logradouro} - Complemento: {complemento} - Bairro: {bairro}")
                print(f"Localidade: {localidade} - Estado: {estado}")
            break
        else:
            print("O CEP deve conter 8 dígitos")

main()
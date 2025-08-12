import requests,json

def main():
    while True:
        cep = input("Digite o CEP que deseja consultar: ")
        if valida_cep(cep):
            try:
                response_json = consulta_api(cep)
                if "erro" in response_json:
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
            except requests.exceptions.RequestException as e:
                print(f"Erro ao consultar o CEP: {e}")
        else:
            print("O CEP deve conter 8 dígitos")

def valida_cep(cep):
    if len(cep) == 8 and cep.isdigit():
        return True

def consulta_api(cep):
    url = f"https://viacep.com.br/ws/{cep}/json"
    return json.loads(requests.get(url).text)

main()
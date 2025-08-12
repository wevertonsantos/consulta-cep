import requests,json

def main():
    while True:
        cep = input("Digite o CEP que deseja consultar: ").strip()
        if valida_cep(cep):
            try:
                dados_cep = consulta_api(cep)
                if "erro" in response_json:
                    print(f"CEP: {cep} não existe, informe outro.")
                    continue
                else:
                    resultado_api(response_json)
                break
            except requests.exceptions.RequestException as e:
                print(f"Erro ao consultar o CEP: {e}")
        else:
            print("O CEP deve conter apenas 8 dígitos sem traço. Ex: 01001000")

def valida_cep(cep):
    if len(cep) == 8 and cep.isdigit():
        return True

def consulta_api(cep):
    url = f"https://viacep.com.br/ws/{cep}/json"
    return json.loads(requests.get(url).text)

def resultado_api(response_json):
    logradouro = response_json['logradouro']
    complemento = response_json['complemento']
    bairro = response_json['bairro']
    localidade = response_json['localidade']
    estado = response_json['uf']
    print(f"Nome da rua: {logradouro} - Complemen{complemento} - Bairro: {bairro}")
    print(f"Localidade: {localidade} - Estado: {estado}")

main()
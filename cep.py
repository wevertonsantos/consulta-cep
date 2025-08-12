import requests

def main():
    while True:
        cep = input("Digite o CEP que deseja consultar: ").strip()
        if valida_cep(cep):
            try:
                dados_cep = consulta_api(cep)
                if "erro" in dados_cep:
                    print(f"CEP: {cep} não existe, informe outro.")
                    continue
                else:
                    resultado_api(dados_cep)
                break
            except requests.exceptions.RequestException as e:
                print(f"Erro ao consultar o CEP: {e}")
        else:
            print("O CEP deve conter apenas 8 dígitos sem traço. Ex: 01001000")

def valida_cep(cep):
    return len(cep) == 8 and cep.isdigit()

def consulta_api(cep):
    url = f"https://viacep.com.br/ws/{cep}/json"
    return requests.get(url).json()

def resultado_api(dados_cep):
    logradouro = dados_cep['logradouro']
    complemento = dados_cep['complemento']
    bairro = dados_cep['bairro']
    localidade = dados_cep['localidade']
    estado = dados_cep['uf']
    print(f"Nome da rua: {logradouro} - Complemen{complemento} - Bairro: {bairro}")
    print(f"Localidade: {localidade} - Estado: {estado}")

main()
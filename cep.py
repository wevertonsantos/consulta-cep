def main():
    while True:
        escolha_usuario = input("Digite o CEP que deseja consultar: ")
        if len(escolha_usuario) == 8:
            print(escolha_usuario)
            break
        else:
            print("O CEP deve conter 8 dígitos")

main()
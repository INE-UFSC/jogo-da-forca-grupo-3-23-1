from main import Jogo

class Menu():
    def __init__(self):
        pass

    def iniciar(self):
        print("Jogo da forca")
        print("1. Jogar.")
        print("2. Sair.")
        option = input("Digite o que voce deseja fazer.")
        while True:
            
            #jogo
            if option == "1":
                palavra = input("Digite a palavra desejada para o jogo.")
                jogo = Jogo(palavra)
                while True:
                    jogo.rodar()
                    if jogo.fim_de_jogo:
                        break

                if jogo.ganhou:
                    print('Voce ganhou')
                    again = input("Deseja jogar novamente? (y/n)")
                    if again == "y":
                        option = "3"
                    else:
                        break
                else:
                    print('Voce perdeu')
                    again = input("Deseja jogar novamente? (y/n)")
                    if again == "y":
                        option ="3"
                    else:
                        break

            #sai do jogo
            elif option == "2":
                break

            #volta para o menu apos um jogo
            elif option == "3": 
                print("Jogo da forca")
                print("1. Jogar.")
                print("2. Sair.")
                option = input("Digite o que voce deseja fazer.")

            #opcao de contra erros
            else:
                print("1. Jogar.")
                print("2. Sair.")
                option = input("Opção invalida, digite novamente.")

menu = Menu()
menu.iniciar()

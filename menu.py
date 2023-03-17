from main import Jogo

class Menu():
    def __init__(self):
        pass

    def iniciar(self):
        
        while True:
            print("Jogo da forca")
            print("1. Jogar.")
            print("2. Sair.")
            option = input("Digite o que voce deseja fazer.")
            if option == "1":
                palavra = input("Digite a palavra desejada para o jogo.")
                jogo = Jogo(palavra)
                while True:
                    jogo.rodar()
                    if jogo.fim_de_jogo:
                        break

                if jogo.ganhou:
                    print('Voce ganhou')
                    
                else:
                    print('Voce perdeu')


            elif option == "2":
                break
            else:
                print("1. Jogar.")
                print("2. Sair.")
                option = input("Opção invalida, digite novamente.")

menu = Menu()
menu.iniciar()

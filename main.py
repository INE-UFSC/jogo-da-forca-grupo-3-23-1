class Jogo:
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras = [False]*len(palavra)
        self.fim_de_jogo = False
        self.ganhou = False
        self.vida = 5

    def rodar(self):
        self.mostrar()
        letra = self.lerLetra()
        self.logica(letra)
        print()

    def mostrar(self):
        print(f'Vida: {self.vida}')
        print(f'Palavra: {self.palavra}')
        print(f'Letras: {self.letras}') 

    def lerLetra(self):
        return input('Digite a letra: ')

    def logica(self, letra):
        acertou = False
        for i, c in enumerate(self.palavra):
            if c == letra:
                self.letras[i] = True
                acertou = True

        if not acertou:
            self.vida -= 1

        if all(self.letras):
            self.fim_de_jogo = True
            self.ganhou = True

        if self.vida <= 0:
            self.fim_de_jogo = True
            self.ganhou = False


palavra = 'chocolate'
jogo = Jogo(palavra)

while True:
    jogo.rodar()

    if jogo.fim_de_jogo:
        break

if jogo.ganhou:
    print('Voce ganhou')
else:
    print('Voce perdeu')


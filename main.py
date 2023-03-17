class Jogo:
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras = [False]*len(palavra)
        self.fim_de_jogo = False
        self.ganhou = False
        self.vida = 7
        self.letras_erradas = []
        self.letras_ja_digitadas = []

    def rodar(self):
        self.mostrar()
        letra = self.lerLetra()
        self.logica(letra)
        print()

    def mostrar(self):
        print()
        self.mostrarLetrasErradas()
        self.mostrarForca()
        print()
        self.mostrarPalavra()


    def lerLetra(self):
        letra = input('Digite a letra: ').lower()
        while len(letra) != 1 or letra in self.letras_ja_digitadas:
            letra = input('Digite apenas 1 letra ainda não digitada: ').lower()

        self.letras_ja_digitadas.append(letra)
        
        return letra

    def logica(self, letra):
        acertou = False
        for i, c in enumerate(self.palavra):
            if c == letra:
                self.letras[i] = True
                acertou = True

        if not acertou:
            self.vida -= 1
            self.letras_erradas.append(letra)

        if all(self.letras):
            self.fim_de_jogo = True
            self.ganhou = True

        if self.vida <= 0:
            self.fim_de_jogo = True
            self.ganhou = False

    def mostrarPalavra(self):
        print("Palavra: ", end = " ")
        for n, l in enumerate(self.letras):
            if not l:
                print("_", end = "")
            else:
                print(self.palavra[n], end = "")
        print()

    def mostrarLetrasErradas(self):
        if len(self.letras_erradas) != 0:
            print("Letras erradas já digitadas:", end = " ")
            for e in self.letras_erradas:
                print(e, end= " ")
            print()


    def mostrarForca(self):
        if self.vida == 7:
            print(" _______")
            print("|       |")
            print("|")
            print("|")
            print("|")
            print("|")
        elif self.vida == 6:
            print(" _______")
            print("|       |")
            print("|      (_)")
            print("|")
            print("|")
            print("|")
        elif self.vida == 5:
            print(" _______")
            print("|       |")
            print("|      (_)")
            print("|       |")
            print("|")
            print("|")
        elif self.vida == 4:
            print(" _______")
            print("|       |")
            print("|      (_)")
            print("|     \ |")
            print("|")
            print("|")
        elif self.vida == 3:
            print(" _______")
            print("|       |")
            print("|      (_)")
            print("|     \ | /")
            print("|")
            print("|")
        elif self.vida == 2:
            print(" _______")
            print("|       |")
            print("|      (_)")
            print("|     \ | /")
            print("|       |")
            print("|")

        elif self.vida == 1:
            print(" _______")
            print("|       |")
            print("|      (_)")
            print("|     \ | /")
            print("|       |")
            print("|     /")

import random

class palavras():

    def __init__(self):
        pass

    def get_palavra(self):
        #ler arquivo de palavras
        palavras = open("palavras_forca", 'r', encoding = "utf8")

        #criar uma lista de palavras, com cada linha do arquivo sendo uma string
        lista_palavras = palavras.readlines()

        #gerar número aleatório 
        number_palavra = random.randint(0, len(lista_palavras))

        # escolher palavra específica na lista de palavras
        palavra = lista_palavras[number_palavra]
        return palavra






        
        
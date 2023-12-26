import os
from Artigos import Artigo
class Mercado:
    #Construtor
    def __init__(self):
        pass

    #Adiciona um novo artigo
    def adicionar_artigo(self, artigo):
        pass

    #Elimina um artigo
    def remover_artigo(self, artigo):
        pass

    #Mostra o nome, preço e quantidade do artigo recebido
    def mostrar_artigo(self, artigo):
        os.system('cls')
        print(artigo.nome,'\nPreço:', artigo.mostrar_preco(), '\nQuantidade:', artigo.mostrar_quantidade())


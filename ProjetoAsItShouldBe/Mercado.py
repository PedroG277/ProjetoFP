import os
from Artigos2 import Artigo

class Mercado:
    #Construtor
    def __init__(self):
        pass

    #Adiciona um novo artigo
    def adicionar_artigo(self, artigo):
        propriedades = artigo.split(',')
        novo_artigo = Artigo(propriedades[0], int(propriedades[2]), propriedades[1], int(propriedades[3]))


        return novo_artigo
        

    #Elimina um artigo
    def remover_artigo(self, artigo):
        pass

    #Mostra o nome, preço e quantidade do artigo recebido
    def mostrar_artigo(self, artigo):
        print('Artigo: ', artigo.nome, ', Preço: ', int(artigo.preco), ', Tipologia: ', artigo.tipologia, ', Quantidade: ', artigo.quantidade, sep='')


from Artigos import Artigo
from Utilizadores import Utilizador
import pickle

class FeiraVirtual:    
    #Construtor
    def __init__(self, ListaArtigos=[], ListaUtilizadores=[]):
        self.ListaArtigos = ListaArtigos
        self.ListaUtilizadores = ListaUtilizadores
        self.importar_utilizadores('utilizadoresartigos.txt')

    #Adiciona um novo utilizador recebendo o nome, interesses e artigos
    def registar_utilizador (self, nome, interesses, artigos_disponiveis):
        self.nome = nome
        self.interesses = interesses
        self.artigos_disponiveis = artigos_disponiveis

        nome = str(input('Insira o seu primeiro nome. Será o seu nome de utilizador.'))
        interesses = str(input('Insira os seus intereses.'))
        artigos_disponiveis = str(input('Insira os ertigos que tem para venda'))


    #Importa uma lista de utilizadores a partir de um ficheiro
    def importar_utilizadores(self, nome_ficheiro):
        ListaDados = []
        with open(nome_ficheiro, 'r') as file:
            for line in file:
                line = line.replace('[', '')
                line = line.replace(']', '')
                line = line.strip('\n')

                Entry = []
                parametros = line.split(';')

                vendedor = parametros[0]

                interesses = (parametros[1].split(','))

                if parametros[2] == "\n": #o utilizador não tem produdos associados
                    artigos = ['']
                else:
                    artigos = parametros[2].split('&')

                self.ListaUtilizadores.append(Utilizador(vendedor, interesses, artigos))

                conjArtigos = []
                for l in range(len(artigos)):
                    conjArtigos.append(artigos[l].split(','))
                    if conjArtigos[l] != ['']:
                        self.ListaArtigos.append(Artigo(conjArtigos[l][0], conjArtigos[l][1], conjArtigos[l][2], conjArtigos[l][3], vendedor))


    #Elimina um utilizador
    def eliminar_conta(self, nome_utilizador):
        pass


    #Apresenta todos os artigos disponíveis ordenados por preço
    def listar_artigos(self):
        artigosOrdenados = sorted(self.ListaArtigos, key=lambda x: int(x.preco))
        for j in artigosOrdenados:
            print(j.nome, j.preco)

    #Efetua uma compra de um artigo. O comprador e o vendedor são os nomes de dois utilizadores registados
    def comprar_artigo(self, comprador, vendedor, artigo):
        self.comprador = comprador
        self.vendedor = vendedor
        self.artigo = artigo

    #Calcula a reputação de um utilizador com base nas suas avaliações
    def calcular_reputacao(self, utilizador):
        pass

    #Coloca um artigo à venda. O vendedor é o nome de um utilizador
    def colocar_artigo_para_venda(self, vendedor, artigo, preco, tipologia, quantidade):
        self.vendedor = vendedor
        self.artigo = artigo
        self.preco = preco
        self.tipologia = tipologia
        self.quantidade = quantidade


        self.ListaArtigos.append(Artigo(self.artigo, self.preco, self.tipologia, self.quantidade, self.vendedor))        

        
    #Encontra os nomes de utilizadores interessados no artigo recebido
    def encontrar_compradores_interessados(self, artigo):
        pass

    #Exporta a lista de artigos para um ficheiro ordenados por quantidade
    def exportar_artigos_preco(self, nome_ficheiro):
        with open(nome_ficheiro, "w") as file:
            artigosOrdenados = sorted(self.ListaArtigos, key=lambda x: int(x.preco))
            for artigo in artigosOrdenados:
                file.write(f"{artigo.nome};{artigo.tipologia};{artigo.preco};{artigo.vendedor}\n")



    #Exporta a lista de utilizadores para um ficheiro ordenados por reputação
    def exportar_utilizadores(self, nome_ficheiro):
        with open(nome_ficheiro, "w") as file:
            for user in self.ListaUtilizadores:
                file.write(f"{user.nome};{user.interesses};{user.artigos_disponiveis}\n")

    #Início da feira. O grupo deve apresentar testes do projeto nesta função
    def main():
        pass






    main()
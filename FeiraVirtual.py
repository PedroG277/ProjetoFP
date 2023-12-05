#Construtor
def __init__(self):
    pass

#Adiciona um novo utilizador recebendo o nome, interesses e artigos
def registar_utilizador (self, nome, interesses, artigos_disponiveis):
    pass

#Importa uma lista de utilizadores a partir de um ficheiro
def importar_utilizadores(self, nome_ficheiro):
    pass

#Importa uma lista de artigos a partir de um ficheiro
def importar_artigos(self, nome_ficheiro):
    pass

#Elimina um utilizador
def eliminar_conta(self, nome_utilizador):
    pass

#Apresenta todos os artigos disponíveis ordenados por preço
def listar_artigos(self):
    pass

#Efetua uma compra de um artigo. O comprador e o vendedor são os nomes de dois utilizadores registados
def comprar_artigo(self, comprador, vendedor, artigo):
    pass

#Calcula a reputação de um utilizador com base nas suas avaliações
def calcular_reputacao(self, utilizador):
    pass

#Coloca um artigo à venda. O vendedor é o nome de um utilizador
def colocar_artigo_para_venda(self, vendedor, artigo, preco):
    pass

#Encontra os nomes de utilizadores interessados no artigo recebido
def encontrar_compradores_interessados(self, artigo):
    pass

#Exporta a lista de artigos para um ficheiro ordenados por quantidade
def exportar_artigos_preco(self, nome_ficheiro):
    pass


#Exporta a lista de utilizadores para um ficheiro ordenados por reputação
def exportar_utilizadores(self):
    pass

#Início da feira. O grupo deve apresentar testes do projeto nesta função
def main():
    print('Bem-vindo/a à Feira Virtual. Pretende aceder a:\n1 - Utilizadores\n2 - Artigos\n3 - Mercado')

main()
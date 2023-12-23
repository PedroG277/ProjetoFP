class Artigo:
    #Construtor
    def __init__(self, nome, preco, tipologia, quantidade, vendedor):
        self.nome = nome
        self.preco = preco
        self.tipologia = tipologia
        self.quantidade = quantidade
        self.vendedor = vendedor
        
    
    #Altera o nome de um artigo para o novo nome recebido
    def editar_nome(self, nome):
        pass
    
    #Altera o preço de um artigo de acordo com a percentagem dada
    def ajustar_preco(self, percentagem_alteracao):
        pass
    
    #Altera o preço para o novo preço recebido
    def editar_preco(self, preco):
        pass
    
    #Apresenta o preço do artigo
    def mostrar_preco(self):
        pass
    
    #Altera a quantidade
    def editar_quantidade(self, nova_quantidade):
        pass
    
    #Apresenta a quantidade do artigo
    def mostrar_quantidade(self):
        pass
    
    #Altera a tipologia
    def editar_tipo (self, novo_tipo):
        pass
    
    #Apresenta a tipologia do artigo
    def mostrar_tipo (self):
        pass
    
class Artigo:
    #Construtor
    def __init__(self, nome, preco, tipologia, quantidade):
        self.nome = nome
        self.preco = preco
        self.tipologia = tipologia
        self.quantidade = quantidade
        self.vendedor = 'nao existe um vendedor'
        self.oferta = 'erro ao determinar oferta'
        

    def atribuirVendedor(self, vendedor):
        self.vendedor = vendedor
        
    def atribuirOferta(self, oferta):
        self.oferta = oferta

    #Altera o nome de um artigo para o novo nome recebido
    def editar_nome(self, nome):
        self.nome = nome
    
    #Altera o preço de um artigo de acordo com a percentagem dada
    def ajustar_preco(self, percentagem_alteracao):
        self.preco = float(self.preco)
        self.preco = self.preco*(percentagem_alteracao/100)
        if percentagem_alteracao < 100:
            self.oferta = 'alta'
        else:
            self.oferta = 'baixa'
    
    #Altera o preço para o novo preço recebido
    def editar_preco(self, preco):
        self.preco = preco
    
    #Apresenta o preço do artigo
    def mostrar_preco(self):
        print('Preço:', self.preco)
    
    #Altera a quantidade
    def editar_quantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade
    
    #Apresenta a quantidade do artigo
    def mostrar_quantidade(self):
        print('Quantidade:', self.quantidade)
    
    #Altera a tipologia
    def editar_tipo (self, novo_tipo):
        self.tipologia = novo_tipo
    
    #Apresenta a tipologia do artigo
    def mostrar_tipo (self):
        print('Tipologia:', self.tipologia)
    
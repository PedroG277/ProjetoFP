class Utilizador:
    #Construtor
    def __init__(self, nome, interesses, artigos_disponiveis): #[[3, 'leccalecca'], [2, 'liccalicca']]
        self.nome = nome
        self.interesses = interesses
        self.artigos_disponiveis = artigos_disponiveis
        self.pycoins = 50
        self.avaliacoes_comentarios = []
    #Altera os interesses e/ou os artigos de um utilizador
    def editar_conta(self, novos_interesses, novos_artigos):
        self.novos_interesses = novos_interesses
        self.novos_artigos = novos_artigos
    
    #Adiciona uma nova avaliação, podendo incluir um comentário
    def deixar_avaliacao(self, estrelas, comentario):
        self.avaliacoes_comentarios.append([estrelas, comentario])

        
       
    
    #Apresenta todas as avaliações e comentários (juntos)
    def listar_avaliacoes(self):
        print(self.avaliacoes)
        # for avaliacoes in range(self.avaliacoes):
        #     print(avaliacoes)
        # for comentarios in range(self.comentarios):
        #     print(comentarios)    
    
    #Apresenta todos os interesses
    def mostrar_interesses(self):
        print('Os interesses são:', self.interesses)
    
    #Apresenta todos os artigos
    def mostrar_artigos(self):
        print(self.artigos_disponiveis)
    
    #Altera o número de pycoins
    def alterar_pycoins(self, numero_pycoins):
        self.pycoins = numero_pycoins
        
    
    #Apresenta o número de pycoins
    def mostrar_pycoins(self):
        print('O seu número de pycoins é:', self.pycoins)
    
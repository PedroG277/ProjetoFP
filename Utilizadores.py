class Utilizador:
    #Construtor
    def __init__(self, nome, interesses, artigos_disponiveis, pycoins):#, reputacao, comentarios):
        self.nome = nome
        self.interesses = interesses
        self.artigos_disponiveis = artigos_disponiveis
        self.pycoins = pycoins
        #self.reputacao = reputacao
        #self.comentarios = comentarios
    
    #Altera os interesses e/ou os artigos de um utilizador
    def editar_conta(self, novos_interesses, novos_artigos):
        self.novos_interesses = novos_interesses
        self.novos_artigos = novos_artigos
    
    #Adiciona uma nova avaliação, podendo incluir um comentário
    def deixar_avaliacao(self, estrelas):
        self.estrelas = estrelas
        estrelas = int(input('Quer avaliar este utilizador? \n 1-Sim 2-Não'))
        if estrelas == 1:
            estrelas = int(input('Como quer avaliar este utilizador? \n Escolha entre 1-5 estrelas.'))
        else:
            estrelas = "Não foi avaliado"
        
        
        # self.comentario = comentario
        # comentario = int(input('Quer deixar o seu comentário? \n 1-Sim 2-Não'))
        # if comentario == 1:
        #     comentario = str(input('Deixe o seu comentário'))
        # else:
        #     comentario = "Não foi deixado nenhum comentário"
        
    
    #Apresenta todas as avaliações e comentários
    def listar_avaliacoes(self):
        pass
    
    #Apresenta todos os interesses
    def mostrar_interesses(self):
        pass
    
    #Apresenta todos os artigos
    def mostrar_artigos(self):
        pass
    
    #Altera o número de pycoins
    def alterar_pycoins(self, numero_pycoins):
        self.numero_pycoins = numero_pycoins
        
    
    #Apresenta o número de pycoins
    def mostrar_pycoins(self):
        pass
    
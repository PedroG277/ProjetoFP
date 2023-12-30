import os
class Utilizador:
    #Construtor
    def __init__(self, nome, interesses, artigos_disponiveis): #[[3, 'leccalecca'], [2, 'liccalicca']]
        self.nome = nome
        self.interesses = interesses
        self.artigos_disponiveis = artigos_disponiveis
        self.pycoins = 50
        self.avaliacoes_comentarios = []
        self.reputacao = 0
    #Altera os interesses e/ou os artigos de um utilizador
    def editar_conta(self, novos_interesses, novos_artigos):
        self.novos_interesses = novos_interesses
        self.novos_artigos = novos_artigos
    
    #Adiciona uma nova avaliação, podendo incluir um comentário
    def deixar_avaliacao(self, estrelas, comentario):
        self.avaliacoes_comentarios.append([estrelas, comentario])

        
       
    
    #Apresenta todas as avaliações e comentários (juntos)
    def listar_avaliacoes(self):
        if self.avaliacoes_comentarios == []:
            os.system('cls')
            print('Ainda não tem avaliações!')

        try:
            for avaliacoes in self.avaliacoes_comentarios:
                print('Estrelas:', str(avaliacoes[0]), '\nComentário:', str(avaliacoes[1]), '\n-----')
        except IndexError:
            os.system('cls')
            print('Ainda não tem avaliações!')


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
        print('Pycoins:', self.pycoins)
    
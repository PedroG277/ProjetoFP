#Construtor
def __init__(self, nome, interesses, artigos_disponiveis):
    self.nome = nome
    self.interesses = interesses
    self.artigos_disponiveis = artigos_disponiveis

#Altera os interesses e/ou os artigos de um utilizador
def editar_conta(self, novos_interesses, novos_artigos):
    self.novos_interesses = novos_interesses
    self.novos_artigos = novos_artigos

#Adiciona uma nova avaliação, podendo incluir um comentário
def deixar_avaliacao(self, estrelas, comentario):
    self.estrelas = estrelas
    self.comentario = comentario

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

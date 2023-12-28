class Utilizador:
    #Construtor
    def __init__(self, nome, interesses, artigos_disponiveis):
        self.nome = nome
        self.interesses = interesses
        self.artigos_disponiveis = artigos_disponiveis
        
        self.pycoins = 50

    #Altera os interesses e/ou os artigos de um utilizador
    def editar_conta(self, novos_interesses, novos_artigos):
        self.novos_interesses = novos_interesses
        self.novos_artigos = novos_artigos

    #Adiciona uma nova avaliação, podendo incluir um comentário
    def deixar_avaliacao(self, estrelas, comentario):
        self.avaliacoes_comentarios.append([estrelas, comentario])

    #Apresenta todas as avaliações e comentários
    def listar_avaliacoes(self):
        pass

    #Apresenta todos os interesses
    def mostrar_interesses(self):
        conjInteresses = ''
        for i in range(len(self.interesses)):
            conjInteresses += 'Interesse ' + str(i+1) + ': ' + str(self.interesses[i]) + ', '
        conjInteresses = conjInteresses.strip(', ')
        print(conjInteresses)

    #Apresenta todos os artigos
    def mostrar_artigos(self):
        for artigo in self.artigos_disponiveis:
            print('Artigo: ', artigo.nome, ', Preço: ', int(artigo.preco), ', Tipologia: ', artigo.tipologia, ', Quantidade: ', artigo.quantidade, sep='')

    #Altera o número de pycoins
    def alterar_pycoins(self, numero_pycoins):
        self.numero_pycoins = numero_pycoins

    #Apresenta o número de pycoins
    def mostrar_pycoins(self):
        print('Pycoins:', self.numero_pycoins)

from Artigos import Artigo
from Utilizadores import Utilizador

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


                conjArtigos = []
                ListaDeArtigosDoUtilizador = []
                for l in range(len(artigos)):
                    conjArtigos.append(artigos[l].split(','))
                    if conjArtigos[l] != ['']:
                        artigo = Artigo(conjArtigos[l][0], conjArtigos[l][1], conjArtigos[l][2], conjArtigos[l][3], vendedor)
                        self.ListaArtigos.append(artigo)
                        ListaDeArtigosDoUtilizador.append(artigo)
                
                
                self.ListaUtilizadores.append(Utilizador(vendedor, interesses, ListaDeArtigosDoUtilizador))


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
    def main(self):
        userPrompt = ">> "
        voltarOuSair = "\n V - Voltar a trás \n S - Sair \n"
        perguntaUtilizadores = " Pretende aceder a: \n" \
            + " 1-Registo de Utilizadores\n" \
            + " 2-Alteração de um utilizador\n" \
            + " 3-Eliminação de conta de um utilizador\n" \
            + " 4-Lista de utilizadores\n" \
            + " 5-Mostrar artigos de um utilizador\n" \
            + " 6-Mostrar interesses de um utilizador\n" \
            + " 7-Mostrar Pycoins de um utilizador"
        perguntaArtigos = " Pretende aceder a: \n1 – Mostrar preço de um artigo \n 2 – Mostrar quantidade de um artigo \n 3 – Mostrar tipo de um artigo"
        
        closed = False
        while not closed:
            print("Bem vindo à Feira Virtual. Pretende: \n 1-LogIn \n 2-Criar Conta")
            match input(userPrompt):
                case '1': #CAGUEI E NAO ACABEI ISTO PORQUE NAO TAVA MEMO A DAR
                    logginin = True
                    while logginin:
                        inputNome = input("Nome de Utilizador:")
                        for i in self.ListaUtilizadores:
                            print(i.nome)
                            if i.nome == inputNome:
                                TheUtilizador = i
                                foundUser = True
                                break
                        if not foundUser:
                            print('Não existe uma conta com esse nome. Pode:\n1-Introduzir Novamente\n2-Criar Conta')
                            resposta = input(userPrompt)
                        if resposta == '1':
                            break
                        elif resposta == '2':
                                logginin = False
                                break


                    print(perguntaUtilizadores, voltarOuSair) 
                    resposta = input(userPrompt)
                    print("respondeu =", resposta)
                    if resposta == '4':
                        for i in self.ListaUtilizadores:
                            print(i.nome)
                    if resposta.upper() == 'S':
                        closed = True
                        continue
                    if resposta.upper() == 'V':
                        continue
                
                case '2':
                    self.listar_artigos()

                    print(perguntaArtigos, voltarOuSair) #caga nisto q n tá de acordo c aquele guia q tá no one note, dps mudo o q for preciso :)
                    resposta2 = input(userPrompt) #o meu cérebro já não tá capaz são quase 3 
                    print("respondeu =", resposta2)
                    if resposta2.upper() == 'S':
                        closed = True
                        continue
                    if resposta2.upper() == 'V':
                        continue
                    
                case '3':
                    print("merc")
                



                case 's':
                    closed = True


                case _:
                    print("Not a valid input")
            
    
    
TheFeira = FeiraVirtual()
TheFeira.main()

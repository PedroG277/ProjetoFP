from Artigos2 import Artigo
from Utilizadores import Utilizador
from Mercado import Mercado

import os

class FeiraVirtual:
    #Construtor
    def __init__(self):
        self.ListaArtigos = []
        self.ListaUtilizadores = []
        
        self.importar_utilizadores('utilizadoresartigos.txt')

    #Adiciona um novo utilizador recebendo o nome, interesses e artigos
    def registar_utilizador (self, nome, interesses, artigos_disponiveis):
        self.nome = nome 
        self.interesses = interesses
        self.artigos_disponiveis = artigos_disponiveis

    #Importa uma lista de artigos a partir de um ficheiro (REMOVIDA)
    def importar_utilizadores(self, nome_ficheiro):
        with open(nome_ficheiro, 'r') as file:
            for line in file:
                line = line.replace('[', '')
                line = line.replace(']', '')
                line = line.strip('\n')

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
                        artigo = Artigo(conjArtigos[l][0], float(conjArtigos[l][1]), conjArtigos[l][2], int(conjArtigos[l][3]))
                        self.ListaArtigos.append(artigo)
                        ListaDeArtigosDoUtilizador.append(artigo)
                
                try:
                    pycoins = parametros[3]
                except IndexError:
                    pycoins = 50

                try:
                    avcoms = parametros[4]
                    avcoms = avcoms.split('&')

                    conjAvcoms = []
                    for m in range(len(avcoms)):
                        AvComSep = avcoms[m].split(',')
                        conjAvcoms.append(AvComSep)
                except IndexError:
                    conjAvcoms = ''
                
                
                self.ListaUtilizadores.append(Utilizador(vendedor, interesses, ListaDeArtigosDoUtilizador))

        #for artg in self.ListaArtigos:
        #    self.definir_Ajustes_preco(artg)

    #Elimina um utilizador
    def eliminar_conta(self, nome_utilizador):
        os.system('cls')

        utilizador_a_apagar = self.getUser(nome_utilizador)
            
        for artigo in utilizador_a_apagar.artigos_disponiveis:
            self.ListaArtigos.remove(artigo)

        self.ListaUtilizadores.remove(utilizador_a_apagar)

        #self.exportar_tudo('utilizadoresartigos.txt')

    #Apresenta todos os artigos disponíveis ordenados por preço
    def listar_artigos(self):
        artigosParaMostrar = []
        nomesUnicos = []
        for artigo in self.ListaArtigos:
            unico = True
            for nome in nomesUnicos:
                if artigo.nome == nome:
                    unico = False
                    break
            if unico == True:
                nomesUnicos.append(artigo.nome)
                artigosParaMostrar.append(artigo)

        artigosOrdenados = sorted(artigosParaMostrar, key=lambda x: float(x.preco))

        os.system('cls')
        print('Artigos Disponíveis no Mercado:')
        for j in range(len(artigosOrdenados)):
            print(j+1, '. ', sep='', end='')
            TheMercado.mostrar_artigo(artigosOrdenados[j])

    def listar_utilizadores(self):
        for user in self.ListaUtilizadores:
            print(user.nome)

    #Efetua uma compra de um artigo. O comprador e o vendedor são os nomes de dois utilizadores registados
    def comprar_artigo(self, comprador, vendedor, artigo):
        self.comprador = comprador
        self.vendedor = vendedor
        self.artigo = artigo

    #Calcula a reputação de um utilizador com base nas suas avaliações
    def calcular_reputacao(self, utilizador):
        pass

    #Coloca um artigo à venda. O vendedor é o nome de um utilizador
    def colocar_artigo_para_venda(self, vendedor, artigo, preco):
        self.vendedor = vendedor
        self.artigo = artigo
        self.preco = preco 

    #Encontra os nomes de utilizadores interessados no artigo recebido
    def encontrar_compradores_interessados(self, artigo):
        pass

    #Exporta a lista de artigos para um ficheiro ordenados por quantidade
    def exportar_artigos_preco(self, nome_ficheiro):
        pass
    
    #Exporta a lista de utilizadores para um ficheiro ordenados por reputação
    def exportar_utilizadores(self):
        pass


    def getUser(self, nome):
        for user in self.ListaUtilizadores:
            if user.nome == nome:
                return user
            
    
    def getArtigo(self, nome):
        for artigo in self.ListaArtigos:
            if artigo.nome == nome:
                return artigo

    #Início da feira. O grupo deve apresentar testes do projeto nesta função
def main():
    def inicio(frase):
        print(frase + '\n1 - Utilizadores\n2 - Artigos\n3 - Mercado')
        match input():
            case '1':
                paginaUtilizadores()
            case '2':
                paginaArtigos()
            case '3':
                paginaMercado()
    def paginaUtilizadores():
        os.system('cls')
        print('Pretende aceder a:\n1 – Registo de utilizadores\n2 – Alteração de um utilizador\n3 – Eliminação de conta de um utilizador\n4 – Lista de utilizadores\n5 – Mostrar artigos de um utilizador\n6 – Mostrar interesses de um utilizador\n7 – Mostrar Pycoins de um utilizador\nV – Voltar atrás\nS – Sair')
        match input():
            case '1':
                paginaRegisto()
            case '2':
                pass
            case '3': #eliminar conta
                paginaApagarUtilizador()
            case '4': #lista utilizadores
                paginaListarUtilizadores()
            case '5':
                paginaConsultarArtigos()
            case '6':
                paginaMostrarInteresses()
            case '7':
                paginaMostrarPycoins()
            case 'V':
                inicio('Pretende aceder a:')
            case 'S':
                exit()
    def paginaRegisto():
        os.system('cls')
        print('Pretende aceder a:\n1 – Registo manual\n2 – Registo por ficheiro')
        match input():
            case '1':
                pass
            case '2':
                os.system('cls')
                TheFeira.importar_utilizadores('utilizadoresartigos.txt')
                print('Registo criado com sucesso.')
                inicio('Pretende aceder a:')


    def paginaApagarUtilizador():
        print('Introduza o nome do utilizador que deseja eliminar')
        utilizadorEscolhido = input()
        TheFeira.eliminar_conta(utilizadorEscolhido)
        print('Utilizador eliminado com sucesso.')
        inicio('Pretende aceder a:')

    def paginaListarUtilizadores():
        os.system('cls')
        print('Estes são os utilizadores registados na FeiraVirtual:')
        TheFeira.listar_utilizadores()
        inicio('Pretende aceder a:')

    def paginaConsultarArtigos():
        os.system('cls')
        print('Introduza um utilizador para consultar os seus artigos:')
        nomeIntroduzido = input()
        TheFeira.getUser(nomeIntroduzido).mostrar_artigos()
        
        inicio('Pretende aceder a:')
        
    def paginaMostrarInteresses():
        os.system('cls')
        print('Introduza um utilizador para consultar os seus interesses:')
        nomeIntroduzido = input()
        TheFeira.getUser(nomeIntroduzido).mostrar_interesses()

        inicio('Pretende aceder a:') 
#Interesse 1: Tecnologia, Interesse 2: Moda
        
        #mostrar pycoins de um utiliador 
    def paginaMostrarPycoins():
        os.system('cls')
        print('Introduza um nome de utilizador para consultar os seus Pycoins:')
        nomeIntroduzido = input()
        TheFeira.getUser(nomeIntroduzido).mostrar_pycoins()
        inicio('Pretende aceder a:')
    





    def paginaArtigos():
        print('Pretende aceder a:\n1 – Mostrar preço de um artigo\n2 – Mostrar quantidade de um artigo\n3 – Mostrar tipo de um artigo\nV – Voltar atrás\nS – Sair')

        match input():
            case '1':
                paginaMostarPeco()
            case '2':
                paginaMostrarQuantidade()
            case '3':
                paginaMostarTipo()
            case 'V':
                inicio('Pretende aceder a:')
            case 'S':
                exit()
        
    def paginaMostarPeco():
        os.system('cls')
        print('Introduza o artigo que deseja ver o preço:')
        artigoIntroduzido = input()
        TheFeira.getArtigo(artigoIntroduzido).mostrar_preco()
        inicio('Pretende aceder a:')
        
    def paginaMostrarQuantidade():
        os.system('cls')
        print('Introduza o artigo que deseja ver a sua quantidade:')
        artigoIntroduzido = input()
        TheFeira.getArtigo(artigoIntroduzido).mostrar_quantidade()
        inicio('Pretende aceder a:')

    def paginaMostarTipo():
        os.system('cls')
        print('Introduza o artigo que deseja ver a tipologia:')
        artigoIntroduzido = input()
        TheFeira.getArtigo(artigoIntroduzido).mostrar_tipo()
        inicio('Pretende aceder a:')







    def paginaMercado():
        print('Pretende aceder a:\n1 – Adicionar Artigo ao Mercado\n2 – Remover Artigo do Mercado\n3 – Listar Artigos do Mercado\nV – Voltar atrás\nS – Sair')
        
        match input():
            case '1':
                paginaAdicionarArtigo()
            case '2':
                paginaRemoverArtigo()
            case '3':
                TheFeira.listar_artigos()
            case 'V':
                inicio('Pretende aceder a:')
            case 'S':
                exit()

    def paginaAdicionarArtigo():
    
        os.system('cls')
        TheFeira.ListaArtigos.append(TheMercado.adicionar_artigo(input('Insira os detalhes do artigo para adicionar ao mercado (nome, tipologia, preço, quantidade):')))
        inicio('Pretende aceder a:')
    
    def paginaRemoverArtigo():
        pass


          
    inicio('Bem-vindo/a à Feira Virtual. Pretende aceder a:')
TheFeira = FeiraVirtual()
TheMercado = Mercado()

main()
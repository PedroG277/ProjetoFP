import os

from Artigos import Artigo
from Utilizadores import Utilizador
from Mercado import Mercado

class FeiraVirtual:    
    #Construtor
    def __init__(self, TheUtilizador = Utilizador('', [], [], 0, []), ListaArtigos=[], ListaUtilizadores=[]):
        self.ListaArtigos = ListaArtigos
        self.ListaUtilizadores = ListaUtilizadores
        self.TheUtilizador = TheUtilizador
        self.importar_utilizadores('utilizadoresartigos.txt')

    #Adiciona um novo utilizador recebendo o nome, interesses e artigos
    def registar_utilizador (self, nome = '', interesses = '', artigos_disponiveis = ''):
        self.nome = nome
        self.interesses = interesses
        self.artigos_disponiveis = artigos_disponiveis

        nome = str(input('Insira o seu primeiro nome. Será o seu nome de utilizador.\n>> '))
        interesses = []
        interesses.append(str(input('Insira os seus intereses.')))
        while True:
            novo_interesse = input('Pode introduzir outro interesse, ou escrever "s" para concluir.\n>> ')
            match novo_interesse:
                case 's':
                    break
                case _:
                    interesses.append(novo_interesse)

        novoUtilizador = Utilizador(nome, interesses, [], 50, [])
        self.ListaUtilizadores.append(novoUtilizador)

        match input('Quer adicionar artigos para vender?\n1-Sim\n2-Não\n>> '):
            case '1':
                while True:
                    self.colocar_artigo_para_venda(novoUtilizador, input('Nome:'), input('Preço:'), input('Tipologia:'), input('Quantidade:'))
                    match input('Quer adicionar mais artigos?\n1-Sim\n2-Não\n>> '):
                        case '1':
                            continue
                        case '2':
                            break    
            case '2':
                artigos_disponiveis = []


        
        self.exportar_tudo('exportTest.txt')


    #Importa uma lista de utilizadores a partir de um ficheiro
    def importar_utilizadores(self, nome_ficheiro):
        ListaDados = []
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
                        artigo = Artigo(conjArtigos[l][0], int(conjArtigos[l][1]), conjArtigos[l][2], int(conjArtigos[l][3]), vendedor)
                        self.ListaArtigos.append(artigo)
                        ListaDeArtigosDoUtilizador.append(artigo)
                
                
                self.ListaUtilizadores.append(Utilizador(vendedor, interesses, ListaDeArtigosDoUtilizador, 50, []))


    #Elimina um utilizador
    def eliminar_conta(self, nome_utilizador):
        os.system('cls')



    #Apresenta todos os artigos disponíveis ordenados por preço
    def listar_artigos(self):
        artigosOrdenados = sorted(self.ListaArtigos, key=lambda x: int(x.preco))
        for j in artigosOrdenados:
            print(j.nome, j.preco)

    #Efetua uma compra de um artigo. O comprador e o vendedor são os nomes de dois utilizadores registados (e deixar um comentário)
    def comprar_artigo(self, comprador, vendedor, artigo):
        os.system('cls')
        if int(comprador.pycoins) < int(artigo.preco):
            print('Não tem pycoins suficientes!')
        else:
            comprador.pycoins -= artigo.preco
            vendedor.pycoins += artigo.preco
            artigo.quantidade -= 1
            if artigo.quantidade == 0:
                self.ListaArtigos.remove(artigo)
            print('Compra efetuada com sucesso!')
            print('Saldo restante:', self.TheUtilizador.pycoins)
            
            # deixar avaliação
            avaliacoes = int(input('Quer avaliar este utilizador? \n 1-Sim 2-Não'))
            if avaliacoes == 1:
                avaliacoes = int(input('Como quer avaliar este utilizador? \n Escolha entre 1-5 estrelas.'))
            else:
                avaliacoes = "Não foi avaliado" 

            comentario = int(input('Quer deixar o seu comentário? \n 1-Sim 2-Não'))
            if comentario == 1:
                comentario = str(input('Deixe o seu comentário'))
            else:
                comentario = "Não foi deixado nenhum comentário"
           
            vendedor.deixar_avaliacao(avaliacoes, comentario)

            #print(self.ListaUtilizadores[7].avaliacoes_comentarios)

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

        novoArtigo = Artigo(self.artigo, self.preco, self.tipologia, self.quantidade, self.vendedor)
        self.ListaArtigos.append(novoArtigo)
        vendedor.artigos_disponiveis.append(novoArtigo)        

        
    #Encontra os nomes de utilizadores interessados no artigo recebido
    def encontrar_compradores_interessados(self, artigo):
        pass

    #Exporta a lista de artigos para um ficheiro ordenados por quantidade
    def exportar_artigos_preco(self, nome_ficheiro):
        with open(nome_ficheiro, "w") as file:
            artigosOrdenados = sorted(self.ListaArtigos, key=lambda x: int(x.preco))
            for artigo in artigosOrdenados:
                file.write(f"{artigo.nome};{artigo.preco};{artigo.tipologia};{artigo.quantidade};{artigo.vendedor}\n")



    #Exporta a lista de utilizadores para um ficheiro ordenados por reputação
    def exportar_utilizadores(self, nome_ficheiro):
        with open(nome_ficheiro, "w") as file:
            for user in self.ListaUtilizadores:
                info = []
                infoArtigos = []
                for artigo in user.artigos_disponiveis:
                    info = []
                    info.append(artigo.nome)
                    info.append(artigo.preco)
                    info.append(artigo.tipologia)
                    info.append(artigo.quantidade)

                    infoArtigos.append(info)

                file.write(f"{user.nome};{user.interesses};{infoArtigos}\n")


    def exportar_tudo(self, nome_ficheiro):
        with open(nome_ficheiro, 'w') as file:
            for user in self.ListaUtilizadores:
                interesses = (str(user.interesses).replace("'", "")).replace(" ", "")
                artigos = '['
                
                for artigo in user.artigos_disponiveis:
                    artigos = artigos + f"{artigo.nome},{artigo.preco},{artigo.tipologia},{artigo.quantidade}&"
                artigos = artigos.strip('&')
                artigos += ']'
                file.write(f"{user.nome};{interesses};{artigos}\n")


    def GetUser(self, actionPrompt, adminExcept = 'Não pode fazer esta ação ao Administrador', notFoundExept =  'Não foi encontrado nenhum utilizador com esse nome.', logIn = False): #Entra uma string, sai 'admin' se admin, Utilizador (objeto) se nome válido, False se nome inválido
        def checkUser(UserName):
            if UserName == 'admin':
                return 'admin'
            else:
                for i in self.ListaUtilizadores:
                    if i.nome == UserName:
                        return i
                return False
        
        while True:
            getuser = checkUser(input(actionPrompt + '\n>> '))
            if isinstance(getuser, Utilizador):
                return getuser
            else:
                if getuser == 'admin':
                    if not logIn:
                        print(adminExcept)
                    else:
                        return 'admin'
                elif getuser == False:
                    print(notFoundExept)

                if not logIn:
                    print('Pode:\n1-Introduzir novamente\n2-Cancelar')
                    match input('>> '):
                        case '1':
                            os.system('cls')
                            continue
                        case '2':
                            break
                else:
                    print('Pode:\n1-Introduzir novamente\n2-Criar Conta')
                    match input('>> '):
                        case '1':
                            os.system('cls')
                            continue
                        case '2':
                            self.registar_utilizador()
                            break                    


    def LogIn(self):
      return self.GetUser('Para fazer LogIn, introduza o seu nome de utilizador.', logIn=True)     
            
        
    def adminPage(self):
        os.system('cls')
        print(" 1-Eliminação de conta de um utilizador\n" \
            + " 2-Lista de utilizadores\n" \
            + " 3-Mostrar artigos de um utilizador\n" \
            + " 4-Mostrar interesses de um utilizador\n" \
            + " 5-Mostrar Pycoins de um utilizador")
        
        match input('>> '):
            case '1': #Eliminar utilizador
                self.eliminar_conta('')
                self.adminPage()
                
            case '2': #Listar/Exportar utilizadores
                os.system('cls')
                match input(('Pretende:\n1-Mostrar a lista de utilizadores\n2-Exportar a lista de utilizadores\n>> ')):
                    case '1':
                        pass
                    case '2':
                        self.exportar_utilizadores('users.txt')

            case '3': #Mostrar artigos de um utilizador
                user = self.GetUser('Introduza um utilizador para consultar os seus artigos.')
                for artigo in user.artigos_disponiveis:
                    print(artigo.nome)

            case '4': #Mostrar interesses de um utilizador
                user = self.GetUser('Introduza um utilizador para consultar os seus interesses.')
                count = 0
                conjInteresses = ''
                for interesse in user.interesses:
                    count += 1
                    conjInteresses = conjInteresses + 'Interesse ' + str(count) + ': ' + interesse + ', '
                print(conjInteresses.strip(', '))


            case '5':
                user = self.GetUser('Introduza um utilizador para consultar as suas PyCoins.')
                print(user.pycoins)

        

    #Início da feira. O grupo deve apresentar testes do projeto nesta função
    def main(self):
        userPrompt = ">> "
        # voltarOuSair = "\n V - Voltar a trás \n S - Sair \n"


        def start():
            print("Bem vindo à Feira Virtual. Pretende: \n 1-LogIn \n 2-Criar Conta")
            match input(userPrompt):
                case '1':
                    os.system('cls')
                    self.TheUtilizador = self.LogIn()
                    if self.TheUtilizador == 'admin':
                        self.adminPage()
                    else:
                        home()

                case '2':
                    os.system('cls')
                    self.registar_utilizador()   


        
        def home():
            print("Olá,", self.TheUtilizador.nome, ". Pretende aceder a: \n 1-Navegar Loja \n 2-Espaço pessoal")
            match input(userPrompt):
                case '1':
                    verLoja()
                case '2':
                    espaçoPessoal()

                    

        
        def verLoja():
            print('Produtos disponíves na Loja:         PyCoins:', self.TheUtilizador.pycoins)
            self.listar_artigos()

            print('Voltar: s; Ver apenas produtos dos meus interesses: i; Ver produto: escreva o nome do produto' )
            escolha = input(userPrompt)
            match escolha:
                case 's':
                    pass
                case 'i':
                    pass
                case _:
                    for i in self.ListaArtigos:
                        if escolha == i.nome:
                            TheMercado.mostrar_artigo(i)
                            print('1-Comprar Artigo\n2-Voltar')
                            escolha = input(userPrompt)
                            match escolha:
                                case '1': #COMPRAR ARTIGO
                                    for a in self.ListaUtilizadores:
                                        if a.nome == i.vendedor:
                                            vendedeiro = a
                                            break

                                    self.comprar_artigo(self.TheUtilizador, vendedeiro, i)
                                    print('Pretende:\n1-Voltar à loja\n2-Sair')
                                    match input('>> '):
                                        case '1':
                                            verLoja()
                                        case '2':
                                            home()
                                case '2':
                                    verLoja()


        def espaçoPessoal(): #1-adicionar artigo,2-ver avaliações,3-alterar interesses,4-apagar conta
            print("Pretende aceder a:\n 1-Adicionar artigo \n 2-Ver avaliações \n 3-Alterar interesses \n 4-Apagar conta")
            escolha = input(userPrompt)
            match escolha:
                case '1': #adicionar artigo
                    self.colocar_artigo_para_venda(self.TheUtilizador, input('Nome:'), input('Preço:'), input('Tipologia:'), input('Quantidade:'))
                case '2': #ver avaliações
                    self.TheUtilizador.listar_avaliacoes()
                case '3': #alterar interesses
                    pass
                case '4': #apagar conta
                    pass
                case _:
                    pass





        self.exportar_tudo('exportTest.txt')
        start()

    
TheFeira = FeiraVirtual()
TheMercado = Mercado()
TheFeira.main()

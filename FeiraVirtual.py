import os
from Artigos import Artigo
from Utilizadores import Utilizador
from Mercado import Mercado

class FeiraVirtual:    
    #Construtor
    def __init__(self):
        self.ListaArtigos = []
        self.ListaUtilizadores = []
        self.TheUtilizador = Utilizador('', [], [])
        self.importar_utilizadores('utilizadoresartigos.txt')

    #Adiciona um novo utilizador recebendo o nome, interesses e artigos
    def registar_utilizador (self, nome, interesses, artigos_disponiveis):
        os.system('cls')
        
        novoUtilizador = Utilizador(nome, interesses, artigos_disponiveis)
        self.ListaUtilizadores.append(novoUtilizador)
        self.TheUtilizador = novoUtilizador

        self.exportar_tudo('utilizadoresartigos.txt')


    def setInteresses(self): #criado por nós
        interesses = []
        interesses.append(str(input('Insira os seus intereses.\n>> ')))
        while True:
            novo_interesse = input('Pode introduzir outro interesse, ou escrever "s" para concluir.\n>> ')
            match novo_interesse:
                case 's':
                    break
                case _:
                    interesses.append(novo_interesse)
        return interesses


    #Importa uma lista de utilizadores a partir de um ficheiro
    def importar_utilizadores(self, nome_ficheiro):
        with open(nome_ficheiro, 'r', encoding='utf-8') as file:
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
                        artigo.atribuirVendedor(vendedor)
                        artigo.atribuirOferta('normal')
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
                
                utilizador = Utilizador(vendedor, interesses, ListaDeArtigosDoUtilizador)

                utilizador.alterar_pycoins(float(pycoins))
                utilizador.avaliacoes_comentarios = conjAvcoms
            
                utilizador.reputacao = self.calcular_reputacao(utilizador)
                if isinstance(utilizador.reputacao, str):
                    utilizador.reputacao = 0
                self.ListaUtilizadores.append(utilizador)


        
        
        artigosUnicos = self.getArtigosUnicos()
            
        for bruh in artigosUnicos:
            self.definir_Ajustes_preco_Procura(bruh)
            


    def definir_Ajustes_preco_Procura(self, artigo): #criado por nós
        ocorrencias = self.getOcorrenciasArtigo(artigo.nome)
        #reajustar preço para trabalhar sobre normal
        
        try:
            if ocorrencias[0].oferta == 'baixa':
                precoMaisBaixo = ocorrencias[0].preco/1.25
            elif ocorrencias[0].oferta == 'alta':
                precoMaisBaixo = ocorrencias[0].preco/0.75
            else:
                precoMaisBaixo = ocorrencias[0].preco
        except IndexError:
            return


        quantidade_no_mercado = 0
        for artigoRepetido in ocorrencias:                
            if float(artigoRepetido.preco) < precoMaisBaixo:
                precoMaisBaixo = artigoRepetido.preco
            quantidade_no_mercado += int(artigoRepetido.quantidade)
        #sai deste ciclo o preço mais baixo e a quantidade total no mercado

        for ArtigoRepetido in ocorrencias:
            ArtigoRepetido.preco = precoMaisBaixo
            if quantidade_no_mercado <= 3:
                ArtigoRepetido.ajustar_preco(125)
            elif quantidade_no_mercado >= 10:
                ArtigoRepetido.ajustar_preco(75)
            else:
                artigo.oferta = 'normal'



    #Elimina um utilizador
    def eliminar_conta(self, nome_utilizador):
        if self.TheUtilizador == 'admin':
            while True:
                os.system('cls')
                utilizador_a_apagar = self.getUser(nome_utilizador)
                if utilizador_a_apagar:
                    break
                else:
                    match input('Utilizador não encontrado. Pode:\n 1-Introduzir novamente\n 2-Voltar\n>> '):
                        case '1':
                            return True
                        case '2':
                            return False
        else:
            while True:
                os.system('cls')
                nome = input('Para confirmar, insira o seu nome de utilizador.\n>> ')
                if nome == nome_utilizador:
                    utilizador_a_apagar = self.getUser(nome_utilizador)
                    break
                else:
                    match input('Nome de utilizador incorreto. Apagar conta cancelado. Pode:\n 1-Tentar novamente\n 2-Cancelar\n>> '):
                        case '1':
                            continue
                        case '2':
                            return
            
        for artigo in utilizador_a_apagar.artigos_disponiveis:
            self.ListaArtigos.remove(artigo)

        self.ListaUtilizadores.remove(utilizador_a_apagar)

        self.exportar_tudo('utilizadoresartigos.txt')

        return True

    #Apresenta todos os artigos disponíveis ordenados por preço
    def listar_artigos(self):
        artigosOrdenados = self.ordenarArtigosPorPreco(self.getArtigosUnicos())
        for j in artigosOrdenados:
            print(j.nome, j.preco)

   #mostra os artigos do interesse do utilizador
    def listar_artigos_do_meu_interesse(self):
        artigosUnicos = self.getArtigosUnicos()
        artigosInteressantes = []
        for artigo in artigosUnicos:
            for interesse in self.TheUtilizador.interesses:
                if interesse == artigo.tipologia: 
                    artigosInteressantes.append(artigo)
        
        artigosOrdenados = self.ordenarArtigosPorPreco(artigosInteressantes)
        
        for artigointeressante in artigosOrdenados:
            print(artigointeressante.nome, artigointeressante.preco)   

    #ordena os artigos por preço
    def ordenarArtigosPorPreco(self, listaDeArtigos):
        return sorted(listaDeArtigos, key=lambda x: float(x.preco))


    def getArtigosUnicos(self):
        nomesUnicos = []
        artigosUnicos = []
        for artigo in self.ListaArtigos:
            unico = True
            for nome in nomesUnicos:
                if artigo.nome == nome:
                    unico = False
                    break
            if unico == True:
                nomesUnicos.append(artigo.nome)
                artigosUnicos.append(artigo)

        return artigosUnicos


    def exibir_Artigo_com_Vendedores(self, artigo):
        os.system('cls')
        print(artigo.nome, 'Preço:', artigo.preco)
        print('------------\nVendedores:') 

        infoLista = []
        for occArtigo in self.getOcorrenciasArtigo(artigo.nome):
            reputacao = self.calcular_reputacao(self.getUser(occArtigo.vendedor))
            if isinstance(reputacao, str):
                reputacao = 0
            infoSublista = [occArtigo.vendedor,'\n  Reputação: ', reputacao,  '\n  Quantidade disponível: ', occArtigo.quantidade, '\n']
            infoLista.append(infoSublista)

        InfosOrdenados = sorted(infoLista, key=lambda x: float(x[2]), reverse=True)

        for subInfos in InfosOrdenados:
            for infotexto in subInfos:
                print(infotexto, end='')


    #Efetua uma compra de um artigo. O comprador e o vendedor são os nomes de dois utilizadores registados (e deixar um comentário)
    def comprar_artigo(self, comprador, vendedor, artigo):
        while True:
            os.system('cls')
            print(artigo.nome, ', Preço: ', artigo.preco, '\nVendedor:', vendedor.nome, '\nQuantidade disponível: ', artigo.quantidade, sep='')
            quantidade_a_comprar = int(input('\nQuantas unidades pretende comprar?\n>> '))
            if quantidade_a_comprar > int(artigo.quantidade):
                match input('Essa quantidade não está disponível! Pode:\n 1-Introduzir outro valor\n 2-Cancelar\n>> '):
                    case '1':
                        continue
                    case '2':
                        return
            else:
                break
            
        if float(comprador.pycoins) < (float(artigo.preco)*quantidade_a_comprar):
            print('Não tem pycoins suficientes!')
        else:
            comprador.pycoins -= float(artigo.preco)*quantidade_a_comprar
            vendedor.pycoins += float(artigo.preco)*quantidade_a_comprar
            artigo.quantidade -= quantidade_a_comprar

            if artigo.quantidade == 0:
                self.ListaArtigos.remove(artigo)
                vendedor.artigos_disponiveis.remove(artigo)
                
            self.definir_Ajustes_preco_Procura(artigo)


            print('Saldo restante:', self.TheUtilizador.pycoins)

            # deixar avaliação
            avaliacoes = int(input('Quer avaliar este utilizador? \n 1-Sim 2-Não\n>> '))
            if avaliacoes == 1:
                while True:
                    try: 
                        avaliacoes = int(input('Como quer avaliar este utilizador? \n Escolha entre 1-5 estrelas.\n>> '))
                        if not 1 <= avaliacoes <= 5:
                            print('Número inválido. Insira um número de 1 a 5')
                            continue
                        break
                    except ValueError:
                        print('Número inválido. Insira um número de 1 a 5')

            else:
                avaliacoes = 0

            comentario = int(input('Quer deixar o seu comentário? \n 1-Sim 2-Não\n>> '))
            if comentario == 1:
                comentario = str(input('Deixe o seu comentário\n>> '))
            else:
                comentario = ''

            vendedor.deixar_avaliacao(avaliacoes, comentario)
            #print(vendedor.avaliacoes_comentarios)

            os.system('cls')
            match input('Artigo comprado com sucesso!\nPretende:\n 1-Voltar à loja\n 2-Sair\n>> '):
                case '1':
                    return 'voltar'
                case '2':
                    return 'sair'
                  

    #Calcula a reputação de um utilizador com base nas suas avaliações
    def calcular_reputacao(self, utilizador):
        #print(utilizador.avaliacoes_comentarios)
        if utilizador.avaliacoes_comentarios == [['']]:
            return 'Este vendedor ainda não tem avaliações.'
        else:
            somaAval = 0
            numAval = 0
            for av in utilizador.avaliacoes_comentarios:
                #print(av)
                try:
                    somaAval += int(av[0])
                    if int(av[0]) != 0:
                        numAval += 1
                except ValueError:
                    return 'Erro ao calcular reputação'

            try:
                reputação = somaAval/numAval
                return float(reputação)
            except ZeroDivisionError:
                return 'Erro ao calcular reputação'


    #Coloca um artigo à venda. O vendedor é o nome de um utilizador
    def colocar_artigo_para_venda(self, vendedor, artigo, preco):

        tipologia = input('Tipologia:')
        quantidade = input('Quantidade:')           

        os.system('cls')


        novoArtigo = Artigo(artigo, float(preco), tipologia, int(quantidade))
        novoArtigo.atribuirVendedor(vendedor)
        novoArtigo.atribuirOferta('normal')
        self.ListaArtigos.append(novoArtigo)
        
        theVendedor = self.getUser(vendedor)

        if theVendedor:
            theVendedor.artigos_disponiveis.append(novoArtigo)
        

        print('O artigo foi adicionado com sucesso!') 

        self.definir_Ajustes_preco_Procura(novoArtigo)

        self.encontrar_compradores_interessados(novoArtigo)

        return novoArtigo


        
    #Encontra os nomes de utilizadores interessados no artigo recebido
    def encontrar_compradores_interessados(self, artigo):
        cidadaosInteressados = []
        for cidadao in self.ListaUtilizadores:
            for i in cidadao.interesses:
                if i == artigo.tipologia:
                    if cidadao.nome != self.TheUtilizador.nome:
                        cidadaosInteressados.append(cidadao)
                        break
        if len(cidadaosInteressados) != 0:
            print('Existem utilizadores possivelmente interessados no seu produto:')
            for cidadointeressado in cidadaosInteressados:
                print(cidadointeressado.nome)
            
    

    #Exporta a lista de artigos para um ficheiro ordenados por quantidade
    def exportar_artigos_preco(self, nome_ficheiro):
        with open(nome_ficheiro, "w") as file:
            artigosOrdenados = sorted(self.ListaArtigos, key=lambda x: float(x.preco))
            for artigo in artigosOrdenados:
                file.write(f"{artigo.nome};{artigo.preco};{artigo.tipologia};{artigo.quantidade};{artigo.vendedor}\n")



    #Exporta a lista de utilizadores para um ficheiro ordenados por reputação
    def exportar_utilizadores(self):
        with open('utilizadores.txt', "w") as file:
            for user in self.ListaUtilizadores:
                info = []
                infoArtigos = []
                for artigo in user.artigos_disponiveis:
                    info = []
                    info.append(artigo.nome)
                    info.append(artigo.preco)
                    info.append(artigo.tipologia)
                    info.append(artigo.quantidade)
                    info.append(artigo.oferta)

                    infoArtigos.append(info)
                
            utilizadoresOrdenados = sorted(self.ListaUtilizadores, key=lambda x: float(x.reputacao), reverse=True)

            for user in utilizadoresOrdenados:
                file.write(f"{user.nome};{user.interesses};{infoArtigos};{user.reputacao}\n")


    def exportar_tudo(self, nome_ficheiro):
        with open(nome_ficheiro, 'w', encoding='utf-8') as file:
            for user in self.ListaUtilizadores:
                interesses = (str(user.interesses).replace("'", "")).replace(" ", "")
                artigos = '['
                for artigo in user.artigos_disponiveis:
                    preconormal = artigo.preco
                    if artigo.oferta != "normal":
                        if artigo.oferta == "alta":
                            preconormal =  artigo.preco/0.75
                        if artigo.oferta == "baixa":
                            preconormal = artigo.preco/1.25
                            

                    artigos = artigos + f"{artigo.nome},{preconormal},{artigo.tipologia},{artigo.quantidade},{artigo.oferta}&"
                artigos = artigos.strip('&')
                artigos += ']'


                avaliacoes_comentarios = '['
                for i in user.avaliacoes_comentarios:
                    try:
                        avaliacoes_comentarios += f'{i[0]},{i[1]}&'
                    except IndexError:
                        continue
                avaliacoes_comentarios = avaliacoes_comentarios.strip('&')
                avaliacoes_comentarios += ']'

                        
                file.write(f"{user.nome};{interesses};{artigos};{user.pycoins};{avaliacoes_comentarios}\n")

    def getUser(self, nomeUtilizador): #devolve o Utilizador (objeto) em função do nome fornecido
        for user in self.ListaUtilizadores:
            if user.nome == nomeUtilizador:
                return user
        return False #não encontrou utilizador pelo nome dado
            
    def getArtigo(self, nomeArtigo, nomeVendedor = ''): #devolve o artigo (objeto) em função do nome fornecido e do vendedor pretendido
        for artigo in self.ListaArtigos:                #se nao for indicado vendedor específico é devolvida a primeira ocorrência do artigo encontrada
            if artigo.nome == nomeArtigo:
                if nomeVendedor != '':
                    if artigo.vendedor == nomeVendedor:
                        return artigo
                else:
                    return artigo


    def LogIn(self):
      while True:
          os.system('cls')
          user = (input('Para fazer LogIn, introduza o seu nome de utilizador.\n>> '))
          if user == 'admin':
              return 'admin'
          else:
            user = self.getUser(user)
            if user:
                return user
            else:
                match input('Utilizador não encontrado. Pode:\n 1-Introduzir novamente\n 2-Cancelar'):
                    case '1':
                        continue
                    case '2':
                        return
            
        
    def adminPage(self):
        os.system('cls')
        print(" 1-Eliminação de conta de um utilizador\n" \
            + " 2-Lista de utilizadores\n" \
            + " 3-Mostrar artigos de um utilizador\n" \
            + " 4-Mostrar interesses de um utilizador\n" \
            + " 5-Mostrar Pycoins de um utilizador\n" \
            + " 6-Voltar")
        
        match input('>> '):
            case '1': #Eliminar utilizador
                while self.eliminar_conta(input('Que utilizador deseja eliminar?\n>> ')):
                    continue
                self.adminPage()
                
            case '2': #Listar/Exportar utilizadores
                os.system('cls')
                match input(('Pretende:\n1-Mostrar a lista de utilizadores\n2-Exportar a lista de utilizadores\n>> ')):
                    case '1':
                        for utilizador in TheFeira.ListaUtilizadores:
                            print(utilizador.nome)
                        input('\nEnter para voltar')
                        self.adminPage()

                       
                    case '2':
                        self.exportar_utilizadores()
                        os.system('cls')
                        print('Utilizadores exportados com sucesso!')
                        input('\nEnter para voltar')
                        self.adminPage()

            case '3': #Mostrar artigos de um utilizador
                while True:
                    os.system('cls')
                    user = self.getUser(input('Introduza um utilizador para consultar os seus artigos.\n>> '))
                    if not user:
                        match input('Utilizador não encontrado. Pode:\n 1-Introduzir novamente\n 2-Cancelar\n>> '):
                            case '1':
                                continue
                            case '2':
                                break
                    break
                for artigo in user.artigos_disponiveis:
                    print(artigo.nome)
                input('\nEnter para voltar')
                self.adminPage()

            case '4': #Mostrar interesses de um utilizador
                while True:
                    os.system('cls')
                    user = self.getUser(input('Introduza um utilizador para consultar os seus interesses.\n>> '))
                    if not user:
                        match (input('Utilizador não encontrado. Pode:\n 1-Introduzir novamente\n 2-Voltar\n>> ')):
                            case '1':
                                continue
                            case '2':
                                break
                    else:
                        count = 0
                        conjInteresses = ''
                        for interesse in user.interesses:
                            count += 1
                            conjInteresses = conjInteresses + 'Interesse ' + str(count) + ': ' + interesse + ', '
                        print(conjInteresses.strip(', '))
                        break
                input('\nEnter para voltar')
                self.adminPage()

            case '5':
                while True:
                    os.system('cls')
                    user = self.getUser(input('Introduza um utilizador para consultar as suas Pycoins.\n>> '))
                    if not user:
                        match (input('Utilizador não encontrado. Pode:\n 1-Introduzir novamente\n 2-Voltar\n>> ')):
                            case '1':
                                continue
                            case '2':
                                break
                    else:
                        user.mostrar_pycoins()
                        break
                input('\nEnter para voltar')
                self.adminPage()
            
            case '6':
                pass

    def getOcorrenciasArtigo(self, nomeArtigo):
                ocorrenciasArtigo = []
                for g in self.ListaArtigos:
                    if g.nome == nomeArtigo:
                        ocorrenciasArtigo.append(g)
                return ocorrenciasArtigo

                        #for user in TheFeira.ListaUtilizadores:
                        #    if user.nome == g.vendedor:
                        #        vendedeiro = user
                        #        break

#Início da feira. O grupo deve apresentar testes do projeto nesta função
def main():
    userPrompt = ">> "
    # voltarOuSair = "\n V - Voltar a trás \n S - Sair \n"
    def start():
        os.system('cls')
        print("Bem vindo à Feira Virtual. Pretende: \n 1-LogIn \n 2-Criar Conta \n 3-Sair da FeiraVirtual")
        match input(userPrompt):
            case '1':
                os.system('cls')
                TheFeira.TheUtilizador = TheFeira.LogIn()
                if TheFeira.TheUtilizador == 'admin':
                    TheFeira.adminPage()
                else:
                    home()
            case '2': #registar utilizador
                os.system('cls')
                while True:
                    nome = input('Insira o seu primeiro nome. Será o seu nome de utilizador.\n>> ')
                    if TheFeira.getUser(nome):
                        match input('Já existe um utilizador com esse nome. Pode:\n 1-Introduzir outro nome\n 2-Cancelar\n>> '):
                            case '1':
                                continue
                            case '2':
                                start()
                                break
                    else:
                        break

                
                interesses = TheFeira.setInteresses()

                artigos_disponiveis = []
                match input('Quer adicionar artigos para vender?\n1-Sim\n2-Não\n>> '):
                    case '1':
                        while True:
                            artigos_disponiveis.append(TheFeira.colocar_artigo_para_venda(nome, input('Nome:'), input('Preço:')))
                            match input('Quer adicionar mais artigos?\n1-Sim\n2-Não\n>> '):
                                case '1':
                                    continue
                                case '2':
                                    break    
                    case '2':
                        artigos_disponiveis = []
                    
                TheFeira.registar_utilizador(nome, interesses, artigos_disponiveis)
                  
                home()
            case '3':
                os.system('cls')
                exit()
    
    def home():
        os.system('cls')
        print("Olá, ", TheFeira.TheUtilizador.nome, ". Pretende aceder a: \n 1-Navegar Loja \n 2-Espaço pessoal \n 3-Sair", sep='')
        match input(userPrompt):
            case '1':
                verLoja()
            case '2':
                espaçoPessoal()
            case '3':
                TheFeira.exportar_tudo('utilizadoresartigos.txt')
                start()
    
    def verLoja():
        while True:
            os.system('cls')
            print('Produtos disponíves na Loja:         PyCoins:', TheFeira.TheUtilizador.pycoins)
            TheFeira.listar_artigos()
            print('Voltar: s; Ver apenas produtos dos meus interesses: i; Ver produto: escreva o nome do produto' )
            escolha = input(userPrompt)
            match escolha:
                case 's':
                    home()
                case 'i':
                    os.system('cls')
                    TheFeira.listar_artigos_do_meu_interesse()
                    print('Voltar: s; Voltar a ver todos os produtos: i; Ver produto: escreva o nome do produto' )
                    escolha = input(userPrompt)
                    match escolha:
                        case 's':
                            home()
                        case 'i':
                            verLoja()
                        case _:
                            if not abrirArtigo(escolha):
                                continue                  
                case _:
                    if not abrirArtigo(escolha):
                        continue
            break

    def abrirArtigo(escolha):
        artigoEscolhido = TheFeira.getArtigo(escolha)
        if not artigoEscolhido:
            os.system('cls')
            input("Artigo não encontrado. 'Enter' para voltar à loja.")
            return False
        else:
            while True:
                os.system('cls')
                TheFeira.exibir_Artigo_com_Vendedores(artigoEscolhido)   
                vendedeiroEscolhido = TheFeira.getUser(input('Escreva o nome do vendedor a que quer comprar o artigo.\n>> '))
                if not vendedeiroEscolhido:
                    match input('Não foi encontrado nenhum vendedor com esse nome. Pode:\n 1-Introduzir novamente\n 2-Voltar\n>> '):
                        case '1':
                            continue
                        case '2':
                            break
                else:
                    if vendedeiroEscolhido.nome == TheFeira.TheUtilizador.nome:
                        os.system('cls')
                        input("Não pode comprar o seu próprio artigo! 'Enter' para continuar.")
                        continue
                    for artigo in vendedeiroEscolhido.artigos_disponiveis:
                        if artigo.nome == escolha:
                            artigoEscolhido = artigo
                            break
                    if TheFeira.comprar_artigo(TheFeira.TheUtilizador, vendedeiroEscolhido, artigoEscolhido) == 'voltar':
                        verLoja()
                        break
                    else:
                        home()

    def espaçoPessoal(): #1-adicionar artigo,2-ver avaliações,3-alterar interesses,4-apagar conta
        os.system('cls')
        print("Pretende aceder a:\n 1-Adicionar artigo\n 2-Ver os meus artigos disponíveis\n 3-Ver avaliações \n 4-Alterar interesses \n 5-Apagar conta \n 6-Voltar")
        escolha = input(userPrompt)
        match escolha:
            case '1': #adicionar artigo
                while True:
                    TheFeira.colocar_artigo_para_venda(TheFeira.TheUtilizador.nome, input('Nome:'), input('Preço:'))
                    match input('Pretende:\n 1-Adicionar mais um artigo\n 2-Concluir\n>> '):
                        case '1':
                            continue
                        case '2':
                            break
                espaçoPessoal()
            case '2': #ver artigos
                os.system('cls')
                print('Estes são os artigos que tem à venda na FeiraVirtual:')
                for meuArtigo in TheFeira.TheUtilizador.artigos_disponiveis:
                    print(meuArtigo.nome)
                
                print('Pode:\n Escrever o nome do produto para ver e/ou editar detalhes\n v-Voltar')
                escolha = input('>> ')
                match escolha:
                    case 'v':
                        pass
                    case _:
                        produtoEncontrado = False
                        for i in TheFeira.ListaArtigos:
                            if escolha == i.nome:
                                produtoEncontrado = True
                                os.system('cls')
                                print(i.nome, '          ', i.preco)
                                print('------------\nVendedores:')
                                ocorrenciasArtigo = []
                                #devem aparecer os dados do artigo: preço, quantidade, tipologia, vendedor
                                textoVendedores = ''
                                for g in TheFeira.ListaArtigos:
                                    #print(g.nome)
                                    if g.nome == i.nome:
                                        ocorrenciasArtigo.append(g)
                                        for user in TheFeira.ListaUtilizadores:
                                            if user.nome == g.vendedor:
                                                vendedeiro = user
                                                break
                                        if vendedeiro.nome == TheFeira.TheUtilizador.nome:
                                            nomeAMostrar = TheFeira.TheUtilizador.nome + ' (VOCÊ)'
                                        else:
                                            nomeAMostrar = g.vendedor
                                        
                                        textoVendedores += nomeAMostrar +'\n  Reputação:' + str(TheFeira.calcular_reputacao(vendedeiro)) +  '\n  Quantidade disponível:' + str(g.quantidade) + '\n'
                                if len(ocorrenciasArtigo) == 1: #só ha um vendedor, que será o próprio utilizador logged in
                                    textoVendedores = 'É o único vendedor deste artigo.'
                                print(textoVendedores)
            #alterar preço, quantidade, tipologia
                        print('O que deseja fazer com este artigo:\n 1-Alterar preço\n 2-Alterar quantidade\n 3-Alterar tipologia')       
                        escolha = input(userPrompt)
                        match escolha:
                            case '1':
                                meuArtigo.editar_preco((int(input('Insira o novo preço.\n>> '))))
                                TheFeira.definir_Ajustes_preco_Procura(meuArtigo)
                                espaçoPessoal()
                            case '2':
                                meuArtigo.editar_quantidade(int(input('Insira a nova quantidade do seu artigo.\n>>')))
                                TheFeira.definir_Ajustes_preco_Procura(meuArtigo)
                                espaçoPessoal()
                            case '3':
                                meuArtigo.editar_tipo(str(input('Insira a nova tipologia do seu artigo\n>>')))
                                espaçoPessoal()
                               
            case '3': #ver avaliações
                TheFeira.TheUtilizador.listar_avaliacoes()
            case '4': #alterar interesses
                TheFeira.TheUtilizador.interesses = TheFeira.setInteresses()
                espaçoPessoal()
                #TheFeira.exportar_tudo('utilizadoresartigos.txt')
            case '5': #apagar conta
                TheFeira.eliminar_conta(TheFeira.TheUtilizador.nome)
                start()
            case '6':
                home()
            case _:
                pass
    TheFeira.exportar_tudo('utilizadoresartigos.txt')
    start()

    
TheFeira = FeiraVirtual()
TheMercado = Mercado()
main()

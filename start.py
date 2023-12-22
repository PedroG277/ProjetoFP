from FeiraVirtual import FeiraVirtual

TheFeira = FeiraVirtual()
while True:    
    print('1: ver todos os artigos\n2: adicionar um artigo\n3: exportar lista de artigos\n4: exportar lista de utilziadores')
    escolha = int(input())
    if escolha == 1:
        TheFeira.listar_artigos()
    elif escolha == 2:
        TheFeira.colocar_artigo_para_venda(input('Vendedor:'), input('Nome:'), input('Preço:'), input('Tipologia:'), input('Quantidade:'))
    elif escolha == 3:
        TheFeira.exportar_artigos_preco("artigos.txt")
    elif escolha == 4:
        TheFeira.exportar_utilizadores('users.txt')
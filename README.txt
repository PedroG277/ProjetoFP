
Página start:
    Log in: permite aceder à loja, adicionar produtos, e fazer alterações à conta, na perspetiva de um utilizador registado
        Para fazer log in, escreva o nome de utilizador (não há passwords)
        Se introduzir 'admin', é feito log in como administrador da feira.
        Feito o log in, passa à página home
    Criar conta
        É criada uma nova conta com:
        Nome (do utilizador) - tem de ser diferente dos já existentes.
        Interesses - introduzidos um de cada vez, concluindo ao introduzir 's'.
        Artigos disponíves - é dada a opção de adicionar artigos, se escolhida passa à página novo_artigo. Concluído o processo, é dada a opção de adicionar mais um produto. O processo repete-se até ser escolhido não adicionar mais um produto.
        Terminada a criação da conta, passa à página home, com o novo utilizador logged in.
    Sair da FeiraVirtual
        Termina a execução do programa.

    Página home
        Como utilizador, as opções são:
            Navegar loja
                É exibida a lista de todos os artigos disponíves na feira, como o nome e o preço. Produtos iguais (vendidos por mais do que um utilizador) são exibidos só uma vez. As opções de ação são:
                    Voltar, ao introduzir 's'
                        Volta à página home
                    Ver apenas produtos do meu interesse, ao introduzir 'i'
                        Passam a ser exibidos apenas os artigos cuja tipologia corresponda a um dos interesses do utilizador logged in. As opções são:
                            Voltar, ao introduzir 's'
                                Volta à página home
                            Voltar a ver todos os produtos, ao introduzir 'i'
                                Volta a ver a lista normal
                            Ver produto, ao escrever o nome do produto na lista
                                Abre a página ver produto, na versão de navegar loja
                    Ver produto, ao escrever o nome do produto na lista
                        Abre a página de ver produto


            Espaço pessoal
                Nesta página estão as opções e ações de caráter pessoal do utilizador logged in:
                    Adicionar artigo
                        Leva para a sequência novo_artigo
                    Ver os meus artigos disponíveis
                        É exibida a lista dos artigos (nome) vendidos pelo utilizador. São dadas as opções:
                            Escrever o nome do produto para ver e/ou editar detalhes
                                Abre a página ver produto, na versão do espaço pessoal
                            Voltar
                                Volta à página Espaço pessoal  
                    Ver avaliações
                        Leva para uma página em que são exibidos os conjuntos de avaliações e comentários deixados ao utilizador
                    Alterar interesses
                        É pedido que sejam introduzidos interesses do mesmo modo que ocorre ao criar conta. O conjunto de interesses introduzidos substitui o existente.
                    Apagar conta
                        Passa para uma página em que é pedido o nome de utilizador para confirmar a eliminação de conta. Se for introduzido o nome correto, o utilizador e os seus artigos são eliminados, e passa para a página start.
                    Voltar
                        Volta para a página home
            Sair
                Volta à página start


Página ver produto
    Nesta página é exibido o nome e preço do produto (ajustado à oferta), e todos os seus vendedores. Os vendedores aparecem com o nome, a reputação, e a quantidade do artigo que têm disponível. As opções nesta página são, conforme a entrada nesta página:
        Entrada ao navegar loja:
            Comprar o artigo, ao escrever o nome do vendedor a que pretende comprar
               Passa para uma página com o nome e preço do produto, o vendedor escolhido e a sua quantidade disponível. É pedido para introduzir a quantidade que se pretende comprar. Introduzida uma quantidade válida, se o comprador tiver pycoins suficientes, é efetuada a compra. Se forem compradas todas as unidades, o artigo é eliminado.
               Efetuada a compra, é exibido o saldo de pycoins do utilizador, e é possível deixar uma avaliação (1-5 estrelas) e um comentário, ambos opcionais.
            Voltar, ao introduzir 's'
                Volta à página anterior
        Entrada pelo Espaço pessoal:
            Alterar preço - é introduzido um novo preço ao produto.
            Alterar quantidade - é introduzida uma nova quantidade ao produto. Se indicada quantidaade 0, o produto é eliminado.
            Alterar tipologia - é introduzida uma nova tipologia ao produto.



Sequência novo_artigo
    Esta é uma sequência de inputs para adicionar um novo artigo ao mercado:
        Nome - introduzir o nome do artigo. É o nome que é verificado para considerar este artigo igual a outros no mercado
        Preço - introduzir o preço do artigo. Pode ser introduzido qualquer preço, mas, ao finalizar criar o artigo, se existirem produtos iguais no mercado com preço menor, o novo produto assume este preço, e vice-versa.
        Tipologia - introduzir a tipologia do produto. É a tipologia que é usada para procurar compradores interessados, na perspetiva do vendedor, ou artigos do meu interesse, na perspetiva do comprador.
        Quantidade: introduzir a quantidade disponível. Esta quantidade irá influenciar a oferta global do produto no mercado e, assim, o seu eventual ajuste de preço para +/- 25%
    Concluída a adição do artigo, são dadas as opções de adicionar mais um artigo, que repete o processo, ou voltar, que volta para a página anterior.
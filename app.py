import pandas as pd

def deletar(dfLivros):
    delete =input('qual livro você quer deletar: ')
    filtroTitulo = dfLivros[dfLivros["titulo"] == delete]
    if filtroTitulo.empty:
        print("o livro que você busca não existe")
    else:
        # achei o livro, bora deletar
        indice = filtroTitulo.index[0]

        coluna = dfLivros['titulo']
        linha = coluna.iloc[indice]

        dfLivros = dfLivros.drop(indice)
        print(f'o livro {delete}, já foi deletado')
        print(dfLivros.tail())
        dfLivros.to_excel('livros.xlsx')

def escrever():
    print("para você escrever preciso de algumas informações, só ir respondendo a baixo: ")
    # criando o resumo do livro
    novoTitulo = input('qual o titulo do livro: ')
    novoAutor = input('qual o autor do livro: ')
    novoGenero = input('qual o genero do livro: ')
    novoAnoLancamento = input('qual o ano de lançamento do livro: ')
    novoResumo = input('dê um breve resumo do livro ou escreva a sua dedicatória: ')

    # paddando os valores de que as colunas da nova linha irá receber
    novaLinha = {'titulo': novoTitulo, 
                'autor': novoAutor,
                'genero': novoGenero,
                'ano de lançamento': novoAnoLancamento,
                'resumo': novoResumo,
                'estado': False}
        
    # adicionando as informações no nosso excel
    dfLivros.loc[len(dfLivros)] = novaLinha
    print(dfLivros.tail())
    dfLivros.to_excel('livros.xlsx')

def buscaTitulo():
    titulo = input("digite o titulo do livro: ")
    filtroTitulo = dfLivros[dfLivros["titulo"] == titulo]
 
    # caso a variável esteja vazia é porque o livro não foi encontrado, ou seja, não existe
    if filtroTitulo.empty:
        print(f"O livro com o título {titulo} não foi encontrado.")
        # caso o livro não seja encontrad o usuário poderá escrever sobre o mesmo
        escrever = input("quer escrever sobre ele: ")
        if (escrever == "s"):
            print("vc irá escrever sobre o livro!")
            escrever()
        else:
            print("vc não irá escrever sobre!")

    else:
        print("Livro(s) encontrado(s):")
        print(filtroTitulo)
        indice = filtroTitulo.index[0] # criando uma variávelpara receber o indice/n° da linha, do que foi buscado pela filtragem
        emprestar =input("deseja pegar o livro emprestado (s/n): ")

        if(emprestar == "s"):
            print("você irá quer o livro emprestado")
            # ver o estado que está 
            coluna = dfLivros['estado']
            linha = coluna.iloc[indice]
            print(linha)

            if (linha == True):
                print("EMPRESTADO JÁ")
                # abrir uma lista com o nome de pessoas que estão em sua frente
                # dai vem a outra parte, que é o sistema de login para validar quem está com o livro
            elif (linha == False):
                print("AINDA NÃO FOI EMPRESTADO")
                # adicionar a pessoa que quer na lista de qm está com o livro e abrir a lista de espera
        else:
            print("você nao quer pegar o livro emprestado!")

def modoBuscarFuncao():
    modoBuscar = input("você quer buscar o livro através do titulo, autor, gênero ou ano de lançamento (titulo, autor, genero, ano): ")

    if(modoBuscar == "titulo"):
        buscaTitulo()
    elif(modoBuscar == "autor"):
        print("você quer buscar o livro através de seu autor")
        autor = input("digite o nome do autor do livro: ")
        filtroAutor = dfLivros[dfLivros["autor"] == autor]

        if filtroAutor.empty:
            print(f"O livro com o título {autor} não foi encontrado.")
        else:
            print("Livro(s) encontrado(s):")
            print(filtroAutor)
            buscaTitulo()
    elif(modoBuscar == "genero"):
        print("você quer buscar o livro através de seu gênero")
        genero = input("digite o gênero do livro: ")
        filtroGenero = dfLivros[dfLivros["genero"] == genero]
        
        if filtroGenero.empty:
            print(f"O livro com o título {genero} não foi encontrado.")
        else:
            print("Livro(s) encontrado(s):")
            print(filtroGenero)
            buscaTitulo()
    elif(modoBuscar == "ano"):
        print("você quer buscar o livro através de seu ano de lançamento")
        ano = input("digite o ano de lançamento do livro: ")
        ano = int(ano)
        filtroAno = dfLivros[dfLivros["ano de lançamento"] == ano]

        if filtroAno.empty:
            print(f"O livro com o título {ano} não foi encontrado.")
        else:
            print("Livro(s) encontrado(s):")
            print(filtroAno)
            buscaTitulo()
    else:
        print("informe algo válido")

dfLivros = pd.read_excel("livros.xlsx")
funcao = input("você quer buscar algum livro, deletar ou escrever sobre (buscar, deletar ou escrever): ")

if (funcao == "buscar"):
    print("você escolheu buscar por uma obra")
    modoBuscarFuncao()
elif (funcao == "deletar"):
    print("você escolheu deletar uma obra")
    deletar(dfLivros)
elif (funcao == "escrever"):
    print("você escolheu escrever sobre uma obra")
    escrever()
else:
    print("informe algo válido")

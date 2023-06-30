def resumo():
    mensagem = "Alan Mathison Turing  foi um matemático britânico, pioneiro da computação e considerado o pai da ciência computacional e da inteligência artificial."
    return mensagem


def doutorado():
    mensagem = ""
    return mensagem


def contribuicoes():
    mensagem = ""
    return mensagem


def artigos():
    mensagem = "Com o artigo On Computable Numbers, apresentou a ideia de uma máquina universal, a qual seria chamada, posteriormente, de Máquina de Turing. \nNa Victoria University of Manchester, ele ajudou a desenvolver a concepção e a construção dos primeiros computadores com programa armazenado na Inglaterra, além de contribuir no estudo sobre biologia matemática com o artigo sobre a base química da morfogênese, prevendo reações químicas oscilantes."
    return mensagem


def citacoes():
    mensagem = "Ciência é uma equação diferencial. Religião é a condição de contorno. \nNós só podemos ver um pouco do futuro, mas o suficiente para perceber que há muito a fazer. \nEu não fico muito impressionado com argumentos teológicos, independentemente daquilo que eles estão sendo usado para apoiar. Esses argumentos frequentemente se revelaram insatisfatórios no passado. \nEu acredito que às vezes são as pessoas que ninguém espera nada que fazem as coisas que ninguém consegue imaginar."
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Allan Turing.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)

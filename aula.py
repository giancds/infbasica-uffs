def resumo():
    mensagem = "Geoffrey Everest Hinton CC FRS FRSC (born 6 December 1947)is a British-Canadian cognitive psychologist and computer scientist, most noted for his work on artificial neural networks. "
    return mensagem


def doutorado():
    mensagem = "Hinton foi eleito Fellow da Royal Society (Londres, Reino Unido) em 1998, além de ser o primeiro ganhador do prêmio Rumelhart em 2001. Neste mesmo ano recebeu um doutorado honorário (honoris causa) da Universidade de Edimburgo, além de uma longa lista de prêmios e reconhecimentos nos anos seguintes, como IJCAI Award for Research Excellence (2005), Herzberg Canada Gold Medal for Science and Engineering (2011) e mais um doutorado honoris causa da Université de Sherbrooke (2013)."
    return mensagem


def contribuicoes():
    mensagem = "O pioneiro em Inteligência Artificial"
    return mensagem


def artigos():
    mensagem = "1º artigo mais citado - Imagenet classification with deep convolutional neural networks - 127230 citações" 
    "2º artigo mais citado - Deep learning - 60553 citações"
    "3º artigo mais citado - Dropout: a simple way to prevent neural networks from overfitting - 40878 citações"
    return mensagem


def citacoes():
    mensagem = "Total de citações em 08/02/2023 as 21:05h 657011"
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Geoffrey Everest Hinton.\n")

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

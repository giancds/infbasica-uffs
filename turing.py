# fonte: https://pt.wikipedia.org/wiki/John_McAfee
def resumo():
    mensagem = "John McAfee (18 de setembro de 1945—23 de junho de 2021)[2] foi um programador de computadores britânico, fundador da McAfee. Foi uma das primeiras pessoas a projetar software antivírus e desenvolver scanner de vírus. "
    return mensagem


def doutorado():
    mensagem = "Recebeu seu diploma de bacharel em matemática pela Faculdade de Roanoke em 1967, e recebeu um doutorado honorário da Faculdade de Roanoke em 2008. "
    return mensagem


def contribuicoes():
    mensagem = "Em 1987 fundou a McAfee Associates, uma empresa de software de antivírus. Ele foi o primeiro a distribuir software antivírus usando shareware."
    return mensagem


def artigos():
    mensagem = "Em um artigo de 2012 no jornal interno da Mensa, ele afirmou que ser o desenvolvedor do primeiro programa antivírus comercial fez dele ""o alvo mais popular dos Hackers"", tendo informado que ""Hackers me veem como uma medalha de ouro""."
    return mensagem


def citacoes():
    mensagem = "Você não pode parar coisas como a Bitcoin. É como tentar parar pólvora."
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

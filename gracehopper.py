def resumo():
    mensagem = "Conhecida como "Rainha do Software", Grace Hopper foi uma cientista da computação e almirante da Marinha dos Estados Unidos."
    return mensagem


def diplomas():
    mensagem = "Grace Hopper frequentou a Universidade Yale, onde obteve seu diploma de bacharel em matemática e física em 1928. Mais tarde, ela continuou seus estudos e recebeu seu mestrado em matemática pela Universidade Yale em 1930."
    return mensagem


def contribuicoes():
    mensagem = "Grace foi uma das primeiras programadoras do computador Harvard Mark I e contribuiu para o desenvolvimento do COBOL (Common Business-Oriented Language), uma das primeiras linguagens de programação de alto nível."
    return mensagem


def artigos():
    mensagem = ""
    return mensagem


def citacoes():
    mensagem = ""
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Grace Hopper.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Diplomas
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
        print("2 - Diplomas")
        mensagem = diplomas()

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

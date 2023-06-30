def resumo():
    mensagem = "Guido van Rossum estudou matemática na Universidade de Amesterdã onde teve seu primeiro contato com uma linguagem de programação. \nEm 1999, Van Rossum submeteu uma proposta de financiamento a DARPA chamada de Computer Programming for Everybody, na qual ele definiu \nseus objetivos para a linguagem Python \nEm 2002, Guido recebeu o Prêmio por Avanços em Software Livre de 2001 \nDe 2005 a 2012, Van Rossum foi empregado do Google, onde passava metade do tempo desenvolvendo a linguagem Python. \nEm 2020, Rossum junta-se à Microsoft onde passa a atuar como Distinguished Engineer"
    return mensagem


def doutorado():
    mensagem = "Matemática e Ciência da Computação"
    return mensagem


def contribuicoes():
    mensagem = "Python"
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


print("\nOlá! você está aprendendo sobre Guido van Rossum.\n")

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
        print("1 - Resumo:")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado:")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições:")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos:")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações:")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
	

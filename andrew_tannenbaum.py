def resumo():
    mensagem = "Andrew Stuart Tanenbaum[1] (White Plains, 16 de março de 1944) é o chefe do Departamento de sistemas de computação, na Universidade Vrije, Amsterdã nos Países Baixos."
    return mensagem


def doutorado():
    mensagem = "Recebeu o título de bacharelado pelo MIT e o doutorado pela UC Berkeley em 1971."
    return mensagem


def contribuicoes():
    mensagem = " Ele é o autor do MINIX, um sistema operacional baseado no Unix com propósito educacional, e é conhecido por seus livros sobre ciência da computação."
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


print("\nBoa noite! Você está aprendendo sobre Andrew Tannenbaum.\n")

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
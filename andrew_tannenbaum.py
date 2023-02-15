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
    mensagem = "- Redes de computadores. \n- Sistemas Operacionais: Projeto e Implementação, (co-autor com Albert Woodhull). \n- Sistemas Operacionais Modernos. \n- Organização Estruturada de Computadores. \n- Sistemas Distribuídos: Princípios e Paradigmas, (co-autor com Maarten van Steen)."
    return mensagem


def citacoes():
    mensagem = '“The good thing about standards is that there are so many to choose from.” ― Andrew S. Tanenbaum. \n“The amount of improvement that has occurred in computer technology in the past half century is truly staggering and unprecedented in other industries. ... If cars had improved at this rate in the same time period, a Rolls Royce would now cost 10 dollars and get a billion miles per gallon. (Unfortunately, it would probably also have a 200-page manual telling how to open the door.)”\n― Andrew Tanenbaum '
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
def resumo():
    mensagem = "Alan Mathison Turing foi um ateu e homossexual, matemático e criptógrafo britânico, pioneiro da computação e considerado o pai da ciência computacional, uma vez que por meio de suas ideias, foi possível desenvolver o que chamamos hoje de computadores, além de também ser pineiro da inteligência artificial."
    return mensagem


def doutorado():
    mensagem = "Em 1938, Turing obteve seu PhD pelo Departamento de Matemática da Universidade de Princeton. Durante a Segunda Guerra Mundial, trabalhou para a Sede de Comunicações do Governo, localizada no Centro de decodificação Britânico, em Bletchley Park, no desenvolvimento da Ultra."
    return mensagem


def contribuicoes():
    mensagem = "Máquina Universal de Turing\nDesenvolveu o Automatic Computing Engine (ACE)\nConstruiu o primeiro computador digital com programa armazenado eletronicamente.\nSistema de programação usado no Ferranti Mark I, o primeiro computador digital eletrônico comercial de 1951.\nTeste de Turing\nDispositivo eletromecânico denominado “The Bombe”"
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

def resumo():
    mensagem = ""
    return mensagem


def doutorado():
    mensagem = "ele tem Ph.D. em mateática pela universidade de Princeton"
    return mensagem


def contribuicoes():
    mensagem = "suas contribuições foram foram a abordagem logisitcas para IA e levou ao desenvolvimento da linguagem de computador LISP"
    return mensagem


def artigos():
    mensagem = "artigo sobre linguagem de programção:Funções Recursivas de Expressões Simbólicas e sua Computação por Máquina (Parte I), artigo sobre teoria matematica da computção:A Basis for a Mathematical Theory of Computation,"
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

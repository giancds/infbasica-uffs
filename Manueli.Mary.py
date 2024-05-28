def resumo():
    mensagem = "MARY KELLER, É considerada a primeira mulher a receber um doutorado em Ciência da Computação. Também obteve mestrado em Matemática e Física. Foi uma freira norte-americana, nascida em Ohio. Ela participou no desenvolvimento da linguagem de programação BASIC. Também foi forte ativista feminista e desenvolveu projetos para inclusão e estímulo de mulheres e crianças na computação."
    return mensagem


def doutorado():
    mensagem = "doutorado em Ciência da Computação"
    return mensagem


def contribuicoes():
    mensagem = "Ela participou no desenvolvimento da linguagem de programação BASIC."
    return mensagem


def artigos():
    mensagem = "O Martelo e a Flauta : Mulheres, Poder e Posse do Espírito, Mary Keller"
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


print("\nBoa noite! Você está aprendendo sobre Mary Keller.\n")

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

def resumo():
    mensagem = "\nAlan Mathison Turing  foi um matemático britânico, pioneiro da computação e considerado o pai da ciência computacional e da inteligência artificial."
    return mensagem


def doutorado():
    mensagem = "\nTorvalds estudou na Universidade de Helsinki, de 1988 até 1996, com um mestrado em Ciência da Computação a partir do grupo NODES.\n Sua carreira acadêmica foi interrompida após 1 ano de estudo, pois entrou no Exéricto da Finlândia."
    return mensagem


def contribuicoes():
    mensagem = ""
    return mensagem


def artigos():
    mensagem = "\nLinus foi autor de 2 livros, 'Just for Fun'(Só por diversão) de 2001 e 'Open Sources'(Códigos abertos), de 1999.\nAlém disso, Linus foi o criador do kernel Linux e do controle de versões distribuído Git.\nAqui está concentrada a maior parte do seu trabalho:https://github.com/torvalds/linux "
    return mensagem


def citacoes():
    mensagem = ""
    return mensagem


def sair():
    mensagem = "\nObrigad@ pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nOlá! Você está aprendendo sobre Linus Torvalds.\n")

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

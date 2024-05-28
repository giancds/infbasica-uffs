def resumo():
    mensagem = "Larry Page é um empresário e engenheiro de computação americano, mais conhecido por ser o co-fundador da Google junto com Sergey Brin. Ele nasceu em 1973 em Lansing, Michigan, nos Estados Unidos. Page é conhecido por sua visão inovadora e por ter desempenhado um papel fundamental no desenvolvimento do algoritmo de busca do Google, que revolucionou a forma como as pessoas encontram informações na internet. Ele também foi CEO da Google durante vários períodos, desempenhando um papel crucial no crescimento e na expansão da empresa. Além de seu trabalho na Google, Page também é investidor em diversas empresas de tecnologia e tem interesse em áreas como inteligência artificial e mobilidade urbana."
    return mensagem


def doutorado():
    mensagem = "Doutorado em Ciência da Computação na prestigiosa Universidade Stanford."
    return mensagem


def contribuicoes():
    mensagem = ""
    return mensagem


def artigos():
    mensagem = ""
    return mensagem


def citacoes():
    mensagem = "ChatGPT"
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

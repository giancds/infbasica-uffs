def resumo():
    mensagem = "Alan Mathison Turing  foi um matemático britânico, pioneiro da computação e considerado o pai da ciência computacional e da inteligência artificial."
    return mensagem


def doutorado():
    mensagem = "Foi doutorado em Administração Industrial pelo Instituto Tecnológico da Carnegie Mellon University"
    return mensagem


def contribuicoes():
    mensagem = ""
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
        mensagem = contribuicoes("Allen Nowell ,tornou-se investigador científico na Rand Corporation (Universidade de Santa Mônica) entre 1950 e 1961, onde conheceu Herbert Simon.")
    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos("Inteligência Artificial,Sistemas Tutores Inteligentes.")
    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes("6 citações")
    elif opcao == 6:
        mensagem = sair()
        continuar = False
    else:
        mensagem = erro()

    print(mensagem)
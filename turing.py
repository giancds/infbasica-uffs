def resumo():
    mensagem = "Leslie B. Lamport (7 de fevereiro de 1941) é um cientista da computação estadunidense. "
    return mensagem


def doutorado():
    mensagem = "Lamport formou-se em matemática pelo Massachusetts Institute of Technology em 1960, com mestrado e doutorado em matemática pela Universidade Brandeis, concluídos respectivamente em 1963 e 1972."
    return mensagem


def contribuicoes():
    mensagem = "Suas pesquisas contribuíram com a fundação da teoria de sistemas distribuídos."
    return mensagem


def artigos():
    mensagem = " Time, Clocks, and the Ordering of Events in a Distributed System"
    "Distributed snapshots: determining global states of distributed systems"
    "The Byzantine Generals Problem"
    "The Part-time Parliament""
    return mensagem


def citacoes():
    mensagem = "https://pt.wikipedia.org/wiki/Leslie_Lamport"
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

def resumo():
<<<<<<< HEAD
    mensagem = "Leslie B. Lamport (7 de fevereiro de 1941) é um cientista da computação estadunidense. "
=======
    mensagem = "Leslie Lamport é um cientista da computação estadunidense, nascido em Nova York no ano de 1941 em Nova York, fez importantes contribuições no campo da computação"
>>>>>>> aed3eb291d1f3a7a9c6fba97dfe75ca824843c1e
    return mensagem



def doutorado():
<<<<<<< HEAD
    mensagem = "Lamport formou-se em matemática pelo Massachusetts Institute of Technology em 1960, com mestrado e doutorado em matemática pela Universidade Brandeis, concluídos respectivamente em 1963 e 1972."
=======
    mensagem = "Formou-se doutor em matemática pela Universidade Brandeis em 1972, sua tese de dou"
>>>>>>> aed3eb291d1f3a7a9c6fba97dfe75ca824843c1e
    return mensagem


def contribuicoes():
<<<<<<< HEAD
    mensagem = "Suas pesquisas contribuíram com a fundação da teoria de sistemas distribuídos."
=======
    mensagem = "relógios lógicos (logical clocks) e a relação antes-depois, bem como as falhas Bizantinas"
>>>>>>> aed3eb291d1f3a7a9c6fba97dfe75ca824843c1e
    return mensagem


def artigos():
<<<<<<< HEAD
    mensagem = " Time, Clocks, and the Ordering of Events in a Distributed System"
    "Distributed snapshots: determining global states of distributed systems"
    "The Byzantine Generals Problem"
    "The Part-time Parliament""
=======
    mensagem = "Seus principais artigos foram: Time, Clocks, and the Ordering of Events in a Distributed System, Distributed snapshots: determining global states of distributed systems, The Byzantine Generals Problem, The Part-time Parliament"
>>>>>>> aed3eb291d1f3a7a9c6fba97dfe75ca824843c1e
    return mensagem


def citacoes():
<<<<<<< HEAD
    mensagem = "https://pt.wikipedia.org/wiki/Leslie_Lamport"
=======
    mensagem = "relógios lógicos (logical clocks) e a relação antes-depois são alguns de seus conceitos mais citados"
>>>>>>> aed3eb291d1f3a7a9c6fba97dfe75ca824843c1e
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

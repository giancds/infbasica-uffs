def resumo():
    mensagem = "Edsger Wybe Dijkstra foi um renomado cientista da computação nascido em 11 de maio de 1930, nos Países Baixos, e falecido em 6 de agosto de 2002. Ele é amplamente considerado um dos pioneiros da ciência da computação e teve uma influência significativa no desenvolvimento de linguagens de programação e algoritmos."
    return mensagem


def doutorado():
    mensagem = "Edsger Dijkstra não obteve um doutorado formalmente. Ele concluiu sua educação em 1956 com um mestrado em matemática e física pela Universidade de Leiden, nos Países Baixos."
    return mensagem


def contribuicoes():
    mensagem = "Algoritmo de Dijkstra; Semáforos e exclusão mútua; Notação de Guarda."
    return mensagem


def artigos():
    mensagem = "A Note on Two Problems in Connexion with Graphs (1959); Solution of a Problem in Concurrent Programming Control (1965); Guarded Commands, Nondeterminacy and Formal Derivation of Program (1975)."
    return mensagem


def citacoes():
    mensagem = "Um problema digno de ser atacado prova seu valor lutando contra nós; A separação de preocupações é a essência da programação modular; O programador competente está plenamente consciente do tamanho estritamente limitado de seu próprio crânio; portanto, ele aborda a tarefa de programação com plena humildade e, entre outras coisas, evita truques inteligentes como a praga."
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Edsger Dijkstra.\n")

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

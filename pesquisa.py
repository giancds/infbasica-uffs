def resumo():
    mensagem = ""
    return mensagem


def doutorado():
    mensagem = "2 doutorados foram realizados pro John hopcroft\n O primeiro doutorado foi em matemática na universidade de Stanford, em 1964, "
    return mensagem


def contribuicoes():
    mensagem = "Suas contribuições incluem avanços significativos em algoritmos, teoria dos grafos, teoria dos autômatos e linguagens formais, aprendizado de máquina e ciência da computação teórica em geral. Ele foi premiado com o Prêmio Turing de 1986, considerado o mais prestigioso prêmio em ciência da computação, por suas contribuições fundamentais à teoria da computação e por liderar a próxima geração de cientistas da computação."
    return mensagem


def artigos():
    mensagem = "John Hopcroft escreveu 'An N log N Algorithm for Minimizing States in a Finite Automaton', 'The Complexity of Theorem Proving Procedures', 'A Linear Time Algorithm for Isomorphism of Planar Graphs', 'Data Structures and Algorithms', 'Optimal Computer Search Trees and Variable-Length Alphabetical Codes', 'Partitioning Digital Images', 'The Hopcroft-Karp Algorithm for Maximum Matching in Bipartite Graphs', 'On the Universality of Folded Hypercubes', 'Randomized Algorithms for Matrices and Data' e por fim 'A Algorithm for Automatically Fitting Digitized Curves', sendo esse ultimo artigo publicado em 2003."
    return mensagem


def citacoes():
    mensagem = "Segundo o que diz o Google Scholar, ele tem mais de 150.000 citações e um índice h de 91."
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre .\n")

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

#     1971, An n log n Algorithm for Minimizing States in a Finite Automaton
# 1972, The Complexity of Theorem Proving Procedures
# 1974, A Linear Time Algorithm for Isomorphism of Planar Graphs
# 1983, Data Structures and Algorithms
# 1984, Optimal Computer Search Trees and Variable-Length Alphabetical Codes

# 1994, 
# 1996, 
# 1999, 
# 2003, 
def resumo():
    mensagem = "Mary Kenneth Keller foi uma importante freira e cientista da computação, foi a primeira mulher doutora em ciência da computação."
    return mensagem


def doutorado():
    mensagem = "Keller, Mary Kenneth (1965). Inductive inference on computer generated patterns (PhD Thesis). Madison, Wisconsin: The University of Wisconsin."
    return mensagem


def contribuicoes():
    mensagem = "Contribuiu para a criação da linguagem de programação BASIC, que seria utilizada para fins didáticos."
    return mensagem


def artigos():
    mensagem = " \n-Keller, Mary Kenneth (1965). Inductive inference on computer generated patterns (PhD Thesis). Madison, Wisconsin: The University of Wisconsin. (Doctoral Dissertation)\n-Computer graphics and applications of matrix methods : three dimensional computer graphics and projections by Mary K Keller; Consortium for Mathematics and Its Applications (U.S.); Undergraduate Mathematics and Its Applications Project (U.S.) Lexington, MA : COMAP/UMAP, 1983. U106, U110.\n-Electrical circuits and Applications of matrix methods : analysis of linear circuits Mary K Keller; Consortium for Mathematics and Its Applications (U.S.); Undergraduate Mathematics and Its Applications Project (U.S.), 1978. U108.\n-Food service management and Applications of matrix methods : food service and dietary requirements by Mary K Keller; Consortium for Mathematics and Its Applications (U.S.); Undergraduate Mathematics and Its Applications Project (U.S.) Lexington, MA : COMAP/UMAP, 1983. U105, U109.\n-Markov chains and applications of matrix methods : fixed point and absorbing Markov chains by Mary K Keller; Consortium for Mathematics and Its Applications (U.S.); Undergraduate Mathematics and Its Applications Project (U.S.) Lexington, MA : COMAP/UMAP, 1983. U107, U111."
    return mensagem


def citacoes():
    mensagem = "Pela primeira vez podemos simular mecanicamente o processo cognitivo. Podemos completar estudos em inteligência artificial. Além disso, este mecanismo [o computador] pode ser usado para auxiliar as pessoas no aprendizado. Visto que com o tempo teremos alunos mais maduros e em qualidade superior, este tipo de ensinamento será provavelmente sempre mais importante."
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Mary Kenneth Keller.\n")

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

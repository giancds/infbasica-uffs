#Donald-knuth

def resumo():
    mensagem = "Donald Evin Knuth (1938) é um matemático e cientista de computadores norte-americano, cientista computacional de renome e professor emérito da Universidade de Stanford. É o autor do livro The Art of Computer Programming, uma das principais referências da ciência da computação. Ele praticamente criou o campo de análise de algoritmos e fez muitas das principais contribuições a vários ramos da teoria da computação. Ele também criou o sistema tipográfico TeX, o sistema de criação de fontes METAFONT, além de ser pioneiro do conceito de programação literária. Finalmente, desenvolveu o conceito de número surreal."
    return mensagem


def doutorado():
    mensagem = "Graduou-se em 1960 e em 1963 obteve o doutorado no Instituto de Tecnologia da Califórnia (Caltech)"
    return mensagem


def contribuicoes():
    mensagem = "É o autor do livro The Art of Computer Programming, uma das principais referências da ciência da computação."
    return mensagem


def artigos():
    mensagem = "Donald Evin Knuth (1938) é um matemático e cientista de computadores norte-americano, cientista computacional de renome e professor emérito da Universidade de Stanford."
    return mensagem


def citacoes():
    mensagem = "A ciência é o que nós compreendemos suficientemente bem para explicar a um computador. A arte é tudo mais"
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Donald Knuth.\n")

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
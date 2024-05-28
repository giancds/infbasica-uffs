def resumo():
    mensagem = "Alan Mathison Turing  foi um matemático britânico, pioneiro da computação e considerado o pai da ciência computacional e da inteligência artificial."
    return mensagem


def doutorado():
    mensagem = "John McCarthy obteve um doutorado em matemática pela Universidade de Princeton em 1951. Sua tese foi intitulada Aplicações de Funções Operacionais de Análise Espacial"
    return mensagem


def contribuicoes():
    mensagem = ""
    return mensagem


def artigos():
    mensagem = "John McCarthy publicou uma série de artigos notáveis ao longo de sua carreira, muitos dos quais tiveram um impacto significativo no desenvolvimento da inteligência artificial e da ciência da computação. Alguns dos seus principais artigos incluem: \n Programs with Common Sense (1959) - Neste artigo, McCarthy discute a necessidade de dotar os computadores com senso comum, uma ideia fundamental para a inteligência artificial. \n Towards a Mathematical Science of Computation (1961) - Este artigo aborda questões fundamentais relacionadas à teoria da computação e à formalização dos processos computacionais. \n A Basis for a Mathematical Theory of Computation (1963) - Aqui, McCarthy apresenta a linguagem de programação Lisp, que se tornou fundamental no desenvolvimento de inteligência artificial e é amplamente utilizada até hoje. \n Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I (1960) - Este artigo, escrito juntamente com o cientista da computação Stephen Cole Kleene, introduz a notação de funções recursivas e é fundamental para a compreensão da teoria da computação. \n Artificial Intelligence: A General Survey (1973) - McCarthy fornece uma visão geral abrangente do campo emergente da inteligência artificial, discutindo várias abordagens e aplicações."
    return mensagem


def citacoes():
    mensagem = "Como fazer um programa de computador compreender coisas como 'eu quero uma xícara de café' é muito difícil mesmo para o mais avançado dos programas de computador. Mas, 'por favor, me dê uma página do livro tal e me mostre onde está a palavra tal', é bem possível."
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

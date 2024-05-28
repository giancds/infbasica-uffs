def resumo():
    mensagem = "John McCarthy foi um cientista da computação de notabilidade incontestável, responsável por introduzir e desenvolver o conceito de inteligência artificial. A sua contribuição para essa área começou com a organização de uma conferência emblemática em 1955, onde o termo “inteligência artificial” foi utilizado pela primeira vez, estabelecendo um precedente para décadas de pesquisa subsequente."
    return mensagem


def doutorado():
    mensagem = ""
    return mensagem


def contribuicoes():
    mensagem = "Inteligência Artificial (IA):Fundador da IA: McCarthy é amplamente reconhecido como um dos fundadores do campo da Inteligência Artificial.\n Ele cunhou o termo Inteligência Artificial em 1956. Dartmouth Conference: Organizou a conferência seminal em Dartmouth College em 1956, que é considerada o evento fundador da IA como um campo de pesquisa. Linguagens de Programação:\nLISP: McCarthy desenvolveu a linguagem de programação LISP em 1958. LISP tornou-se uma das principais linguagens de programação usadas na pesquisa de IA devido à sua capacidade de manipular símbolos e listas de maneira eficiente.\nComputação em Tempo Compartilhado:\nMcCarthy foi pioneiro na ideia de computação em tempo compartilhado, que permitiu a vários usuários acessar um computador simultaneamente. Esta inovação foi crucial para o desenvolvimento de sistemas operacionais modernos.\nTeoria da Computação e Lógica Formal:\nTrabalhou extensivamente em lógica formal e seus usos em computação. Contribuiu para a teoria da computabilidade e formalização de problemas de IA em termos matemáticos precisos.\nContribuições Acadêmicas:\nInstituições: Lecionou no Instituto de Tecnologia de Massachusetts (MIT), na Universidade de Stanford e na Universidade de Princeton.\nPublicações: McCarthy publicou inúmeros artigos influentes sobre IA, lógica matemática e teoria da computação"
    
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

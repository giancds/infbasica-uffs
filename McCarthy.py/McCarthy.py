def resumo():
    mensagem = ""
    return mensagem


def doutorado():
    mensagem = "McCarthy recebeu seu PhD em matemática da universidade de Princeton em 1951, após completar sua dissertação nomeada Operadores de projeção e equações diferenciais parciais."
    return mensagem


def contribuicoes():
    mensagem = ""
    return mensagem


def artigos():
    mensagem = "Entre suas principais publicações podemos citar:\n McCarthy, J. 1959. Programs with Common Sense. In Proceedings of the Teddington Conference on the Mechanization of Thought Processes, 756-91. London: Her Majesty's Stationery Office.\n\nMcCarthy, J. 2002. Actions and other events in situation calculus. In Fensel, D.; Giunchiglia, F.; McGuinness, D.; and Williams, M., eds., Proceedings of KR-2002, 615-628."
    return mensagem


def citacoes():
    mensagem = "Progressos fundamentais não podem ser alcançados através de avanços incrementais em tecnologias existentes.\nJohn McCarthy."
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre John McCarthy.\n")

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
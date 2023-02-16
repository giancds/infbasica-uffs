def resumo():
    mensagem = "Considerado um dos pioneiros dos estudos e desenvolvimentos da inteligência artificial, McCarthy é o pai de tecnologias como a linguagem de programação LISP e os sistemas de computação por tempo compartilhado, fazendo com que o poder ocioso de mainframes pudessem ser utilizados. Os computadores que hoje conhecemos como computadores pessoais, só vieram a existir cerca de dez anos depois da criação do conceito de Tempo Compartilhado(Time sharing)"
    return mensagem


def doutorado():
    mensagem = "McCarthy recebeu seu PhD em matemática da universidade de Princeton em 1951, após completar sua dissertação nomeada Operadores de projeção e equações diferenciais parciais."
    return mensagem


def contribuicoes():
    mensagem = "É considerado um dos fundadores da Inteligência artificial\n2- em 1958 propôs o conceito de 'Advice Talker' que inspirou trabalhos posteriores no ramo da Programação lógica\n3-Criador da linguagem de programação Lisp\n4- em 1959 criou o método 'Garbage Collection, uma espécie de gerenciamento automatico de memória, para resolver problemas em Lisp\n5- Em 1966, McCarthy e sua equipe em Stanford escreveram um programa de computador usado para jogar uma série de partidas de xadrez com contrapartes na União Soviética"
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
def resumo():
    mensagem = "John Hopcroft é um matemático e cientista da computação americano, nascido em 7 de outubro de 1939 em Seattle, Washington. Ele é conhecido por suas contribuições à teoria da computação e aos algoritmos. Ele recebeu seu diploma de bacharel em engenharia elétrica pela Universidade de Seattle em 1961 e seu doutorado em matemática pela Universidade de Stanford em 1964. Começou sua carreira acadêmica como professor assistente na Universidade de Princeton em 1964, onde permaneceu até 1967. Em seguida, tornou-se professor de ciência da computação na Universidade Cornell, onde passou a maior parte de sua carreira, tornando-se professor emérito em 2000. Entre as suas contribuições mais importantes para a ciência da computação, destacam-se a definição do conceito de 'nível de determinação' para as gramáticas formais, o algoritmo de Hopcroft-Karp para a determinação de fluxo máximo em redes, o algoritmo de particionamento espectral para grafos e a coautoria do livro 'Introdução à Teoria dos Grafos'. Hopcroft foi o destinatário de vários prêmios e honras por suas contribuições, incluindo o Prêmio Turing em 1986, a Medalha Nacional de Ciência em 1987, e a Medalha John von Neumann em 2010. Ele também é membro da Academia Nacional de Engenharia, da Academia Nacional de Ciências e da Academia Americana de Artes e Ciências. Hoje em dia, John Hopcroft é um dos principais pesquisadores em ciência da computação e continua ativo na pesquisa e no ensino em sua área de especialização."
    return mensagem


def doutorado():
    mensagem = ""
    return mensagem


def contribuicoes():
    mensagem = ""
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


print("\nBoa noite! Você está aprendendo sobre John Hopcroft.\n")

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
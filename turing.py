def resumo():
    mensagem = "Charles Babbage foi um cientista, matemático, filósofo, engenheiro mecânico e inventor inglês, que criou o conceito de um computador programável. Ele é principalmente conhecido por ter criado o primeir conputador de uso geral, utilizando partes mecânicas, chamado de máquina análitica, porém exigia técnicas e materais caros na época, e nunca foi construído. Nascido na Inglaterra, mais precisamente em Londres, em meados de 1791. Nascido de uma famíilia rica, seu pai possibilitou que Babbage tivesse acesso a uma ensino muito bom, o que alavancou a carreira acadêmica de Babbage."
    return mensagem


def doutorado():
    mensagem = "Chales Babbage não possui doutorado, mas conta com bacharelado em várias áreas e já atuou como professor de Matemática, no Trinity College, em Cambrigde. Posteriormente foi até mesmo membro da Royal Society of Lodon. Também publicou diversos e artigos recebeu uma bolsa do governo para projectar uma calculadora com capacidade para até a vigésima casa decimal."
    return mensagem


def contribuicoes():
    mensagem = "A contribuição mais famosa de Babbage, foi o primeiro computador de uso geral, mas ele também teve muita influência me várias outras áreas e até criou o conceito de Computador Programável."
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

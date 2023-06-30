def resumo():
    mensagem = "Karen Spärck Jones foi uma cientista da computação britânica especializada em processamento de linguagem natural e recuperação de informações."
    return mensagem


def doutorado():
    mensagem = "Karen Spärck Jones realizou seus estudos em Cambridge, na Inglaterra. Sua tese de doutorado 'Synonymy and Semantic Classification' é agora reconhecida como à frente de seu tempo na exploração de técnicas estatísticas e simbólicas combinadas em PNL. "
    return mensagem


def contribuicoes():
    mensagem = "Criou o conceito conhecido como 'freqüência inversa do termo', que é a base dos sistemas de busca e localização. Ele analisa os termos que mais aparecem nos textos e os cruzam com um sistema de filtro, mostrando a relevância dos temas para a busca."
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

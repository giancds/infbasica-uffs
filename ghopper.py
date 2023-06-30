def resumo():
    mensagem = "Grace Brewster Murray Hopper, nascida em 1906, em Nova York, foi uma grande contribuinte no desenvolvimento das linguagens de programação no que são hoje. Atuou na Marinha Americana dos Estados Unidos da América e teve grande influência na indústria computacional."
    return mensagem


def doutorado():
    mensagem = "Na vida acadêmica, formou-se em Matemática e Física em 1928 no Vassar College, terminando em Yale seu mestrado em matemática em 1930, e doutorado em Matemática em 1934."
    return mensagem


def contribuicoes():
    mensagem = "A cientista contribuiu para a indústria em diversos aspectos. Alguns de seus trabalhos mais marcantes incluem a criação e desenvolvimento da linguagem COBOL - linguagem que foi essencial à simplificação da programação -, além do compilador, ferramenta que, figurativamente falando, traduz o código do programa para uma linguagem legível à maquina."
    return mensagem


def artigos():
    mensagem = "BEYER, Kurt W. Grace Hopper and the invention of the information age. Mit Press, 2012.\n\nWILLIAMS, Kathleen Broome. Grace Hopper: Admiral of the cyber sea. Naval Institute Press, 2013.\n\nSAMMET, Jean. Farewell to Grace Hopper—end of an era!. Communications of the ACM, v. 35, n. 4, p. 128-131, 1992."
    return mensagem


def citacoes():
    mensagem = "Devemos declarar relacionamentos, não procedimentos\n\nPlease cut off a nanosecond and send it over to me.\n\nHumans are allergic to change. They love to say, We've always done it this way. I try to fight that. Thats why I have a clock on my wall that runs counter-clockwise.\n\nEstamos inundando as pessoas com muitas informações. Precisamos alimentá-las por meio de um processador. Um ser humano deve transformar informação em inteligência ou conhecimento. Temos a tendência de esquecer que nenhum computador jamais fará uma pergunta nova."
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Grace Brewster Murray Hopper.\n")

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

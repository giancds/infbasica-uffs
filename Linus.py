def resumo():
    mensagem = "\nLinus Benedict Torvalds (28 de dezembro de 1969) é um engenheiro de software, nascido na Finlândia e naturalizado estado-unidense em 2010."
    return mensagem


def doutorado():
    mensagem = "\nTorvalds estudou na Universidade de Helsinki, de 1988 até 1996, com um mestrado em Ciência da Computação a partir do grupo NODES.\n Sua carreira acadêmica foi interrompida após 1 ano de estudo, pois entrou no Exéricto da Finlândia."
    return mensagem


def contribuicoes():
    mensagem = "\nLinus é criador, e por muito tempo o desenvolvedor mais importante do núcleo Linux, sendo utilizado em importantes sistemas Linux, Android e Chrome OS.\nÉ também o criador do Git, sistema de controle de versão amplamente utilizado, e o aplicativo para planejamento e registro de mergulho, Subsurface."
    return mensagem


def artigos():
    mensagem = "\nLinus foi autor de 2 livros, 'Just for Fun'(Só por diversão) de 2001 e 'Open Sources'(Códigos abertos), de 1999.\nAlém disso, Linus foi o criador do kernel Linux e do controle de versões distribuído Git.\nAqui está concentrada a maior parte do seu trabalho:https://github.com/torvalds/linux "
    return mensagem


def citacoes():
    mensagem = "\nDentre suas citações temos:\n'Nunca me chamaram de um cara legal.'\n'Na minha opinião, a Microsoft é muito melhor em fazer dinheiro do que Sistemas Operacionais.'\n'Se a Microsoft faz aplicações para Linux que significa que eu ganhei.'"
    return mensagem


def sair():
    mensagem = "\nObrigad@ pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nOlá! Você está aprendendo sobre Linus Torvalds.\n")

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

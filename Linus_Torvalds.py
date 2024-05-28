def resumo():
    mensagem = "\n Linus Benedict Torvalds é um engenheiro de software, nascido na Finlândia e naturalizado estado-unidense em 2010, criador, e por muito tempo o desenvolvedor mais importante do núcleo Linux."
    return mensagem


def doutorado():
    mensagem = "Não encontrado"
    return mensagem


def contribuicoes():
    mensagem = "\n É o criador do Kernel do Linux, base fundamental sobre a qual são construídos diversos sistemas operacionais gratuitos, como as distribuições Linux Ubuntu, Debian e Fedora, além de produtos do Google, como o Chrome OS e o Android"
    return mensagem


def artigos():
    mensagem = "Com base em pesquisas, não foi possível encontrar nenhum artigo escrito por Linus Torvalds."
    return mensagem


def citacoes():
    mensagem = "Se a Microsoft faz aplicações para Linux que significa que eu ganhei."
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

def resumo():
    mensagem = "John von Neumann, nascido em 23 de dezembro de 1903 na região de Margittai Neumann János Lajos, foi um matemático húngaro de origem judaica, naturalizado estadunidense.\nFoi um dos responsáveis pela criação do ENIAC (Electronic Numeric Integrator and Computer), o primeiro computador para uso profissional (militar). Desensolvedor de uma arquitetura capaz de armazenar e executar programas em uma máquina, que posteriormente seria conhecida como Arquitetura de Von Neumann."
    return mensagem


def doutorado():
    mensagem = "Doutoramento em Matemática"
    return mensagem


def contribuicoes():
    mensagem = "Contribuiu na teoria dos conjuntos, análise funcional, teoria ergódica, mecânica quântica, ciência da computação, economia, teoria dos jogos, análise numérica, hidrodinâmica das explosões, estatística e muitas outras áreas da matemática.\nEntre suas obras, estão: Autômato celular de von Neumann, Vizinhança de von Neumann, Construtor universal de Von Neumann, arquitetura de von Neumann, Álgebra de von Neumann, entre outros."
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


print("\nBoa noite! Você está aprendendo sobre John von Neumann.\n")

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

def resumo():
    mensagem = "Katherine Louise Bouman é uma professora assistente de ciência da computação no Instituto de Tecnologia da Califórnia. Ela pesquisa métodos computacionais para geração de imagens e foi uma das pessoas responsáveis pela reprodução da primeira imagem de um buraco negro. "
    return mensagem


def doutorado():
    mensagem = "Doutorado      em ciência da computação e inteligência artificial no Instituto de Tecnologia de Massachusetts (MIT), nos Estados Unidos"
    return mensagem


def contribuicoes():
    mensagem = "Liderou o desenvolvimento do algoritmo que possibilitou capturar a primeira imagem de um buraco negro. Em conjunto com outros cientistas, foi uma das principais responsáveis por criar e elaborar este algoritmo, que foi capaz de contabilizar os dados obtidos pelos telescópios e gerar a imagem."
    return mensagem


def artigos():
    mensagem = "Imagens extremas via inversão de modelo físico: vendo além dos cantos e criando imagens de buracos negros"
    return mensagem


def citacoes():
    mensagem = "É possível enxergar algo que, por definição, é impossível de ser visto?"
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Katherine Bouman.\n")

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

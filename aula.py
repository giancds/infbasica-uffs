def resumo():
    mensagem = "GGeoffrey Everest Hinton nasceu em 6 de dezembro de 1947 em Londres, Reino Unido, e é um especialista em psicologia cognitiva e cientista da computação reconhecido por ser trabalho em redes neurais artificiais. Professor no departamento de ciência da computação na Universidade de Toronto (Canadá), também atua como conselheiro de Aprendizado de Máquina no Instituto Canadense de Pesquisa Avançada. Em 2012 ofereceu um curso on-line gratuito sobre Redes Neurais na plataforma educacional Coursera."
    return mensagem


def doutorado():
    mensagem = ""
    return mensagem


def contribuicoes():
    mensagem = ""
    return mensagem


def artigos():
    mensagem = "1º artigo mais citado - Imagenet classification with deep convolutional neural networks - 127230 citações" 
"2º artigo mais citado - Deep learning - 60553 citações"
"3º artigo mais citado - Dropout: a simple way to prevent neural networks from overfitting - 40878 citações"
    return mensagem


def citacoes():
    mensagem = "Total de citações em 08/02/2023 as 21:05h 657011"
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
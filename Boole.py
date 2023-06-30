def resumo():
    mensagem = "George Boole (1815-1864) foi um matemático inglês, criador da Álgebra Booleana, trabalho fundamental para a posterior evolução dos computadores."
    return mensagem


def doutorado():
    mensagem = "Em 1835 abriu uma escola e passou a estudar matemática. Ao estudar as obras de Newton, Laplace e Lagrange, escreveu uma série de textos. Foi encorajado pelo matemático Duncan Gregory e começou a estudar álgebra e a publicar seus trabalhos no Cambridge Mathematical Journal."
    return mensagem


def contribuicoes():
    mensagem = "Em 1857, Boolen foi eleito membro da Royal Society. Recebeu títulos das Universidades de Dubli e Oxford. Entre seus trabalhos publicados estão: “Tratado em Equações Diferenciais” (1859), “Tratado em Cálculo de Diferenças Finitas” (1860), além de mais de 50 trabalhos sobre as propriedades básicas dos números."
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

def resumo():
    mensagem = "Alan Mathison Turing  foi um matemático britânico, pioneiro da computação e considerado o pai da ciência computacional e da inteligência artificial."
    return mensagem


def doutorado():
    mensagem = ""
    return mensagem


def contribuicoes():
    mensagem = ""
    return mensagem


def artigos():
    mensagem = "Performance and Operational Economics Estimates for a Coal Gasification\nCombined-Cycle Cogeneration Powerplant. Nainiger, Joseph J.; Burns, Raymond K.;\nEasley, Annie J. NASA, Lewis Research Center, Cleveland, Ohio. NASA Tech Memo 82729 Mar 1982 31p.\n\nBleed Cycle Propellant Pumping in a Gas-Core Nuclear Rocket Engine System. Kascak,\nA. F.; Easley, A. J. National Aeronautics and Space Administration. Lewis\nResearch Center, Cleveland, Ohio. Report No.: NASA-TM-X-2517; E-6639 March 1972.\n\nEffect of Turbulent Mixing on Average Fuel Temperatures in a Gas-Core Nuclear Rocket\nEngine. Easley, A. J.; Kascak, A. F.; National Aeronautics and Space Administration.\nLewis Research Center, Cleveland, Ohio. Report No.: NASA-TN-D-4882 Nov 1968."
    return mensagem


def citacoes():
    mensagem = "Nada jamais foi dado às minorias ou às mulheres. Foi necessário lutar para conseguir oportunidades iguais, e continuamos lutando hoje em dia.\nAnnie Easley"
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

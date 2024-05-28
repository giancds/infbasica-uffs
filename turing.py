def resumo():
    mensagem = ("""
    Herbert Alexander Simon foi um economista alemão, com cidadania estadunidense. Foi agraciado com o Prémio de Ciências Económicas em Memória de Alfred Nobel de 1978. Foi um pesquisador nos campos de psicologia cognitiva, informática, administração pública, sociologia económica, e filosofia.""")
    return mensagem


def doutorado():
    mensagem = ("Simon recebeu seu doutorado em ciências políticas pela Universidade de Chicago em 1943. Sua obra abrangeu campos tão diversos como economia, ciência da computação, psicologia cognitiva e teoria da administração. Em 1978 recebeu o Prêmio Nobel de Economia, juntamente com seu colega, por seu trabalho pioneiro em teoria da decisão. Fora isso, Recebeu ainda a Medalha Nacional de Ciência, em 1986 e o Award for Outstanding Lifetime Contributions to Psychology, da APA, em 1993.")
    return mensagem


def contribuicoes():
    mensagem = """Foi agraciado com o prêmio Turing de 1975 (considerado o prêmio Nobel da ciência da computação) e de fato foi um dos pioneiros da disciplina tecnocientífica chamada “inteligência artificial” (I.A.).  """
    return mensagem


def artigos():
    mensagem = """1938 (com Clarence E. Ridley). Measuring Municipal Activities: a Survey of Suggested Criteria and Reporting Forms For Appraising Administration.
1943. Fiscal Aspects of Metropolitan Consolidation.
1945. The Technique of Municipal Administration, 2d ed.
1955. "A Behavioral Model of Rational Choice", Quarterly Journal of Economics, vol. 69, 99–118.
1956. "Reply: Surrogates for Uncertain Decision Problems", Office of Naval Research, Jan. 1956.
– Reprinted in 1982, In: H.A. Simon, Models of Bounded Rationality, Volume 1, Economic Analysis and Public Policy, Cambridge, Mass., MIT Press, 235–44. """
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

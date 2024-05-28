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
    mensagem = ("1947. The Mathematician, The Works of the Mind. ed. por R. B. Heywood, University of Chicago Press, 180–196. \n"
    + "1951. The Future of High-Speed Computing, Resumo de um discurso no Seminário IBM sobre Computação Científica, novembro de 1949, Proc. Comp. Sem. , IBM, 13. \n"
    + "1954. The Role of Mathematics in the Sciences and in Society. Address at 4th Conference of Association of Princeton Graduate Alumni, Junho, 16–29. \n"
    + "1954. The NORC and Problems in High Speed Computing, Address por ocasião da primeira exibição pública da IBM Naval Ordnance Research Calculator, Dez. 2. \n"
    + "1955. Method in the Physical Sciences, The Unity of Knowledge, ed. por L. Leary, Doubleday, 157–164. \n"
    + "1955. Can We Survive Technology?, Junho. \n"
    + "1955. Impact of Atomic Energy on the Physical and Chemical Sciences, Speech - M.I.T. Alumni Day Symposium, Junho 13, Summary, Tech. Rev. 15–17. \n"
    + "1955. Defense in Atomic War, Paper delivered at a symposium in honor of Dr. R. H. Kent, Dez. 7, 1955, The Scientific Bases of Weapons, Journ. Am. Ordnance Assoc., 21–23. \n"
    + "1956. The Impact of Recent Developments in Science on the Economy and on Economics, Partial text of a talk at the National Planning Assoc., Washington, D.C., Dez. 12, 1955, Looking Ahead, 4:11. \n")
    return mensagem


def citacoes():
    mensagem = ("The legend of John von Neumann, Halmos, P.R. (Amer. Math. Monthly 80, 1973). \n"
    + "John von Neumann and Norbert Wiener: From mathematics to the tecnologies of life and death, Heims, S. J. (Cambridge, MA, MIT Press, 1980). \n"
    + "John von Neumann, Ulam (Bull. Amer. Math. Soc. 64, pg. 1-49, 1958)")
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

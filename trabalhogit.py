def resumo():
    mensagem = """
    Timothy John Berners-Lee nasceu em Londres, Inglaterra, em 8 de junho de 1955. 
    Ele é um físico britânico, cientista da computação e professor do MIT (Instituto de Tecnologia de Massachusetts, em inglês). 
    Seu cargo mais conhecido é ser o criador da World Wide Web, o famoso termo técnico WWW."""


    return mensagem


def doutorado():
    mensagem = """
    Timothy John Berners-Lee estudou no The Queen's College, em Oxford, de 1973 a 1976, onde diplomou-se em Física. 
    É um pesquisador sênior e titular e fundador da cadeira de 3Com no Laboratório de Inteligência Artificial e Ciência da Computação do MIT (CSAIL).
    É um diretor da The Web Science Research Initiative (WSRI)e um membro do conselho consultivo do Centro de Inteligência Coletiva do MIT.
    Em abril de 2009, foi eleito como membro da Academia Nacional de Ciências dos Estados Unidos, sediada em Washington, D.C.
     Em 2011, foi nomeado como um membro do conselho de administração da Fundação Ford. """

    return mensagem


def contribuicoes():
    mensagem = """
    Em 1980, Timothy John Berners-Lee começou a desenvolver um projeto a partir do conceito de hipertexto, visando o compartilhamento de informações entre os pesquisadores,
    do qual apresentou um protótipo ENQUIRE. Depois de um período fora do CERN e trabalhando em contato com redes de computadores, ele retorna em 1984,
    quando junta as ideias de hipertexto retomando o desenvolvimento da ideia de sistema de compartilhamento de informações global que temos hoje, a World Wide Web."""
    return mensagem


def artigos():
    mensagem = "(1989). Information Management: A Proposal.: proposta de Berners-Lee onde a ideia da Web foi apresentada."
    return mensagem


def citacoes():
    mensagem = """
    1- A web não está concluída, é apenas a ponta do iceberg. As novas mudanças irão balançar o mundo ainda mais.
    2- "O poder da web está em sua universalidade. O acesso por todos, independentemente da deficiência é um aspecto essencial."""
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
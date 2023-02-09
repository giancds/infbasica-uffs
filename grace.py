def resumo():
    mensagem = "Grace Murray Hopper foi almirante e analista de sistemas da Marinha dos Estados Unidos nas décadas de 1940 e 1950, criadora da linguagem de programação de alto nível Flow-Matic e uma das primeiras programadoras do computador Harvard Mark I em 1944."
    return mensagem


def doutorado():
    mensagem = "obteve um doutorado em Matemática por Yale em 1934 e, quando os EUA entraram na Segunda Guerra Mundial, abandonou seu trabalho de professora de matemática e ingressou na Marinha, onde chegou à patente de contra-almirante."
    return mensagem


def contribuicoes():
    mensagem = "Grace Hopper foi a criadora da COBOL, a primeira linguagem de programação complexa. Formou-se em 1944 como a primeira da turma e foi designada para a Bureau of Ships Computation Project da Harvard University como tenente júnior. Ela serviu na equipe de programação Mark I computer dirigida por Howard H. Aiken."
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

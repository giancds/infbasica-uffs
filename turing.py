def resumo():
    mensagem = "Howard Hathaway Aiken was an American physicist and a pioneer in computing, being the original conceptual designer behind IBM's Harvard Mark I computer."
    return mensagem


def doutorado():
    mensagem = "Aiken studied at the University of Wisconsin–Madison and later obtained his Ph.D. in physics at Harvard University in 1939."
    return mensagem


def contribuicoes():
    mensagem = "He envisioned an electro-mechanical computing device that could do much of the tedious work for him. This computer was originally called the ASCC (Automatic Sequence Controlled Calculator) and later renamed Harvard Mark I."
    return mensagem

def artigos():
    mensagem = "Howard Aiken: Portrait of a computer pioneer"
    return mensagem


def citacoes():
    mensagem = '"Don\'t worry about people stealing an idea. If it\'s original, you will have to ram it down their throats."'
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

def resumo():
    mensagem = "Alan Mathison Turing  foi um matemático britânico, pioneiro da computação e considerado o pai da ciência computacional e da inteligência artificial."
    return mensagem


def doutorado():
    mensagem = ""
    return mensagem


def contribuicoes():
    mensagem = "Linus Torvalds contribuiu imensamente para a área da computação, principalmente por criar o kernel Linux, que é amplamente utilizado em sistemas operacionais em todo o mundo."
    return mensagem


def artigos():
    mensagem = "Linus Torvalds escreveu muitos artigos técnicos e posts em fóruns de discussão, mas ele é mais conhecido por seu trabalho no desenvolvimento e manutenção do kernel Linux."
    return mensagem


def citacoes():
    mensagem = "Uma das citações famosas de Linus Torvalds é: 'A vida é curta demais para mergulhar no código de outra pessoa.'"
    return mensagem


def sair():
    mensagem = "\nBoa noite! Você está aprendendo sobre Linus Torvalds."
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

def resumo():
    mensagem = "Blaise Pascal foi responsável pela invenção da primeira calculadora mecânica, um vislumbre do potencial computacional que os próximos séculos viriam a ostentar."
    return mensagem


def doutorado():
    mensagem = "Crescido em uma família com negócios já bem estabelecido, Pascal marcou seu nome na história não por uma formação excepcional com diversas certificações, uma vez que embora frequentasse algumas universidades ocasionalmente, teve sua criação pautada no ensino familiar e no autodidatismo, tendo o tédio e o fascínio pela física, matemática e filosofia como principal motivação de suas descobertas."
    return mensagem


def contribuicoes():
    mensagem = "Pascal desenvolveu a primeira calculadora mecânica de operações básicas, a teoria das probabilidades, e fez ponderações sobre a mecânica dos fluídos e a natureza do vácuo. Flertou ainda com algumas ideias do campo filosófico, tendo como maiores motivações Kant e Descartes."
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

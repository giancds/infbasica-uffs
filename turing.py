def resumo():
    mensagem = "Barbara Liskov nascida em Los Angeles no dia 7 de Novembro de 1939, cresceu em San Francisco filha de Jane e Moses Huberman. Não ingressou diretamente na universidade, trabalhando antes alguns anos."
    return mensagem


def doutorado():
    mensagem = "Doutorado em Ciência da Computação"
    return mensagem


def contribuicoes():
    mensagem = "Liskov é membro da Academia Nacional de Engenharia (NAE), da Academia Nacional de Ciências, parceira da Academia Americana de Artes e Ciência e da associação de Maquinário para Computação (ACM). Liskov liderou muitos projetos significativos, incluindo o sistema operacional Vénus, um sistema interativo pequeno, de baixo custo e compartilhado."
    return mensagem


def artigos():
    mensagem = "É autora de mais de 140 artigos científicos"
    return mensagem


def citacoes():
    mensagem = "A principal motivação para desenvolver boas abstrações é a de permitir a construção de sistemas grandes e complexos de maneira compreensível e gerenciável.2-O desenvolvimento de software é inerentemente difícil porque é um esforço humano, e as pessoas são falíveis. Devemos criar ferramentas e metodologias que ajudem a mitigar essa falibilidade."
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Barbara Liskov .\n")

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

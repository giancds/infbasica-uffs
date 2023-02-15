def resumo():
    mensagem = "Larry Wall é um programador e autor americano que criou a linguagem de programação Perl."
    return mensagem


def doutorado():
    mensagem = """
        Bacharelado: Linguagens Naturais e Artificiais - Seattle Pacific University
        Bacharelado: Linguística - Berkley University
    
    """
    return mensagem


def contribuicoes():
    mensagem = """
        Larry Wall criou a linguagem de programação Perl em 1987 para facilitar o processamento de relatórios. 
        É uma linguagem muito utilizada na administração de sistemas.
        Além do Perl, Larry também criou a linguagem Raku (inicialmente chamada de Perl 6) em 2015 para corrigir erros antigos.
        Por fim, Larry também é autor do programa patch do Unix, um programa que aplica as diferenças textuais entre dois programas [wikipedia].
    """
    return mensagem


def artigos():
    mensagem = """
        Hobbits Would Make Great Programmers - Big Think
        Programming Perl - O'Reilly
    
    """
    return mensagem


def citacoes():
    mensagem = "'O Perl foi projetado para nunca ser perfeito. Foi projetado para evoluir, para ser adaptável, como dizem.' - Larry Wall, Linux Journal."
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Larry Wall.\n")

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
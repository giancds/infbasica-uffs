def resumo():
    mensagem = "\nRasmus Lerdorf é um programador canadiano-dinamarquês.\n Ele é o autor da primeira versão da linguagem de programação PHP.\n Lerdorf foi co-autor das versões seguintes do PHP, juntamente com os israelitas fundadores da Zend Technologies, Andi Gutmans e Zeev Suraski."
    return mensagem


def doutorado():
    mensagem = "\nSe formou na King City Secondary School em 1988, e, em 1993, formou-se na University of Waterloo como Bacharel em Applied Science in Systems Design Engineering."
    return mensagem


def contribuicoes():
    mensagem = "Contibuiu para o Apache HTTP Server, adicionou a cláusula LIMIT para o mSQL DBMS, e lançou a primeira versão do PHP (Hypertext Preprocessor) em 1995."
    return mensagem


def artigos():
<<<<<<< HEAD
    mensagem = "[[Inventing PHP: Rasmus Lerdorf], [25 Years of PHP with Rasmus Lerdorf], [Programming PHP 2e]"
=======
    mensagem = "[[Inventing PHP: Rasmus Lerdorf], \n[25 Years of PHP with Rasmus Lerdorf], \n[Programming PHP 2e]"
>>>>>>> origin/pedro
    return mensagem


def citacoes():
<<<<<<< HEAD
    mensagem = "[[For all the folks getting excited about my quotes. Here is another - Yes, I am a terrible coder, but I am probably still better than you], [We have things like protected properties. We have abstract methods. We have all this stuff that your computer science teacher told you you should be using. I don't care about this crap at all.]"
=======
    mensagem = "[[For all the folks getting excited about my quotes. Here is another - Yes, I am a terrible coder, but I am probably still better than you], \n[We have things like protected properties. We have abstract methods. We have all this stuff that your computer science teacher told you you should be using. I don't care about this crap at all.]"        
>>>>>>> origin/pedro
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Rasmus Lerdorf.")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
Digite o número correspondente ao menu que você deseja acessar:
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

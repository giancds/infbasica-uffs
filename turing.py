def resumo():def resumo():
    mensagem = "Annie J. Easley foi uma cientista da computação, matemática e cientista de foguetes americana.\nFoi a líder do time responsável pelo desenvolvimento do software Centaur para processo conhecido como \nstaging- processo de combinação de várias sessões de foguete que pegam fogo em uma ordem específica e, então, \nse destacam da nave principal, para que essa atinja o espaço. Além disso, Annie foi uma das primeiras \nmulheres afro-descendentes a trabalhar, como cientista da computação, para a NASA."
    return mensagem


def doutorado():
    mensagem = "Annie não possui doutorado, pois estudar já era difícil para uma mulher negra na época. Entretanto, ela tem formação\nem Farmácia na Universidade Xavier e bacharel de Ciência em Matemática pela Universidade do Estado de Cleveland. "
    return mensagem


def contribuicoes():
    mensagem = "Sua carreira de 34 anos incluiu o desenvolvimento e a implementação de códigos de computação, que analisavam tecnologias de energias \nalternativas.Além disso, ela auxiliou a construção do sistema de stage super energético Centaur, estruturou projetos de energia solar, \neólica e identificou sistemas de conversão de energia e sistemas alternativos, a fim de solucionar problemas energéticos. Entre seus \nestudos na área energética, pode-se destacar pesquisas com o propósito de determinar a vida útil de baterias de armazenamento - \nutilizadas em veículos elétricos. Suas contribuições na computação, têm sido utilizadas para identificar sistemas de conversão de \nenergia, que oferecem melhorias, em relação às tecnologias disponíveis no mercado. O trabalho de Easley,com o projeto Centaur, \najudou a assentar os fundamentos tecnológicos para futuros lançamentos de naves espaciais e lançamentos de satélites para fins \nclimáticos, comunicacionais e militares. Em conjunto a isso, seu trabalho contribuiu para o voo da sonda Cassini, em 1997, para Saturno. \nO lançamento dessa sonda, tinha Centaur como sua referência de stage."
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


print("\nBoa noite! Você está aprendendo sobre Annie Easley.\n")

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
    mensagem = "Alan Mathison Turing  foi um matemático britânico, pioneiro da computação e considerado o pai da ciência computacional e da inteligência artificial."
    return mensagem


def doutorado():
    mensagem = ""
    return mensagem


def contribuicoes():
    mensagem = ""
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
        input

def resumo():
    mensagem = "John Bardeen nasceu dia 23 de outubro de 1908 em Medison - EUA. Suas principais criações envolvem as pesquisas dos semicondutores e foi o criador dos transistores"
    return mensage

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
    mensagem = "John Bardeen foi um dos grandes físicos do século XX. Sua contribuição para o desenvolvimento do transistor e para a compreensão da supercondutividade foi monumental. - Steven Chu" +

"A mente brilhante por trás do transistor e da teoria da supercondutividade, John Bardeen deixou um legado que continua a influenciar profundamente a física e a tecnologia modernas. - Richard Feynman" +

"John Bardeen exemplifica a combinação de criatividade, rigor intelectual e dedicação que define os grandes cientistas. Seu trabalho inovador mudou o mundo de maneiras que nunca poderíamos ter previsto. - Murray Gell-Mann" +

"John Bardeen personificava a busca incansável pelo conhecimento e pela excelência científica. Sua abordagem meticulosa e sua capacidade de pensar de forma original o destacaram como uma figura verdadeiramente notável na história da física - Nicolaas Bloembergen" +

"A genialidade de John Bardeen reside não apenas em suas descobertas revolucionárias, mas também em sua capacidade de compartilhar seu conhecimento e inspirar futuras gerações de cientistas. - Chen-Ning Yang"
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

def resumo():
    mensagem = "Alan Mathison Turing  foi um matemático britânico, pioneiro da computação e considerado o pai da ciência computacional e da inteligência artificial."
    return mensagem


def doutorado():
    mensagem = ""
    return mensagem


def contribuicoes():
    mensagem = ""
    return mensagem


def artigos():
    mensagem = " Guido van Rossum: The Modern Era of Python Publicado na revista IEEE Journals & Magazine em março de 2015\n https://ieeexplore.ieee.org/document/7063180\n "

   
   
    return mensagem


def citacoes():
    mensagem = "    Bonito é melhor que feio.\n Explícito é melhor que implícito.\n Simples é melhor que complexo.\n Complexo é melhor que complicado.\n Linear é melhor do que aninhado.\n Esparso é melhor que denso.\n Legibilidade conta.\n Casos especiais não são especiais o bastante para quebrar as regras.\n Ainda que praticidade vença a pureza.\n Erros nunca devem passar silenciosamente.\n menos que sejam explicitamente silenciados.\n Diante da ambiguidade, recuse a tentação de adivinhar. \n Dever haver um — e preferencialmente apenas um — modo óbvio para fazer algo. \n Embora esse modo possa não ser óbvio a princípio a menos que você seja holandês. \n Agora é melhor que nunca.\n Apesar de que nunca normalmente é melhor do que exatamente agora \n Se a implementação é difícil de explicar, é uma má ideia Se a implementação é fácil de explicar, pode ser uma boa ideiaNamespaces são uma grande ideia — vamos ter mais dessas!"
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
        print(mensagem)

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()



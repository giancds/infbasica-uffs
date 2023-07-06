def resumo():
    mensagem = ""
    return mensagem


def diplomas():
    mensagem = ""
    return mensagem


def contribuicoes():
    mensagem = ""
    return mensagem


def artigos():
    mensagem = "Grace Hopper, uma pioneira da ciência da computação, fez contribuições significativas para o campo. Embora ela tenha escrito diversos artigos e palestras, não existem registros de que tenha publicado dissertações acadêmicas. No entanto, faz-se necessário citar uma lista de algumas de suas obras mais conhecidas:\n1)'The Education of a Computer' - esta palestra, apresentada em 1947, é uma das primeiras descrições públicas sobre o funcionamento interno de um computador. Hopper introduziu conceitos como programação de alto nível e compiladores.\n2)'Automatic Coding for Digital Computers' - Este artigo, publicado em 1952, descreve o desenvolvimento do primeiro compilador, chamado A-0, e apresenta a ideia de programação de alto nível.\n3)'The Computer as a Tool' - Essa palestra, realizada em 1973, discute o papel dos computadores como ferramentas para solucionar problemas complexos e promover a colaboração entre pessoas.\n'Nanoseconds' - durante a década de 1960, Hopper popularizou o termo 'nanossegundos' como uma unidade de tempo para medir a velocidade de processamento dos computadores."
    return mensagem


def citacoes():
    mensagem = "Grace Hopper possui diversas citações inspiradoras, podemos citar algumas, por exemplo:\n1)'Para mim, a programação é mais do que uma importante arte prática. É também um empreendimento gigantesco nas bases do conhecimento.'\n2)'A única frase de que nunca gostei foi: 'Ora, sempre fizemos assim'. Eu sempre digo aos jovens: 'Vá em frente e faça isso. Você sempre pode se desculpar depois'.\n3)'Na época dos pioneiros, eles usavam bois para puxar pesado e, quando um boi não conseguia mover uma tora, eles não tentavam criar um boi maior. Não deveríamos estar tentando computadores maiores, mas mais sistemas de computadores.''"
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Grace Hopper.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Diplomas
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
        print("2 - Diplomas")
        mensagem = diplomas()

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

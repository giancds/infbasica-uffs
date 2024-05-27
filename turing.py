def resumo():
    mensagem = "Alan Turing foi um matemático e cientista da computação britânico cujo trabalho teve um impacto profundo e duradouro em várias disciplinas. Ele é mais conhecido por formular o conceito da Máquina de Turing, um modelo abstrato de um computador, que estabeleceu os fundamentos teóricos da computabilidade e da ciência da computação.Durante a Segunda Guerra Mundial, Turing desempenhou um papel crucial na quebra dos códigos de comunicação nazistas, contribuindo para a vitória dos Aliados." 
    return mensagem


def doutorado():
    mensagem = "De setembro de 1936 a julho de 1938, Turing realizou seu doutorado em Princeton, Nova Jersey, sob a orientacao de Alonzo Church."
    return mensagem


def contribuicoes():
    mensagem = "Máquina de Turing: Turing é mais conhecido por formular o conceito teórico da Máquina Turing em 1936. Esse dispositivo, embora uma abstração matemática, é considerado o modelo básico de qualquer computador digital. Ele ajudou a estabelecer os fundamentos teóricos da computação e da computabilidade. Teoria da Computação: Turing desenvolveu conceitos fundamentais para a teoria da computabilidade, estabelecendo limites teóricos para o que pode ser calculado e o que não pode. Seu trabalho influenciou profundamente o desenvolvimento da teoria da complexidade computacional e da lógica matemática. este de Turing: Em 1950, Turing propôs o Teste de Turing em seu artigo Computing Machinery and Intelligence. Ele sugeriu que um computador pode ser considerado inteligente se pudesse enganar um humano a acreditar que está interagindo com outro humano durante uma conversa.Este teste continua a ser uma referência importante na discussão sobre inteligência artificial."
    return mensagem


def artigos():
    mensagem = "On Computable Numbers, with an Application to the Entscheidungsproblem (1936). Computing Machinery and Intelligence (1950). Digital Computers Applied to Games (1953). The Chemical Basis of Morphogenesis" (1952)"
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

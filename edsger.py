def resumo():
    mensagem = "Edsger Dijkstra (1930-2002) foi um renomado cientista da computação holandês, conhecido por suas contribuições fundamentais para a teoria da computação e a prática da programação. Ele é considerado um dos pioneiros do campo da ciência da computação e um dos mais importantes teóricos de algoritmos do século XX. Além de seu trabalho em ciência da computação, Dijkstra também foi um defensor ativo de práticas de programação rigorosas e metodologias formais, e seus escritos sobre esses tópicos tiveram uma influência significativa na disciplina de engenharia de software. Ele recebeu vários prêmios e honras em reconhecimento por seu trabalho, incluindo o Prêmio Turing de 1972, o mais alto prêmio da ciência da computação."
    return mensagem


def doutorado():
    mensagem = "Edsger Dijkstra obteve seu doutorado em matemática na Universidade de Amsterdã, em 1959. Sua tese de doutorado, intitulada Uma extensão do cálculo de programação, explorava a aplicação do cálculo lambda na construção de algoritmos de programação. A tese é considerada uma das primeiras obras sobre métodos formais na programação, e estabeleceu a base para grande parte do trabalho subsequente de Dijkstra."
    return mensagem


def contribuicoes():
    mensagem = "Entre suas contribuições notáveis estão o algoritmo de Dijkstra, que é usado para encontrar o caminho mais curto entre dois pontos em um grafo, e a estrutura de dados conhecida como fila de prioridade, que é amplamente utilizada em algoritmos de programação. Dijkstra também foi fundamental no desenvolvimento da linguagem de programação Algol, que se tornou um padrão internacional na década de 1960."
    return mensagem


def artigos():
    mensagem = "Alguns dos artigos mais conhecidos de Edsger Dijkstra: A Case against the GOTO Statement (1968); Cooperating Sequential Processes (1965); Go To Statement Considered Harmful (1968); Hierarchical Ordering of Sequential Processes (1965)."
    return mensagem


def citacoes():
    "Não é a linguagem de programação que define o programador, mas sim sua lógica de pensamento."
    "A simplicidade é uma grande virtude, mas requer muito trabalho para alcançá-la e educação para apreciá-la. E para tornar as coisas simples, você precisa realmente entender profundamente todo o assunto."
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Edsger Dijkstra.\n")

continuar = True
while continuar == True:
    """
    1 - Resumo
    2 - Doutorado
    3 - Contribuições
    4 - Principais Artigos
    5 - Citações
    6 - Sair 
"""

    opcao = input( ) 

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()
    elif opcao == 5:
        print("5 - Citaçõe")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
def resumo():
    mensagem = "Niklaus Emil Wirth (Winterthur, 15 de fevereiro de 1934) é um professor e cientista da computação " \
               "suíço. Ele projetou várias linguagens de programação, incluindo Pascal, e foi pioneiro em vários " \
               "outros tópicos classicos em engenharia de software. "
    return mensagem


def doutorado():
    mensagem = "Niklaus Wirth realizou seu PhD na Universidade da Califórnia em Berkeleyem 1963. Seu instrutor foi Harry Huskey! \n Não mais registro técnicos do seu doutorado disponível."
    return mensagem


def contribuicoes():
    mensagem = "Suas principais contribuições foram:\n" \
               "O livro 'The Pascal User Manual and Report' , escrito em conjunto com Kathleen Jensen, serviu de base para " \
               "muitos esforços de implementação de linguagens nas décadas de 1970 e 1980 nos Estados Unidos e em toda a Europa.\n\
                Seu artigo 'Program Development by Stepwise Refinement' sobre o ensino da programação, é considerado um texto \
                clássico em engenharia de software. Em 1975, ele escreveu o livro 'Algorithms + Data Structures = Programs', que ganhou " \
               "amplo reconhecimento. As principais revisões deste livro com o novo título 'Algoritmos + Estruturas de Dados' foram publicadas em " \
               "1985 e 2004. Os exemplos da primeira edição foram escritos em Pascal. Estes foram substituídos nas edições posteriores por " \
               " exemplos escritos em Modula-2 e Oberon, respectivamente." \
               "Seu livro 'Programação Sistemática': Uma Introdução, foi considerado uma boa fonte para os estudantes que queriam " \
               "fazer mais do que apenas codificar. Como um texto desafiador para se trabalhar"\
               "Em 1992, ele publicou (juntamente com Jürg Gutknecht) a documentação completa do sistema operacional Oberon. Um " \
               "segundo livro (junto com Martin Reiser) foi planejado como um guia do programador."
    return mensagem


def artigos():
    mensagem = "Artigo Principal - Lei de Wirth.\n Em 1995, ele popularizou o ditado, agora conhecido como lei de Wirth," \
               " que afirma que o software está ficando mais lento mais rapidamente do que o hardware.\n" \
               "Artigo: 'Program Development by Stepwise Refinement' sobre o ensino da programação, é considerado um texto clássico em engenharia de software."
    return mensagem


def citacoes():
    mensagem = "Citações \n 1-Não consideramos uma boa prática de engenharia consumir um recurso generosamente apena porque ele é barato.\n" \
               "2- A experiência mostra uqe o sucesso de um curso de programação depende criticamente da escolha desses exempolos.\n" \
               "3- A programação geralmente é ensinada por exemplos." \
               "4- O software fica mais lento mais rápido do que o hardware fica mais rápido"
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Niklaus Wirth.\n")


continuar = True
while continuar == True:
    opcao = int(input("\nDigite o número correspondente ao menu que você deseja acessar:1-Resumo 2-Doutorado 3-"
                      "Contribuições 4-Principais Artigos 5 Citações 6-Sair\n"))

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

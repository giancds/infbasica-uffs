def resumo():
    mensagem = "Margaret Heafiel Hamilton é uma cientista da computação, engenheira de software e empresaria. Participou do projeto Apollo 11, a primeira missao tripulada á Lua, contribuiu sendo a diretora da Divisão de Software no Laboratorio de instrumentação do MIT, desenvolvendo o programa de voo usado no projeto."
    return mensagem


def doutorado():
    mensagem = "Ensino Médio:  Hancock High School;\nGraduação: Universidade de Michigan - Earlham College;\nPós Graduação: Metereologia no MIT."
    return mensagem


def contribuicoes():
    mensagem = "Além de desenvolver o programa de voo usado na missão Apollo 11, Margaret foi uma das desenvolvedors dos conceitos de computação paralela, teste de sistema, e capacidade de decisão com integração humana, tal como mostradores de prioridade que viriam a ser fundamento do design de software ultra confiável. Margaret recebe creditos por ter criado o termo 'engenharia de softaware'."
    return mensagem


def artigos():
    mensagem = "Publicou mais de 130 artigos, atas e relatórios relacionados aos 60 projetos e 6 programas importantes nos quais ela esteve envolvida. "
    return mensagem

def citacoes():
    mensagem = "“O que eles faziam quando você começava nessa organização era colocar você em um projeto que ninguém tinha conseguido ainda entender, ou sequer fazer algo funcionar. Quando eu comecei, eles me colocaram nesse projeto também. Era um código complicado e a pessoa que primeiro escreveu o software se orgulhava do fato que todos os comentários estavam em Grego ou Latim. Então me colocaram nesse projeto, e eu consegui fazer ele funcionar. Eu até imprimi as respostas em Grego e Latim. Eu fui a primeira que conseguiu fazer o projeto funcionar”."
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Margaret Hamilton.\n")

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

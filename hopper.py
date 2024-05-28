def resumo():
<<<<<<< HEAD
    mensagem = "Grace Hopper foi uma almirante e analista de sistemas da Marinha dos Estados Unidos criadora da linguagem de programação Flow-Matic, que foi base para COBOL"
=======
    mensagem = ""
>>>>>>> f9c1d4224d73a17eb2810acdcaee55c252fc1533
    return mensagem


def doutorado():
<<<<<<< HEAD
    mensagem = ""
=======
    mensagem = "Graduou-se em 1928 como bacharel em Matemática e Física e, em 1930, concluiu seu mestrado na Yale University. Em 1934, também na Yale University, conquistou seu Ph.D. em Matemática sob a orientação de Øystein Ore.["
>>>>>>> f9c1d4224d73a17eb2810acdcaee55c252fc1533
    return mensagem


def contribuicoes():
<<<<<<< HEAD
    mensagem = ""
=======
    mensagem = "Tudo foi feito sem definir os comandos para minimizar melindres entre os técnicos das empresas convocadas a participar da criação de um denominador comum entre todos os fabricantes existentes na época. Grace Hopper participou contribuindo com a abertura dos comandos FLOW-MATIC."
>>>>>>> f9c1d4224d73a17eb2810acdcaee55c252fc1533
    return mensagem


def artigos():
<<<<<<< HEAD
    mensagem = ""
=======
    mensagem = "Ela serviu na equipe de programação Mark I computer dirigida por Howard H. Aiken. Hopper e Aiken escreveram três artigos sobre o Mark I, também conhecido como a Calculadora Automática Controlada por Sequência."
>>>>>>> f9c1d4224d73a17eb2810acdcaee55c252fc1533
    return mensagem


def citacoes():
<<<<<<< HEAD
    mensagem = ""
=======
    mensagem = "A frase mais perigosa é: 'Sempre fizemos assim' ! Mudanças podem ser difíceis, mas são necessárias para o progresso. É importante estar aberto a novas ideias e abordagens, mesmo que elas pareçam diferentes ou desafiadoras."
>>>>>>> f9c1d4224d73a17eb2810acdcaee55c252fc1533
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

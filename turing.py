def resumo():
    mensagem = "Grace Murray Hopper (Nova Iorque, 9 de dezembro de 1906 — Condado de Arlington, 1 de janeiro de 1992) foi almirante e analista de sistemas da Marinha dos Estados Unidos nas décadas de 1940 e 1950, criadora da linguagem de programação de alto nível Flow-Matic (em desuso) — base para a criação do COBOL — e uma das primeiras programadoras do computador Harvard Mark I em 1944."
    return mensagem


def doutorado():
    mensagem = "Em 1934, também na Yale University, conquistou seu Ph.D. em Matemática sob a orientação de Øystein Ore."
    return mensagem


def contribuicoes():
    mensagem = "Grace Hopper foi uma das mulheres mais influentes da ciência da computação do século XX. Uma das primeiras a se tornar PhD em Matemática, ela trabalhou na Marinha dos Estados Unidos durante a Segunda Guerra Mundial, sendo uma das responsáveis por programar o Mark I, o primeiro computador eletromecânico do mundo. A verdadeira revolução veio com seu trabalho no UNIVAC I, o primeiro computador comercial dos EUA, onde Hopper desenvolveu o primeiro compilador, uma ferramenta que traduzia instruções escritas em linguagem de alto nível para código de máquina compreensível pelos computadores. Na primavera de 1959, especialistas da industria e do governo juntaram-se em uma conferência que durou dois dias conhecida como a Conference on Data Systems Languages (CODASYL). Hopper foi consultora técnica para a comitê, e muitos dos seus funcionários contribuíram para a curto prazo na comitê que definiu a nova linguagem COBOL (um acrônimo para COmmon Business-Oriented Language). A nova linguagem estendeu a linguagem FLOW-MATIC de Hopper com algumas da equivalente da IBM, o COMTRAN. Ela acreditava que programas deveriam ser escritos na linguagem mais próxima do Inglês (ao invés de código de máquina ou em linguagens próximas de código de máquina, como a Linguagem Assembly) foi capturado na nova linguagem de negócio, e COBOL se tornou a linguagem de negócio mais onipresente até a atualidade. Nos anos de 1970, Hopper defendeu para que o Departamento de Defesa substituísse grandes, centralizados sistemas com redes de pequenos computadores distribuídos. Como qualquer usuário de qualquer node de computador conseguia acessar bases de dados comuns localizadas na rede.[20] Ela desenvolveu a implementação de padrões para testar sistemas de computadores e componentes, principalmente para as linguagens de programação FORTRAN e COBOL. Os testes da Marina de conformidade em relação a esses padrões levaram a convergências significativas entre os dialetos de linguagens de programação dos vendedores dos principais computadores. Já nos anos de 1980, esses teste, e a sua administração oficial, foram assumidos pelo Escritório Nacional de Padrões (NBS), conhecido atualmente como o Instituto Nacional de Padrões e Tecnologia (NIST)."
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

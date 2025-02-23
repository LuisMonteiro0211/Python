def pergunta_nome():
    #FUNÇÃO DESTINADA A VALIDAÇÃO DE ENTRADAS DO USUÁRIO
    while True:
        #UM LAÇO DE REPETIÇÃO SEMPRE VERDADEIRO, FORÇANDO A EXECUÇÃO DO MESMO
        nome = input("INFORME SEU NOME: ").strip()
        confirmacao = nome.isspace() or nome =="" #EXPRESSÃO DE CONFIRMAÇÃO
        if confirmacao != True:
            break# FORÇA A SAÍDA DO WHILE
        else:
            print("O NOME INFORMADO NÃO É VALIDO. TENTE NOVAMENTE!")
    return nome
#=============================================================================================
def contador(nome):
    #FUNÇÃO DESTINADA A CONTAGEM E MANIPUALÇÃO DE CARACTERES CONFORNE A NECESSIDADE DO EXERCÍCIO
    #QUANTIDADE DE CARACTERES (SEM CONTAR ESPAÇOS)
    #CONTAGEM DE CARACTERES DO PRIMEIRO NOME
    tem_espaco = " " in nome #Variável de controle
    contador_caractere = (len(nome)-nome.count(" "))#FAZ O CÁLCULO SEM ESPAÇOS
    if tem_espaco:
        nome_final = nome.split()
    else:
        nome_final = [nome]
    return{
        "NOME_DIVIDIDO": nome_final[0],
        "CONTAGEM_CARACTERE": contador_caractere,
        "ESPACO_NOME":tem_espaco
    }
#---------------------------------------------------------------
def exibicao(nome):
    #EXIBIÇÃO DAS POSSÍVEIS VARIAÇÕES DA VARIÁVEL
    sinal = "="
    quantidade = 10
    #====================================
    final_nome = contador(nome)
    nome_tratado = nome.strip()
    print(f"""
{sinal*quantidade}MUDANÇA NA VISUALIZAÇÃO{sinal*quantidade}
- NOME EM MAÍUSCULO: {nome_tratado.upper()}
- NOME EM MINÚSCULO: {nome_tratado.lower()}
- NOME CAPITALIZADO: {nome_tratado.capitalize()}

{sinal*quantidade}CONTAGEM DE CARACTERE{sinal*quantidade}
- SEU NOME POSSUI UM TOTAL DE: {final_nome["CONTAGEM_CARACTERE"]}
- SEU PRIMEIRO NOME É: {final_nome["NOME_DIVIDIDO"]}
- TEM UM TOTAL DE: {len(final_nome["NOME_DIVIDIDO"])} LETRAS
    """)
    #-----------------------------------------------------

nome = pergunta_nome()
main=(exibicao(nome))

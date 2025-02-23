TOTAL_DIGITOS = 4

def armazena_valor(numero_digitado):
    fatiamento=[num for num in numero_digitado]
    #FAZ COM QUE CADA VALOR SEJA UMA POSSIÇÃO NA LISTA
    #------------TRATAMENTO-------------------
    casas_faltantes = TOTAL_DIGITOS-len(fatiamento) #CALCULO DE CASAS FALTANTES PARA UM NUMERO COM 4 DIGITOS
    if casas_faltantes != 0:
    #COMPLETA COM ZEROS AS CASAS FALTANTES
        for i in range(casas_faltantes):
            fatiamento.insert(0,'0')
    #------------------------------------------
    return fatiamento
#===================================================
def valida ():
    while True:
        numero = input("DIGITE UM VALOR: ")
        if numero.isdigit() == True:
            if int(numero)<9999:
                break
            else:
                print("VALOR MAIOR QUE 9999 - DIGITE NOVAMENTE\n")
        else:
            print("""O VALOR DIGITADO NÃO É VALIDO
-VERIFIQUE SE É REALMENTE UM NÚMERO
""")
    return numero
#===================================================
def decompor_numero(lista_num, numero_digitado):
    #FAZ A EXIBIÇÃO DOS VALORES
    print(f"""
O NUMERO DIGITADO {numero_digitado} DECOMPOSTO É:
- UNIDADES: {lista_num[3]}
- DEZENAS: {lista_num[2]}
- CENTENAS: {lista_num[1]}
- MILHAR: {lista_num[0]}
          """)
#===================================================
numero = valida()
fatiamento_numero = armazena_valor(numero)
decompor_numero(fatiamento_numero, numero)

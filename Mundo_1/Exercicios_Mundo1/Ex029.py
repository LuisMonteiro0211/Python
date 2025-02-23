VALOR_MULTA = 7 #VALOR PADRÃO PARA CADA KM ACIMA DA VELOCIDADE
VELOCIDADE_PERMITIDA = 80
#==========================================================================
def multa_pagar(velocidade_informada):
    #FUNÇÃO DESTINADA AO CÁLCULO DO VALOR DA MULTA
    if velocidade_informada > VELOCIDADE_PERMITIDA:
        calculo_multa = (velocidade_informada-VELOCIDADE_PERMITIDA)*VALOR_MULTA
        return calculo_multa
    else:
        return 0
#===========================================================================
pergunta_usuario = int(input('INFORME A VELOCIDADE DO SEU VEÍCULO: '))

if pergunta_usuario > 80:
    total_pagar = multa_pagar(pergunta_usuario)
    print(f"""VOCÊ PASSOU ACIMA DA VELOCIDADE PERMITIDA!
- VELOCIDADE PERMITIDA DE {VELOCIDADE_PERMITIDA}KM/h
- SUA VELOCIDADE FOI DE {pergunta_usuario}KM/h
- GERANDO UM VALOR TOTAL DE R${total_pagar:.2f}
- O VALOR É REFERENTE A R${VALOR_MULTA:.2f} POR KM/h EXCEDIDO""")
else:
    print("TUDO NORMAL POR AQUI")

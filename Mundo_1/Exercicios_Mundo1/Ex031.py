import re

def validacao(valor_usuario):
    padrao = re.compile(r'^[\.\d]+$')
    valida_info = re.search(padrao,valor_usuario)
    return bool(valida_info)
#==================================================================================
def calculo_viagem(km_viajado: float): 
    """
    FUNÇÃO DEDICADA PARA CÁLCULO DO VALOR DA VIAGEM COM BASE NA KM RODADA
    - NO CASO DE SER MENOS QUE 200KM O VALOR É DE R$0.50 POR VIAGEM
    - NO CASO DE SER MAIOR O VALOR DO KM PASSA A SER DE R$0.45
    """
    preco_km = 0.50 if km_viajado <= 200 else 0.45
    preco_viagem = km_viajado*preco_km

    return{
        "PRECO_KM": preco_km,
        "PRECO_VIAGEM": preco_viagem
    }
#==================================================================================
while True:
    km_rodado = input("INFORME QUANTOS KM FOI SUA VIAGEM: ")
    valida_entrada = validacao(km_rodado)
    if valida_entrada:
        break
    else:
        print("POR FAVOR, INFORMA UM VALOR VÁLIDO (INFORME SOMENTE NÚMEROS)")

info_viagem = calculo_viagem(float(km_rodado))

print(f"""{"="*15}AGÊNCIA DE VIAGENS{"="*15}
BEM VINDO VIAJANTE, É UM PRAZER TER VOCÊ CONOSCO!!
CONFORME INFORMADO, SUA VIAGEM TEVE UM TOTAL DE {km_rodado}KM
=================FATURA=================
- O VALOR POR KM RODADO É DE: R${info_viagem["PRECO_KM"]:.2f}
- O VALOR FINAL FOI DE: R${info_viagem["PRECO_VIAGEM"]:.2f}
""")

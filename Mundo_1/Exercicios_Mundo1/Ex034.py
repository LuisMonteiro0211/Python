import re
from time import sleep
from typing import TypedDict, reveal_type

class dicionario_retorno(TypedDict):
    """dicionario_retorno é um TypedDict que contém as informações do aumento do salário do funcionário
    - PORCENTAGEM_AUMENTO - FLOAT
    - VALOR_AUMENTO - FLOAT
    - SALARIO_FINAL - FLOAT
    """

    PORCENTAGEM_AUMENTO: float
    VALOR_AUMENTO: float
    SALARIO_FINAL: float

def validacao(valor_salario: str)-> bool:
    """'validacao' verifica se o valor informado é um número válido para o cálculo"""
    return bool(re.fullmatch(r'[\.\d]+|(EXIT)', valor_salario))

def aumento_salario (valor_salario: float)-> dicionario_retorno:
    """
        Função destinada ao cálculo do valor do salário com base na tabela de aumento
        15% para salários até R$1250,00 e 10% para salários acima de R$1250,00
        Informe o valor do salário e a função retornará um dicionário com as informações do aumento

        --------
        Args:
            valor_salario (float): Valor do salário do funcionário
            
        --------
        Returns:
            dict: Dicionário contendo as informações do aumento
            - PORCENTAGEM_AUMENTO (10% ou 15%)
            - VALOR_AUMENTO qual o valor em R$ foi adicionado ao salário
            - SALARIO_FINAL qual o valor do salário após o aumento
    """
    porcentagem_aumento = 0.10 if valor_salario >1250 else 0.15
    aumento = valor_salario * porcentagem_aumento
    valor_final = aumento + valor_salario
    return{
        "PORCENTAGEM_AUMENTO": porcentagem_aumento*100,
        "VALOR_AUMENTO": aumento,
        "SALARIO_FINAL": valor_final
    }
def folha_pagamento(valor_convertido: float, valor_salario: dicionario_retorno) -> None:
    """
        Função destinada a exibição do resultado obtido nos calculos anteriores sem retorno

        Args:
            valor_convertido (float): Valor do salário do funcionário
            valor_salario (dict): Dicionário contendo as informações do aumento
    """
    print(f"""\n{"="*30}
      FOLHA DE PAGAMENTO
{"="*30}
OLÁ FUNCIONÁRIO, SEGUE INFORMAÇÕES SOBRE O PAGAMENTO:
- SALARIO BASE: R${valor_convertido:.2f}
- PARA ESSE MÊS, TEMOS UM AUMENTO DE: R${valor_salario["PORCENTAGEM_AUMENTO"]:.1f}%
- VALOR DO AUMENTO: R${valor_salario["VALOR_AUMENTO"]:.2f}

- AO FINAL, VOCÊ RECEBERA: R${valor_salario["SALARIO_FINAL"]:.2f}
""")
#help(aumento_salario)
while True:
    entrada_usuario = input("INFORME O VALOR DO SEU SALÁRIO: ")
    if entrada_usuario.upper() == "EXIT":
        print("ENCERRANDO PROGRAMA...")
        sleep(2)
        break
    elif validacao(entrada_usuario):
        valor_convertido =float(entrada_usuario)
        if valor_convertido > 0 :
            valor_salario = aumento_salario(valor_convertido)
            folha_pagamento(valor_convertido, valor_salario)
            break
    else:
        print("POR FAVOR, INFORME SOMENTE NÚMEROS PARA O CÁLCULO\n")

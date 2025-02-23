import math
def negrito (texto):
    return f'\033[1m{texto:.2f}\033[0m'

def conversor (valor):
    valor_radiano = math.radians(valor)
    seno = math.sin(valor_radiano)
    cosseno = math.cos(valor_radiano)
    tangente = math.tan(valor_radiano)

    dicionario = {'Seno': seno, 
                  'Cosseno': cosseno, 
                  'Tangente': tangente
                  }
    return dicionario

valor = float(input('DIGITE O VALOR DE UM ÂNGULO: '))

resultado_final = conversor(valor)

print(f'''
      SEGUE RELAÇÃO REFENTE AO VALOR DE: {negrito(valor)}°
      #------------------------------------------------
      - SENO: {negrito(resultado_final['Seno'])}
      - COSSENO: {negrito(resultado_final['Cosseno'])}
      - TANGENTE: {negrito(resultado_final['Tangente'])}
      ''')
import re

def validacao(numero):
    #FUNÇÃO PARA VERIFICAÇÃO BÁSICA SE O VALOR É UM NÚMERO/DIGITO
    return bool(re.fullmatch(r'\d+',numero))
#=========INICIALIZAÇÃO============
iteracao = 1
lista_numeros = []
#================================================================
while iteracao <=4:
    #COMEÇA COM A ITERAÇÃO COM O USUÁRIO
    while True:
        #NESSE WHILE COMEÇA A VERIFICAÇÃO SE O VALOR ATENDE A REGEX (SER UM DÍGITO)
        entrada_usuario = input(f"INFORME O {iteracao}° VALOR: ")
        if validacao(entrada_usuario):
            numero = int(entrada_usuario)
            lista_numeros.append(numero)#ADD O VALOR A LISTA PARA MOSTRAR NO FINAL
            break
        else:
            print("POR FAVOR, INFORME SOMENTE NÚMEROS")
#===============================================================
    if iteracao == 1:
        #INICIALIZAÇÃO DAS VARIÁVEIS DE COMPARAÇÕES NA PRIMEIRA ITERAÇÃO
        menor = numero
        maior = numero
    #DEMAIS COMPARAÇÕES APÓS A PRIMEIRA ITERAÇÃO
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    iteracao +=1
#===================================FINAL=======================================
print(f'\n========RESULTADO========\n-MENOR: {menor}\n-MAIOR: {maior}')
print(sorted(lista_numeros))

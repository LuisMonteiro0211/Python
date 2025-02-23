lado1 = int(input("INFORME O VALOR DE L1: "))
lado2 = int(input("INFORME O VALOR DE L2: "))
lado3 = int(input("INFORME O VALOR DE L3: "))

if ((lado1+lado2 > lado3)and(lado1+lado3 > lado2)and(lado2+lado3 > lado1)):
    print("É POSSÍVEL FORMA UM TRIÂNGULO!")
else:
    print("NÃO É POSSÍVEL FORMA UM TRIÂNGULO")

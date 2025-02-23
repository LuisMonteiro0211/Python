def soma (v1, v2):
    return v1+v2
#--------------------------------------
print()
num1 = int(input("DIGITE UM VALOR: "))
num2 = int(input("DIGITE OUTRO VALOR: "))
#Se não tivesse o INT seria apenas uma concatenação de strings

print(f"A SOMA DE {num1} E {num2} É IGUAL A {soma(num1, num2)}")
print()
nota1 = float(input("DIGITE A 1° NOTA: "))
nota2 = float(input("DIGITE A 2° NOTA: "))
#------------------------------------
def media (n1, n2):
    return (n1 + n2)/2
#----------------------------------------------
print("===============================================")
print(f'SUA MEDIA FOI DE {media(nota1, nota2):.1f}')

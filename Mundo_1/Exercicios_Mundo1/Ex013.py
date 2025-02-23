def aumento(salario_atual, aumento):
    porcentagem = aumento/100
    aumento_reais = salario_atual*porcentagem
    aumento_final = salario_atual+aumento_reais
    dicionario = {"aumento": aumento_reais, "aumento_final": aumento_final}
    
    return dicionario
# end def
#--------------------------------------------------------------------------------------------------
print()
salario = float(input("INFORME O VALOR DO SEU SALÁRIO: "))
porcentagem_aumento = float(input("INFORME A PORCENTAGEM DO AUMENTO: "))

final = aumento(salario, porcentagem_aumento)

print(f"O VALOR DO SEU AUMENTO FOI DE R${final["aumento"]:.2f}\n"
      f"- SEU SALARIO FOI DE R${salario:.2f}\n"
      f"- PARA R${final["aumento_final"]:.2f} COM {porcentagem_aumento}% DE AUMENTO")

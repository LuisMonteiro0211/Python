cidade = input("INFORME O NOME DA SUA CIDADE: ")
cidade_final = (cidade.strip()).upper()

if cidade_final.startswith("SANTO "):
    print("SUA CIDADE COMEÇA COM 'SANTO' ")
else:
    print("SUA CIDADE NÃO COMEÇA COM 'SANTO'")

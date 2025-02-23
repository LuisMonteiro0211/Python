import re

padrao = re.compile(r'^SANTO\b')
#PADRAO DE BUSCA PELA PALAVRA NO INICIO DA FRASE/INPUT
cidade = input("INFORME O NOME DA SUA CIDADE: ")
cidade_final = (cidade.strip()).upper()
#TRATAMENTO DO INPUT

verifica = bool(re.match(padrao, cidade_final))

if verifica:
    print("SUA CIDADE COMEÇA COM A PALAVRA SANTO!!")
else:
    print("SUA CIDADE NÃO COMEÇA COM A PALAVRA SANTO!!")

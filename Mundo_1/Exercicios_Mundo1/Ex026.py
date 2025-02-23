frase = "ESTOU APRENDENDO A PROGRAMAR EM PYTHON"
caractere_analisado = "A"
conta_caractere = frase.count(caractere_analisado)
primeira_corresp = frase.find(caractere_analisado) if conta_caractere > 0 else "NÃO ENCONTRADO"
ultima_corresp = frase.rfind(caractere_analisado) if conta_caractere> 0 else "NÃO ENCONTRADO"

print(f"""
===============ANALISE DA STRING================
- FRASE: {frase}
- A LETRA "{caractere_analisado}" ANALISADA CORRESPONDE:
- {conta_caractere} CORRESPONDÊNCIAS NO CÓDIGO
- SUA PRIMEIRA CORRESPONDÊNCIA ESTÁ NA POSIÇÃO {primeira_corresp}
- SUA ULTIMA CORRESPONDÊNCIA ESTÁ NA POSIÇÃO {ultima_corresp}
""")

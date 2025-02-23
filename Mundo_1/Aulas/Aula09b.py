frase = "Curso em Video Python"
frase_nova = frase.replace("Python", "Android")
frase_espaco = " Curso em Video Python "
frase_separada = frase.split(" ")
frase_com_problema = "!!!Curso em Video Python!!!!"
print(f"""
    ABAIXO SERÃO APRESENTANDO ALGUNS MÉTODOS DE MANIPULAÇÃO E ANALISE DE STRINGS

    MANIPULAÇÃO STRING:
    FRASE SEM ALTERAÇÃO: {frase}
    - TAMNHO DA CADEIA DE CARACTER: {len(frase)}
    - TROCANDO O PYTHON POR ANDROID
    {frase.replace("Python", "Android")}
    - TAMANHO DA FRASE NOVA: {len(frase_nova)}
    - FRASE CONVERTIDA EM CAIXA ALTA: {frase.upper()}
    - FRASE 2 CONVERTIDA PARA CAIXA ALTA: {frase_nova.upper()}
    - FRASE TODA EM MINUSCULO: {frase.lower()}
    - FRASE 2 EM MINUSCULO: {frase_nova.lower()}
    - FRASE CAPITALIZADA: {frase.capitalize()}
    - FRASE 2 EM CAPTALIZADA: {frase_nova.capitalize()}
    - FRASE COM ESPAÇO NO COMEÇO E FINAL: {frase_espaco}
    - TAMANHO DA FRASE ACIMA: {len(frase_espaco)}
    - RETIRANDO ESPAÇOS NO COMEÇA E FINAL: {frase_espaco.strip()}
    - TAMANHO DA NOVA FRASE: {len(frase_espaco.strip())}
    - FRASE SEPARADA PELO ESPAÇO
    {frase_separada}
    - JUNTANDO A FRASE COM "-"
    {"-".join(frase_separada)}
    - REMOVENDO CARACTER DA FRASE {frase_com_problema}
        - REMOÇÃO TOTAL
        {frase_com_problema.strip("!")}
        - REMOÇÃO DA DIREITA
        {frase_com_problema.rstrip("!")}
        - REMOÇÃO DA ESQUERDA
        {frase_com_problema.lstrip("!")}

    ----------------------------------------------------------------------
    ANALISE DE STRINGS:
    - ANALISANDO APENAS O INDICIE 2: {frase[2]}
    - ANALISANDO INTERNVALO DE 2 A 15:
    {frase[2:15]}
    - QUANDO NÃO SEI O TAMANHO DA STRING 2 (COMEÇO) ATÉ O FINAL:
    {frase[2:]}
    - QUANDO QUERO IR DO COMEÇO (0) ATÉ UM DETERMINADO VALOR (15):
    {frase[:15]}
    - QUANDO QUERO MOSTRAR A FRASE COMPLETA PULANDO DE 2 EM 2:
    {frase[::2]}
    - DO INDICIE 10 ATÉ O FINAL (FINAL DESCONHECIDO) PULANDO DE DOIS EM DOIS:
    {frase[10::2]}
    - DO INDICIE 0 ATE 0 15 PULANDO DE DOIS EM DOIS
    {frase[0:15:2]}
    - A FRASE {frase} TEM A PALAVRA "CURSO"
    {"Curso" in frase}
    - EXISTE A PALAVRA "curso" NA FRASE {frase}
    {"curso" in frase}
    - APÓS DEIXAR TUDO EM MINUSCULO "{frase.lower()}"
    {"curso" in frase.lower()}
    - PALAVRA CURSO EM CAIXA ALTA EM "{frase.upper()}"
    {"CURSO" in frase}
    - FRASE COMEÇA COM "Curs"
    {frase.startswith("Curs")}
    - FRASE COMEÇA COM "Python"
    {frase.startswith("Python")}
    - FRASE TERMINA COM "Curs"
    {frase.endswith("Curs")}
    - FRASE TERMINA COM "Python"
    {frase.endswith("Python")}
    - QUANTAS LETRAS "o" TEM NA FRASE {frase}
    {frase.count("o")}
    

""")
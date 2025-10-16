"""
Objetivo: Dado um conjunto de palavras, determinar se a palavra eh reconhecida ou nao pelo 
AFD equivalente gerado na parte 1. 
Alfabeto: {0,1} 
Entrada: um arquivo com as palavras a serem reconhecidas, uma palavra por linha. 

Saida: um arquivo com todas as palavras e na frente de cada palavra por aceito ou nao aceito 
(reconhecido ou nao reconhecido). Por uma palavra por linha. 
Ex:  
    Na linha 1: qwefr aceito 
    Na linha 2: abder nao aceito 
"""

# ler arquivo do AFD
arquivo_AFD = []
with open("saidas/saida_AFD.txt", "r") as f:
    for linha in f:
        arquivo_AFD.append(linha)

# ler arquivos com as palavras
palavras = []
with open("entrada_palavras_AFD.txt", "r") as f:
    for palavra in f:
        texto_aux = palavra.strip()
        palavras.append(texto_aux)

# variaveis auxiliares utilizadas ao longo do programa
quantidade_palavras = len(palavras)
linhas_arquivo_AFD = len(arquivo_AFD)
estado_inicial = arquivo_AFD[1].replace("\n", "")
estados_finais = arquivo_AFD[2].split()

i = 0
while i < quantidade_palavras:
    caracteres_palavra = list(palavras[i])
    caractere_pos = 0
    estado_atual = estado_inicial

    j = 3
    while j < linhas_arquivo_AFD:
        transicao = arquivo_AFD[j].split()

        if estado_atual == transicao[0] and caracteres_palavra[caractere_pos] == transicao[1]:
            estado_atual = transicao[2]
            caractere_pos += 1
            # reinicia a busca de transicoes
            j = 3 

            # se for o final da palavra, dizer se aceita ou nao
            if caractere_pos >= len(caracteres_palavra):
                palavra_aux = palavras[i].strip()
                if estado_atual in estados_finais:
                    palavras[i] = palavra_aux + " aceito\n"
                else:
                    palavras[i] = palavra_aux + " nao aceito\n"
                break
        else:
            j += 1
    i += 1

# criar arquivo com as palavras aceitas/rejeitadas
with open("saidas/saida_palavras_aceitas.txt", "w") as f:
    for palavra in palavras:
        f.write(palavra)
"""
Objetivo: Converter um AFND (com movimentos vazios) em um AFD
Alfabeto: {0,1}
Entrada: um arquivo com a tabela do AFND.
Formato do arquivo de entrada:
    Linha 0: a sequencia de estados separados por espaco. EX: A B C D E F
    Linha 1: estado inicial
    Linha 2: estados finais separados por espaco (se houver mais de um estado final)
    Linha 3 em diante: estado atual, espaco, caractere lido, espaco, proximo estado
    Obs: respresentar a transicao vazia por h.

Saída: um arquivo com a tabela do AFD
Formato do arquivo de saida: o mesmo do arquivo de entrada.

Usar o GraphViz para fazer a exibicao do grafo do AFND e do AFD.
Usar o JFLAP e desenhar os dois automatos: o de entrada e o de saida.
"""
from graphviz import Digraph    


def formatar_como_tabela(dados):
    """
    Formata os dados em formato de tabela
    """
    print("\n" + "=" * 60)
    print("TABELA DE TRANSICOES".center(60))
    print("=" * 60)
    print(f"{'Estado':<10} {'Transicao p/ 0':<15} {'Transicao p/ 1':<15}".center(60))
    print("-" * 60)
    
    for item in dados:
        estado = item[0]
        transicoes = item[1]
        
        trans0 = transicoes[0] if len(transicoes) > 0 else "N/A"
        trans1 = transicoes[1] if len(transicoes) > 1 else "N/A"
        
        print(f"{estado:<10} {trans0:<15} {trans1:<15}")


# Ler arquivo e inserir linhas numa lista
linhas_arquivo_AFND = []
with open("entrada_AFND.txt", "r") as f:
    for linha in f:
        linhas_arquivo_AFND.append(linha)

# Pegar somente as transicoes do arquivo
transicoes_AFND = linhas_arquivo_AFND[3:]
tam_transicoes_AFND = len(transicoes_AFND)

# variaveis para criacao do AFD
estado_inicial = linhas_arquivo_AFND[1].replace("\n", "")
estado_final = linhas_arquivo_AFND[2].replace("\n", "")
estados_finais = []
transicoes_AFD = []

# buscar transicoes vazias (h)
transicoes_vazias = []
for transicao in transicoes_AFND:
    if "h" in transicao:
        transicoes_vazias.append(transicao)
        
# criar novo estado inicial (AFD)
for i in range(len(transicoes_vazias)):
    if transicoes_vazias[i][0] in estado_inicial:
        estado_inicial = estado_inicial + transicoes_vazias[i][4]

# forma da transicao do AFD: [estado, [estado p/ mov 0, estado p/ mov 1]]
transicoes_AFD.append([estado_inicial, ["", ""]])

# criar tabela de transicoes do AFD
i = 0
while i < len(transicoes_AFD):
    estado_quebrado = list(transicoes_AFD[i][0])
    
    for k in range(tam_transicoes_AFND):
        # movimentos p/ 0 com h antes
        if transicoes_AFND[k][0] in estado_quebrado and "h" in transicoes_AFND[k]:
            estado_atual = transicoes_AFND[k][4]
            l = 0
            while l < tam_transicoes_AFND:
                if estado_atual in transicoes_AFND[l][0] and "h" in transicoes_AFND[l]:
                    estado_atual = transicoes_AFND[l][4]
                if estado_atual in transicoes_AFND[l][0] and "0" in transicoes_AFND[l]:
                    transicoes_AFD[i][1][0] += transicoes_AFND[l][4]
                    transicoes_AFD[i][1][0] = "".join(sorted(set(transicoes_AFD[i][1][0])))
                l += 1
        
        # movimentos p/ 0 com h depois
        if transicoes_AFND[k][0] in estado_quebrado and "0" in transicoes_AFND[k]:
            if transicoes_AFND[k][4] in transicoes_AFD[i][1][0]:
                continue
            transicoes_AFD[i][1][0] += transicoes_AFND[k][4]

            estado_atual = transicoes_AFND[k][4]
            l = 0
            while l < tam_transicoes_AFND:
                if estado_atual in transicoes_AFND[l][0] and "h" in transicoes_AFND[l]:
                    estado_atual = transicoes_AFND[l][4]
                    transicoes_AFD[i][1][0] += transicoes_AFND[l][4]
                    transicoes_AFD[i][1][0] = "".join(sorted(set(transicoes_AFD[i][1][0])))
                l += 1

        # movimentos p/ 1 com h antes
        if transicoes_AFND[k][0] in estado_quebrado and "h" in transicoes_AFND[k]:
            estado_atual = transicoes_AFND[k][4]
            l = 0
            while l < tam_transicoes_AFND:
                if estado_atual in transicoes_AFND[l][0] and "h" in transicoes_AFND[l]:
                    estado_atual = transicoes_AFND[l][4]
                if estado_atual in transicoes_AFND[l][0] and "1" in transicoes_AFND[l]:
                    transicoes_AFD[i][1][1] += transicoes_AFND[l][4]
                    transicoes_AFD[i][1][1] = "".join(sorted(set(transicoes_AFD[i][1][1])))
                l += 1

        # movimentos p/ 1 com h depois
        if transicoes_AFND[k][0] in estado_quebrado and "1" in transicoes_AFND[k]:
            if transicoes_AFND[k][4] in transicoes_AFD[i][1][1]:
                continue
            transicoes_AFD[i][1][1] += transicoes_AFND[k][4]

            estado_atual = transicoes_AFND[k][4]
            l = 0
            while l < tam_transicoes_AFND:
                if estado_atual in transicoes_AFND[l][0] and "h" in transicoes_AFND[l]:
                    estado_atual = transicoes_AFND[l][4]
                    transicoes_AFD[i][1][1] += transicoes_AFND[l][4]
                    transicoes_AFD[i][1][1] = "".join(sorted(set(transicoes_AFD[i][1][1])))
                l += 1
    
    # colocar estados em ordem alfabetica
    # transicoes_AFD[i][1][0] = "".join(sorted(transicoes_AFD[i][1][0])) if transicoes_AFD[i][1][0] != "" else "-"
    # transicoes_AFD[i][1][1] = "".join(sorted(transicoes_AFD[i][1][1])) if transicoes_AFD[i][1][1] != "" else "-"
    for j in range(2):  
        valor = transicoes_AFD[i][1][j]
        transicoes_AFD[i][1][j] = "".join(sorted(valor)) if valor != "" else "-"


    cont = 0
    while cont < len(transicoes_AFD):
        nome = transicoes_AFD[cont][0]
        conexoes = transicoes_AFD[cont][1]

        # Verifica os dois elementos da sublista
        for conexao in conexoes:
            # Ignorar valores vazios ou None
            if conexao == "" or conexao is None:
                continue
            # Verifica se o elemento ja existe em alguma lista[i][0]
            existe = any(conexao == item[0] for item in transicoes_AFD)

            # Se nao existe, adiciona um novo item com sublista vazia
            if not existe:
                transicoes_AFD.append([conexao, ["", ""]])

        cont += 1  

    if estado_final in transicoes_AFD[i][0] and estado_final not in estados_finais:
        estados_finais.append(transicoes_AFD[i][0])
    i += 1

# exibir tabela do AFD no console
formatar_como_tabela(transicoes_AFD)
print("Estados Finais:", estados_finais)

# criar arquivo de saida do AFD
with open("saidas/saida_AFD.txt", "w") as f:
    # Linha com os estados do automato
    for item in transicoes_AFD:
        f.write(item[0] + " ")
    
    # estado inicial
    f.write(f"\n{estado_inicial}\n")
    
    # estados finais 
    for item in estados_finais:
        f.write(item + " ")
    f.write("\n")

    # tabela de transicoes
    for item in transicoes_AFD:
        f.write(f"{item[0]} 0 {item[1][0]}\n")
        f.write(f"{item[0]} 1 {item[1][1]}\n")

# criar grafo do AFD
dot = Digraph("Automato Finito Deterministico")
dot.attr(rankdir="LR")
dot.node(estado_inicial, estado_inicial, style="filled", fillcolor="green")

for item in transicoes_AFD:
    if estado_final in item[0]:
        dot.node(item[0], item[0], shape="doublecircle", style="filled", fillcolor="red")
    dot.node(item[0], item[0])  

for item in transicoes_AFD:       
   dot.edge(item[0], item[1][0], label="0")
   dot.edge(item[0], item[1][1], label="1")

dot.render("automatos-graphviz/graphviz_afd", format="png")

# criar grafo do AFND
dot = Digraph("Automato Finito Nao Deterministico")
dot.attr(rankdir="LR")
dot.node(linhas_arquivo_AFND[1], linhas_arquivo_AFND[1], style="filled", fillcolor="green")

for item in transicoes_AFND:
    if linhas_arquivo_AFND[2].replace("\n", "") in item[4]:
        dot.node(item[4], item[4], shape="doublecircle", style="filled", fillcolor="red")
    dot.node(item[0], item[0])  

for item in transicoes_AFND:       
   dot.edge(item[0], item[4], label=item[2])

dot.render("automatos-graphviz/graphviz_afnd", format="png")
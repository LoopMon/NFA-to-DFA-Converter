import random

# Parâmetros
alfabeto = ["0", "1"]
quantidade = 20      # número de palavras a gerar
tamanho_max = 8      # comprimento máximo de cada palavra

palavras = []

for _ in range(quantidade):
    tamanho = random.randint(1, tamanho_max)
    palavra = "".join(random.choice(alfabeto) for _ in range(tamanho))
    palavras.append(palavra)

# Embaralha a lista para garantir ordem aleatória
random.shuffle(palavras)

# Exibe o resultado
for p in palavras:
    print(p)

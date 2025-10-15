# 🧮 Conversor de AFND (com ε-transições) para AFD e Validador de Palavras

## 📖 Descrição do Projeto

Este projeto tem como objetivo **converter um Autômato Finito Não Determinístico (AFND)** — incluindo **ε-transições (movimentos vazios)** — em um **Autômato Finito Determinístico (AFD)**.

Além da conversão, o sistema também realiza a **validação de palavras** pertencentes ao alfabeto `{0, 1}`, verificando se cada palavra é **aceita ou rejeitada** de acordo com o AFD gerado.

## ⚙️ Estrutura do Projeto

O projeto é composto por **dois arquivos Python principais**:

1. **Conversão do AFND para AFD** (`parte-1.py`)

    - Lê um arquivo `.txt` contendo a **tabela de transição do AFND**.
    - Realiza o processo de conversão, incluindo o tratamento de **ε-transições**.
    - Gera um **novo arquivo `.txt`** com a **tabela de transição do AFD** correspondente.

2. **Validação de Palavras** (`parte-2.py`)

    - Utiliza o arquivo `.txt` gerado pelo conversor (tabela do AFD).
    - Lê um arquivo com **várias palavras** formadas pelos símbolos `{0, 1}`.
    - Analisa cada palavra e **gera um arquivo de saída** informando se foi **aceita** ou **rejeitada** pelo autômato.

## 📂 Formato dos Arquivos

-   O arquivo de entrada do **AFND** deve conter:

    -   Linha 0: a sequência de estados separados por espaco. EX: A B C D E F
    -   Linha 1: estado inicial
    -   Linha 2: estados finais separados por espaco (se houver mais de um estado final)
    -   Linha 3 em diante: estado atual, espaco, caractere lido, espaco, proximo estado
    -   Obs: respresentar a transição vazia por h.

-   O arquivo de saída do **AFD** segue o mesmo formato, mas sem ε-transições e com estados determinísticos.
-   O arquivo de palavras contém uma lista de palavras, uma por linha, usando apenas os símbolos `0` e `1`.

## 🧩 Instruções de Execução

O projeto é dividido em **duas etapas principais**, cada uma executada por um arquivo Python distinto.

### **1️⃣ Etapa 1 — Conversão do AFND para AFD**

O primeiro script realiza a leitura do arquivo de entrada contendo a **tabela de transição do AFND**.
A partir dessas informações, ele gera um novo arquivo com a **tabela de transição equivalente em AFD**.

Durante esse processo, o programa:

-   Lê o arquivo `entrada_AFND.txt`, que contém os estados, transições e símbolos do autômato não determinístico;
-   Constrói o AFD correspondente, aplicando a conversão e removendo ε-transições;
-   Gera o arquivo `saidas/saida_AFD.txt`, que contém a **tabela determinística resultante**;
-   Cria representações gráficas dos autômatos (AFND e AFD) na pasta `automatos-graphviz`, no formato `.png`.

Após essa etapa, o AFD estará completamente definido e pronto para ser utilizado na validação de palavras.

### **2️⃣ Etapa 2 — Validação de Palavras**

O segundo script utiliza o arquivo `saidas/saida_AFD.txt` produzido na etapa anterior para validar palavras do alfabeto `{0, 1}`.

Nesta fase, o programa:

-   Lê o arquivo `entrada_palavras_AFD.txt`, contendo uma lista de palavras (uma por linha);
-   Processa cada palavra segundo a tabela de transição do AFD;
-   Indica se cada palavra é **aceita** ou **rejeitada** pelo autômato;
-   Gera um arquivo `saidas/saida_palavras_aceitas.txt`, listando o resultado para cada palavra analisada.

### 📄 Resumo do Fluxo de Arquivos

| Etapa        | Arquivo de Entrada                                  | Arquivo de Saída                    | Função Principal                      |
| :----------- | :-------------------------------------------------- | :---------------------------------- | :------------------------------------ |
| 1️⃣ Conversão | `entrada_AFND.txt`                                  | `saidas/saida_AFD.txt`              | Converter AFND (com ε) em AFD         |
| 2️⃣ Validação | `entrada_palavras_AFD.txt` + `saidas/saida_AFD.txt` | `saidas/saida_palavras_aceitas.txt` | Validar palavras aceitas e rejeitadas |

### 🗂️ Estrutura Esperada de Pastas

```
.
├── entrada_AFND.txt
├── entrada_palavras_AFD.txt
├── parte-1.py
├── parte-2.py
├── saidas/
│   ├── saida_AFD.txt
│   └── saida_palavras_aceitas.txt
└── automatos-graphviz/
    ├── graphviz_afnd.png
    └── graphviz_afd.png
```

## 🚀 Funcionalidades Principais

-   Conversão automática de AFND (com ε) para AFD.
-   Geração de tabelas de transição completas em formato `.txt`.
-   Validação de palavras.
-   Geração de Grafos representando os autômatos usando a lib GraphViz.

## 🧠 Conceitos Envolvidos

O projeto foi desenvolvido com base em princípios da **Teoria da Computação**, incluindo:

-   Autômatos finitos determinísticos e não determinísticos.
-   Fechamento-ε (epsilon closure).
-   Construção do autômato determinístico equivalente.
-   Reconhecimento de linguagem formal por autômatos.

## 📌 Observações

-   Os arquivos de entrada devem estar formatados corretamente para garantir a leitura e conversão corretas.
-   O projeto foi desenvolvido em **Python 3** e pode ser executado em qualquer ambiente compatível.

## 👨‍💻 Autor

Desenvolvido por **João Lucas da Costa**

💡 Projeto acadêmico com foco em **autômatos finitos e teoria da computação**.

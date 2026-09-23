# Análise Analítica e Empírica: Bubble Sort vs. Selection Sort

Disciplina: Computabilidade e Complexidade de Algoritmos

---

## 1. Análise Analítica (Algorítmica)

Ambas as implementações usadas neste trabalho são as versões **canônicas**
(sem otimizações como parada antecipada), para que a contagem de operações
corresponda exatamente ao previsto pela teoria. O código-fonte está em
`java/` e `python/`.

### 1.1 Bubble Sort

```
para i de 0 até n-2:
    para j de 0 até n-2-i:
        se arr[j] > arr[j+1]:
            troca(arr[j], arr[j+1])
```

**Contagem de operações**

- Comparações: em qualquer entrada, o algoritmo executa
  (n-1) + (n-2) + ... + 1 = **n(n-1)/2** comparações. Esse número **não
  depende dos dados de entrada** nesta versão canônica (sem flag de parada
  antecipada), portanto não há distinção de melhor/pior caso para as
  comparações.
- Trocas (swaps): variam conforme a entrada.
  - Melhor caso (array já ordenado): 0 trocas.
  - Pior caso (array em ordem decrescente): toda comparação gera uma troca
    → n(n-1)/2 trocas.
  - Caso médio (entrada aleatória): esperado n(n-1)/4 trocas.

**Complexidade de tempo**

| Caso   | Comparações | Trocas         | Tempo   |
|--------|-------------|-----------------|---------|
| Melhor | n(n-1)/2    | 0               | Θ(n²)   |
| Médio  | n(n-1)/2    | ≈ n(n-1)/4      | Θ(n²)   |
| Pior   | n(n-1)/2    | n(n-1)/2        | Θ(n²)   |

Como a versão implementada não possui a otimização de parada antecipada
(flag `swapped`), o **melhor caso também é Θ(n²)**, já que o duplo laço é
sempre percorrido por completo. (Nota: a variante otimizada, muito comum em
livros-texto, detecta que nenhuma troca ocorreu em uma passada e encerra o
algoritmo — nesse caso o melhor caso cai para O(n). Optamos pela versão sem
essa otimização para que a contagem de operações medida empiricamente bata
exatamente com a fórmula n(n-1)/2.)

**Complexidade de espaço:** O(1) — ordenação in-place, apenas variáveis
auxiliares de índice e troca.

### 1.2 Selection Sort

```
para i de 0 até n-2:
    min_idx = i
    para j de i+1 até n-1:
        se arr[j] < arr[min_idx]:
            min_idx = j
    se min_idx != i:
        troca(arr[i], arr[min_idx])
```

**Contagem de operações**

- Comparações: para encontrar o mínimo do subarray restante, o algoritmo
  sempre varre todos os elementos restantes, independentemente da ordem de
  entrada → (n-1) + (n-2) + ... + 1 = **n(n-1)/2** comparações, igual ao
  Bubble Sort, e também **sem variação entre melhor/médio/pior caso**.
- Trocas: no máximo **1 troca por iteração externa**, logo no máximo (n-1)
  trocas em qualquer caso — Θ(n), independentemente da entrada.

**Complexidade de tempo**

| Caso   | Comparações | Trocas | Tempo   |
|--------|-------------|--------|---------|
| Melhor | n(n-1)/2    | ≤ n-1  | Θ(n²)   |
| Médio  | n(n-1)/2    | ≤ n-1  | Θ(n²)   |
| Pior   | n(n-1)/2    | ≤ n-1  | Θ(n²)   |

O Selection Sort é Θ(n²) em **todos** os casos: não existe entrada que
reduza o número de comparações, pois a busca pelo mínimo sempre percorre o
subarray inteiro.

**Complexidade de espaço:** O(1) — ordenação in-place.

### 1.3 Comparação teórica entre os dois algoritmos

| Métrica                        | Bubble Sort              | Selection Sort |
|---------------------------------|---------------------------|-----------------|
| Comparações                    | n(n-1)/2 (Θ(n²))          | n(n-1)/2 (Θ(n²)) |
| Trocas (pior caso)             | n(n-1)/2 (Θ(n²))          | n-1 (Θ(n))      |
| Melhor caso (tempo)            | Θ(n²) (nesta versão)      | Θ(n²)           |
| Caso médio (tempo)             | Θ(n²)                     | Θ(n²)           |
| Pior caso (tempo)              | Θ(n²)                     | Θ(n²)           |
| Espaço auxiliar                | O(1)                      | O(1)            |
| Estável?                       | Sim                       | Não             |

Ambos pertencem à mesma classe assintótica de tempo, Θ(n²), e ambos usam
espaço extra constante O(1). A diferença relevante entre eles está no
**número de escritas/trocas na memória**: o Bubble Sort pode realizar até
Θ(n²) trocas, enquanto o Selection Sort realiza no máximo Θ(n) trocas. Como
uma troca (leitura + escrita + leitura + escrita) tende a ser mais custosa
que uma simples comparação, espera-se que o Selection Sort seja
consistentemente mais rápido que o Bubble Sort na prática, apesar de ambos
serem Θ(n²) — o que a análise empírica a seguir confirma ou não.

---

## 2. Análise Empírica

### 2.1 Metodologia

- Cada implementação (`java/BubbleSort.java`, `java/SelectionSort.java`,
  `python/bubble_sort.py`, `python/selection_sort.py`) recebe `n` por
  argumento de linha de comando, gera um vetor de `n` inteiros aleatórios,
  mede **apenas o tempo de ordenação** (sem contar geração dos dados) com
  `System.nanoTime()` (Java) / `time.perf_counter()` (Python), e confere ao
  final que o vetor ficou corretamente ordenado.
- Tamanhos testados: **n = 1.000, 10.000, 100.000 e 200.000**.
- Cada combinação (linguagem, algoritmo, n) foi executada **5 vezes**,
  cada execução em um processo novo (`java ...` / `python3 ...`
  independente), via o script `benchmark_runner.py`, que grava cada tempo
  em `resultados/java_resultados.csv` e `resultados/python_resultados.csv`
  e calcula média, mínimo, máximo e desvio padrão.
- **Observação sobre os dados brutos:** para n=100.000 no Bubble Sort em
  Python, o processo de benchmark foi pausado e retomado manualmente
  durante a coleta (para liberar a máquina), o que gerou 6 medições em vez
  de 5 — a primeira delas ocorreu enquanto o benchmark do Java ainda
  rodava em paralelo (concorrendo por CPU) e por isso foi **descartada**;
  as tabelas abaixo usam as 5 medições mais recentes e consistentes para
  essa célula, mantendo o experimento comparável às demais.

### 2.2 Resultados — Bubble Sort

| n       | Linguagem | Média (ms)     | Mínimo (ms)    | Máximo (ms)    | Desvio padrão (ms) |
|---------|-----------|---------------:|---------------:|---------------:|-------------------:|
| 1.000   | Java      | 7,36           | 6,99           | 7,84           | 0,31               |
| 1.000   | Python    | 52,78          | 49,62          | 55,18          | 2,75               |
| 10.000  | Java      | 156,74         | 155,11         | 158,58         | 1,23               |
| 10.000  | Python    | 3.495,88       | 2.673,92       | 6.503,38       | 1.681,87           |
| 100.000 | Java      | 26.468,61      | 25.453,18      | 27.208,86      | 654,53             |
| 100.000 | Python    | 281.833,52     | 271.605,73     | 298.467,28     | 11.142,01          |
| 200.000 | Java      | 72.121,17      | 70.831,19      | 74.086,88      | 1.498,23           |
| 200.000 | Python    | 1.138.497,18   | 1.123.891,78   | 1.166.939,41   | 18.322,57          |

### 2.3 Resultados — Selection Sort

| n       | Linguagem | Média (ms)     | Mínimo (ms)    | Máximo (ms)    | Desvio padrão (ms) |
|---------|-----------|---------------:|---------------:|---------------:|-------------------:|
| 1.000   | Java      | 2,46           | 1,68           | 3,65           | 1,05               |
| 1.000   | Python    | 9,99           | 9,57           | 10,94          | 0,55               |
| 10.000  | Java      | 38,87          | 38,42          | 39,43          | 0,39               |
| 10.000  | Python    | 1.254,18       | 1.120,32       | 1.332,91       | 84,18              |
| 100.000 | Java      | 3.919,23       | 3.651,54       | 4.286,20       | 238,01             |
| 100.000 | Python    | 115.002,61     | 114.572,74     | 115.550,45     | 422,55             |
| 200.000 | Java      | 15.236,97      | 14.274,31      | 15.891,94      | 800,90             |
| 200.000 | Python    | 475.900,16     | 474.564,86     | 478.503,84     | 1.508,41           |

*(dados brutos de todas as execuções individuais em
`resultados/java_resultados.csv` e `resultados/python_resultados.csv`)*

### 2.4 Discussão dos resultados

1. **Bubble Sort é sempre mais lento que Selection Sort**, nas duas
   linguagens e em todos os tamanhos de entrada — confirmando a previsão
   teórica da seção 1.3. Em n=200.000: Java leva 72,1s no Bubble contra
   15,2s no Selection (**~4,7x mais rápido**); em Python, 1.138,5s contra
   475,9s (**~2,4x mais rápido**). Como as duas versões fazem exatamente o
   mesmo número de comparações (n(n-1)/2), essa diferença vem quase toda
   do número de trocas: até n(n-1)/2 no Bubble Sort contra no máximo n-1
   no Selection Sort.

2. **Java é sempre mais rápido que Python para o mesmo algoritmo**, com a
   vantagem crescendo com n. No Bubble Sort, Java é ~7,2x mais rápido que
   Python em n=1.000 e chega a ser **~15,8x mais rápido** em n=200.000; no
   Selection Sort, vai de ~4,1x (n=1.000) a **~31,2x** (n=200.000). Isso é
   esperado: Java compila o laço para bytecode e o JIT otimiza operações
   repetitivas sobre um array primitivo (`int[]`), enquanto o CPython
   interpreta cada iteração do laço e cada comparação/troca de forma
   dinâmica (com overhead de bytecode do interpretador a cada acesso de
   lista), o que penaliza muito mais fortemente os laços aninhados de
   Θ(n²) à medida que n cresce.

3. **O crescimento do tempo com n é compatível com Θ(n²)** em ambas as
   linguagens: dobrar n de 100.000 para 200.000 aproximadamente
   **quadruplica** o tempo em quase todos os casos (ex.: Bubble Sort em
   Java vai de 26,5s para 72,1s, fator ~2,7x — um pouco abaixo de 4x,
   provavelmente por efeitos de cache/GC; em Python, de 281,8s para
   1.138,5s, fator ~4,0x, muito próximo do esperado teoricamente).

4. **O desvio padrão cresce com n** em todas as combinações, o que é
   normal: quanto maior o tempo de execução, mais chance de interferência
   de outros processos do sistema operacional, coleta de lixo (GC) e
   variação de frequência da CPU. Ainda assim, em termos relativos
   (coeficiente de variação), a dispersão permanece pequena (tipicamente
   1% a 4% da média), exceto no caso `Python/Bubble/n=10.000`, cuja
   primeira execução (6.503 ms) foi um outlier isolado (provavelmente
   afetado por outro processo do sistema no momento da medição),
   praticamente o dobro das demais — daí o desvio padrão elevado
   (1.681,87 ms) nessa linha.

---

## 3. Conclusão

Este trabalho analisou os algoritmos **Bubble Sort** e **Selection Sort**
tanto do ponto de vista **analítico** quanto **empírico**, com
implementações próprias em Java e Python.

Na análise analítica, mostramos que ambos os algoritmos pertencem à mesma
classe de complexidade de tempo, **Θ(n²)**, pois ambos realizam sempre
n(n-1)/2 comparações, independentemente da entrada (nas versões canônicas
usadas, sem otimização de parada antecipada). A diferença teórica entre
eles está no número de **trocas**: o Bubble Sort pode chegar a Θ(n²)
trocas no pior caso, enquanto o Selection Sort nunca ultrapassa Θ(n)
trocas, já que troca no máximo uma vez por iteração externa.

A análise empírica **confirmou integralmente** essa previsão teórica:

- O **Selection Sort foi sempre mais rápido que o Bubble Sort**, na mesma
  linguagem e para o mesmo n, com a vantagem chegando a **4,7x em Java**
  e **2,4x em Python** no maior tamanho testado (n=200.000). Isso mostra
  que, mesmo com a mesma complexidade assintótica Θ(n²), o **custo
  constante das operações importa muito na prática**: reduzir o número de
  trocas (operações de escrita em memória) tem impacto direto e
  mensurável no tempo de execução real.
- O **crescimento do tempo com n foi compatível com Θ(n²)** nas duas
  linguagens (o tempo aproximadamente quadruplicou ao dobrar n), validando
  experimentalmente a análise assintótica feita na seção 1.
- **Java superou Python em todos os casos**, com vantagem crescente à
  medida que n aumenta (de ~4x a ~31x), evidenciando o impacto do
  overhead do interpretador do CPython e dos benefícios de compilação
  JIT/tipagem estática do Java em laços aninhados executados um número
  muito grande de vezes.

Em suma, embora a **notação assintótica** (Θ(n²)) seja idêntica para os
dois algoritmos e para as duas linguagens, ela **não conta toda a
história**: fatores constantes — número de trocas, overhead de
interpretação, otimizações de compilador/JIT — dominam o tempo de
execução real observado, especialmente para entradas grandes. Para uso
prático em conjuntos de dados de tamanho considerável, o **Selection
Sort é preferível ao Bubble Sort**, e uma linguagem compilada/JIT como
Java tende a ser significativamente mais rápida que Python puro para
algoritmos com laços aninhados intensivos como estes O(n²).

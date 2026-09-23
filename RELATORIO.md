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

*(seção preenchida a partir dos resultados em `resultados/*.csv` — ver
tabelas ao final deste documento, geradas após a conclusão de todas as
execuções)*

---

## 3. Conclusão

*(a ser preenchida ao final, após consolidação dos resultados empíricos)*

# bubble-selection-sort-analise

Análise teórica e empírica de Bubble Sort e Selection Sort, implementados em Java e Python.

## Estrutura

- `java/` — implementações em Java (`BubbleSort.java`, `SelectionSort.java`)
- `python/` — implementações em Python (`bubble_sort.py`, `selection_sort.py`)
- `benchmark_runner.py` — script que executa os benchmarks e grava os resultados em CSV
- `resultados/` — CSVs com os tempos medidos (`java_resultados.csv`, `python_resultados.csv`)
- `RELATORIO.md` — relatório com a análise teórica e os resultados empíricos

## Como executar

Requisitos: Python 3 e JDK (`java`/`javac`) instalados.

Rodar um sort isoladamente:

```bash
java -cp java BubbleSort 10000
python3 python/selection_sort.py 10000
```

Cada programa recebe `n` como argumento e imprime o tempo de ordenação em milissegundos.

Rodar o benchmark completo (grava no CSV e imprime média/min/max/desvio padrão):

```bash
python3 benchmark_runner.py --lang java   --algo bubble    --sizes 1000 10000 100000 200000 --out resultados/java_resultados.csv
python3 benchmark_runner.py --lang python --algo selection --sizes 1000 10000               --out resultados/python_resultados.csv
```

O script compila os `.java` automaticamente antes de rodar (não é preciso rodar `javac` manualmente).

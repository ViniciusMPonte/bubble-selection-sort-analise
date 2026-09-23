#!/usr/bin/env python3
"""
Orquestrador dos benchmarks de Bubble Sort e Selection Sort (Java e Python).

Para cada combinacao (linguagem, algoritmo, n) executa o programa `repeats`
vezes como subprocesso, le o tempo de ordenacao (ms) impresso por ele, e
grava cada execucao em um CSV (append), alem de um resumo (media, min, max,
desvio padrao) ao final de cada tamanho de entrada.

Uso:
    python3 benchmark_runner.py --lang java   --algo bubble    --sizes 1000 10000 100000 200000 --out resultados/java_resultados.csv
    python3 benchmark_runner.py --lang python --algo selection --sizes 1000 10000               --out resultados/python_resultados.csv
"""
import argparse
import csv
import os
import statistics
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

COMMANDS = {
    ("java", "bubble"): ["java", "-cp", os.path.join(BASE_DIR, "java"), "BubbleSort"],
    ("java", "selection"): ["java", "-cp", os.path.join(BASE_DIR, "java"), "SelectionSort"],
    ("python", "bubble"): [sys.executable, os.path.join(BASE_DIR, "python", "bubble_sort.py")],
    ("python", "selection"): [sys.executable, os.path.join(BASE_DIR, "python", "selection_sort.py")],
}


def run_once(cmd, n):
    full_cmd = cmd + [str(n)]
    result = subprocess.run(full_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Falhou: {' '.join(full_cmd)}\n{result.stderr}")
    return float(result.stdout.strip())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lang", required=True, choices=["java", "python"])
    parser.add_argument("--algo", required=True, choices=["bubble", "selection"])
    parser.add_argument("--sizes", required=True, type=int, nargs="+")
    parser.add_argument("--repeats", type=int, default=5)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    cmd = COMMANDS[(args.lang, args.algo)]
    out_path = os.path.join(BASE_DIR, args.out) if not os.path.isabs(args.out) else args.out
    file_exists = os.path.exists(out_path)

    with open(out_path, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["lang", "algo", "n", "run", "tempo_ms"])

        for n in args.sizes:
            times = []
            for run in range(1, args.repeats + 1):
                t = run_once(cmd, n)
                times.append(t)
                writer.writerow([args.lang, args.algo, n, run, f"{t:.4f}"])
                f.flush()
                print(f"[{args.lang}/{args.algo}] n={n} run={run}/{args.repeats} -> {t:.2f} ms", flush=True)

            avg = statistics.mean(times)
            mn = min(times)
            mx = max(times)
            sd = statistics.stdev(times) if len(times) > 1 else 0.0
            print(
                f"  => resumo n={n}: media={avg:.2f}ms min={mn:.2f}ms "
                f"max={mx:.2f}ms desvio_padrao={sd:.2f}ms",
                flush=True,
            )


if __name__ == "__main__":
    main()

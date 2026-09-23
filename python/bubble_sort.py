import random
import sys
import time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def main():
    n = int(sys.argv[1])
    arr = [random.randint(-1_000_000_000, 1_000_000_000) for _ in range(n)]

    start = time.perf_counter()
    bubble_sort(arr)
    end = time.perf_counter()

    for i in range(1, n):
        if arr[i - 1] > arr[i]:
            print("ERRO: array nao ordenado corretamente", file=sys.stderr)
            sys.exit(1)

    ms = (end - start) * 1000.0
    print(ms)


if __name__ == "__main__":
    main()

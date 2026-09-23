import java.util.Random;

/**
 * Bubble Sort - implementacao canonica (sem otimizacao de parada antecipada),
 * para que o numero de comparacoes corresponda exatamente a analise
 * algoritmica de pior/medio caso: n*(n-1)/2 comparacoes sempre.
 *
 * Uso: java -cp java BubbleSort <n>
 * Imprime em stdout apenas o tempo de ordenacao em milissegundos.
 */
public class BubbleSort {

    public static void sort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 1 - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    int tmp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = tmp;
                }
            }
        }
    }

    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        Random rnd = new Random();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = rnd.nextInt();
        }

        long start = System.nanoTime();
        sort(arr);
        long end = System.nanoTime();

        for (int i = 1; i < n; i++) {
            if (arr[i - 1] > arr[i]) {
                System.err.println("ERRO: array nao ordenado corretamente");
                System.exit(1);
            }
        }

        double ms = (end - start) / 1_000_000.0;
        System.out.println(ms);
    }
}

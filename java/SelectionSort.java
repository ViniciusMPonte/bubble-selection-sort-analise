import java.util.Random;

public class SelectionSort {

    public static void sort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIdx]) {
                    minIdx = j;
                }
            }
            if (minIdx != i) {
                int tmp = arr[i];
                arr[i] = arr[minIdx];
                arr[minIdx] = tmp;
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

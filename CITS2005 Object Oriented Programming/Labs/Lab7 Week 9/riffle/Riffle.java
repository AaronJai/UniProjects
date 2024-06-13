package riffle;

public class Riffle {
    /*
        Riffles the first half of the array with the second half of the array.
        Assumes that the array always has even length.
        For example, if the array is {1, 2, 3, 4, 5, 6}, then after calling
        riffle, the array should be {1, 4, 2, 5, 3, 6}.
        In other words, the first half of the array should be interleaved
        with the second half of the array.
    */
    public static void riffle(int[] a) {
        // TODO (note: this is easier, start here)
        int n = a.length / 2;
        int[] temp = new int[a.length];
        int index = 0;

        for (int i = 0; i < n; i++) {
            temp[index++] = a[i];
            temp[index++] = a[n + i];
        }

        for (int i = 0; i < a.length; i++) {
            a[i] = temp[i];
        }
    }

    /*
        === This is the challenge problem ===
        Achieves the same result as riffle, but with the restriction that
        the array is riffled in place. That is, no additional space can be
        allocated. This means no new arrays or objects are allowed to be created
        either directly or indirectly (e.g. no using new int[], Arrays.copyOf,
        or new ArrayList).
        The method should achieve the riffle by swapping elements of the input
        array.
    */
    public static void riffleInPlace(int[] a) {
        // TODO (note: this is the hard part of the challenge)
        int n = a.length;
        int half = n / 2;
        int start = 0;
        while (start < n - 1) {
            int cur = start;
            int prev = a[cur];
            do {
                int next = cur < half ? 2 * cur : 2 * (cur - half) + 1;
                int temp = a[next];
                a[next] = prev;
                prev = temp;
                cur = next;
            } while (cur != start);
            start += 2;
        }
    }

    public static void main(String[] args) {
        // Output should be 1 100 2 200 3 300 4 400 5 500 6 600 7 700 8 800 9 900 10 1000
        int[] a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000};

        riffle(a);
        for (int i = 0; i < a.length; i++) {
            System.out.print(a[i] + " ");
        }
        System.out.println();

        a = new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000};
        riffleInPlace(a);
        for (int i = 0; i < a.length; i++) {
            System.out.print(a[i] + " ");
        }
        System.out.println();
    }
}
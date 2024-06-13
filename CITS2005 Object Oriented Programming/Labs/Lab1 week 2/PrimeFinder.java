import java.util.Scanner;

public class PrimeFinder {

    public boolean isPrime(int number) {
        
        // 1 and numbers less than 1 are not prime
        if (number < 2) {
            return false;
        }
        // check for factors from 2 to sqrt(number)
        for (int i = 2; i*i <= number; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        // if no factors found, number is prime
        return true;
    }

    public int countPrimes(int start, int end) {
        int count = 0;
        for (int i = start; i <= end; i++) {
            if (isPrime(i)) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        // Scanner sc = new Scanner(System.in);
        // System.out.print("Enter start: ");
        // int start = sc.nextInt();
        // System.out.print("Enter end: ");
        // int end = sc.nextInt();
        // PrimeFinder pf = new PrimeFinder();
        // System.out.println("There are " + pf.countPrimes(start, end) + " primes between " + start + " and " + end);


        // Parse command-line arguments
        int start = Integer.parseInt(args[0]);
        int end = Integer.parseInt(args[1]);

        PrimeFinder pf = new PrimeFinder();
        System.out.println("There are " + pf.countPrimes(start, end) + " primes between " + start + " and " + end);



        // ------------FOR isPrime FUNCTION-----------------//
        // int number = Integer.parseInt(args[0]);

        // boolean isPrime = isPrime(number);
        // System.out.println(isPrime);
    }

}
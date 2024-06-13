import java.util.Scanner;

public class PrimeFinder2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a positive number: ");
        
        for (;;) { // repeatedly asks user for prime number, until break is reached
            int num = sc.nextInt();
            if (num < 1)
                break;
            // Note the use of continue
            if (num == 1) {
                System.out.println("1 is not prime");
                continue;
            }
            boolean isPrime = true;
            // for numbers from 2 up to number exclusive.
            // similar to 2 up to the square root of the number.
            // this way is more efficient for smaller numbers. other way for bigger
            for (int d = 2; d < num; ++d) {
                if (num % d == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime)
                System.out.println(num + " is prime");
            else
                System.out.println(num + " is not prime");
        }
    }

}
import java.util.Scanner;

public class Factorial {
    
    public static double factorial(int n) {
        if (n == 0) {
            return 1;
        } else {
            return n * factorial(n-1);
        }
        
    }
    
    public static void main(String[] args) {
        // Scanner scanner = new Scanner(System.in);
        // System.out.println("What do you want to find the factorial of?");
        // int num = scanner.nextInt();
         

        int num = Integer.parseInt(args[0]);
        double result = factorial(num);

        System.out.println("The factorial of " + num + " is " + result);
    }
}

// NOTES
// Changed return type to long to be able to do larger factorials like 17!
// this wont work for 30!, but we can approximate it by using return type "double"
// BigInt (other file) to be able to get integers like 30! 
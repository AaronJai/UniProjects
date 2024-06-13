import java.util.Scanner;

public class Maximum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a: ");
        int a = sc.nextInt();
        System.out.print("Enter b: ");
        int b = sc.nextInt();

        // int maximum = a;
        // if (b > a)
        //     maximum = b;
        
        // TERNARY OPERATORS:  condition ? expression1 : expression2
        // If condition, expression1. Else, expression2

        int maximum = (a > b) ? a : b;

        System.out.println("Maximum: " + maximum);
    }
}
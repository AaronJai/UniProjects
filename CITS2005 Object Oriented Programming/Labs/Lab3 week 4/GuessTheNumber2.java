import java.util.Scanner;
import java.util.Random;

public class GuessTheNumber2 {
    public static void main(String[] args) {
        Random rand = new Random();
        int secretNumber = rand.nextInt(101);

        
        System.out.println("I am thinking of a number between 1 and 100. Guess what it is.");
        Scanner scanner = new Scanner(System.in);
        int guess;
        do {
            guess = scanner.nextInt();
            if (guess < 1) {
                System.out.println("Enter a positive number!");
            } else if (guess > secretNumber) {
                System.out.println("Nope, too high!");
            } else if (guess < secretNumber) {
                System.out.println("Nope, too low!");
            }

        } while (guess != secretNumber);
        System.out.println("You got it!");
    }
}
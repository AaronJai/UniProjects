import java.math.BigInteger;

public class Factorial2 {
    
    public static BigInteger factorial(BigInteger n) {
        if (n.equals(BigInteger.ZERO) || n.equals(BigInteger.ONE)) {
            return BigInteger.ONE;
        } else {
            return n.multiply(factorial(n.subtract(BigInteger.ONE)));
        }
    }
    
    public static void main(String[] args) {
        int num = Integer.parseInt(args[0]);
        BigInteger result = factorial(BigInteger.valueOf(num));
        System.out.println("Exact factorial of " + num + " is " + result);
    }
}

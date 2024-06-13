public class BankExample4 {
    public static void main(String [] args) {
        BankAccount4 account = new BankAccount4();
        account.ownerName = "Donald Knuth";
        account.balance = 1000;
        account.depositMoney(500);

        //int withdrawn = account.withdrawMoney(2000);
        account.withdrawMoney(1500);
        
        System.out. println (account.ownerName + " has $" + account.balance);
        //System.out. println ("Withdrawn $" + withdrawn);
    }
}
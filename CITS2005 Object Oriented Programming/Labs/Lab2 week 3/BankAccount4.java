class BankAccount4 {
    String ownerName;
    int balance;
    
    void depositMoney(int amount) {
        if (amount < 0) {
            System.out. println ("You can't deposit a negative amount!");
            return;
        }
        balance += amount;
    }

    int withdrawMoney(int amount) {
        if (amount > balance) {
        amount = balance;
        }
        balance -= amount;
        return amount;
    }
}
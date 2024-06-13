import java.util.ArrayList;

public class EmailManager {
    ArrayList<Email> emails;

    public EmailManager() {
        emails = new ArrayList<Email>();
    }

    public void addEmail(Email email) {
        emails.add(email);
    }

    public void printEmails() {
        for (Email email : emails) {
            System.out.println("Subject: " + email.subject);
            System.out.println("Sender: " + email.sender);
            System.out.println("Message: " + email.message);
        }
    }

    public ArrayList<Email> getEmailsLongerThan(int minMessageLength) {
        // TODO
        ArrayList<Email> longEmails = new ArrayList<Email>();
        for (Email email : emails) {
            if (email.message.length() > minMessageLength) {
                longEmails.add(email);
            }
        }
        return longEmails;
    }

    public static void main(String[] args) {
        // You can run this class to test your code
        EmailManager em = new EmailManager();
        em.addEmail(new Email("Hello", "Donald", "Hello, world!"));
        em.addEmail(new Email("CITS2005", "Max", "Good luck with the lab!"));
        em.addEmail(new Email("The halting problem", "Alan", "I'm not sure if this is solvable."));
        em.printEmails();

        System.out.println("Long emails:");
        for (Email email : em.getEmailsLongerThan(20)) {
            System.out.println(email.subject);
        }
    }
}
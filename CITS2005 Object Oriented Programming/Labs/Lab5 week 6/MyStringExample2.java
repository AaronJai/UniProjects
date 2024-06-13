public class MyStringExample2 {
    public static void main(String[] args) {
        MyString s = new MyString("Hello".toCharArray()); // to convert into a char array. is originally just string literal
        
        s = s.concatenate(new MyString("World".toCharArray()));
        s = s.substring(3, 6);

        System.out.println(s.length());
        System.out.println(s.charAt(0));

        if (s.equals(new MyString("loW".toCharArray())))
            System.out.println("Success");
        else
            System.out.println("Failure");

        for (int i = 0; i < s.length(); i++)
            System.out.println(s.charAt(i));

       
    }
}
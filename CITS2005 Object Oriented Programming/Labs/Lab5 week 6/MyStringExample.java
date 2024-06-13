public class MyStringExample {
    public static void main(String[] args) {
        MyString s = new MyString("Hello".toCharArray());
        s.chars[0] = 'J';
        for (int i = 0; i < s.length(); i++)
            System.out.println(s.charAt(i));
    }
}
public class MyString {
    private char[] chars;

    public MyString(char[] chars) {
        this.chars = new char[chars.length];
        for (int i = 0; i < chars.length; i++) {
            this.chars[i] = chars[i];
        }
    }

    public char charAt(int index) {
        return chars[index];
    }

    public int length() {
        return chars.length;
    }

    public boolean equals(MyString s) {
        if (length() != s.length())
            return false;
        for (int i = 0; i < length(); i++) {
            if (charAt(i) != s.charAt(i))
                return false;
        }
        return true;
    }

    // added
    public boolean equals(String s) {
        if (length() != s.length())
            return false;
        for (int i = 0; i < length(); i++) {
            if (charAt(i) != s.charAt(i))
                return false;
        }
        return true;
    }

    public MyString substring(int start, int end) {
        char[] newChars = new char[end - start];
        for (int i = start; i < end; i++) {
            newChars[i - start] = chars[i];
        }
        return new MyString(newChars);
    }

    // added
    public MyString substring(int start) {
        return substring(start, length());
    }


    public MyString concatenate(MyString s) {
        char[] newChars = new char[chars.length + s.length()];
        for (int i = 0; i < chars.length; i++)
            newChars[i] = chars[i];
        for (int i = 0; i < s.length(); i++)
            newChars[chars.length + i] = s.charAt(i);
        return new MyString(newChars);
    }

    // added
    public MyString concatenate(char c) {
        char[] newChars = new char[chars.length + 1];
        for (int i = 0; i < chars.length; i ++) {
            newChars[i] = chars[i];
        }
        newChars[chars.length] = c;
        return new MyString(newChars);
    }
}
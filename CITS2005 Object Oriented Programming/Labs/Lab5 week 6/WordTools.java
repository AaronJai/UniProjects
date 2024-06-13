public class WordTools {

    public static boolean isWord(String string) {
        return string != null && string.matches("[A-Za-z]+");
    }

    public static boolean isLowerCaseWord(String string) {
        //return string != null && string.equals(string.toLowerCase());
        return string != null && string.trim().equals(string.toLowerCase()); // only accounts for leading and trailing whitespace
    }

    public static boolean isUpperCaseWord(String string) {
        //return string != null && string.equals(string.toUpperCase());
        return string != null && string.trim().equals(string.toUpperCase());
    }

    public static boolean isSarcasmCaseWord(String string) {
        if (!isWord(string)) {
            return false;
        }

        // Check for sarcasm case starting with a lowercase letter
        boolean isLowercaseStartSarcasm = true;
        // Check for sarcasm case starting with an uppercase letter
        boolean isUppercaseStartSarcasm = true;

        for (int i = 0; i < string.length(); i++) {
            char c = string.charAt(i);
            if (i % 2 == 0) {
                if (!Character.isLowerCase(c)) {
                    isLowercaseStartSarcasm = false;
                }
                if (!Character.isUpperCase(c)) {
                    isUppercaseStartSarcasm = false;
                }
            } else {
                if (!Character.isUpperCase(c)) {
                    isLowercaseStartSarcasm = false;
                }
                if (!Character.isLowerCase(c)) {
                    isUppercaseStartSarcasm = false;
                }
            }
        }

        return isLowercaseStartSarcasm || isUppercaseStartSarcasm;
    }

    public static void main(String[] args) {
        System.out.println(isWord("Hello")); // true
        System.out.println(isWord("Hello!")); // false
        System.out.println(isWord("H ello")); // false
        System.out.println(isLowerCaseWord("hello")); // true
        System.out.println(isLowerCaseWord("hI")); // false
        System.out.println(isUpperCaseWord("TEST")); // true
        System.out.println(isUpperCaseWord("TEST ")); // false
        System.out.println(isUpperCaseWord("tEST")); // false
        System.out.println(isSarcasmCaseWord("tEsT")); // true
        System.out.println(isSarcasmCaseWord("TeSt")); // true
        System.out.println(isSarcasmCaseWord("test")); // false
        System.out.println(isSarcasmCaseWord("TeST")); // false
    }
}
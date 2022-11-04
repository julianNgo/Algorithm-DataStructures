public class SampleString {

    public static void main(String[] args) {
        String s1 = "Hello World!";
        String s2 = new String("Hello World!");

        for (int i = 0; i < s1.length(); i++) {
            char c = s1.charAt(i);
            System.out.println(c);
        }
    }
}
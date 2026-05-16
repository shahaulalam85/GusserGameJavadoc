
public class main {

    public static void main(String[] args) {

        String s1 = new String("CAT");
        // String s2 = s1.intern();
        String s3 = "CAT";

        // System.err.println(s2.hashCode());
        System.err.println(s3.hashCode());
        System.err.println(s1.hashCode());
    }
}

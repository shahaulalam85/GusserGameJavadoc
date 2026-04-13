
public class main {

    public static void main(String[] args) {
        Integer obj = Integer.valueOf(675656);

        obj.doubleValue(); // 65.0    (double)
        obj.floatValue();  // 65.0    (float)
        obj.longValue();   // 65L     (long)
        obj.byteValue();   // 65      (byte)
        obj.shortValue();  // 65      (short)
        System.out.println(obj.intValue());    // 65      (int)
        System.out.println(obj.floatValue());    // 65      (int)
        System.out.println(obj.longValue());    // 65      (int)
        System.out.println(obj.byteValue());    // 65      (int)
        System.out.println(obj.shortValue());    // 65      (int)
    }
}

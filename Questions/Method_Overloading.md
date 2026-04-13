## Tricky ambiguity cases
```java
@ Case 1 — null argument

    public class Main{
        void handle(String s) {
            System.out.println("String");
        }

        void handle(Object o) {
            System.out.println("Object");
        }
        
        public static void main(String[] args) {
 		 //handle(null);   // → "String" — most specific type wins            
            Main obj = new Main();
            obj.handle(null); // String

        }
    }

🧠 Why Error Occurs
main() is static, but handle() methods are non-static.
You are calling:
handle(null);
This is equivalent to calling a non-static method without object, which is not allowed.

Alternative 
-----------
    class main {
        static void handle(String s) { // static
            System.out.println("String");
        }
        static void handle(Object o) { // static
            System.out.println("Object");
        }
        public static void main(String[] args) {

            handle(null);   // → "String" — most specific type wins
        }
    }


@ Case 2 — ambiguous call (compile error)

    void ambig(int a, double b)  { }
    void ambig(double a, int b)  { }

    ambig(1, 2);   // COMPILE ERROR — both are equally specific

@ Case 3 — varargs ambiguity

    void v(int... a)    { }
    void v(int a, int b) { }

    v(1, 2);   // picks v(int, int) — fixed-arity wins over varargs
    v(1, 2, 3); // picks v(int...) — only match


```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


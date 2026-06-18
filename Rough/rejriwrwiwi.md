```java
1. 
class Test {
    public static void main(String[] args) {
        try {
            System.out.println("A");
            throw new RuntimeException();
        }
        finally {
            System.out.println("B");
        }
    }
}

2. 
class Test {
    static void m1() {
        try {
            return;
        }
        finally {
            System.out.println("Finally");
        }
    }

    public static void main(String[] args) {
        m1();
    }
}

3. 
class Test {
    public static void main(String[] args) {

        try {
            throw new Exception();
        }
        catch(RuntimeException e) {
            System.out.println("R");
        }
        catch(Exception e) {
            System.out.println("E");
        }
    }
}

4. 
class Test {

    static void m1() throws Exception {
        throw new java.io.IOException();
    }

    public static void main(String[] args) {

        try {
            m1();
        }
        catch(java.io.FileNotFoundException e) {
            System.out.println("F");
        }
        catch(Exception e) {
            System.out.println("E");
        }
    }
}

5.

class Test {

    public static void main(String[] args) {

        try {
            System.out.println(10/0);
        }
        catch(Exception e) {
            System.out.println("A");
        }
        catch(ArithmeticException e) {
            System.out.println("B");
        }
    }
}

6. 
class Test {

    static void m1() throws Exception {
        throw new Exception();
    }

    static void m2() throws Exception {
        try {
            m1();
        }
        catch(Exception e) {
            throw e;
        }
    }
}

7. 
class Parent {
    void m() throws Exception {}
}

class Child extends Parent {
    void m() throws RuntimeException {}
}

8. 
class Parent {
    void m() throws java.io.IOException {}
}

class Child extends Parent {
    void m() throws Exception {}
}

9. 
class Test {

    public static void main(String[] args) {

        try {
            throw null;
        }
        catch(NullPointerException e) {
            System.out.println("NPE");
        }
    }
}

10. 
class Test {

    public static void main(String[] args) {

        try {
            throw null;
        }
        catch(Exception e) {
            System.out.println(e);
        }
    }
}

11.
class Test {

    public static void main(String[] args) {

        try {
            System.exit(0);
        }
        finally {
            System.out.println("Finally");
        }
    }
}

12. 
class Test {

    public static void main(String[] args) {

        try {
            return;
        }
        finally {
            return;
        }
    }
}

13.
class Test {

    public static void main(String[] args) {

        try {
            throw new Error();
        }
        catch(Exception e) {
            System.out.println("E");
        }
    }
}

14.
class Launch {}

public class Test {

    public static void main(String[] args) {

        throw new Launch();
    }
}

15. 
class Test {

    public static void main(String[] args) {

        try {
            int x = 10/0;
        }
        finally {
            System.out.println("F");
        }
    }
}

Grandmaster Challenge
public class Test {
    public static void main(String[] args) {

        try {
            throw null;
        }
        catch(ArithmeticException e) {
            System.out.println("A");
        }
        catch(NullPointerException e) {
            System.out.println("N");
        }
        catch(Exception e) {
            System.out.println("E");
        }
    }
}

```
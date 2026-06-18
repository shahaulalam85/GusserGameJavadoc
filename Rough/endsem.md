## Abstraction
```java
How to achive abstraction 
    1. Abstract classes 
    2. Interfaces

Abstract keyword:
    1. applied to class and methods 
    2. abstract class cannot be instantiated(object of that class cannot be created) only be extended by other class 
    3. if a class has only one abstract method then the class must be decleared as abstract

Abstract Classes:
    1. contians abstract methods and normal methods 
    2. contains constructor 
    3. contains instance variable
    4. contains static methods and static variables
    5. java supports only single inheritance so a class can only extends only one abstract class.

Abstract Methods:
    1. abstract void draw(); // this is simple method signature 
    2. abstract methods cannot be private, final, static 

Why Abstration:
    1. Securuty 
    2. less complex
    3. easy maintanance 
    4. flexible 
    5. code resuability 
    6. loose coupling

Can abstract method be overloaded: Yes (Method Overloading is allowed.)
    abstract class Maths{
        abstract void add(int a, int b);
        abstract void add(int a, int b, int c);
        abstract void add(float a, int b);
    }


Rules of Abstraction:
    1. if a class have only one abstract method then the class must be decleated as abstract.

Not Allowed:
    1. abstract + final
    2. abstract + private
    3. abstract + static

Important points:
    1.  class Animal
        {
            abstract void eat(); // compile time error
        }

    2.  Valid syntax
        a.  abstract class A{};
        b.  abstract class A{
                void show(){}
            }
    
    3. abstract class A
        {
            abstract void show();
        }

        class B extends A
        {
        } // compile error 

    4.  A obj = new C();
        obj.show();
       // method resolution happens at run time

    5.  abstract static void show(); // invalid 
        abstract final void show(); // invalid
        abstract private void show(); // invalid

        abstract protected void show(); // valid ******

    6.  Static block executes once when class loads.
        Constructor executes during object creation.
    
    7.  abstract class A
        {
            abstract void show();
            public static void main(String[] args)
            {
                System.out.println("Main");
            }
        }
        Abstract classes can have:
            ✔ main() **********************
            ✔ constructors
            ✔ variables
            ✔ static blocks
            Only object creation is prohibited.
    
    8. 


Rules:
Rule 1: Abstract Class Constructor Executes
Fact: Abstract classes cannot create objects, but their constructors execute when a child object is created.

                    abstract class A
                    {
                        A()
                        {
                            System.out.print("A ");
                        }
                    }
                    class B extends A
                    {
                        B()
                        {
                            System.out.print("B ");
                        }
                    }
                    public class Test
                    {
                        public static void main(String[] args)
                        {
                            new B(); // A B
                        }
                    }

Rule 2: Runtime Polymorphism Works Inside Constructors
Fact:   Even inside a parent constructor:
                A()
                {
                    show();
                }
        Java still calls the child overridden method.

                    abstract class A
                    {
                        A()
                        {
                            show();
                        }
                        abstract void show();
                    }
                    class B extends A
                    {
                        void show()
                        {
                            System.out.print("B");
                        }
                    }
                    public class Test
                    {
                        public static void main(String[] args)
                        {
                            new B(); // B
                        }
                    }


Rule 3: Child Variables Not Initialized Yet
                    abstract class A
                    {
                        A()
                        {
                            show();
                        }

                        abstract void show();
                    }

                    class B extends A
                    {
                        int x = 100;

                        void show()
                        {
                            System.out.print(x + " ");
                        }
                    }

                    public class Test
                    {
                        public static void main(String[] args)
                        {
                            new B();
                        }
                    }

    q2:

        abstract class A
        {
            A()
            {
                System.out.print("A ");
                show();
            }

            abstract void show();
        }

        class B extends A
        {
            int x = 5;

            B()
            {
                System.out.print("B ");
            }

            void show()
            {
                System.out.print(x + " ");
            }
        }

        class C extends B
        {
            int x = 10;

            C()
            {
                System.out.print("C ");
            }

            void show()
            {
                System.out.print(x + " ");
            }
        }

        public class Test
        {
            public static void main(String[] args)
            {
                new C();
            }
        }

Rule 4: Variables Are NOT Polymorphic


Rule 5: Constructor Execution Order
                1. Memory Allocation

                2. Default Values
                        x=0
                        name=null
                        flag=false

                3. Parent Instance Variables

                4. Parent Constructor

                5. Child Instance Variables

                6. Child Constructor











Questions:
1. 
    abstract class A{ A()}
    class B extends A{ B()}
    in main B b = new B(); // A B
2. 
abstract class A
{
    A()
    {
        show();
    }
    abstract void show();
}

class B extends A
{
    int x = 10;

    void show()
    {
        System.out.print(x);
    }
}

public class Test
{
    public static void main(String[] args)
    {
        new B(); // 0
    }
}

3. How many errors -> 3 errors
abstract class A
{
    abstract final void m1(); // ❌

    abstract static void m2(); // ❌

    abstract private void m3(); // ❌

    abstract void m4(); // ✅
}

3. 
abstract class A
{
    int x = 10;
    A()
    {
        System.out.print(getX() + " ");
    }
    int getX()
    {
        return x;
    }
}
class B extends A
{
    int x = 20;
    int getX()
    {
        return x;
    }
}

public class Test
{
    public static void main(String[] args)
    {
        A obj = new B(); // 0
        System.out.print(obj.getX()); // 20
    }
}
Looks like it should call A.getX(), right?

❌ Wrong!

Because getX() is overridden.
Java uses runtime polymorphism even inside constructors.
So JVM calls: B.getX()

```

## Interface

```java

Why Interfaces are introduced ?
    Befor Interface : class -> inheritance -> reuse
    Problem: java doesnot support multiple inheritance using class.
    solution: Interface 

Interface provides:
    1. 100% abstraction
    2. Loose coupling
    3. runtime polymorphism
    4. multiple inheritance ✅
    5. doesnot support constructor ❌
    6. Instance variable doesnot not ❌ (only constant)


What is an Interface?
    Class -> blueprint of an object
    Interface -> blueprint of a class 

Important points:
    1. Methods are automatically public abstract even if it is not written 
    2. keyword for connection => implements

Every database have different API , so standardise this, java defined JDBC conection interface with three standard methods.
    1. getConnection()
    2. executeQuery()
    3. close()
```
```java

Proof — Same Code Works for Any Database
-----------------------------------------
    // ORACLE
    Connection con  = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:XE", "user", "pass");
    Statement  stmt = con.createStatement();
    ResultSet  rs   = stmt.executeQuery("SELECT * FROM employees");
    con.close();

    // MYSQL — only URL changed, everything else is IDENTICAL
    Connection con  = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "user", "pass");
    Statement  stmt = con.createStatement();
    ResultSet  rs   = stmt.executeQuery("SELECT * FROM employees");
    con.close();

    // POSTGRESQL — only URL changed, everything else is IDENTICAL
    Connection con  = DriverManager.getConnection("jdbc:postgresql://localhost:5432/mydb", "user", "pass");
    Statement  stmt = con.createStatement();
    ResultSet  rs   = stmt.executeQuery("SELECT * FROM employees");
    con.close();
``` 
```java

Rules of Interface:
    1. Interfaces achive standardiasation 
    2. Interfaces provide a contract
    3. Interface is the blue print of class (Interface → Class → Object)
    4. Interface achives 100% abstraction (Every methods in the inteface is implicity public abstract)
                interface Calculator{
                    void add(); // after compilation public abstract void add()
                    void sub(); // after compilation public abstract void sub()
                }
    5. Any number of classes can implement an Inteface
                interface Calculatable { void add(); void sub(); }
                class Casio implements Calculatable {...}
                class Orpat implements Calculatable{...}
                class Citizen implements Calculatable{...} // all valid 
    6. Cannot instantiate but reference can be created 
            Using interface reference we can only access overriden methods but to access specialized method of an implimenting class require downcasting.

    7. Multiple inheritance is possible in interface 
            A class can implement any number of interfaces
                    interface Calculatable1 { void add(); void sub();}
                    interface Calculatable2 { void add(); void sub();}

                    class Casio implements Calculatable1 , Calculatable2{...}
    8. Interface cannot implement(❌) another interface but Interface extends(✅) another interface 

    9. Interface can extends multiple in interfaces
                    interface Calculatable3 extends Calculatable1, Calculatable2 {
                        void sqr(); void pow();
                    }
    10. extends first and implements second
                    class Casio extends Maths implements Calculatable {
                        public void add() { /* ... */ }
                        public void sub() { /* ... */ }
                    }

    11. Partial implementation of interface then decleare class with abstract 

    12. Interface variables are constant (implicitly public static final)
                    interface Calculatable {
                        double PI = 3.141;  // implicitly: public static final double PI = 3.141;
                        void add();  // implicitly: public abstract void add();
                        void sub();
                    }

    13. Marker or Tagged Interface - Empty Interface ✅
                    interface Calculatable { } // Valid — Marker Interface
    
    14. Default methods - Backward-Compatible Evolution(Java 8) - Defender Method, Saviour method
                    interface Calculatable {
                        void add();
                        void sub();
                        default void mul() { // NEW functionality added safely
                        System.out.println("Default implementation of mul()");
                        }
                    }

    15. Static methods in Inteface -> they belong to inteface itself
            they cannot be overriden , they can only be invoked using interface name         
                    interface Calculatable {
                        void add();
                        static void max() {
                            int num1 = 50, num2 = 85;
                            System.out.println(num1 > num2 ? "Max: "+num1 : "Max: "+num2);
                        }
                    }
                    class Launch {
                    public static void main(String[] args) {
                        Calculatable.max(); // ✓ Correct — called via interface name ✅
                        // Casio cas = new Casio();
                        // cas.max(); // max(); // ✗ ERROR — cannot access static method via instance ❌
                        // ✗ ERROR — must use interface name
                        }
                    }

    16. Functional Interface - SAM Inteface 
            |-> It can have any number of static and default methods but only ONE abstract methods
                    @FunctionalInterface // optional but recommended for safety guard 
                    interface Calculatable {
                        void add(); // ← The ONE abstract method (SAM)
                        default void mul() { System.out.println("mul default"); }
                        static void max() { System.out.println("max static"); }
                    }
                    // Can be implemented using a Lambda Expression:
                    Calculatable c = () -> System.out.println("Lambda add!");
                    c.add();

            |-> If we try to add another method to @FunctionalInterface then it throws compilation error 

    17. Private methods in Interfaces (both static and non-static)
            |-> they improve code reuseablity and encapsulation 
                    interface Calculatable {
                        default void add(){...}
                        private void printInfo() {...}
                    }

    18. .class file is generated for every interface 
            |-> it is possible to define main() inside interface 
                    interface Launch {
                        public static void main(String[] args) {
                            System.out.println("main() inside an Interface!");
                        }
                    }
                    // Compile: javac Launch.java → generates Launch.class
                    // Run: java Launch → prints: main() inside an Interface!
                This means: Can we execute a Java program without a class?
                YES — using an Interface with a static main() method (Java 8+)

```

## Exception Handling 
```java

Exception -> refer to the mistake that occurs during the execution of a program 
        |-> because of abnormal termination valuable resources may be lost 

Exception handling -> the process of handling the exception object in such a manner that it prevents abnormal termination 

try -> risky code 
catch -> handling code 
finally -> cleanup code 
throw -> to handover the exception object to the jvm manually 
throws -> to delegate the responsibility of handling the exception to the caller 

Exception object contians three pieces of information 
        1. Name of the exception
        2. Description of an exception 
        3. Stack Trace
```
```java

Methods to print exception information(from throwable class)
        1. e.getMessage()
        2. e.toString()
        3. e.printStackTrace()

Abnormal Termination -> any code after the exception point is skipped .

Invalid (compilation error) -> catch(Exceptio e) followed by catch(ArithmeticException e) ❌ => reverse is correct 
            |-> i.e generic exception is placed at the end of the hierarchy 

Different Ways to handle the exception 
        1. Handling the exception [try-catch]
                        |-> exception handled within the SAME methods
        2. Rethrows the exception [try-catch-throw-throws-finally]
                        |-> if a method explicity throw an exception then 'thows' keyword is used if checked 
                                            |-> Checked exception -- throws is mandatory if it is not handled using catch block else opt.
                                            |-> Unchecked exception --- throws is optional
        3. Ducking the exception [throws]
                        |-> a methods doesnot want to handle exception and hands over responsiblities to the caller using 'throws'      keyword in the signature. 


Rules of throws in exception 
        1. Unchecked exception -> if you throw a RUNTIME exception then 'throws' is optional
        2. checked exception -> YES , throws mendatory if exception is not handled 


finally vs return : finally dominated over the return 
finally vs System.exit(0) : System.exit(0) donimates over finally 
                       |-> 0 means normal termination and !=0 means abnormal termination

Difference checked vs unchecked 
                checked                  |                   unchecked 
        ---------------------------------------------------------------------------------------
        1. compile time check                           1. No compile time check
        2. enforces handling by compiler                2. no enforcement 
        3. further classified (fully and partially)     3. No further classified 
        4. throws keyword is mandatory                  4. thorws keyword is optional
        5. Program can be recovered                     5. Program cannot be recovered 
        6. Generally outside the program                6. generally inside the program 
        7. end result is normal termination             7. end result is abnormal terminantion 

Difference between error and exception 

                error                               |                    exception
        ---------------------------------------------------------------------------------------
        1. occurs due to lack of system resources               1. occure due to program code 
        2. non-recoverable                                      2. recoverabel
        3. handles by try-catch                                 3. no mean of handle
        4. unchecked only                                       4. both checked and unchecked 
        5. always abnormal termination                          5. both normal and abnormal termination

Difference throw vs throws 

                    throw                            |                      throws 
        ---------------------------------------------------------------------------------------
        1. explicitly throw exception to the jvm                1. it delegates the exception to the caller 
        2. followed by throwable instance                       2. followe by exception class name 
        3. decleared within the method                          3. decleared with the signature of the methods/constructor
        4. single throw clause only                             4. multiple exception class name allowed 
        5. used in rethrowing                                   5. used in rethrowing and ducking

throw: 
        1. jvm can throw automatically 
        2. programmer can throw manually 
        3. throw followed by throwable object 
        4. no statement after throw 

throws:
        1. throws followed by exception class 

valid method overridding:
        for checked: (have restriction)
            1. parent
                |
               child (same , smaller , none)
            2. child cannot be bigger 

        for unchecked: (no restriciton)




```

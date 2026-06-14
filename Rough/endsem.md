## Abstrction
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




1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
```
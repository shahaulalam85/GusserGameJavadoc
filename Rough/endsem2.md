## 1.
```java
(a) Why is encapsulation suitable for this scenario? (2 Marks)
-> Encapsulation hides the member data from direct access.
-> Data can be modified only through methods, ensuring security and control.
-> It helps maintain data integrity.



b.
class Member 
{
    private int membershipId;
    private String name;
    private int borrowBooks;
    
    // constructor 
    public Member(int membershipId, String name, int borrowBooks){
        this.membershipId = membershipId;
        this.name = name;
        this.borrowBooks = borrowBooks;
    }
    
    // getter 
    public int getMembershipId(){
        return membershipId;
    }
    public String getName(){
        return name;
    }
    public int getBorrowBooks(){
        return borrowBooks;
    }
    
    // method
    public void borrowBooks(){
        borrowBooks++;
    }
}


class Main {
    public static void main(String[] args) {
        Member a = new Member(12, "Shahaul", 123);
        
        System.out.println(a.getBorrowBooks());
    }
}


```

## 2
```java

(a) Which OOP concept is most appropriate? (2 Marks)

Polymorphism (Method Overriding)

Justification:
-> Different delivery options calculate charges differently.
-> A common method calculateCharge() can be defined in the superclass and overridden in subclasses.
-> This provides flexibility and code reusability.


b. 
class Delivery
{
    public void calculateCharge(){
        System.out.println("Delivery Charge");
    }
}

class StandardDelivery extends Delivery
{
    @Override
    public void calculateCharge(){
        System.out.println("Standard Delivery Charge = 50");
    }
}

class ExpressDelivery extends Delivery
{
    @Override
    public void calculateCharge(){
        System.out.println("Express Delivery Charge = 100");
    }
}

class Main {
    public static void main(String[] args) {
        Delivery d1 = new StandardDelivery();
        Delivery d2 = new ExpressDelivery();
        d1.calculateCharge();
        d2.calculateCharge();
    }
}

```

## 3.
```java
a. 
class Main {
    public static void main(String[] args) {
        int[] marks = {10, 20, 30, 40, 50};
        int maxi = marks[0];
        
        for(int m : marks){
            if(m>maxi){
                maxi = m;
            }
        }
        
        System.out.println(maxi);
    }
}

b.
(b) Why are arrays suitable? (2 Marks)
-> Arrays store multiple values of the same data type in a single variable.
-> They allow easy access and processing of marks using indexes and loops.
-> Memory is allocated efficiently.


```

## 4.
```java

a. 
(a) OOP Concept Demonstrated (2 Marks)
Polymorphism (Method Overriding)

Reason:
-> All devices have the same method turnOn().
-> Each device performs a different action when the method is called.
-> This is achieved using method overriding.

b. 
class Device
{
    public void turnOn(){
        System.out.println("Device is ON");
    }
}

class Fans extends Device
{
    @Override
    public void turnOn(){
        System.out.println("Fan is ON");
    }
}

class Lights extends Device
{
    public void turnOn(){
        System.out.println("Light is ON");
    }
}


class Main {
    public static void main(String[] args) {
        Device d1 = new Fans();
        Device d2 = new Lights();
        d1.turnOn();
        d2.turnOn();
    }
}

```

## 5.
```java
a. 
(a) Why is Exception Handling Important? (2 Marks)
-> Exception handling prevents the program from crashing when an error occurs.
-> It allows the application to handle errors gracefully and display meaningful messages to users.
-> It improves the reliability and security of banking applications.

b.
class Main {
    public static void main(String[] args) {
        int balance = 5000;
        int withdrawlAmount = 7000;
        
        try
        {
            if(withdrawlAmount>balance){
               throw new Exception("Insufficient Balance");
            }
            
            balance = balance - withdrawlAmount;
            System.out.println("Withdrawal Successful");
        }
        catch (Exception e)
        {
            System.out.println(e.getMessage());
        }
        finally
        {
            System.out.println("Transection Completed");
        }
        
    }
}

```

## 6. 
```java

a. 
(a) Which Java Collection Class? (2 Marks)

TreeSet
Reasons:
    -> Does not allow duplicate elements.
    -> Stores elements in sorted (alphabetical) order automatically.


b. 
import java.util.TreeSet;
class Main {
    public static void main(String[] args) {
        TreeSet<String> courses = new TreeSet<>();
        courses.add("Java");
        courses.add("DBMS");
        courses.add("Maths");
        courses.add("DSA");
        courses.add("English");
        
        for(String s : courses){
            System.out.println(s);
        }
    }
}
```

## 7.
```java
Constructor Overloading in Java (5 Marks)

Definition
        -> Constructor overloading is the process of defining multiple constructors in the same class with different parameter lists.

Advantages
        -> Provides multiple ways to initialize objects.
        -> Improves code flexibility and readability.
        -> Allows object creation with different sets of data.


class Student
{
    String name;
    int age;
    
    // Default constructor 
    Student(){
        this.name = "Unknown";
        this.age = 0;
    }
    
    // Parameterised construcor 
    Student(String name, int age){
        this.name = name;
        this.age = age;
    }
    
    public void dispaly(){
        System.out.println("Name is: " + name);
        System.out.println("Age is: " + age);
    }
}




class Main {
    public static void main(String[] args) {
        Student s = new Student("Saha", 21);
        Student s2 = new Student();
        s.dispaly();
        s2.dispaly();
    }
}

```

## 8. 
```java
Definition
        -> Method overriding occurs when a child class provides its own implementation of a method already defined in the parent class.

        -> It is used to achieve runtime polymorphism.

Any Two Rules of Method Overriding
        -> The method name, return type, and parameters must be the same in both parent and child classes.
        -> The method being overridden cannot be private, final, or static.


class Animal
{
    public void sound(){
        System.out.println("Animal make a sound");
    }
}

class Dog extends Animal
{
    public void sound(){
        System.out.println("Dog barks");
    }
}


class Main {
    public static void main(String[] args) {
        Animal a = new Dog();
        a.sound();
    }
}
```
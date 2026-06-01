## Correct Syntax of creation of object 

```java
1️⃣ Standard Object Creation
    Student s1 = new Student();

2️⃣ Declaration then Creation
    Student s1;
        s1 = new Student();

3️⃣ Multiple Objects
    Student s1 = new Student(), s2 = new Student();

4️⃣ Anonymous Object
    new Student();

5️⃣ With Constructor Parameters
    Student s1 = new Student(101, "Ali");

6️⃣ Class Name and object reference name are same
    Students Students = new Students();

7️⃣ Assigning null then object
    Car c = null;
        c = new Dog();


8️⃣ Multiple References, One Object
        Animal a, b, c;
            a = b = c = new Animal();
```

 ## ✅ Valid — main() in a non-public class (multiple mains possible)
```java

// File: MyProgram.java

class A {
    public static void main(String[] args) {   // main in A
        System.out.println("Main of A");
    }
}

class B {
    public static void main(String[] args) {   // main in B
        System.out.println("Main of B");
    }
}

public class main {  // main in main
    public static void main(String[] args) {   // main in MyProgram
        System.out.println("Main of MyProgram");
    }
}

// output

javac MyProgram.java
        ↓
  A.class  B.class  MyProgram.class

java A            →  prints "Main of A"
java B            →  prints "Main of B"
java MyProgram    →  prints "Main of MyProgram"
```
## Important File Naming Rule
```java

❗ Only ONE public class allowed per .java file
❗ File name MUST match the public class name

// File: MyProgram.java

public class MyProgram { }   ✅ matches filename
class Helper { }             ✅ non-public, fine
public class Other { }       ❌ ERROR — two public classes in one file

```
## What About Inner Classes?
```java

public class Outer {
    class Inner {               // inner class
        void hello() { }
    }

    static class StaticNested { // static nested class
        void hi() { }
    }
}

// output
javac Outer.java
        ↓
  Outer.class
  Outer$Inner.class          ← $ separates outer$inner
  Outer$StaticNested.class
```
## Anonymous Classes
```java
public class MyProgram {
    public static void main(String[] args) {
        Runnable r = new Runnable() {     // anonymous class
            public void run() {
                System.out.println("Running");
            }
        };

        r.run();   // 🔴 required to execute
    }
}
//output

MyProgram.class
MyProgram$1.class     ← anonymous class gets numbered name


```
## 
```java
┌─────────────────────────────────────────────┐
│                  STREAMS                    │
│                                             │
│   ┌─────────────────┐  ┌─────────────────┐  │
│   │   BYTE STREAM   │  │  CHAR STREAM    │  │
│   │                 │  │                 │  │
│   │ reads/writes    │  │ reads/writes    │  │
│   │ RAW bytes       │  │ CHARACTERS      │  │
│   │ (0s and 1s)     │  │ (text/unicode)  │  │
│   │                 │  │                 │  │
│   │ images, audio,  │  │ .txt files      │  │
│   │ video, binary   │  │ .java files     │  │
│   └─────────────────┘  └─────────────────┘  │
└─────────────────────────────────────────────┘
```

## 1️⃣ Reading from Keyboard — System.in
```java

import java.util.Scanner;

public class Input {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);  // System.in = keyboard stream

        System.out.print("Enter name: ");
        String name = sc.nextLine();           // reads String

        System.out.print("Enter age: ");
        int age = sc.nextInt();                // reads integer

        System.out.println("Name: " + name + ", Age: " + age);

        sc.close();   // always close stream
    }
}
Flow:
Keyboard ──▶ System.in ──▶ Scanner ──▶ your variable
             (byte stream)  (wrapper)

```
## 2️⃣ Reading from a File — FileInputStream (Byte)
```java 

import java.io.*;

public class FileInput {
    public static void main(String[] args) throws IOException {
        FileInputStream fis = new FileInputStream("data.txt");

        int data;
        while ((data = fis.read()) != -1) {   // reads one byte at a time
            System.out.print((char) data);     // cast byte to char
        }

        fis.close();
    }
}

Flow:
data.txt (HDD) ──▶ FileInputStream ──▶ your program
                   (byte by byte)

```

## Writting to Screen - System.out
```java

public class Output {
    public static void main(String[] args) {
        System.out.print("No newline");         // no newline
        System.out.println("With newline");     // adds newline
        System.out.printf("Age: %d", 25);       // formatted output
    }
}

```

```java 

import java.util.Scanner;
// System.in alone — reads raw bytes (rarely used directly)
int x = System.in.read();   // reads one byte

// Wrapped with Scanner — practical usage
Scanner sc = new Scanner(System.in);
String name = sc.nextLine(); // reads String
int age = sc.nextInt(); // reads Integer

```
## @Override
```java 


class Dog {
    String name = "Bruno"; // instance field
    // Object's original toString()
    public String toString() {
        return getClass().getName() + "@" + hashCode();
        // would print something like:  Dog@1b6d3586
    }
    @Override
    // Dog's overridden toString()
    public String toString() {
        return "Dog: " + name;
        // prints:  Dog: Bruno
    }
}
public class main {
    public static void main(String[] args) {
        Dog d = new Dog();
        System.out.println(d.toString());  // Dog: Bruno
        System.out.println(d.getClass());  // class Dog
    }
}


```

## hashCode()
```java


class Dog {
    String name;
    int age;
    Dog(String name, int age) {
        this.name = name;
        this.age = age;
    }
    @Override
    public int hashCode() {        // ✅ allowed
        return name.hashCode() + age;   // based on fields now
    }
}
public class main {

    public static void main(String[] args) {
        Dog d1 = new Dog("Buddy", 5);
        Dog d2 = new Dog("Buddy", 5);
        System.out.println(d1.hashCode());  // 64537259
        // will print a hash code based on name and age
        System.out.println(d2.hashCode());  // 64537259 (same as d1)
        // will print the same hash code as d1 since they have the same name and age
    }
}


@ Withour Override

Dog d1 = new Dog("Bruno", 3);
Dog d2 = new Dog("Bruno", 3);

// WITHOUT override
d1.hashCode();   // e.g. 123456  ← memory based
d2.hashCode();   // e.g. 789012  ← different — different objects
                // even though d1 and d2 have the same name and age

// WITH override
d1.hashCode();   // same value  ← content based
d2.hashCode();   // same value  ← same name + age = same hash


```


## equal()
```java 


class Dog {
    String name;
    int age;

    // Object's default — compares memory address (reference)
    public boolean equals(Object obj) {
        return (this == obj);    // true only if same object in heap
    }
    @Override
    public boolean equals(Object obj) {    // ✅ allowed
        if (this == obj) return true;      // same reference
        if (obj == null) return false;     // null check
        if (getClass() != obj.getClass()) return false;  // same class?
        Dog other = (Dog) obj;             // cast
        return this.name.equals(other.name) && this.age == other.age;
    }
}

@ Why Overide

Dog d1 = new Dog("Bruno", 3);
Dog d2 = new Dog("Bruno", 3);

// WITHOUT override
d1.equals(d2);   // false ← compares memory address, different objects

// WITH override
d1.equals(d2);   // true  ← compares name and age, same content

@ Golden Rule — Always Override Both Together
if you override equals()  →  you MUST override hashCode()
if you override hashCode() →  you SHOULD override equals()

@ Why?
// Contract:
// if a.equals(b) is true
// then a.hashCode() == b.hashCode() MUST also be true

// if you break this — HashMap, HashSet will behave wrongly
Dog d1 = new Dog("Bruno", 3);
Dog d2 = new Dog("Bruno", 3);

d1.equals(d2)      // true  — you overrode equals
d1.hashCode()      // 123456
d2.hashCode()      // 789012  ← different! — you forgot hashCode

// now HashMap breaks — d1 and d2 go into different buckets
// even though they are "equal"

@ Final Summary

java.lang.Object
├── getClass()   →  final  →  ❌ cannot override
├── hashCode()   →  not final  →  ✅ can override — do it for content equality
├── equals()     →  not final  →  ✅ can override — do it for content equality
└── toString()   →  not final  →  ✅ can override — do it for readable output


```
### System Class

```java

public final class System {
    // ── Fields ──────────────────────────────
    public static final InputStream  in;   // standard input
    public static final PrintStream  out;  // standard output
    public static final PrintStream  err;  // standard error

    // ── Constructor ─────────────────────────
    private System() {}                    // cannot instantiate

    // ── Methods ─────────────────────────────

    // time
    public static long currentTimeMillis();
    public static long nanoTime();
    // exit
    public static void exit(int status);
}


// usage
System.out.println("Hello");           // print to console
System.err.println("Error!");          // print error
System.exit(0);                        // terminate program
long time = System.currentTimeMillis();// time in milliseconds
System.gc();                           // request garbage collection

// fast array copy
int[] src  = {1, 2, 3, 4, 5};
int[] dest = new int[5];
System.arraycopy(src, 0, dest, 0, 5);  // very fast copy


@ Fields — the 3 static fields
System
├── in   →  java.io.InputStream   (keyboard / standard input)
├── out  →  java.io.PrintStream   (console / standard output)
└── err  →  java.io.PrintStream   (console / standard error — prints in red)
```

## Identity Hash
```java 


class Student {
    int id;
    Student(int id) {
        this.id = id;
    }
    @Override
    public int hashCode() {
        return 100;   // forced same hash for all objects
    }
}
public class main {
    public static void main(String[] args) {
        Student s1 = new Student(1);
        Student s2 = new Student(2);

        System.out.println("hashCode:");
        System.out.println(s1.hashCode()); // 100
        System.out.println(s2.hashCode()); // 100

        System.out.println("\nidentityHashCode:");  
        // returns original Object hashCode — even if overridden
        System.out.println(System.identityHashCode(s1)); // 622488023
        System.out.println(System.identityHashCode(s2)); // 1933863327
    }
}

@ What Exatly It Is ?
System.out.println("Hello");
  │      │    └── method of PrintStream
  │      └── static field of System class (type: PrintStream)
  └── System class (java.lang)

```

## Inheritance Tree

```java 

java.lang.Object
└── java.io.OutputStream
        └── java.io.FilterOutputStream
                └── java.io.PrintStream        ← System.out / System.err


java.lang.Object
└── java.io.InputStream                        ← System.in
        └── (many subclasses)

```

## How String is Special

```java 

    // normal object creation
    String s1 = new String("hello");   // creates object in heap

    // special shortcut — only String has this
    String s2 = "hello";               // goes to String Pool

    @String Pool
    Heap
    ├── String Pool (special area)
    │       ├── "hello"    ← s2 points here
    │       ├── "world"      
    │
    └── regular heap
            └── new String("hello")   ← s1 points here (separate object)


    @ String Pool (special memory in Heap):

    String a = "Hello";    →  stored in String Pool
    String b = "Hello";    →  reuses SAME object from pool
    String c = new String("Hello"); → creates NEW object in Heap

    a == b       →  true  (same pool object)
    a == c       →  false (different object)
    a.equals(c)  →  true  (same content)


@ Full Ownership Tree

java.lang
└── final class String
        │
        ├── implements Serializable
        ├── implements Comparable<String>
        └── implements CharSequence
        │
        ├── fields
        │     ├── private final char[] value
        │     └── private int hash
        │
        └── methods
              ├── length(), isEmpty(), isBlank(), charAt()
              ├── indexOf(), lastIndexOf(), contains()
              ├── startsWith(), endsWith()
              ├── substring(), split(), toCharArray()
              ├── toUpperCase(), toLowerCase(), trim(), strip()
              ├── replace(), replaceAll(), concat()
              ├── equals(), equalsIgnoreCase(), compareTo()
              ├── valueOf(), format(), join()     ← static
              └── toString(), hashCode(), intern()

```

## Scanner Class
```java 

@ What It Can Read From
// 1. keyboard — most common
Scanner sc = new Scanner(System.in);

// 2. String
Scanner sc = new Scanner("hello 42 3.14");

// 3. File
Scanner sc = new Scanner(new File("data.txt"));

// 4. InputStream
Scanner sc = new Scanner(System.in);


@ How Scannner Tokenizes

Input:  "42  hello  3.14"
         ↓
Scanner splits by whitespace (default delimiter)
         ↓
tokens:  ["42", "hello", "3.14"]
         ↓
nextInt()     → 42
next()        → "hello"
nextDouble()  → 3.14

@ Full Ownership Tree

java.util
└── final class Scanner
        │
        ├── implements Iterator<String>
        └── implements Closeable
        │
        ├── constructors
        │     ├── Scanner(InputStream)   ← System.in
        │     ├── Scanner(String)
        │     ├── Scanner(File)
        │     └── Scanner(Path)
        │
        └── methods
              ├── nextInt(), nextLong(), nextDouble()     ← read primitives
              ├── nextFloat(), nextBoolean()
              ├── next(), nextLine()                      ← read strings
              ├── hasNext(), hasNextInt(), hasNextLine()  ← check before read
              ├── useDelimiter(), delimiter()             ← delimiter control
              └── close(), reset(), skip()               ← misc

```
## Classificatio of methods
```java 

Methods in Java
├── Built-in Methods   (provided by Java libraries)
└── User-Defined Methods
        ├── No Input,  No Output
        ├── No Input,  With Output
        ├── With Input, No Output
        └── With Input, With Output

```
## Part 1 — Built-in Methods
``` java 

@ String Methods

String s = "hello world";

s.length();           // 11
s.toUpperCase();      // "HELLO WORLD"
s.substring(0, 5);    // "hello"
s.contains("world");  // true
s.replace("world", "java"); // "hello java"
s.trim();             // removes leading/trailing spaces
s.split(" ");         // ["hello", "world"]
s.charAt(1);          // 'e'
s.indexOf("o");       // 4

[access modifier] [static] [return type] methodName([parameters]) {
    // body
    [return value;]
}

Caller ────────────────────► Method
                              (does something internally)
Caller ◄──────────────────── (nothing returned)

static void methodName() {
    // body — no parameters, no return
}

```
## Deep Memory Execution in java

```java 

public class Greeting {

    static void wishing() {
        System.out.println("Good Morning!");
        System.out.println("Welcome to Java!");
    }

    public static void main(String[] args) {
        System.out.println("Program Started");
        wishing();
        System.out.println("Program Ended");
    }
}

@ JVM Memory Architecture

┌─────────────────────────────────────────────────────────────┐
│                        JVM MEMORY                           │
├──────────────────┬──────────────────┬───────────────────────┤
│   METHOD AREA    │   STACK MEMORY   │     HEAP MEMORY       │
│                  │                  │                       │
│ • Class metadata │ • Stack Frames   │ • Objects             │
│ • Bytecode       │ • Local vars     │ • Arrays              │
│ • Static data    │ • LIFO order     │ • String pool         │
│ • Constants      │                  │                       │
│                  │                  │                       │
│ (Loaded once,    │ (Per method      │ (Shared, GC managed)  │
│  shared by all)  │  call)           │                       │
└──────────────────┴──────────────────┴───────────────────────┘


1️⃣ Load only required classes dynamically ✅ (Actual behavior)

class A {
    static {
        System.out.println("A loaded");
    }
}

class B {
    static {
        System.out.println("B loaded");
    }
}

public class Test {
    public static void main(String[] args) {
        A obj = new A();
    }
}

## Execution Order Summary

| Order | Event                                        | Output          |
|-------|----------------------------------------------|-----------------|
| 1     | JVM loads Test (has `main()`)                | *(nothing)*     |
| 2     | `new A()` encountered → loads `A`            | `"A loaded"`    |
| 3     | `A` object created on Heap                   | —               |
| 4     | `B` never referenced → never loaded          | `"B loaded"` ❌ |


┌─────────────────────────────────────────────────────────────┐
│                  CLASS LOADING STEPS                        │
│                                                             │
│  java Greeting (command)                                    │
│       │                                                     │
│       ▼                                                     │
│  1. Bootstrap ClassLoader                                   │
│     └─► loads java.lang.* (Object, String, System...)       │
│                                                             │
│  2. Application ClassLoader                                 │
│     └─► finds  Greeting.class  (your compiled bytecode)     │
│                                                             │
│  3. Loading → Linking → Initialization                      │
│       │           │            │                            │
│       │           │            └─► static fields set        │
│       │           └─► bytecode verified                     │
│       └─► class metadata stored in METHOD AREA              │
└─────────────────────────────────────────────────────────────┘

╔══════════════════════════════════════════════════════════╗
║                     METHOD AREA                          ║
╠══════════════════════════════════════════════════════════╣
║  Class: Greeting                                         ║
║  ┌─────────────────────────────────────────────┐         ║
║  │ Metadata                                    │         ║
║  │   • class name   : Greeting                 │         ║
║  │   • access       : public                   │         ║
║  │   • superclass   : java.lang.Object         │         ║
║  │   • interfaces   : none                     │         ║
║  ├─────────────────────────────────────────────┤         ║
║  │ Method Table                                │         ║
║  │   • main(String[])  → bytecode reference    │         ║
║  │   • wishing()       → bytecode reference    │         ║
║  ├─────────────────────────────────────────────┤         ║
║  │ Bytecode (stored as instructions)           │         ║
║  │   main()   : getstatic, ldc, invokevirtual  │         ║
║  │              invokestatic, ...              │         ║
║  │   wishing() : getstatic, ldc, invokevirtual │         ║
║  ├─────────────────────────────────────────────┤         ║
║  │ Constant Pool                               │         ║
║  │   #1 → "Program Started"                    │         ║
║  │   #2 → "Good Morning!"                      │         ║
║  │   #3 → "Welcome to Java!"                   │         ║
║  │   #4 → "Program Ended"                      │         ║
║  └─────────────────────────────────────────────┘         ║
╚══════════════════════════════════════════════════════════╝


┌──────────────────────────────────────────────────────────────┐
│                      STACK MEMORY                            │
│                                                              │
│  ┌────────────────────────────────────┐  ◄── TOP (active)    │
│  │        Frame: main()               │                      │
│  │  ┌──────────────────────────────┐  │                      │
│  │  │ Local Variable Table         │  │                      │
│  │  │  slot[0] → args = null ref   │  │                      │
│  │  ├──────────────────────────────┤  │                      │
│  │  │ Operand Stack (working area) │  │                      │
│  │  │  [ empty at start ]          │  │                      │
│  │  ├──────────────────────────────┤  │                      │
│  │  │ Return Address               │  │                      │
│  │  │  → (back to JVM launcher)    │  │                      │
│  │  └──────────────────────────────┘  │                      │
│  └────────────────────────────────────┘                      │
│                                                              │
│  Stack is EMPTY below main (nothing called it from code)     │
└──────────────────────────────────────────────────────────────┘

METHOD AREA  ──────────────────────────────────────────────────
  Greeting.main bytecode now being executed by JVM engine

```
## Phase 3 — Line 1 of main() executes

```java 

System.out.println("Program Started");   // ← executing this

CONTROL FLOW:
  main() operand stack:
    PUSH  →  reference to System.out
    PUSH  →  "Program Started"  (from constant pool)
    CALL  →  println()          (invokevirtual bytecode)

  A temporary frame for println() is pushed onto stack,
  executes, prints, then immediately POPPED.

OUTPUT:  Program Started

@ Stack State During println:
┌────────────────────────────┐  ◄── TOP
│  Frame: println()          │  (very brief, pops immediately)
├────────────────────────────┤
│  Frame: main()             │  (waiting)
└────────────────────────────┘


wishing();   // ← next line in main()

STEP 1: JVM sees  invokestatic  #wishing
        → Looks up wishing() bytecode in METHOD AREA
        → Creates a NEW Stack Frame for wishing()
        → Pushes it on top of the stack

STEP 2: Control transfers FROM main() TO wishing()
        → main() frame is PAUSED (not deleted, just waiting)
        → wishing() frame becomes the ACTIVE frame


╔══════════════════════════════════════════════════════════╗
║                    STACK MEMORY                          ║
║                                                          ║
║  ┌──────────────────────────────────┐  ◄── TOP (ACTIVE)  ║
║  │       Frame: wishing()           │                    ║
║  │  ┌────────────────────────────┐  │                    ║
║  │  │ Local Variable Table       │  │                    ║
║  │  │   (EMPTY — no params,      │  │                    ║
║  │  │    no local variables)     │  │                    ║
║  │  ├────────────────────────────┤  │                    ║
║  │  │ Operand Stack              │  │                    ║
║  │  │   [ working space ]        │  │                    ║
║  │  ├────────────────────────────┤  │                    ║
║  │  │ Return Address             │  │                    ║
║  │  │  → back to main() line 2   │  │                    ║
║  │  └────────────────────────────┘  │                    ║
║  └──────────────────────────────────┘                    ║
║                                                          ║
║  ┌──────────────────────────────────┐  ◄── PAUSED        ║
║  │       Frame: main()              │                    ║
║  │  ┌────────────────────────────┐  │                    ║
║  │  │ Local Variable Table       │  │                    ║
║  │  │  slot[0] → args            │  │                    ║
║  │  ├────────────────────────────┤  │                    ║
║  │  │ Operand Stack              │  │                    ║
║  │  │  [ paused mid-execution ]  │  │                    ║
║  │  ├────────────────────────────┤  │                    ║
║  │  │ Return Address             │  │                    ║
║  │  │  → JVM launcher            │  │                    ║
║  │  └────────────────────────────┘  │                    ║
║  └──────────────────────────────────┘                    ║
╚══════════════════════════════════════════════════════════╝

METHOD AREA:  wishing() bytecode now being read & executed
HEAP:         String literals referenced (not duplicated)

static void wishing() {
    System.out.println("Good Morning!");     // ← line 1
    System.out.println("Welcome to Java!"); // ← line 2
}

@ Line 1 Executes
wishing() operand stack:
  PUSH → System.out reference
  PUSH → "Good Morning!"   (from Heap String Pool)
  CALL → println()         (temporary frame, pops instantly)

OUTPUT:  Good Morning!

@ Line 2 Executes
wishing() operand stack:
  PUSH → System.out reference
  PUSH → "Welcome to Java!"
  CALL → println()         (temporary frame, pops instantly)

OUTPUT:  Welcome to Java!


╔══════════════════════════════════════════════════════════╗
║                WISHING() FRAME DESTROYED                 ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   wishing() had:                                         ║
║    • No local variables  → nothing to clean up           ║
║    • No return value     → nothing to pass back          ║
║    • No objects created  → heap unchanged                ║
║                                                          ║
║   JVM actions:                                           ║
║    1. wishing() frame POPPED from stack                  ║
║    2. Frame memory immediately FREED                     ║
║    3. Return address read → jump back to main()          ║
║    4. main() frame becomes ACTIVE again                  ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

STACK after wishing() returns:

  ┌──────────────────────────────────┐  ◄── TOP (ACTIVE again)
  │       Frame: main()              │
  │   (resumes from where paused)    │
  └──────────────────────────────────┘


System.out.println("Program Ended");   // ← resumes here

main() operand stack:
  PUSH → System.out reference
  PUSH → "Program Ended"
  CALL → println()

OUTPUT:  Program Ended

╔══════════════════════════════════════════════════════════╗
║                  MAIN() FRAME DESTROYED                  ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   main() frame POPPED from stack                         ║
║   Stack is now COMPLETELY EMPTY                          ║
║                                                          ║
║   JVM triggers shutdown sequence:                        ║
║    1. Shutdown hooks run (if any)                        ║
║    2. Garbage Collector does final sweep                 ║
║    3. Method Area cleared (class metadata unloaded)      ║
║    4. Heap memory released back to OS                    ║
║    5. JVM process exits                                  ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝


JVM Start
    │
    ▼
ClassLoader loads Greeting.class
    │
    ▼
Method Area ◄──── stores main(), wishing(), constants, metadata
    │
    ▼
main() Stack Frame CREATED  ──────────────────────┐
    │                                             │
    ▼                                             │
println("Program Started") ── temp frame, pops    │
    │                                             │
    ▼                                             │
wishing() called                                  │
    │                                             │
    ▼                                             │
wishing() Stack Frame CREATED                     │
    │   (main is PAUSED below)                    │
    ▼                                             │
println("Good Morning!") ── temp frame, pops      │
    │                                             │
    ▼                                             │
println("Welcome to Java!") ── temp frame, pops   │
    │                                             │
    ▼                                             │
wishing() hits } ── VOID return                   │
    │                                             │
    ▼                                             │
wishing() Frame DESTROYED ◄── popped from stack   │
    │                                             │
    ▼                                             │
Control returns to main() ────────────────────────┘
    │
    ▼
println("Program Ended") ── temp frame, pops
    │
    ▼
main() hits } ── VOID return
    │
    ▼
main() Frame DESTROYED ◄── stack is now EMPTY
    │
    ▼
JVM Shutdown → Method Area cleared → Heap GC → Process exits


```
## Type 4 [return type + parameters]

```java


java Main  (command)
     │
     ▼
┌──────────────────────────────────────────────────────────────────┐
│                    CLASS LOADING PIPELINE                        │
│                                                                  │
│  LOADING                                                         │
│    Bootstrap ClassLoader → java.lang.* (Object, String, System)  │
│    App ClassLoader       → Main.class                            │
│                          → Calculator.class                      │
│                                                                  │
│  LINKING                                                         │
│    • Bytecode verified                                           │
│    • Symbolic refs resolved                                      │
│    • 'result' field descriptor registered in Method Area         │
│      (descriptor says: name=result, type=int, default=0)         │
│                                                                  │
│  INITIALIZATION                                                  │
│    • No static blocks → nothing to run                           │
│    • Classes READY                                               │
└──────────────────────────────────────────────────────────────────┘

╔══════════════════════════════════════════════════════════════════════╗
║                          METHOD AREA                                 ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  ┌───────────────────────────────────────────────────────────┐       ║
║  │                   Class: Main                             │       ║
║  │                                                           │       ║
║  │  Metadata:                                                │       ║
║  │    class name  : Main                                     │       ║
║  │    access      : public                                   │       ║
║  │    superclass  : java.lang.Object                         │       ║
║  │                                                           │       ║
║  │  Method Table:                                            │       ║
║  │    main(String[]) → bytecode ref                          │       ║
║  │                                                           │       ║
║  │  Constant Pool:                                           │       ║
║  │    #1 → "The sum is: "                                    │       ║
║  │    #2 → Calculator class ref                              │       ║
║  └───────────────────────────────────────────────────────────┘       ║
║                                                                      ║
║  ┌───────────────────────────────────────────────────────────┐       ║
║  │                Class: Calculator                          │       ║
║  │                                                           │       ║
║  │  Metadata:                                                │       ║
║  │    class name  : Calculator                               │       ║
║  │    superclass  : java.lang.Object                         │       ║
║  │                                                           │       ║
║  │  Field Descriptor Table:        ◄── NEW compared to before│       ║
║  │  ┌──────────┬──────┬─────────┬────────────────────────┐   │       ║
║  │  │ Field    │ Type │ Default │ Note                   │   │       ║
║  │  ├──────────┼──────┼─────────┼────────────────────────┤   │       ║
║  │  │ result   │ int  │   0     │ lives in HEAP per obj  │   │       ║
║  │  └──────────┴──────┴─────────┴────────────────────────┘   │       ║
║  │  ← Only the BLUEPRINT is stored here                      │       ║
║  │    Actual value lives in Heap when object is created      │       ║
║  │                                                           │       ║
║  │  Method Table:                                            │       ║
║  │    add(int, int) → bytecode ref                           │       ║
║  │                                                           │       ║
║  │  Bytecode for add():                                      │       ║
║  │    iload_1          ← push a                              │       ║
║  │    iload_2          ← push b                              │       ║
║  │    iadd             ← compute a+b                         │       ║
║  │    dup              ← duplicate result on stack           │       ║
║  │    putfield result  ← store into this.result on HEAP      │       ║
║  │    ireturn          ← return value to caller              │       ║
║  └───────────────────────────────────────────────────────────┘       ║
║                                                                      ║
║  IMPORTANT: 'result' field blueprint is HERE                         ║
║             'result' field value will be on HEAP (inside object)     ║
╚══════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════╗
║                         STACK MEMORY                                 ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  ┌──────────────────────────────────────────┐  ◄── TOP (ACTIVE)      ║
║  │             Frame: main()                │                        ║
║  │                                          │                        ║
║  │  Local Variable Table:                   │                        ║
║  │  ┌───────┬────────────┬────────────────┐ │                        ║
║  │  │ Slot  │   Name     │   Value        │ │                        ║
║  │  ├───────┼────────────┼────────────────┤ │                        ║
║  │  │  [0]  │  args      │  null ref      │ │                        ║
║  │  │  [1]  │ calculator │  (not yet)     │ │                        ║
║  │  │  [2]  │  result    │  (not yet)     │ │◄── local int           ║
║  │  └───────┴────────────┴────────────────┘ │    (different from     ║
║  │                                          │     obj.result!)       ║
║  │  Operand Stack : [ empty ]               │                        ║
║  │  Return Address: → JVM launcher          │                        ║
║  └──────────────────────────────────────────┘                        ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝

HEAP  : empty



    Calculator calculator = new Calculator();

┌─────────────────────────────────────────────────────────────────────┐
│              OBJECT CREATION STEPS — new Calculator()               │
│                                                                     │
│  Step 1: JVM sees 'new' keyword                                     │
│          → Calculates memory needed for Calculator object           │
│          → Object header  +  int result (4 bytes)                   │
│          → Allocates block on HEAP at address 0xAB12                │
│                                                                     │
│  Step 2: Instance variable initialized                              │
│          → result = 0   (int default value)                         │
│          → Written directly into the Heap object                    │
│                                                                     │
│  Step 3: Default constructor runs                                   │
│          → Calculator() { super(); }  (compiler generated)          │
│          → Object fully constructed                                 │
│                                                                     │
│  Step 4: Reference 0xAB12 returned                                  │
│          → Stored in slot[1] (calculator) in main()'s frame         │
└─────────────────────────────────────────────────────────────────────┘

╔══════════════════════════╗       ╔══════════════════════════════════════╗
║    STACK: main() frame   ║       ║             HEAP                     ║
║                          ║       ║                                      ║
║ slot[0] args     = null  ║       ║  ┌────────────────────────────────┐  ║
║                          ║       ║  │     Calculator Object          │  ║
║ slot[1] calculator       ║──────►║  │     address: 0xAB12            │  ║
║         = 0xAB12         ║       ║  │                                │  ║
║                          ║       ║  │  Object Header:                │  ║
║ slot[2] result   = (none)║       ║  │    class pointer → Method Area │  ║
║                          ║       ║  │    hashcode, GC flags          │  ║
╚══════════════════════════╝       ║  │                                │  ║
                                   ║  │  Instance Fields:              │  ║
                                   ║  │  ┌──────────┬───────────────┐  │  ║
                                   ║  │  │  Field   │    Value      │  │  ║
                                   ║  │  ├──────────┼───────────────┤  │  ║
                                   ║  │  │  result  │      0        │  │  ║
                                   ║  │  └──────────┴───────────────┘  │  ║
                                   ║  │  ← default value, not set yet  │  ║
                                   ║  └────────────────────────────────┘  ║
                                   ╚══════════════════════════════════════╝

METHOD AREA: has the blueprint (field descriptor for result)
HEAP:        has the actual value storage (result = 0 right now)



JVM executes: invokevirtual calculator.add(5, 3)

  Step 1: Read slot[1] → gets 0xAB12
  Step 2: Go to Heap → find Calculator object at 0xAB12
  Step 3: Follow class pointer → Method Area → find add() bytecode
  Step 4: Create add() Stack Frame
  Step 5: Fill Local Variable Table:
            slot[0] = this  = 0xAB12  (reference to heap object)
            slot[1] = a     = 5
            slot[2] = b     = 3
  Step 6: Push add() frame on top of stack
  Step 7: main() is PAUSED


╔══════════════════════════════════════════════════════════════════════╗
║                         STACK MEMORY                                 ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  ┌──────────────────────────────────────────┐  ◄── TOP (ACTIVE)      ║
║  │             Frame: add()                 │                        ║
║  │                                          │                        ║
║  │  Local Variable Table:                   │                        ║
║  │  ┌───────┬────────┬──────────────────┐   │                        ║
║  │  │ Slot  │  Name  │   Value          │   │                        ║
║  │  ├───────┼────────┼──────────────────┤   │                        ║ 
║  │  │  [0]  │  this  │  0xAB12 ─────────┼───┼──► Calculator object   ║
║  │  │  [1]  │  a     │  5               │   │    on Heap             ║ 
║  │  │  [2]  │  b     │  3               │   │                        ║
║  │  └───────┴────────┴──────────────────┘   │                        ║ 
║  │                                          │                        ║
║  │  Operand Stack : [ empty → fills soon ]  │                        ║
║  │  Return Address: → main() slot[2]        │                        ║
║  └──────────────────────────────────────────┘                        ║
║                                                                      ║
║  ┌──────────────────────────────────────────┐  ◄── PAUSED            ║
║  │             Frame: main()                │                        ║
║  │                                          │                        ║
║  │  slot[0] args       = null               │                        ║
║  │  slot[1] calculator = 0xAB12             │                        ║
║  │  slot[2] result     = (waiting...)       │                        ║
║  └──────────────────────────────────────────┘                        ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝

i  load  _1
│    │    │
│    │    └──  slot number in Local Variable Table
│    └───────  operation: load (push onto operand stack)
└────────────  data type: i = integer

```

```java 

i  load  _1
│    │    │
│    │    └──  slot number in Local Variable Table
│    └───────  operation: load (push onto operand stack)
└────────────  data type: i = integer


╔═════════════════════════════════════════════════════════════════════╗
║           add() BYTECODE EXECUTION — STEP BY STEP                   ║
╠══════════════════════╦═══════════════════════╦══════════════════════╣
║   Bytecode           ║   Operand Stack       ║   Heap obj 0xAB12    ║
╠══════════════════════╬═══════════════════════╬══════════════════════╣
║                      ║                       ║                      ║
║  iload_1             ║  [ 5 ]                ║  result = 0          ║
║  (push a=5)          ║                       ║  (unchanged)         ║
║                      ║                       ║                      ║
╠══════════════════════╬═══════════════════════╬══════════════════════╣
║                      ║                       ║                      ║
║  iload_2             ║  [ 5, 3 ]             ║  result = 0          ║
║  (push b=3)          ║                       ║  (unchanged)         ║
║                      ║                       ║                      ║
╠══════════════════════╬═══════════════════════╬══════════════════════╣
║                      ║                       ║                      ║
║  iadd                ║  [ 8 ]                ║  result = 0          ║
║  (pop 5,3 push 8)    ║                       ║  (unchanged)         ║
║                      ║                       ║                      ║
╠══════════════════════╬═══════════════════════╬══════════════════════╣
║                      ║                       ║                      ║
║  putfield result     ║  [ ]  ← 8 consumed    ║  result = 8  ✅      ║ 
║  (pop 8, store into  ║                       ║  ← HEAP UPDATED!     ║
║   this.result        ║  uses 'this'=0xAB12   ║                      ║
║   on Heap)           ║  to locate object     ║                      ║
║                      ║                       ║                      ║
╠══════════════════════╬═══════════════════════╬══════════════════════╣
║                      ║                       ║                      ║
║  getfield result     ║  [ 8 ]                ║  result = 8          ║
║  (read this.result   ║  ← 8 pushed from Heap ║  (still 8)           ║
║   from Heap,         ║                       ║                      ║
║   push onto stack)   ║                       ║                      ║
║                      ║                       ║                      ║
╠══════════════════════╬═══════════════════════╬══════════════════════╣
║                      ║                       ║                      ║
║  ireturn             ║  [ ]  ← 8 returned    ║  result = 8          ║
║  (pop 8, pass back   ║                       ║  (persists in object)║
║   to main())         ║                       ║                      ║
║                      ║                       ║                      ║
╚══════════════════════╩═══════════════════════╩══════════════════════╝

          STACK: add() frame                    HEAP: Calculator obj
        ┌──────────────────────┐              ┌─────────────────────┐
        │  slot[0] this=0xAB12 │──────────►   │  address: 0xAB12    │
        │  slot[1] a = 5       │    putfield  │                     │
        │  slot[2] b = 3       │  ──────────► │  result: 0 → 8  ✅  │
        │                      │              │                     │
        │  Operand Stack:      │    getfield  │                     │
        │  [8] ◄───────────────│  ◄────────── │  result: 8          │
        └──────────────────────┘              └─────────────────────┘

        'this' is the BRIDGE between Stack and Heap
         putfield writes TO heap
         getfield reads FROM heap


╔══════════════════════════════════════════════════════════════════════╗
║                    add() FRAME DESTRUCTION                           ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  ireturn executes:                                                   ║
║    1. Value  8  copied to main()'s operand stack                     ║
║    2. add() frame POPPED from stack → GONE FOREVER                   ║
║    3. slot[0] this=0xAB12 → GONE (but heap object SURVIVES)          ║
║    4. slot[1] a=5         → GONE                                     ║
║    5. slot[2] b=3         → GONE                                     ║
║                                                                      ║
║  main() RESUMES:                                                     ║
║    6. Pops 8 from operand stack                                      ║
║    7. Stores 8 into slot[2] (local 'result' in main)                 ║
║                                                                      ║
║  KEY POINT:                                                          ║
║    Stack local 'result' = 8   (in main's frame, slot[2])             ║
║    Heap  obj.result     = 8   (inside Calculator object at 0xAB12)   ║
║    These are TWO SEPARATE storage locations holding same value!      ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```
```java 

╔═══════════════════════════╗      ╔═══════════════════════════════════╗
║    STACK: main() frame    ║      ║             HEAP                  ║
║                           ║      ║                                   ║
║ slot[0] args    = null    ║      ║  ┌─────────────────────────────┐  ║
║                           ║      ║  │   Calculator Object         │  ║
║ slot[1] calculator        ║─────►║  │   address: 0xAB12           │  ║
║         = 0xAB12          ║      ║  │                             │  ║
║                           ║      ║  │  Instance Fields:           │  ║
║ slot[2] result  =  8  ✅  ║      ║  │  ┌─────────┬────────────┐   │  ║
║         ▲                 ║      ║  │  │  result │     8   ✅ │   │  ║
║         │                 ║      ║  │  └─────────┴────────────┘   │  ║
║    local copy             ║      ║  │        ▲                    │  ║
║    (returned value)       ║      ║  └────────┼────────────────────┘  ║
╚═══════════════════════════╝      ║           │                       ║
                                   ║     persists in object            ║
                                   ║     even after add() ended        ║
                                   ╚═══════════════════════════════════╝


TWO 'result' variables — completely independent:
  main.result      = 8   → Stack  (slot[2], primitive int)
  calculator.result = 8  → Heap   (inside object 0xAB12)


System.out.println("The sum is: " + result);

Steps:
  1. JVM reads slot[2] → result = 8   (from Stack)
  2. Concatenates → "The sum is: " + 8 = "The sum is: 8"
  3. New String "The sum is: 8" created on Heap (String Pool)
  4. println() temp frame pushed → executes → POPPED

OUTPUT:  The sum is: 8

╔══════════════════════════════════════════════════════╗
║                       HEAP                           ║
║                                                      ║
║  ┌───────────────────────────────────────────┐       ║
║  │  Calculator Object  (0xAB12)              │       ║
║  │    result = 8                             │       ║
║  └───────────────────────────────────────────┘       ║
║                                                      ║
║  ┌───────────────────────────────────────────┐       ║
║  │  String Pool                              │       ║
║  │    "The sum is: "   → 0xCC01              │       ║
║  │    "The sum is: 8"  → 0xCC02  (new)       │       ║
║  └───────────────────────────────────────────┘       ║
║                                                      ║
╚══════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════╗
║                       JVM SHUTDOWN SEQUENCE                          ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  1. main() hits closing  }                                           ║
║     → main() frame POPPED                                            ║
║     → Stack COMPLETELY EMPTY                                         ║
║                                                                      ║
║  2. slot[1] 'calculator' reference = 0xAB12 is GONE                  ║
║     → Calculator object at 0xAB12 has ZERO references                ║
║     → Object becomes ELIGIBLE for Garbage Collection                 ║
║     → obj.result = 8 inside it will be wiped                         ║
║                                                                      ║
║  3. slot[2] local 'result' = 8 is GONE                               ║
║     → primitive int, no GC needed, just stack memory freed           ║
║                                                                      ║
║  4. Garbage Collector sweeps Heap                                    ║
║     → Calculator object (0xAB12) → FREED                             ║
║     → String objects            → FREED                              ║
║                                                                      ║
║  5. Method Area cleared                                              ║
║     → Calculator class metadata unloaded                             ║
║     → Main class metadata unloaded                                   ║
║                                                                      ║
║  6. JVM process exits                                                ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝



JVM Start
    │
    ▼
ClassLoader
    ├──► Main.class       → Method Area (main() bytecode)
    └──► Calculator.class → Method Area
                               ├── add() bytecode
                               └── field descriptor: result:int (default 0)
    │
    ▼
main() Stack Frame CREATED
    │  slot[0] args       = null
    │  slot[1] calculator = (empty)
    │  slot[2] result     = (empty)
    │
    ▼
 ┌─────────────────────────────────────────────────────────────┐
 │  new Calculator()                                           │
 │    → HEAP allocates Calculator object at 0xAB12             │
 │    → obj.result initialized = 0  (written to HEAP)          │
 │    → reference 0xAB12 stored → main() slot[1]               │
 └─────────────────────────────────────────────────────────────┘
    │
    ▼
 ┌─────────────────────────────────────────────────────────────┐
 │  calculator.add(5, 3)  — invokevirtual                      │
 │    → read slot[1] = 0xAB12                                  │
 │    → go to Heap object → follow class pointer → Method Area │
 │    → add() Stack Frame CREATED                              │
 │         slot[0] this = 0xAB12   ← bridge to Heap            │
 │         slot[1] a    = 5                                    │
 │         slot[2] b    = 3                                    │
 │    → main() PAUSED                                          │
 └─────────────────────────────────────────────────────────────┘
    │
    ▼
 ┌─────────────────────────────────────────────────────────────┐
 │  Inside add() — bytecode trace                              │
 │                                                             │
 │    iload_1      → push 5 onto operand stack                 │
 │    iload_2      → push 3 onto operand stack                 │
 │    iadd         → pop 5,3  push 8                           │
 │    putfield     → pop 8, write to this.result on HEAP       │
 │                   HEAP obj 0xAB12: result = 8 ✅            │
 │    getfield     → read this.result from HEAP, push 8        │
 │    ireturn      → return 8 to main()                        │
 │                                                             │
 │  add() Frame DESTROYED — slot this,a,b all GONE             │
 │  Heap object SURVIVES — result=8 still there                │
 └─────────────────────────────────────────────────────────────┘
    │
    ▼
main() RESUMES
    → 8 received on operand stack
    → stored in slot[2] (local result = 8)
    │
    ▼
 ┌─────────────────────────────────────────────────────────────┐
 │  System.out.println("The sum is: " + result)                │
 │    → reads slot[2] = 8  (from STACK)                        │
 │    → "The sum is: 8" created on HEAP (String Pool)          │
 │    → println() temp frame → prints → POPPED                 │
 └─────────────────────────────────────────────────────────────┘
    │
    ▼
main() Frame DESTROYED → Stack EMPTY
    │
    ▼
'calculator' ref gone → 0xAB12 unreachable → GC eligible
local 'result'=8 gone → primitive freed with stack frame
    │
    ▼
GC sweeps Heap → Calculator object freed → Strings freed
Method Area cleared → JVM exits

╔══════════════════════════════════════════════════════════════════════╗
║            result  vs  result — NEVER CONFUSE THESE                  ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║   Calculator.result (instance variable)                              ║
║   ┌──────────────────────────────────────────────────────────┐       ║
║   │  WHERE  : Heap — inside the Calculator object            │       ║
║   │  WHEN   : Created when 'new Calculator()' runs           │       ║
║   │  DEFAULT: 0  (int default)                               │       ║
║   │  SET BY : putfield inside add() bytecode                 │       ║
║   │  LIVES  : As long as the Calculator object is alive      │       ║
║   │  DIES   : When GC collects the Calculator object         │       ║
║   └──────────────────────────────────────────────────────────┘       ║
║                                                                      ║
║   main.result (local variable)                                       ║
║   ┌──────────────────────────────────────────────────────────┐       ║
║   │  WHERE  : Stack — inside main()'s frame slot[2]          │       ║
║   │  WHEN   : Created when main() frame is pushed            │       ║
║   │  DEFAULT: undefined (must assign before use)             │       ║
║   │  SET BY : return value from add() stored here            │       ║
║   │  LIVES  : Only while main() is executing                 │       ║
║   │  DIES   : When main() frame is popped from stack         │       ║
║   └──────────────────────────────────────────────────────────┘       ║
║                                                                      ║
║   Both hold value  8  at runtime — but in totally different places   ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝


```

## Instance variable
```java 

public class Car {
    // These are INSTANCE VARIABLES
    String brand;
    int speed;
    String color;
}


public class Example {
    public void myMethod() {
        private int x = 10;  // ❌ Compile error: illegal start of expression
        public String name;  // ❌ Compile error
        int y = 20;          // ✅ Correct — no modifier needed
    }
}

public void myMethod() {
    final int MAX = 100;  // ✅ Valid — prevents reassignment
}


public class Car {
    public void accelerate() {
        // These are LOCAL VARIABLES
        int boost = 10;
        String gear = "3rd";
        
        System.out.println("Accelerating in " + gear + " gear");
    }
}

public class Student {
    String name;                      // instance variable
    static String school = "DPS";     // static variable

    Student(String name) {
        this.name = name;
    }

    public static void main(String[] args) {
        Student s1 = new Student("Alice");
        Student s2 = new Student("Bob");
        Student s3 = new Student("Charlie");

        // Each object has its OWN name
        System.out.println(s1.name);    // Alice
        System.out.println(s2.name);    // Bob
        System.out.println(s3.name);    // Charlie

        // All objects SHARE the same school
        System.out.println(s1.school);  // DPS
        System.out.println(s2.school);  // DPS
        System.out.println(s3.school);  // DPS

        // Change via one object — reflects EVERYWHERE
        s1.school = "IPS";

        System.out.println(s1.school);  // IPS ✅
        System.out.println(s2.school);  // IPS ✅  ← changed!
        System.out.println(s3.school);  // IPS ✅  ← changed!
    }
}

STACK                         HEAP
─────                         ────
main() frame:
  s1 ──────────────────────→  [ Object 1 ]
                                 name → "Alice" (String Pool)

  s2 ──────────────────────→  [ Object 2 ]
                                 name → "Bob"   (String Pool)

  s3 ──────────────────────→  [ Object 3 ]
                                 name → "Charlie" (String Pool)


METHOD AREA
  school = "DPS"  ←── all three objects point here (no copy inside object)


s1.school
  ↓
JVM sees "school is static"
  ↓
goes to METHOD AREA → reads "DPS"    ✅

s2.school → same METHOD AREA → "DPS" ✅
s3.school → same METHOD AREA → "DPS" ✅

All three hit the EXACT same memory location



BEFORE:
  METHOD AREA:  school = "DPS"

s1.school = "IPS"
       ↓
JVM sees "school is static"
       ↓
goes directly to METHOD AREA → updates school = "IPS"
(s1 is just the ACCESS PATH — the write happens in Method Area)

AFTER:
  METHOD AREA:  school = "IPS"   ← ONE change, ONE location



```

## Accessing Static Variables — Best Practice

```java 

Same Method Name  +  Different Parameters  =  Method Overloading

┌─────────────────────────────────────────────────────────┐
│              VALID OVERLOADING CRITERIA                 │
├─────────────────────────────────────────────────────────┤
│  1. Number of parameters       add(int a)               │
│                                add(int a, int b)        │
├─────────────────────────────────────────────────────────┤
│  2. Type of parameters         add(int a, int b)        │
│                                add(double a, double b)  │
├─────────────────────────────────────────────────────────┤
│  3. Order of parameter types   add(int a, double b)     │
│                                add(double a, int b)     │
└─────────────────────────────────────────────────────────┘

class Wrong {

    int getValue() {
        return 10;
    }

    // ❌ COMPILE ERROR — differs only in return type
    double getValue() {
        return 10.0;
    }
}

class AlsoWrong {

    void process(int a, int b) { }

    // ❌ NOT overloading — parameter names don't matter, types are same
    void process(int x, int y) { }
}

// Java's own println — massively overloaded
System.out.println(42);
System.out.println(true);
System.out.println("text");
System.out.println(3.14);


// Without overloading — caller forced to cast
double add(double a, double b) { return a + b; }

int result = (int) add(2, 3);   // ugly, loses type safety

// With overloading, each type gets a precise implementation:
int    add(int a, int b)       { return a + b; }
double add(double a, double b) { return a + b; }

int    r1 = add(2, 3);       // clean
double r2 = add(2.0, 3.0);   // clean

byte → short → int → long → float → double
        char ↗


class TypePromo {

    void display(long a) {
        System.out.println("long: " + a);
    }

    public static void main(String[] args) {
        TypePromo t = new TypePromo();

        // No display(int) exists, so int is promoted to long
        t.display(10);   // → long: 10
    }
}




Method Call: add(5, 10)
                  │
                  ▼
    ┌─────────────────────────────┐
    │  Step 1: Exact type match?  │──── YES ──► Call that method
    └─────────────────────────────┘
                  │ NO
                  ▼
    ┌──────────────────────────────────┐
    │  Step 2: Match via promotion?    │──── YES ──► Promote & call
    └──────────────────────────────────┘
                  │ NO
                  ▼
    ┌──────────────────────────────────┐
    │  Step 3: Match via autoboxing?   │──── YES ──► Box/unbox & call
    └──────────────────────────────────┘
                  │ NO
                  ▼
    ┌──────────────────────────────────┐
    │  Step 4: Match via varargs?      │──── YES ──► Use varargs
    └──────────────────────────────────┘
                  │ NO
                  ▼
          ❌ Compile Error:
        "No suitable method found"


class AutoBoxDemo {
    public static void main(String[] args) {

        int a = 10;

        Integer obj = a;   // Autoboxing happens here

        System.out.println(obj);
    }
}

Integer obj = Integer.valueOf(a);
So primitive int → wrapper Integer automatically.

class AutoBoxDemo {
    public static void main(String[] args) {

        Integer a = 10;   // autoboxing
        Integer b = 20;   // autoboxing

        Integer sum = a + b;

        System.out.println(sum);
    }
}

Internal steps:
a → unboxing → int
b → unboxing → int
addition happens
result → boxing → Integer

class AutoBoxDemo {

    static void show(Integer x){
        System.out.println("Wrapper: " + x);
    }

    static void show(int x){
        System.out.println("Primitive: " + x);
    }

    public static void main(String[] args) {
        show(5);
    }
}

Output : Primitive: 5
//Because exact primitive match wins over autoboxing.



class VarDemo {

    void display(int a) {
        System.out.println("Single int: " + a);
    }

    void display(int... nums) {
        System.out.println("Varargs called");
        for (int n : nums) System.out.print(n + " ");
        System.out.println();
    }

    public static void main(String[] args) {
        VarDemo v = new VarDemo();

        v.display(5);        // → Single int: 5  (exact match wins over varargs)
        v.display(1, 2, 3);  // → Varargs called: 1 2 3
    }
}


class main {

    static void show(int... x) {
        System.out.println(x.length);
    }

    public static void main(String[] args) {
        show(); // output : 0   // allowed
        show(null); // not allowed, because null is ambiguous
    }
}

Because internally: show(new int[]{}); // Varargs array created in heap.

❌ Invalid Example
void show(int... x, int y)  // ERROR
Varargs must be last.
show(String name, int... marks) // Valid


class Demo {

    static int sum(int... nums){
        int total = 0;

        for(int n : nums){
            total += n;
        }

        return total;
    }

    public static void main(String[] args) {

        System.out.println(sum(10,20)); // 30
        System.out.println(sum(10,20,30)); // 60
        System.out.println(sum(10,20,30,40)); // 100
    }
}


class main {

    static void show(String... x) {
        if (x == null) {
            System.out.println("x is null");
        } else {
            System.out.println("Length = " + x.length);
        }
    }

    public static void main(String[] args) {

        show();          // Length = 0
        show("Java");    // Lehgth = 1
        show("A", "B");   // Length = 2
        show(null);      // x is null
        show((String[]) null);  // x is null
        show((String) null);    // Length = 1
    }
}
👉 show(null) is ambiguous, so cast it to String or String[] to remove warning.

1️⃣ show();
show(new String[]{});

2️⃣ show("Java");
show(new String[]{"Java"});

3️⃣ show("A","B");
show(new String[]{"A","B"});

4️⃣ show(null);
show((String[]) null);
→ array reference is null

Important Notes for Exam 📝
show()      → empty array
show(null)  → null reference
They are not same.

Memory View
show()       -> x → String[0]
show(null)   -> x → null

class PriorityDemo {

    static void show(long x) {
        System.out.println("Promotion");
    }

    static void show(Integer x) {
        System.out.println("Autoboxing");
    }

    static void show(int... x) {
        System.out.println("Varargs");
    }

    public static void main(String[] args) {
        show(5); // Promotion
    }
}

👉 Final Priority Order
    Exact match
        ↓
    Type Promotion
        ↓
    Autoboxing
        ↓
    Varargs

┌─────────────────────────────────────────────────────────┐
│                  METHOD OVERLOADING                     │
├──────────────────────┬──────────────────────────────────┤
│  Also called         │  Compile-time / Static           │
│                      │  Polymorphism                    │
├──────────────────────┼──────────────────────────────────┤
│  Where resolved      │  By compiler (before runtime)    │
├──────────────────────┼──────────────────────────────────┤
│  Valid differences   │  # of params, type, order        │
├──────────────────────┼──────────────────────────────────┤
│  NOT valid           │  Return type alone, param names  │
├──────────────────────┼──────────────────────────────────┤
│  Resolution order    │  Exact → Promote → Box → Varargs │
└──────────────────────┴──────────────────────────────────┘

| Term                          | Why Method Overloading is called this | Explanation                                               |
| ----------------------------- | ------------------------------------- | --------------------------------------------------------- |
| **Compile-time polymorphism** | Decision made at compile time         | Compiler decides which method to call before program runs |
| **Static polymorphism**       | Behavior fixed at compile time        | No runtime decision; method resolved statically           |
| **False polymorphism**        | Not true runtime polymorphism         | Same method name, but no dynamic behavior                 |
| **Early binding**             | Binding happens early                 | Method call linked during compilation                     |
| **Static binding**            | Binding based on static type          | Compiler binds method using reference type                |
| **Static dispatch**           | Method dispatched statically          | No runtime dispatch like overriding                       |


```

## Parameter passing techniques

```java 

public class PrimitiveDemo {
    public static void modify(int x) {
        x = 100;  // Only modifies the local copy
        System.out.println("Inside method: " + x);  // 100
    }

    public static void main(String[] args) {
        int num = 10;
        modify(num);
        System.out.println("After method: " + num);  // Still 10 ✅
    }
}

main()          modify()
┌─────────┐     ┌─────────┐
│ num = 10│────▶│ x = 10  │  ← copy
└─────────┘     │ x = 100 │  ← only local change
                └─────────┘


class Person {
    String name;
    Person(String name) { 
        this.name = name; 
    }
}

public class ObjectDemo {
    public static void modify(Person p) {
        p.name = "Alice";  // Modifies the ACTUAL object on heap
    }

    public static void main(String[] args) {
        Person person = new Person("Bob");
        modify(person);
        System.out.println(person.name);  // "Alice" — changed! ✅
    }
}

Stack                      Heap
┌──────────────┐           ┌──────────────────┐
│ person  ─────┼──────────▶│ Person{name="Bob"}│
└──────────────┘     ┌────▶└──────────────────┘
┌──────────────┐     │
│ p (copy) ───-┼─────┘    Both point to same object!
└──────────────┘


public static void reassign(Person p) {
    p = new Person("Charlie");  // p now points to a NEW object
    System.out.println("Inside: " + p.name);  // "Charlie"
}

public static void main(String[] args) {
    Person person = new Person("Bob");
    reassign(person);
    System.out.println("Outside: " + person.name);  // Still "Bob" ✅
}

Stack                      Heap
┌──────────────┐           ┌──────────────────────┐
│ person  ─────┼──────────▶│ Person{name="Bob"}   │  ← original
└──────────────┘           └──────────────────────┘

┌──────────────┐           ┌──────────────────────┐
│ p (copy) ────┼──────────▶│Person{name="Charlie"}│ ← new object
└──────────────┘           └──────────────────────┘

public static void modify(int[] arr) {
    arr[0] = 999;      // Modifies original array ✅
}

public static void reassign(int[] arr) {
    arr = new int[]{1, 2, 3};  // Only changes local copy ❌
}

public static void main(String[] args) {
    int[] data = {10, 20, 30};
    modify(data);
    System.out.println(data[0]);  // 999

    reassign(data);
    System.out.println(data[0]);  // Still 999
}




```

## Wrapper Classes
```java
List<int> list = new ArrayList<>();       // ❌ Compile error
List<Integer> list = new ArrayList<>();   // ✅ Works

// T must be an object — primitives aren't allowed
public <T> void print(T value) { ... }


int x = null;       // ❌ Primitives can't be null
Integer x = null;   // ✅ Objects can be null (useful for optional values in DB, APIs)

Integer.parseInt("42");       // String → int
Integer.toBinaryString(10);   // "1010"
Integer.MAX_VALUE;            // 2147483647

Integer a = new Integer(5);
Integer b = new Integer(5);
System.out.println(a == b); // false ❌ — two different objects



Integer a = Integer.valueOf(5);
Integer b = Integer.valueOf(5);
System.out.println(a == b); // true ✅ — same cached object

Integer x = Integer.valueOf(200);
Integer y = Integer.valueOf(200);
System.out.println(x == y); // false — outside cache range, new object



// Simplified version of what Java does internally in valueOf()
public static Integer valueOf(int i) {
    if (i >= -128 && i <= 127) {
        return IntegerCache.cache[i + 128]; // return existing object
    }
    return new Integer(i); // only creates new if outside range
}

Integer x = 5; // autoboxing → compiler converts this to Integer.valueOf(5)

int a = 5;
Integer obj = a;   // compiler does: Integer obj = Integer.valueOf(a);

Integer obj = 10;
int b = obj;       // compiler does: int b = obj.intValue();



// Simplified source of Integer class
public final class Integer extends Number {
    
    private final int value;  // ← the primitive is stored here
    
    // valueOf() sets this field
    private Integer(int value) {
        this.value = value;
    }

    // intValue() just returns that stored primitive
    public int intValue() {
        return value;  // ← literally just this
    }
}



Integer obj = Integer.valueOf(42);  // primitive 42 wrapped inside an object
int x = obj.intValue();             // unwrap → get primitive 42 back
System.out.println(x); // 42


Integer obj = Integer.valueOf(65);

obj.intValue()    // 65      (int)
obj.doubleValue() // 65.0    (double)
obj.floatValue()  // 65.0    (float)
obj.longValue()   // 65L     (long)
obj.byteValue()   // 65      (byte)
obj.shortValue()  // 65      (short)



// Simplified source inside Integer class
public boolean equals(Object obj) {
    if (obj instanceof Integer) {
        return value == ((Integer) obj).intValue();
        //     ↑ my primitive    ↑ extract their primitive → compare
    }
    return false;
}



Integer a = Integer.valueOf(100);
Integer b = Integer.valueOf(100);
System.out.println(a == b);      // true  ✅ (cached range -128 to 127)

Integer x = Integer.valueOf(200);
Integer y = Integer.valueOf(200);
System.out.println(x == y);      // false ❌ (outside cache, different objects)
System.out.println(x.equals(y)); // true  ✅ (always compares value)



Integer.parseInt("42");           // String → int
Integer.valueOf(42);              // int → Integer (uses cache)
Integer.toString(42);             // int → String
Integer.toBinaryString(10);       // "1010"
Integer.toHexString(255);         // "ff"
Integer.toOctalString(8);         // "10"
Integer.max(3, 7);                // 7
Integer.min(3, 7);                // 3
Integer.sum(3, 7);                // 10
Integer.compare(3, 7);            // negative (3 < 7)
Integer.bitCount(7);              // 3 (number of 1-bits in 0111)
Integer.reverse(1);               // reverses bits
Integer.MAX_VALUE;                // 2147483647
Integer.MIN_VALUE;                // -2147483648

Double.parseDouble("3.14");
Double.isNaN(0.0 / 0.0);         // true
Double.isInfinite(1.0 / 0.0);    // true
Double.MAX_VALUE;
Double.MIN_VALUE;                 // smallest positive (not most negative!)


Character.isDigit('5');           // true
Character.isLetter('A');          // true
Character.isLetterOrDigit('_');   // false
Character.isWhitespace(' ');      // true
Character.isUpperCase('A');       // true
Character.isLowerCase('a');       // true
Character.toUpperCase('a');       // 'A'
Character.toLowerCase('A');       // 'a'
Character.getNumericValue('9');   // 9


Boolean.parseBoolean("true");     // true
Boolean.parseBoolean("yes");      // false (only "true" matches, case-insensitive)
Boolean.toString(true);           // "true"
Boolean.logicalAnd(true, false);  // false
Boolean.logicalOr(true, false);   // true
Boolean.logicalXor(true, false);  // true

Wrapper objects carry overhead — they live on the heap, not the stack.

// ❌ Slow — creates thousands of Integer objects on heap
Long sum = 0L;
for (long i = 0; i < 1_000_000; i++) {
    sum += i;   // unboxing + addition + autoboxing every iteration!
}

// ✅ Fast — stays on stack
long sum = 0L;
for (long i = 0; i < 1_000_000; i++) {
    sum += i;
}

Rule of thumb: use primitives for computation, use wrappers when 
the API demands objects (Collections, Generics, nullable fields).



```

## familly ownership tree

```java 

java.lang.Object
    └── java.lang.Number  (abstract)
            ├── Integer
            ├── Long
            ├── Double
            ├── Float
            ├── Byte
            └── Short

java.lang.Object
    ├── Boolean    (separate — not numeric)
    └── Character  (separate — not numeric)




java.lang.Object
│
└── java.lang.Number  (abstract)
        │
        ├── java.lang.Integer
        │       ├── Fields
        │       │     ├── MIN_VALUE = -2,147,483,648
        │       │     ├── MAX_VALUE =  2,147,483,647
        │       │     ├── SIZE     = 32  (bits)
        │       │     ├── BYTES    = 4
        │       │     └── TYPE     = int.class
        │       │
        │       ├── Core Methods (from Number)
        │       │     ├── intValue()
        │       │     ├── longValue()
        │       │     ├── floatValue()
        │       │     ├── doubleValue()
        │       │     ├── byteValue()
        │       │     └── shortValue()
        │       │
        │       ├── Static Utility Methods
        │       │     ├── valueOf(int i)
        │       │     ├── valueOf(String s)
        │       │     ├── parseInt(String s)
        │       │     ├── parseInt(String s, int radix)
        │       │     ├── toBinaryString(int i)
        │       │     ├── toOctalString(int i)
        │       │     ├── toHexString(int i)
        │       │     ├── compare(int x, int y)
        │       │     ├── max(int a, int b)
        │       │     ├── min(int a, int b)
        │       │     └── sum(int a, int b)
        │       │
        │       └── Object Methods (overridden)
        │             ├── equals(Object obj)
        │             ├── hashCode()
        │             ├── toString()
        │             └── compareTo(Integer another)
        │
        ├── java.lang.Long
        │       ├── Fields
        │       │     ├── MIN_VALUE = -9,223,372,036,854,775,808
        │       │     ├── MAX_VALUE =  9,223,372,036,854,775,807
        │       │     ├── SIZE     = 64  (bits)
        │       │     └── BYTES    = 8
        │       │
        │       ├── Core Methods (from Number)
        │       │     ├── intValue()
        │       │     ├── longValue()
        │       │     ├── floatValue()
        │       │     └── doubleValue()
        │       │
        │       └── Static Utility Methods
        │             ├── valueOf(long l)
        │             ├── parseLong(String s)
        │             ├── toBinaryString(long i)
        │             ├── toHexString(long i)
        │             ├── compare(long x, long y)
        │             ├── max(long a, long b)
        │             ├── min(long a, long b)
        │             └── sum(long a, long b)
        │
        ├── java.lang.Double
        │       ├── Fields
        │       │     ├── MIN_VALUE =  4.9E-324
        │       │     ├── MAX_VALUE =  1.7976931348623157E308
        │       │     ├── NaN
        │       │     ├── POSITIVE_INFINITY
        │       │     ├── NEGATIVE_INFINITY
        │       │     ├── SIZE     = 64  (bits)
        │       │     └── BYTES    = 8
        │       │
        │       ├── Core Methods (from Number)
        │       │     ├── intValue()       ← truncates decimal
        │       │     ├── longValue()
        │       │     ├── floatValue()
        │       │     └── doubleValue()    ← direct return
        │       │
        │       └── Static Utility Methods
        │             ├── valueOf(double d)
        │             ├── parseDouble(String s)
        │             ├── isNaN(double v)
        │             ├── isInfinite(double v)
        │             ├── isFinite(double d)
        │             ├── compare(double d1, double d2)
        │             ├── max(double a, double b)
        │             ├── min(double a, double b)
        │             └── sum(double a, double b)
        │
        ├── java.lang.Float
        │       ├── Fields
        │       │     ├── MIN_VALUE =  1.4E-45
        │       │     ├── MAX_VALUE =  3.4028235E38
        │       │     ├── NaN
        │       │     ├── POSITIVE_INFINITY
        │       │     ├── NEGATIVE_INFINITY
        │       │     ├── SIZE     = 32  (bits)
        │       │     └── BYTES    = 4
        │       │
        │       ├── Core Methods (from Number)
        │       │     ├── intValue()
        │       │     ├── longValue()
        │       │     ├── floatValue()     ← direct return
        │       │     └── doubleValue()
        │       │
        │       └── Static Utility Methods
        │             ├── valueOf(float f)
        │             ├── parseFloat(String s)
        │             ├── isNaN(float v)
        │             ├── isInfinite(float v)
        │             ├── compare(float f1, float f2)
        │             ├── max(float a, float b)
        │             ├── min(float a, float b)
        │             └── sum(float a, float b)
        │
        ├── java.lang.Byte
        │       ├── Fields
        │       │     ├── MIN_VALUE = -128
        │       │     ├── MAX_VALUE =  127
        │       │     ├── SIZE     = 8   (bits)
        │       │     └── BYTES    = 1
        │       │
        │       ├── Core Methods (from Number)
        │       │     ├── intValue()
        │       │     ├── longValue()
        │       │     ├── floatValue()
        │       │     └── doubleValue()
        │       │
        │       └── Static Utility Methods
        │             ├── valueOf(byte b)
        │             ├── parseByte(String s)
        │             └── compare(byte x, byte y)
        │
        └── java.lang.Short
                ├── Fields
                │     ├── MIN_VALUE = -32,768
                │     ├── MAX_VALUE =  32,767
                │     ├── SIZE     = 16  (bits)
                │     └── BYTES    = 2
                │
                ├── Core Methods (from Number)
                │     ├── intValue()
                │     ├── longValue()
                │     ├── floatValue()
                │     └── doubleValue()
                │
                └── Static Utility Methods
                      ├── valueOf(short s)
                      ├── parseShort(String s)
                      └── compare(short x, short y)



         Number  (abstract class)
           |
    ┌──────┼──────┬──────┬──────┐
 Integer Long  Double Float  Byte  Short


 java.lang.Object
    └── java.lang.Number  (abstract)
            ├── Integer
            ├── Long
            ├── Double
            ├── Float
            ├── Byte
            └── Short

java.lang.Object
    ├── Boolean    (separate — not numeric)
    └── Character  (separate — not numeric)


public abstract class Number {
    public abstract int     intValue();
    public abstract long    longValue();
    public abstract float   floatValue();
    public abstract double  doubleValue();

    // non-abstract (has default impl)
    public byte  byteValue()  { return (byte)  intValue(); }
    public short shortValue() { return (short) intValue(); }
}

Number n1 = Integer.valueOf(42);
Number n2 = Double.valueOf(3.14);
Number n3 = Long.valueOf(100L);

// call intValue() on any of them — works for all
System.out.println(n1.intValue()); // 42
System.out.println(n2.intValue()); // 3  (truncated)
System.out.println(n3.intValue()); // 100
System.out.println(n1); // 42
System.out.println(n2); // 3.14
System.out.println(n3); // 100


public class Main
{
	public static void main(String[] args) {
		System.out.println("Hello World");

        
		Integer a = 6578;
		Integer b = 6578;
		System.out.println(a.equals(b)); //true
		System.out.println(a == b); // false
		System.out.println(a); // 6578
		System.out.println(a.toString()); // 6578
		System.out.println(a.hashCode()); // 6578
		System.out.println(System.identityHashCode(a)); // 724542711
		System.out.println(a.getClass()); // class java.lang.Integer
		System.out.println(a.getClass().getName()); // java.lang.Integer
		System.out.println(Integer.toHexString(a)); // 19b2
		System.out.println(a.toHexString(a)); // 19b2
		System.out.println(a.floatValue()); // 6578.0
		int x = a.intValue();
		float y = a.floatValue();
		System.out.println(x); // 6578
		System.out.println(y); // 6578.0
		
		Character c1 = Character.valueOf((char)65);
		Character c2 = Character.valueOf((char)65);
		System.out.println(c1==c2); // true
		
		Character c3 = Character.valueOf((char)128);
		Character c4 = Character.valueOf((char)128);
		System.out.println(c3==c4); // false
		
		Character c5 = Character.valueOf((char)127);
		Character c6 = Character.valueOf((char)127);
		System.out.println(c5==c6); // true
		
		Character c7 = Character.valueOf((char)-128);
		Character c8 = Character.valueOf((char)-128);
		System.out.println(c7==c8); // false
		
		
		Boolean b1 = Boolean.valueOf(true);
		Boolean b2 = Boolean.valueOf(true);
		System.out.println(b1==b2); // true
		
		

	}
}

```

```java 

Integer i = 10;
Integer j = 20;
Integer k = i + j;
System.out.println(k); // 30

What actually happens here:
Integer i = 10;        →  autoboxing:   i = Integer.valueOf(10)
Integer j = 20;        →  autoboxing:   j = Integer.valueOf(20)
Integer k = i + j;     →  unboxing both → 10 + 20 = 30 → autobox → Integer.valueOf(30)

Integer a = 10;
Integer b = a;
++a; // a = Integer.valueOf(a.intValue() + 1); 
the result back into a brand-new Integer object and assigns it to a.
System.out.println(a == b);      // false
System.out.println(a.equals(b)); // false


++a; // a = Integer.valueOf(a.intValue() + 1); 
then boxes the result back into a brand-new Integer object and assigns it to 'a'.

Integer a = 10;   →  a ──→ [ 10 ]   (object on heap)
Integer b = a;    →  b ──→ [ 10 ]   (SAME object, both point to it)
++a;

Instead, the JVM translates ++a into this behind the scenes:
a = Integer.valueOf(a.intValue() + 1);

It unboxes a to int, adds 1, then boxes the result back into 
a brand-new Integer object and assigns it to 'a'.



++a  ≡  a = Integer.valueOf(a + 1)
              ↓ unbox → 10+1=11 → rebox
a ──→ [ 11 ]   ← NEW object
b ──→ [ 10 ]   ← old object, unchanged


Integer m = 499;
Integer n = m;
System.out.println(m == n); // true 

Integer m = 499;   →  m ──→ [ 499 ]
Integer n = m;     →  n ──→ [ 499 ]  ← same object as m
m == n             →  same reference → true ✅

Integer a = 10 ;
Integer b = a;
a++; // wrapper class are immutable creates a new object a = 11;
System.out.println(a==b); // false 
System.out.println(a.equals(b)); // false 
System.out.println(a); // 11 (not 10) => it is a new object
System.out.println(b); // 10
		
Integer x = 10;
int y = 20;
int z = x+y;
Integer w = x + y;
System.out.println(z); // 30
System.out.println(w); // 30

x (Integer) ──unbox──→ 10
                         \
                          + ──→ 30 ──→ int z = 30
                         /
y (int) ────────────→ 20

Integer x = 10         int y = 20
     │                       │
     │  (heap object)        │  (stack primitive)
     │                       │
     └──── unbox ────────────┘
           x.intValue()
                │
              10 + 20
                │
               30  ← primitive result
                │
        ┌───────┴────────┐
        │                │
    int z = 30      Integer w = 30
    (no boxing)     Integer.valueOf(30)
                    (autoboxing → heap object)

int a       = 1000;
Integer b   = 1000;
Integer c   = 1000;

a == b   // true  ← primitive vs wrapper → unbox → 1000 == 1000
b == c   // false ← wrapper vs wrapper  → reference check → different objects
a == c   // true  ← primitive vs wrapper → unbox → 1000 == 1000

static void show(int x)     { System.out.println("int"); }
static void show(Integer x) { System.out.println("Integer"); }

Integer a = 10;
Integer b = 20;
show(a + b);   // prints "int" ← a+b unboxes both, result is primitive int
show(a);       // prints "Integer"

Integer a = null;
Integer b = null;
System.out.println(a == b);  // true ✅


```
```java 

🧱 Declaration
int[] arr;          // preferred style
int arr[];          // C-style (valid but discouraged)


🧱 Initialization
// 1. Declare + allocate
int[] arr = new int[5];         // default values: 0

// 2. Declare + allocate + assign
int[] arr = new int[]{1, 2, 3, 4, 5};

// 3. Shorthand literal
int[] arr = {1, 2, 3, 4, 5};




🔁 6. Traversing an Array

int[] arr = {1, 2, 3, 4, 5};

// 1. Classic for loop
for (int i = 0; i < arr.length; i++) {
    System.out.print(arr[i] + " ");
}

// 2. Enhanced for-each (read-only)
for (int x : arr) {
    System.out.print(x + " ");
}

// 3. Java 8+ streams
Arrays.stream(arr).forEach(x -> System.out.print(x + " "));

```

```java

int[] arr = {10, 20, 30, 40, 50};

STACK                        HEAP
┌──────────────┐             ┌────────────────────────────────────────-----─┐
│ arr  → ref   │────────────►│ [header | length=5 | 10 | 20 | 30 | 40 | 50] │
└──────────────┘             └────────────────────────────────────────-----─┘


Array Object Layout in Heap Memory
┌──────────────────────┐
│   Object Header      │  ← 12 bytes (mark word + class pointer)
├──────────────────────┤
│   length field       │  ← 4 bytes (stores arr.length)
├──────────────────────┤
│   element[0]         │  ← index 0
│   element[1]         │  ← index 1
│   element[2]         │  ← index 2
│      ...             │
│   element[n-1]       │  ← last element
└──────────────────────┘

STACK                        HEAP
──────                       ──────────────────────────────────────
                             ┌────────────────────────────────────┐
                             │         OBJECT HEADER              │  ← 12 bytes (mark word + class pointer)
                             │  ┌────────────────────────────┐    │
arr  ──────────────────────► │  │  Mark Word      (8 bytes)  │    │
[reference]                  │  │  hash | GC age | lock info │    │
                             │  ├────────────────────────────┤    │
                             │  │  Class Pointer  (4 bytes)  │    │
                             │  │  → points to int[] metadata│    │
                             │  └────────────────────────────┘    │
                             ├────────────────────────────────────┤
                             │  Array Length:  5      (4 bytes)   │
                             ├────────────────────────────────────┤
                             │  arr[0]  =  10         (4 bytes)   │
                             │  arr[1]  =  20         (4 bytes)   │
                             │  arr[2]  =  30         (4 bytes)   │
                             │  arr[3]  =  40         (4 bytes)   │
                             │  arr[4]  =  50         (4 bytes)   │
                             └────────────────────────────────────┘
                             Total ≈ 8 + 4 + 4 + 20 = 36 bytes
                             (aligned to 40 bytes with padding)




```
## primitive vs object array
```java

Primitive int[]:                    Object Integer[]:

┌───┬───┬───┬───┬───┐              ┌──────┬──────┬──────┬──────┬──────┐
│ 10│ 20│ 30│ 40│ 50│              │ ref0 │ ref1 │ ref2 │ ref3 │ ref4 │
└───┴───┴───┴───┴───┘              └──┬───┴──┬───┴──┬───┴──┬───┴──┬───┘
  values live HERE                    │      │      │      │      │
                                      ▼      ▼      ▼      ▼      ▼
                                    [10]   [20]   [30]   [40]   [50]
                                    objects elsewhere on heap



int[]     primitive = {10, 20, 30};
Integer[] object    = {10, 20, 30};

STACK
┌──────────────────┐
│ primitive → ref  │──────────────────────────────────────────────────┐
│ object    → ref  │─────────┐                                        │
└──────────────────┘         │                                        │
                             │                                        │
HEAP                         ▼                                        ▼

Integer[] object:                           int[] primitive:
┌─────────┬──────┬───────┬───────┬───────┐  ┌─────────┬──────┬────┬────┬────┐
│ Header  │ len=3│ ref_0 │ ref_1 │ ref_2 │  │ Header  │ len=3│ 10 │ 20 │ 30 │
└─────────┴──────┴───┬───┴───┬───┴───┬───┘  └─────────┴──────┴────┴────┴────┘
                     │       │       │                          |
          ┌──────────┘    ┌──┘       └──────────┐               |
          ▼               ▼                     ▼               |
   ┌────────────┐  ┌────────────┐        ┌────────────┐         |
   │ Header     │  │ Header     │        │ Header     │         |
   │ intValue=10│  │ intValue=20│        │ intValue=30│         |
   └────────────┘  └────────────┘        └────────────┘         |
                                                                ▼
   Each Integer object = 16 bytes                 int[] element = 4 bytes each

int[]     a = new int[1000];      
// 12 (header) + 4 (length) + 1000×4 = ~4016 bytes

Integer[] b = new Integer[1000];  
// 12 + 4 + 1000×4 (refs) + 1000×16 (objects) = ~20016 bytes


int[]     primitive = new int[3];     // → [0, 0, 0]   (zeroed by JVM)
Integer[] object    = new Integer[3]; // → [null, null, null]

int[3] after new:             Integer[3] after new:
┌────┬────┬────┐              ┌──────┬──────┬──────┐
│  0 │  0 │  0 │              │ null │ null │ null │
└────┴────┴────┘              └──────┴──────┴──────┘
  values are 0                 references point nowhere (0x00000000)


Integer[] arr = new Integer[3];
arr[0] = 42;
// arr[1] is still null

System.out.println(arr[0] + 1);  // 43  — fine
System.out.println(arr[1] + 1);  // NullPointerException!


Integer[] arr = new Integer[3];

arr[0] = 10;  // autoboxing: JVM calls Integer.valueOf(10) behind the scenes
              // a new Integer object is created on the heap

int x = arr[0];  // unboxing: JVM calls arr[0].intValue()
                 // extracts the int from the Integer object



Integer[] arr = new Integer[4];
arr[0] = 100;   // returns cached object
arr[1] = 100;   // returns SAME cached object → arr[0] == arr[1] is true
arr[2] = 200;   // creates new object
arr[3] = 200;   // creates another new object → arr[2] == arr[3] is false!

System.out.println(arr[0] == arr[1]);  // true  (same cached reference)
System.out.println(arr[2] == arr[3]);  // false (different heap objects)
System.out.println(arr[2].equals(arr[3]));  // true (same value)

```
## parameter passing techniques to methods

```java 

static void doubleAll(int[] arr) {
    for (int i = 0; i < arr.length; i++)
        arr[i] *= 2;
}

public static void main(String[] args) {
    int[] data = {1, 2, 3};
    doubleAll(data);
    System.out.println(Arrays.toString(data)); // [2, 4, 6]
}




@returning 

static int[] buildArray(int n) {
    int[] result = new int[n];
    for (int i = 0; i < n; i++) result[i] = i * i;
    return result;
}

int[] squares = buildArray(5);
// squares = [0, 1, 4, 9, 16]




static void modify(int[] a) {
    a[0] = 10;
}

public static void main(String[] args) {
    int[] arr = {1, 2, 3, 4, 5};
    modify(arr);
    System.out.println(arr[0]); // prints 10
}



STACK (main)              HEAP
┌─────────────────┐       ┌────────┬───┬───┬───┬───┬───┐
│ arr │ ref:0x100 │──────►│ header │ 1 │ 2 │ 3 │ 4 │ 5 │
└─────────────────┘       └────────┴───┴───┴───┴───┴───┘
                           address: 0x100


@ a[0] = 10 executes inside modify()

STACK (main)              HEAP
┌─────────────────┐       ┌────────┬────┬───┬───┬───┬───┐
│ arr │ ref:0x100 │──────►│ header │ 10 │ 2 │ 3 │ 4 │ 5 │
└─────────────────┘       └────────┴────┴───┴───┴───┴───┘
                                ▲     ▲
STACK (modify)                  │     │
┌─────────────────┐             │     └── a[0] = 10 wrote here
│  a  │ ref:0x100 │─────────────┘
└─────────────────┘


@ modify() returns, its stack frame is destroyed

STACK (main)              HEAP
┌─────────────────┐       ┌────────┬────┬───┬───┬───┬───┐
│ arr │ ref:0x100 │──────►│ header │ 10 │ 2 │ 3 │ 4 │ 5 │
└─────────────────┘       └────────┴────┴───┴───┴───┴───┘

  'a' is gone — its stack frame was popped.
  But the heap object remains, with the modified value.


```


```java

static void reassign(int[] arr) {
    arr = new int[]{99, 99, 99}; // creates a NEW array on heap
    // arr now points to the new object, original is unchanged
}

public static void main(String[] args) {
    int[] data = {1, 2, 3};
    reassign(data);
    System.out.println(Arrays.toString(data));
    // Output: [1, 2, 3]  ← original untouched
}

Step 1 — Array created in main()

STACK (main)               HEAP
┌──────────────────┐       ┌────────┬───┬───┬───┐
│ data │ ref:0x100 │──────►│ header │ 1 │ 2 │ 3 │
└──────────────────┘       └────────┴───┴───┴───┘
                             address: 0x100

Step 2 — reassign(data) is called

STACK (main)               HEAP
┌──────────────────┐       ┌────────┬───┬───┬───┐
│ data │ ref:0x100 │──────►│ header │ 1 │ 2 │ 3 │
└──────────────────┘       └────────┴───┴───┴───┘
                                 ▲
STACK (reassign)                 │
┌──────────────────┐             │
│ arr  │ ref:0x100 │─────────────┘
└──────────────────┘

  arr is a COPY of data's address.
  They point to the same heap object — but are independent variables.


```

```java 

Step 3 — arr = new int[]{99, 99, 99} executes

STACK (main)               HEAP
┌──────────────────┐       ┌────────┬───┬───┬───┐
│ data │ ref:0x100 │──────►│ header │ 1 │ 2 │ 3 │  ← completely untouched
└──────────────────┘       └────────┴───┴───┴───┘
                             address: 0x100

STACK (reassign)               HEAP
┌──────────────────┐       ┌────────┬────┬────┬────┐
│ arr  │ ref:0x200 │──────►│ header │ 99 │ 99 │ 99 │  ← new object
└──────────────────┘       └────────┴────┴────┴────┘
                             address: 0x200

  arr's local copy of the address changed from 0x100 → 0x200.
  data still holds 0x100. It has no idea arr was reassigned.


```
```java 
Step 4 — reassign() returns, its stack frame is destroyed

STACK (main)               HEAP
┌──────────────────┐       ┌────────┬───┬───┬───┐
│ data │ ref:0x100 │──────►│ header │ 1 │ 2 │ 3 │
└──────────────────┘       └────────┴───┴───┴───┘

                            ┌────────┬────┬────┬────┐
                            │ header │ 99 │ 99 │ 99 │  ← orphaned!
                            └────────┴────┴────┴────┘
                                address: 0x200
                                no variable points here anymore
                                → eligible for Garbage Collection



static int[] square(int[] arr) {
    int[] result = new int[arr.length];
    for (int i = 0; i < arr.length; i++) {
        result[i] = arr[i] * arr[i];
    }
    return result;
}

public static void main(String[] args) {
    int[] nums  = {1, 2, 3, 4, 5};
    int[] squares = square(nums);
    System.out.println(Arrays.toString(squares));
    // Output: [1, 4, 9, 16, 25]
    System.out.println(Arrays.toString(nums));
    // Output: [1, 2, 3, 4, 5]  ← original unchanged
}


String[] names = {"Alice", "Bob", "Charlie"};

HEAP

names array object:
┌────────────┬──────────┬──────────┬──────────┬──────────┐
│   Header   │ length=3 │  ref_0   │  ref_1   │  ref_2   │
└────────────┴──────────┴────┬─────┴────┬─────┴────┬─────┘
                              │          │          │
               ┌──────────────┘          │          └──────────────┐
               ▼                         ▼                         ▼
         ┌──────────┐             ┌──────────┐             ┌──────────┐
         │ "Alice"  │             │  "Bob"   │             │"Charlie" │
         └──────────┘             └──────────┘             └──────────┘


String[] names = {"Alice", "Bob", "Charlie"};

// Length of the array (how many strings)
System.out.println(names.length);        // 3

// Length of a specific string
System.out.println(names[0].length());   // 5  ("Alice")
System.out.println(names[2].length());   // 7  ("Charlie")



```

## 2d arrays 

```java 


int[][] matrix = new int[3][3];

HEAP — outer array at 0x100
┌─────────┬───────┬──────┬──────┬──────┐
│ header  │ len=3 │ null │ null │ null │
└─────────┴───────┴──────┴──────┴──────┘

  matrix[0] returns null (ref = 0x00000000)
  matrix[0][0] tries to follow null → NullPointerException

HEAP

0x200               0x300               0x400
┌──────┬───┬───┬───┐ ┌──────┬───┬───┬───┐ ┌──────┬───┬───┬───┐
│len=3 │ 0 │ 0 │ 0 │ │len=3 │ 0 │ 0 │ 0 │ │len=3 │ 0 │ 0 │ 0 │
└──────┴───┴───┴───┘ └──────┴───┴───┴───┘ └──────┴───┴───┴───┘
  row 0                row 1                row 2
  All slots are zero-initialized by the JVM.

--------------------------------------------------------------------------------

int[][] matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

STACK (main)
┌────────────────────┐
│ matrix │ ref:0x100 │
└────────────────────┘
         │
         ▼
HEAP — the outer array (int[][]) at 0x100
┌─────────┬────────┬─────────┬─────────┬─────────┐
│ header  │ len=3  │ ref:200 │ ref:300 │ ref:400 │
└─────────┴────────┴────┬────┴────┬────┴────┬────┘
                        │         │          │
         ┌──────────────┘         │          └──────────────┐
         ▼                        ▼                         ▼
    0x200 — row 0               0x300 — row 1             0x400 — row 2
┌──────┬──────┬───┬───┬───┐ ┌──────┬──────┬───┬───┬───┐ ┌──────┬──────┬───┬───┬───┐
│header│ len=3│ 1 │ 2 │ 3 │ │header│ len=3│ 4 │ 5 │ 6 │ │header│ len=3│ 7 │ 8 │ 9 │
└──────┴──────┴───┴───┴───┘ └──────┴──────┴───┴───┴───┘ └──────┴──────┴───┴───┴───┘

  Row arrays are separate heap objects.
  They are NOT contiguous — 0x200, 0x300, 0x400 can be anywhere on the heap.




```
## command line arguments
```java

java MyProgram arg1 arg2 arg3

public static void main(String[] args)

public class PrintAll {
    public static void main(String[] args) {
        for (int i = 0; i < args.length; i++) {
            System.out.println("args[" + i + "] = " + args[i]);
        }
    }
}


$ java PrintAll foo bar baz
args[0] = foo
args[1] = bar
args[2] = baz



```

```java 

public static void main(String[] args) {
    System.out.println(args[0]);   // prints: Alice
    System.out.println(args[1]);   // prints: 25
    String name = args[0];
    String ageAsString = args[1];
    int age = Integer.parseInt(ageAsString);
}





╔══════════════════════════════════════════════════════════════════════════════════════════╗
║                        COMPLETE MEMORY LAYOUT                                           ║
║                   java CommandLineDemo Alice 25                                         ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝


┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                                   STACK MEMORY                                          │
│                          (fixed size, auto managed)                                     │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                         │
│   ┌─────────────────────────────────────────────────────────────────────────────────┐   │
│   │                        main() STACK FRAME                                       │   │
│   ├───────────────────┬─────────────────────────────────────────────────────────────┤   │
│   │  Variable         │  Value stored on stack                                      │   │
│   ├───────────────────┼─────────────────────────────────────────────────────────────┤   │
│   │  args             │  0x200  ──────────────────────────────────────────────────────────► (points to heap)
│   ├───────────────────┼─────────────────────────────────────────────────────────────┤   │
│   │  name             │  0x100  ──────────────────────────────────────────────────────────► (points to heap)
│   ├───────────────────┼─────────────────────────────────────────────────────────────┤   │
│   │  ageAsString      │  0x104  ──────────────────────────────────────────────────────────► (points to heap)
│   ├───────────────────┼─────────────────────────────────────────────────────────────┤   │
│   │  age              │  25     (primitive int, lives HERE, no heap involved)       │   │
│   └─────────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                         │
└─────────────────────────────────────────────────────────────────────────────────────────┘
        │                  │                  │
        │ args=0x200       │ name=0x100       │ ageAsString=0x104
        │                  │                  │
        ▼                  │                  │
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                                    HEAP MEMORY                                          │
│                         (dynamic size, garbage collected)                               │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                         │
│   ADDRESS 0x200                                                                         │
│   ┌─────────────────────────────────────────────────────────┐                           │
│   │               String[] ARRAY OBJECT                     │                           │
│   ├──────────────────────┬──────────────────────────────────┤                           │
│   │  object header       │  (class pointer, GC metadata)    │                           │
│   ├──────────────────────┼──────────────────────────────────┤                           │
│   │  length              │  2                               │                           │
│   ├──────────────────────┼──────────────────────────────────┤                           │
│   │  index [0]           │  0x100  ──────────────────────────────────────────────────────► String "Alice"
│   ├──────────────────────┼──────────────────────────────────┤                           │
│   │  index [1]           │  0x104  ──────────────────────────────────────────────────────► String "25"
│   └─────────────────────────────────────────────────────────┘                           │
│                                                                                         │
│                                                                                         │
│   ADDRESS 0x100                           ADDRESS 0x104                                 │
│   ┌────────────────────────────┐          ┌────────────────────────────┐                │
│   │     String OBJECT "Alice"  │          │     String OBJECT "25"     │                │
│   ├────────────────┬───────────┤          ├────────────────┬───────────┤                │
│   │  object header │ metadata  │          │  object header │ metadata  │                │
│   ├────────────────┼───────────┤          ├────────────────┼───────────┤                │
│   │  value (ref)   │  0x300 ────────►     │  value (ref)   │  0x400 ────────►           │
│   ├────────────────┼───────────┤    │     ├────────────────┼───────────┤    │           │
│   │  hash          │  0        │    │     │  hash          │  0        │    │           │
│   ├────────────────┼───────────┤    │     ├────────────────┼───────────┤    │           │
│   │  length        │  5        │    │     │  length        │  2        │    │           │
│   └────────────────────────────┘    │     └────────────────────────────┘    │           │
│                                     │                                       │           │
│   ADDRESS 0x300                     │     ADDRESS 0x400                     │           │
│   ┌────────────────────────────┐    │     ┌────────────────────────────┐    │           │
│   │   char[] ARRAY  ◄──────────┘    │     │   char[] ARRAY  ◄──────────┘    │           │
│   ├───────┬───────┬───────┬─────┬───┤     ├───────┬───────┬────────────────-┤           │
│   │  [0]  │  [1]  │  [2]  │ [3] │[4]│     │  [0]  │  [1]  │                             │
│   ├───────┼───────┼───────┼─────┼───┤     ├───────┼───────┤                             │
│   │  'A'  │  'l'  │  'i'  │ 'c' │'e'│     │  '2'  │  '5'  │                             │
│   └───────┴───────┴───────┴─────┴───┘     └───────┴───────┘                             │
│                                                                                         │
└─────────────────────────────────────────────────────────────────────────────────────────┘


╔══════════════════════════════════════════════════════════════════════════════════════════╗
║                        HOW EACH LINE OF CODE USES MEMORY                                ║
╠══════════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                         ║
║  String[] args                                                                          ║
║  ─────────────────────────────────────────────────────────────────────────────────────  ║
║  stack: args = 0x200                                                                    ║
║  args is just an address. The actual array lives on heap at 0x200.                      ║
║                                                                                         ║
║  args.length                                                                            ║
║  ─────────────────────────────────────────────────────────────────────────────────────  ║
║  stack → follow 0x200 → reach heap array → read length field → returns 2               ║
║                                                                                         ║
║  args[0]                                                                                ║
║  ─────────────────────────────────────────────────────────────────────────────────────  ║
║  stack → follow 0x200 → reach heap array → read index[0] = 0x100                       ║
║       → follow 0x100 → reach String object "Alice"                                     ║
║                                                                                         ║
║  args[1]                                                                                ║
║  ─────────────────────────────────────────────────────────────────────────────────────  ║
║  stack → follow 0x200 → reach heap array → read index[1] = 0x104                       ║
║       → follow 0x104 → reach String object "25"                                        ║
║                                                                                         ║
║  String name = args[0]                                                                  ║
║  ─────────────────────────────────────────────────────────────────────────────────────  ║
║  stack: name = 0x100   (copies the reference, NOT the object)                           ║
║  now both args[0] and name point to the SAME "Alice" object on heap                     ║
║                                                                                         ║
║  int age = Integer.parseInt(args[1])                                                    ║
║  ─────────────────────────────────────────────────────────────────────────────────────  ║
║  stack → follow 0x104 → read char[] → '2','5' → converts to int 25                     ║
║  stack: age = 25   (primitive, stored directly on stack, no heap address)               ║
║                                                                                         ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝


╔══════════════════════════════════════════════════════════════════════════════════════════╗
║                              REFERENCE CHAIN SUMMARY                                    ║
╠══════════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                         ║
║  args ──► 0x200 (String[])                                                              ║
║               └── [0] ──► 0x100 (String "Alice")                                       ║
║                               └── value ──► 0x300 (char[] {'A','l','i','c','e'})        ║
║               └── [1] ──► 0x104 (String "25")                                          ║
║                               └── value ──► 0x400 (char[] {'2','5'})                   ║
║                                                                                         ║
║  name       ──► 0x100  (same object as args[0], no copy made)                           ║
║  ageAsString──► 0x104  (same object as args[1], no copy made)                           ║
║  age            25     (primitive, lives on stack, no reference at all)                 ║
║                                                                                         ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝


╔══════════════════════════════════════════════════════════════════════════════════════════╗
║                                  KEY RULES                                              ║
╠══════════════════════╦══════════════════════════════════════════════════════════════════╣
║  String              ║  object → always on heap                                        ║
║  int, char, boolean  ║  primitive → always on stack                                    ║
║  args variable       ║  stack reference → holds address of heap array                  ║
║  args[i]             ║  heap reference → holds address of heap String                  ║
║  args[0] == name     ║  both point to same heap object, no duplication                 ║
║  String → char[]     ║  every String internally wraps a char array on heap             ║
╚══════════════════════╩══════════════════════════════════════════════════════════════════╝



public class Hello {
    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Usage: java Hello <name> <age>");
            return;
        }

        String name = args[0];
        int age = Integer.parseInt(args[1]);

        System.out.println("Hello, " + name + "!");
        System.out.println("You are " + age + " years old.");
    }
}

Run: java Hello Alice 25

Output:
        Hello, Alice!
        You are 25 years old.



You type:   java Hello Alice 25

OS splits:  [ "Hello", "Alice", "25" ]
                 ^         ^       ^
              class     arg[0]  arg[1]
              name
              (not passed to args)

JVM internally does something like this:
```

```java

String s0 = new String("Alice");   // heap address: 0x100
String s1 = new String("25");      // heap address: 0x104

String[] args = new String[2];   // heap address: 0x200
args[0] = s0;                    // stores reference 0x100
args[1] = s1;                    // stores reference 0x104

HEAP MEMORY:
-------------------------------------------
Address  | Content
-------------------------------------------
0x100    | String object → "Alice"
0x104    | String object → "25"
0x200    | String[] object → { 0x100, 0x104 }
-------------------------------------------

public static void main(String[] args)
                                ^
                         args holds 0x200
                         (just a reference, not the actual array)

STACK FRAME (main):
--------------------------
| args = 0x200           |   <-- reference to heap array
--------------------------

HEAP:
--------------------------
| 0x200 : String[2]      |
|   [0] = 0x100          |----> "Alice"
|   [1] = 0x104          |----> "25"
--------------------------


========================================================================


                  STACK                              HEAP
                  ─────                              ────
        ┌────────────────────┐             ┌─────────────────────────────────┐
        │ main() frame       │             │  0x200 → String[2]              │
        │                    │             │    index[0] = 0x100             │
        │  args = 0x200 ─────┼────────────►│    index[1] = 0x104             │
        │                    │             │    length   = 2                 │
        │  name = 0x100 ─────┼──────┐      └────────────┬────────────────────┘
        │                    │      │                   │
        │  ageAsString=0x104 ┼───┐  │      ┌────────────▼────────────────────┐
        │                    │   │  └─────►│  0x100 → String "Alice"         │
        │  age = 25          │   │         │   char[] = {'A','l','i','c','e'}│
        │  (primitive, here) │   │         │   length = 5                    │
        └────────────────────┘   │         └─────────────────────────────────┘
                                 │
                                 │         ┌─────────────────────────────────┐
                                 └────────►│  0x104 → String "25"            │
                                           │    char[] = {'2','5'}           │
                                           │    length = 2                   │
                                           └─────────────────────────────────┘

Each String object internally contains:
            - object header  (class pointer, GC metadata)
            - char[] value   (the actual characters)
            - int hash       (cached hash code, default 0)
            - int length     (number of characters)



public class Calculator {
    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Usage: java Calculator <num1> <num2>");
            return;
        }

        try {
            int a = Integer.parseInt(args[0]);
            int b = Integer.parseInt(args[1]);
            System.out.println("Sum     = " + (a + b));
            System.out.println("Product = " + (a * b));
        } catch (NumberFormatException e) {
            System.out.println("Error: arguments must be integers.");
        }
    }
}



class ConvertDemo {
    public static void main(String[] args) {
        int a = Integer.parseInt(args[0]);
        double b = Double.parseDouble(args[1]);
        boolean c = Boolean.parseBoolean(args[2]);

        System.out.println("Int: " + a);
        System.out.println("Double: " + b);
        System.out.println("Boolean: " + c);
    }
}

RUN :
    java ConvertDemo 10 3.14 true



public class Demo {
    public static void main(String[] args) {
        int num = 10;
        System.out.println(num);
    }
}


// This is a single-line comment
int a = 10;

/* This is a
   multi-line comment */
int b = 20;

/**
 * Adds two numbers
 * @param x first number
 * @param y second number
 * @return sum
 */
int add(int x, int y) {
    return x + y;
}

int[] arr = new int[5];

System.out.println(arr.getClass()); // class [I

String[] names = new String[3];
System.out.println(names.getClass()); //class [Ljava.lang.String;

int[]     a = {1};
double[]  b = {1.0};
String[]  c = {"hi"};

System.out.println(a.getClass().getName());   // [I
System.out.println(b.getClass().getName());   // [D
System.out.println(c.getClass().getName());   // [Ljava.lang.String;

int[][] a = new int[3][5];


```

## Jagged Array
```java

int[][] jagged = new int[3][];   // 3 rows, but column size not decided yet
jagged[0] = new int[2];          // row 0 has 2 columns
jagged[1] = new int[4];          // row 1 has 4 columns
jagged[2] = new int[1];          // row 2 has 1 column

jagged[0][0] = 10;
jagged[0][1] = 20;

jagged[1][0] = 1;
jagged[1][1] = 2;
jagged[1][2] = 3;
jagged[1][3] = 4;

jagged[2][0] = 99;

int[][] jagged = {
    {10, 20},
    {1, 2, 3, 4},
    {99}
};

System.out.println(jagged.length);      // 3  → number of rows

System.out.println(jagged[0].length);   // 2  → columns in row 0
System.out.println(jagged[1].length);   // 4  → columns in row 1
System.out.println(jagged[2].length);   // 1  → columns in row 2


int[][] jagged = {
    {10, 20},
    {1, 2, 3, 4},
    {99}
};

for (int i = 0; i < jagged.length; i++) {
    for (int j = 0; j < jagged[i].length; j++) {   // ← jagged[i].length, not fixed
        System.out.print(jagged[i][j] + " ");
    }
    System.out.println();
}


```

```java

class BankAccount {
    private double balance; // hidden

    public double getBalance() {       // controlled read
        return balance;
    }

    public void deposit(double amount) { // controlled write
        if (amount > 0) balance += amount;
    }

    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) balance -= amount;
        else System.out.println("Invalid withdrawal!");
    }
}

// BUGGY — shadowing problem
public void setDog(String breed, float age, int price) {
// local variable assigned to itself! instance variable never updated
    breed = breed;  
    age = age;
    price = price;
}

// CORRECT — this keyword resolves the shadowing
public void setDog(String breed, float age, int price) {
// this.breed = instance variable; breed = local parameter
    this.breed = breed;   
    this.age = age;
    this.price = price;
}

class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        // Without 'this', name = name does nothing useful
        // Java thinks both refer to the parameter
        this.name = name;  // this.name → instance variable
        this.age  = age;   // age (right side) → parameter
    }
}

## Without this
public Person(String name, int age) {
    name = name; // ❌ assigns parameter to itself — instance variable unchanged
    age  = age;  // ❌ same problem — instance variable stays 0/null
}



class Rectangle {
    private double width;
    private double height;
    private String color;

    // Primary constructor — all fields
    public Rectangle(double width, double height, String color) {
        this.width  = width;
        this.height = height;
        this.color  = color;
        System.out.println("Full constructor called");
    }

    // Delegates to primary constructor with default color
    public Rectangle(double width, double height) {
        this(width, height, "white"); // calls the 3-arg constructor
    }

    // Delegates to 2-arg constructor — creates a square
    public Rectangle(double side) {
        this(side, side); // calls the 2-arg constructor
    }

    // No-arg — creates a default unit square
    public Rectangle() {
        this(1.0); // calls the 1-arg constructor
    }
}

Rectangle r1 = new Rectangle();         // → this(1.0) → this(1,1) → this(1,1,"white")
Rectangle r2 = new Rectangle(5.0, 3.0); // → this(5,3,"white")
Rectangle r3 = new Rectangle(4, 6, "red"); // direct


public Rectangle(double side) {
    System.out.println("hello"); // ❌ compile error — this() must be first
    this(side, side);
}


class Dog {
    private String breed;
    private float age;
    private int price;

    public void setDog(String breed, float age, int price) {
        this.breed = breed;
        this.age   = age;
        this.price = price;
    }

    public String getBreed() { return breed; }
    public float  getAge()   { return age;   }
    public int    getPrice() { return price; }

    public void display() {
        // passing current Dog object to Printer class
        Printer p = new Printer();
        p.print(this);        // 'this' = current Dog object
    }
}

class Printer {
    public void print(Dog d) {
        System.out.println("Breed : " + d.getBreed());
        System.out.println("Age   : " + d.getAge());
        System.out.println("Price : " + d.getPrice());
    }
}

class Launch {
    public static void main(String[] args) {
        Dog d1 = new Dog();
        d1.setDog("BullDog", 4.5f, 6500);
        d1.display();   // passes d1 as 'this' to Printer

        Dog d2 = new Dog();
        d2.setDog("Pug", 3.0f, 4000);
        d2.display();   // passes d2 as 'this' to Printer
    }
}

## What Is Happening 
d1.display() is called
    → inside display(), 'this' refers to d1
    → p.print(this) means p.print(d1)
    → Printer receives d1 and prints its data

d2.display() is called
    → inside display(), 'this' refers to d2
    → p.print(this) means p.print(d2)
    → Printer receives d2 and prints its data



class Parent {

    Parent() {
        System.out.println("Parent");
    }
}

class Child extends Parent {

    Child() {
        // super();   // calls parent constructor
        System.out.println("Child");
    }
}

class main {

    public static void main(String[] args) {
        Child d = new Child(); // Parent Child

    }
}


this();   // ✅ first
super();  // ❌ cannot come after

class Dog {
    private String breed;
    private float  age;
    private int    price;

    // returns Dog instead of void
    public Dog setBreed(String breed) {
        this.breed = breed;
        return this;     // returns current object
    }

    public Dog setAge(float age) {
        this.age = age;
        return this;     // returns current object
    }

    public Dog setPrice(int price) {
        this.price = price;
        return this;     // returns current object
    }

    public String getBreed() { return breed; }
    public float  getAge()   { return age;   }
    public int    getPrice() { return price; }
}





class Launch {
    public static void main(String[] args) {

        // Create object and chain all setters + print together
        Dog d = new Dog()
                    .setBreed("BullDog")
                    .setAge(4.5f)
                    .setPrice(6500);

        System.out.println(d.getBreed());
        System.out.println(d.getAge());
        System.out.println(d.getPrice());
    }
}

class Outer {
    private String name = "Outer";

    class Inner {
        private String name = "Inner";

        void display() {
            System.out.println(this.name);       // "Inner"  — inner class field
            System.out.println(Outer.this.name); // "Outer"  — outer class field
        }
    }
}

Outer outer = new Outer();
Outer.Inner inner = outer.new Inner();
inner.display();


class Counter {
    private int count = 0;
    private static int total = 0;

    public void increment() {
        this.count++;  // ✅ valid — instance method has 'this'
        total++;
    }

    public static void reset() {
        // this.count = 0; // ❌ compile error: non-static variable cannot be referenced from static context
        total = 0;         // ✅ valid — static context can access static fields
    }
}

class Demo {
    static int count = 10;

    static void show() {
        System.out.println(count);      // ✅ allowed
        System.out.println(this.count); // ❌ ERROR
        System.out.println(Demo.count); // ✅ also correct
    }
}



class Dog {
    private String breed;
    private float  age;
    private int    price;

    public void setBreed(String breed) {
        this.breed = breed;
    }
    // What JVM actually processes
    public void setBreed(Dog this, String breed) {
        this.breed = breed;
    }
}

// What you write
d1.setBreed("BullDog");

// What JVM actually does
Dog.setBreed(d1, "BullDog");
//           ↑
//     d1 becomes 'this' inside the method



class Demo {
    int x = 10;

    void show() {
        System.out.println(this.x);
    }
    
    // What JVM actually processes
    void show(Demo this) {
    System.out.println(this.x);
    }
}


```

```java

public class Dog {
    String name;
    int age;
    // Compiler inserts: public Dog() {}
}

public class Dog {
    String name;

    public Dog(String name) {   // you defined this
        this.name = name;
    }
    // public Dog() {} => now jvm will not add this implicitly 
    // if i want this i have to define explicitly(must)
}

// Dog d = new Dog(); ← COMPILE ERROR — default constructor is gone


public class Config {
    private int timeout;
    private boolean debug;

    public Config() {
        this.timeout = 30;      // meaningful defaults
        this.debug = false;
    }
}


public class Point {
    private final double x;
    private final double y;

    public Point(double x, double y) {
        this.x = x;
        this.y = y;
    }
}



class Student {
    int rollNo;
    String name;

    // Parameterized Constructor
    Student(int rollNo, String name) {
        this.rollNo = rollNo;
        this.name = name;
    }

    // Copy Constructor
    Student(Student obj) {
        this.rollNo = obj.rollNo;
        this.name = obj.name;
    }

    void display() {
        System.out.println(rollNo + " " + name);
    }
}

public class Main {
    public static void main(String[] args) {
        Student s1 = new Student(101, "Alam");
        Student s2 = new Student(s1);   // copy of s1

        s1.display(); // 101 Alam
        s2.display(); // 101 Alam

        // Modify s2 — s1 should NOT change
        s2.rollNo = 999;
        s1.display(); // 101 Alam  ✅ unchanged
        s2.display(); // 999 Alam
    }
}

class Address {
    String city;
    Address(String city) { this.city = city; }
}

class Student {
    int rollNo;
    Address address;

    Student(int rollNo, Address address) {
        this.rollNo = rollNo;
        this.address = address;        // same reference copied
    }

    // Shallow Copy Constructor
    Student(Student obj) {
        this.rollNo = obj.rollNo;
        this.address = obj.address;    // ⚠️ both point to same Address object
    }
    // Deep Copy Constructor
    Student(Student obj) {
        this.rollNo = obj.rollNo;
        this.address = new Address(obj.address.city);  // ✅ new object created
    }
}

public class Rectangle {
    private double width;
    private double height;
    private String color;

    public Rectangle() {
        this(1.0, 1.0);          // calls Rectangle(double, double)
    }

    public Rectangle(double width, double height) {
        this(width, height, "white");  // calls 3-arg constructor
    }

    public Rectangle(double width, double height, String color) {
        // Single place where actual assignment happens
        this.width  = width;
        this.height = height;
        this.color  = color;
    }
}

class Animal {
    Animal() {   // no-arg constructor exists
        System.out.println("Animal created");
    }
}

class Dog extends Animal {
    Dog() {
        // compiler inserts super() here automatically
        System.out.println("Dog created");
    }
}

class Animal {
    String name;

    Animal(String name) {  // only parameterized constructor
        this.name = name;
    }
    // ❌ no no-arg constructor — Java did NOT auto-generate one
}

class Dog extends Animal {
    Dog() {
        // compiler tries to insert super() here
        // but Animal() doesn't exist → COMPILE ERROR
    }
}

Error: There is no default constructor available in 'Animal'


class Dog extends Animal {
    Dog() {
        super("Unknown"); // ✅ explicitly call the available constructor
        System.out.println("Dog created");
    }

    Dog(String name) {
        super(name);    // ✅ pass the argument up
        System.out.println("Dog created: " + name);
    }
}









class Animal {

    // Step 1 — Parent static field
    static String kingdom = initKingdom();
    static String initKingdom() {
        System.out.println("1. Parent static field initialized");
        return "Animalia";
    }

    // Step 1 — Parent static initializer block
    static {
        System.out.println("2. Parent static initializer block");
    }

    // Step 3 & 4 — Parent instance field
    String type = initType();
    String initType() {
        System.out.println("4. Parent instance field initialized");
        return "Vertebrate";
    }

    // Step 4 — Parent instance initializer block
    {
        System.out.println("5. Parent instance initializer block");
    }

    // Step 5 — Parent constructor
    Animal() {
        System.out.println("6. Parent constructor body");
    }
}

class Dog extends Animal {

    // Step 2 — Child static field
    static String species = initSpecies();
    static String initSpecies() {
        System.out.println("3. Child static field initialized");
        return "Canis lupus";
    }

    // Step 2 — Child static initializer block
    static {
        System.out.println("  (Child static initializer block — same step)");
    }

    // Step 6 & 7 — Child instance field
    String breed = initBreed();
    String initBreed() {
        System.out.println("7. Child instance field initialized");
        return "Labrador";
    }

    // Step 7 — Child instance initializer block
    {
        System.out.println("8. Child instance initializer block");
    }

    // Step 8 — Child constructor
    Dog() {
        super();   // steps 3–6 happen inside here
        System.out.println("9. Child constructor body");
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("--- Creating first Dog ---");
        Dog d1 = new Dog();

        System.out.println("\n--- Creating second Dog ---");
        Dog d2 = new Dog();   // static steps do NOT repeat
    }
}


--- Creating first Dog ---
1. Parent static field initialized
2. Parent static initializer block
3. Child static field initialized
   (Child static initializer block — same step)
4. Parent instance field initialized
5. Parent instance initializer block
6. Parent constructor body
7. Child instance field initialized
8. Child instance initializer block
9. Child constructor body

--- Creating second Dog ---
4. Parent instance field initialized
5. Parent instance initializer block
6. Parent constructor body
7. Child instance field initialized
8. Child instance initializer block
9. Child constructor body


public class Object {
    // The absolute terminus of every constructor chain
    public Object() { }   // native JVM implementation underneath
}

class Animal {
    Animal() {
        super(); // → calls Object()
        System.out.println("Animal");
    }
}

class Dog extends Animal {
    Dog() {
        super(); // → calls Animal()
        System.out.println("Dog");
    }
}

class Labrador extends Dog {
    Labrador() {
        super(); // → calls Dog()
        System.out.println("Labrador");
    }
}

new Labrador();

```

## String
```java

Before Java 9
char[] value; (UTF-16 format => 2 bytes per character)

String s = "Hello";
memory used = 5 characters × 2 bytes = 10 bytes
Even though ASCII characters need only 1 byte.



After Java 9 (Compact Strings)
Java changed internal storage to:

byte[] value;
byte coder;

If all characters fit in Latin-1 range:
String s = "Hello";
memory used = 5 bytes instead of 10 bytes;

If string contains Unicode characters:
String s = "नमस्ते" (2 bytes per character)


String s = "Hello";
s.concat(" World");   // does NOT change s
System.out.println(s); // still prints: Hello

s = s.concat(" World"); // now s points to a new object
System.out.println(s);  // prints: Hello World


public class Test {
    public static void main(String[] args) {

        String s1 = "Java";
        String s2 = "Java";

        String s3 = new String("Java");

        String s4 = s1 + "";

        final String s5 = "Ja";
        final String s6 = "va";

        String s7 = s5 + s6;

        System.out.println(s1 == s2); // true
        System.out.println(s1 == s3); // false
        System.out.println(s1 == s4); // false
        System.out.println(s1 == s7); // true
    }
}


public class Main {
    public static void main(String[] args) {

        String s1 = "Java";

        String s2 = new String("Java");

        String s3 = s2.intern();

        System.out.println(s1 == s2); // false

        System.out.println(s1 == s3); // true

        System.out.println(s2 == s3); // false
    }
}



```

## string buffer
```java

StringBuffer sb = new StringBuffer("Hello");
sb.append(" World");
System.out.println(sb); // Hello World


// Inside JDK source — StringBuffer
public synchronized StringBuffer append(String str) { ... }
public synchronized StringBuffer insert(int offset, String str) { ... }
public synchronized StringBuffer delete(int start, int end) { ... }
public synchronized StringBuffer reverse() { ... }


Thread 1 calls sb.append("A")  ──→  acquires lock
Thread 2 calls sb.append("B")  ──→  BLOCKED, waits
Thread 1 finishes              ──→  releases lock
Thread 2 proceeds              ──→  acquires lock, appends "B"


// StringBuffer internally (inherits from AbstractStringBuilder):
byte[] value;   // the actual character storage (Java 9+)
int count;      // number of characters currently stored


StringBuffer sb = new StringBuffer();
sb.capacity();  // 16 (default)

StringBuffer sb2 = new StringBuffer("Hello");
sb2.capacity(); // 21 (16 + length of "Hello")


StringBuffer sb = new StringBuffer(100); // pre-allocate for 100 chars

StringBuffer sb1 = new StringBuffer();           // empty, capacity 16
StringBuffer sb2 = new StringBuffer("Hello");    // with value = 21
StringBuffer sb3 = new StringBuffer(50);         // empty, capacity 50
StringBuffer sb4 = new StringBuffer(sb2);        // copy of another = 21


StringBuffer sb = new StringBuffer("Java");
sb.append(" is");
sb.append(" fun");
sb.append(2024);         // int
sb.append(true);         // boolean
sb.append('!');          // char
sb.append(3.14);         // double
System.out.println(sb);  // Java is fun2024true!3.14



public synchronized StringBuffer append(String str) {
    toStringCache = null;
    super.append(str);// delegates to AbstractStringBuilder
    return this;
}

StringBuffer sb = new StringBuffer("Java fun");
sb.insert(4, " is");
System.out.println(sb);  // Java is fun

4. delete() — remove a range

Syntax: sb.delete(start, end);

StringBuffer sb = new StringBuffer("Hello Beautiful World");
sb.delete(6, 16);         // removes index 6 to 15
System.out.println(sb);   // Hello World

5. deleteCharAt() — remove one character

Syntax: sb.deleteCharAt(index);

StringBuffer sb = new StringBuffer("Helllo");
sb.deleteCharAt(3);       // removes extra 'l'
System.out.println(sb);   // Hello

6. replace() — overwrite a range

Syntax: sb.replace(start, end, newString);

StringBuffer sb = new StringBuffer("Hello World");
sb.replace(6, 11, "Java");
System.out.println(sb);   // Hello Java

7. reverse() - Swaps characters from both ends.

StringBuffer sb = new StringBuffer("Hello");
sb.reverse();
System.out.println(sb);   // olleH

8. charAt() and setCharAt()

Syntax: sb.charAt(index); => char 
Syntax: sb.setCharAt(index, character); => void

StringBuffer sb = new StringBuffer("Hello");
char c = sb.charAt(1);    // 'e'  — read
sb.setCharAt(0, 'J');     // write
System.out.println(sb);   // Jello

8. indexOf() and lastIndexOf()

Syntax: sb.indexOf("text"); => int(first occur) / -1(not found)
Syntax: sb.lastIndexOf("text"); => int(last occur) / -1(not found)

StringBuffer sb = new StringBuffer("abcabc");
sb.indexOf("b");           // 1 — first occurrence
sb.lastIndexOf("b");       // 4 — last occurrence
sb.lastIndexOf("d");       // -1 - not found



9. substring()

Syntax: sb.substring(start); => String
Syntax: sb.substring(start, end); => String

StringBuffer sb = new StringBuffer("Hello World");
sb.substring(6);           // "World"
sb.substring(0, 5);        // "Hello"

10. length() and capacity()

Syntax: sb.length(); => int
Syntax: sb.capacity(); => int

StringBuffer sb = new StringBuffer("Hello");
sb.length();     // 5  — actual characters stored
sb.capacity();   // 21 — total buffer size


11. ensureCapacity() 

Syntax: sb.ensureCapacity(size); => void

StringBuffer sb = new StringBuffer();  // capacity 16
sb.ensureCapacity(50);                 // now at least 50
// actual new capacity = max(50, 16*2+2) = 50

12. trimToSize()

Syntax: sb.trimToSize(); => void

StringBuffer sb = new StringBuffer(100);
sb.append("Hi");
sb.trimToSize();  // shrinks capacity to match length (2)

13. toString()

Syntax: sb.toString(); => String(immutable) new object

StringBuffer sb = new StringBuffer("Hello");
String s = sb.toString();  // convert to immutable String


14. Important 

StringBuffer sb = new StringBuffer("abcabc");
System.out.println(sb.append("\ne")); 
Output: 
/*
abcabc 
e (next line)
*/




```

```java

15. setLength()    

Syntax: sb.setLength(size); => void;

StringBuilder sb = new StringBuilder("Hello");
sb.setLength(3);
System.out.println(sb); // Hel
System.out.println(sb.length()); // 3
sb.setLength(8);
System.out.println(sb); // Hel
System.out.println(sb.length()); // 8



16. codePointAt()

Syntax: sb.codePointAt(index); => int

StringBuffer sb = new StringBuffer("ABC");
System.out.println(sb.codePointAt(0)); // 65 
// (Unicode 65 0f 'A')


17. contains()

Snytax: sb.contains("text"); => boolean

StringBuffer sb = new StringBuffer("Java Programming");
System.out.println(sb.contains("Java")); // true



18. startsWith() / endsWith()

Syntax: sb.toString().startsWith("text"); => boolean
Syntax: sb.toString().endsWith("text"); => boolean

StringBuffer sb = new StringBuffer("Java Programming");
sb.toString().startsWith("Java"); // true
sb.toString().endsWith("ming"); // true


19. regionMatches()

Syntax: sb.toString().regionMatches(toffset, other, ooffset, len);
                                => boolean

StringBuffer sb = new StringBuffer("JavaProgramming");
System.out.println(
    sb.toString().regionMatches(4, "Programming", 0, 11)
); // true


20. join()

Syntax: String.join(delimiter, elements); => String

String s = String.join("-", "Java", "Python", "C++");
System.out.println(s); // Java-Python-C++

21. split() - is a method of String class

Syntax: str.split(regex); => String[]

String s = "Java-Python-C++";
String[] arr = s.split("-");
for(String x : arr) {
    System.out.println(x);
}
Output:
/*
Java
Python
C++
*/




```

```java

22. trim() / strip()
// Both remove spaces from beginning and end of a string.

Syntax: str.trim(); => String
Syntax: str.strip(); => String

String s = "   Java   ";
System.out.println(s.trim()); // Java
System.out.println(s.strip()); // Java


23. isEmpty() / isBlank()

Syntax: str.isEmpty(); => boolean
Syntax: str.isBlank(); => boolean

String s = "   ";
System.out.println(s.isEmpty()); // false
System.out.println(s.isBlank()); // true


24. toCharArray()

Syntax: str.toCharArray(); => char[]

String s = "JAVA";
char[] arr = s.toCharArray();
for(char ch : arr) {
    System.out.println(ch);
}
Output:
/*
J
A
V
A
*/


25. repeat() 

Syntax: str.repeat(n); => String

String s = "Hi ";
System.out.println(s.repeat(3)); // Hi Hi Hi


26. StringJoiner

Syntax: StringJoiner(CharSequence delimiter)
Syntax: StringJoiner(CharSequence delimiter,
             CharSequence prefix,
             CharSequence suffix)

import java.util.StringJoiner;
class Test {
    public static void main(String[] args) {
        StringJoiner sj =
            new StringJoiner(", ", "[", "]");
        sj.add("A");
        sj.add("B");
        sj.add("C");
        System.out.println(sj); // [A, B, C]
    }
}



```
## inheritance
```java


  IS-A Relationship                  HAS-A Relationship
  (Inheritance)                      (Association)
  -----------------                  ------------------
  Student  "is a"  Human             Student  "has a"  Book
  Plane    "is a"  Vehicle           Plane    "has a"  Engine
  Deer     "is a"  Animal            Deer     "has a"  Heart

  Uses: extends keyword              Uses: object reference inside class



String classes:
                    +--------+
                    | Object |  <-- Parent / Base / Super class
                    +--------+
                    /   |    \
                   /    |     \
              +------+ +------------+ +-------------+
              |String| |StringBuffer| |StringBuilder|  <-- Child/Derived/Sub class
              +------+ +------------+ +-------------+

Wrapper classes:
                    +--------+
                    | Object |
                    +--------+
                    /         \
                   /           \
              +--------+   +---------+  +-----------+
              | Number |   | Boolean |  | Character |
              +--------+   +---------+  +-----------+
              /  | | \ \
             /   | |  \ \
          +----+-----+-------+------+-------+--------+
          |Byte|Short|Integer| Long | Float | Double |
          +----+-----+-------+------+-------+--------+



  +-------+
  | Demo1 |  <-- Parent
  +-------+
      ^
      |
  +-------+
  | Demo2 |  <-- Child
  +-------+

Code:
  class Demo1                      class Launch
  {                                {
    void disp1()                     public static void main(String[] args)
    {                                {
      s.o.p("Learn from Leader");      Demo2 d2 = new Demo2();
    }                                  d2.disp1();  // inherited from Demo1
  }                                    d2.disp2();  // defined in Demo2
                                     }
  class Demo2 extends Demo1         }
  {
    void disp2()
    {
      s.o.p("Pioneering Education");
    }
  }

Output:
  Learn from Leader
  Pioneering Education


  +--------+
  | Demo 1 |
  +--------+
      ^
      |
  +--------+
  | Demo 2 |
  +--------+
      ^
      |
  +--------+
  | Demo 3 |
  +--------+

Code:
  class Demo1                       class Demo2 extends Demo1
  {                                 {
    void disp1()                        void disp2()
    {                                   {
      s.o.p("Learn from leader");       s.o.p("Pioneering Education");
    }                                   }
  }                                 }

  class Demo3 extends Demo2         class Launch
  {                                 {
    void disp3()                        public static void main(String[] args)
    {                                   {
      s.o.p("Work is Worship");             Demo3 d3 = new Demo3();
    }                                       d3.disp1();
  }                                         d3.disp2();
                                            d3.disp3();
                                        }
                                    }

Output:
  Learn from Leader
  Pioneering Education
  Work is Worship


Diagram:
              +-------+
              | Demo1 |
              +-------+
             /    |    \
            /     |     \
      +-------+ +-------+ +-------+
      | Demo2 | | Demo3 | | Demo4 |
      +-------+ +-------+ +-------+

Extended version:
              +-------+
              | Demo1 |
              +-------+
             /    |    \
            /     |     \
      +-------+ +-------+ +-------+
      | Demo2 | | Demo3 | | Demo4 |
      +-------+ +-------+ +-------+
       /   \      /   \      /   \
   +--+ +--+  +--+ +--+  +--+ +--+
   |D5| |D6|  |D7| |D8|  |D9| |D10|
   


Code:
  class Demo1 {}
  class Demo2 extends Demo1 {}
  class Demo3 extends Demo1 {}
  class Demo4 extends Demo1 {}
  class Demo5 extends Demo2 {}
  class Demo6 extends Demo2 {}
  class Demo7 extends Demo3 {}
  class Demo8 extends Demo3 {}
  class Demo9 extends Demo4 {}
  class Demo10 extends Demo4 {}


Diagram:
          +--------+
          | Object |
          +--------+
          /         \
         /           \
    +-------+     +-------+
    | Demo1 |     | Demo2 |
    | i = 9 |     | i = 99|
    +-------+     +-------+
          \         /
           \       /
          +--------+
          | Demo3  |   <-- Which 'i' to use? Ambiguity!
          +--------+


Code (INVALID -- will not compile):
  class Demo1 extends Object { int i = 9;  }
  class Demo2 extends Object { int i = 99; }

  class Demo3 extends Demo1, Demo2    // <-- COMPILATION ERROR
  {
    void disp()
    {
      s.o.p(i);   // Which 'i'? Demo1's 9 or Demo2's 99? Ambiguous!
    }
  }

Solution: Use Interfaces to achieve similar functionality without ambiguity.





Diagram:
      +-------+
      | Demo1 |          Valid parts:  Demo2 extends Demo1  (Single)     [OK]
      +-------+                        Demo3 extends Demo1  (Hierarchical)[OK]
       /     \
      /       \           Invalid part: Demo4 extends Demo2, Demo3
  +-------+ +-------+                  (Multiple Inheritance)            [X]
  | Demo2 | | Demo3 |
  +-------+ +-------+
       \       /
        \     /
       +-------+
       | Demo4 |    <-- This line causes COMPILATION ERROR
       +-------+

Code:
  class Demo1 {}                          // OK
  class Demo2 extends Demo1 {}            // OK
  class Demo3 extends Demo1 {}            // OK
  class Demo4 extends Demo2, Demo3 {}     // COMPILATION ERROR




Diagram:
  class Demo1            class Demo2 extends Demo1
  {                      {
    int x;                 int a;
    int y;                 int b;
  }                      }

  Demo2 d2 = new Demo2(); 

  Stack          Heap
  +----+         +---------------------+
  | d2 |--1000-->| Demo2 object @ 1000 |
  +----+         +---------------------+
                 | x  |  0  | <-- Inherited from Demo1
                 | y  |  0  | <-- Inherited from Demo1
                 | a  |  0  | <-- Declared in Demo2
                 | b  |  0  | <-- Declared in Demo2
                 +---------------------+

Key Point: There is NO separate Demo1 object.
           Parent members live INSIDE the child object's memory block.



Example:
  class AccountHolder
  {
    private:
      int acc_no = 52914;
      int pwd    = 62521;

    public:
      void setAccDetails(int acc_no, int pwd)
      {
        this->acc_no = acc_no;
        this->pwd    = pwd;
      }
      void display()
      {
        s.o.p(acc_no);
        s.o.p(pwd);
      }
  }

  class Hacker extends AccountHolder   // "is-a" AccountHolder
  {
    // No new members
  }



   INVALID:                             VALID:
   --------                             ------
  Hacker h = new Hacker();            Hacker h = new Hacker();
  h.acc_no;  // ERROR                 h.setAccDetails(52914, 62521);
  h.pwd;     // ERROR                 h.display();  // Output: 52914
                                                     //         62521

  Memory layout of Hacker object:
  +---------------------------+
  | AccountHolder part        |
  | (inherited)               |
  |  acc_no | 52914           |
  |  pwd    | 62521           |
  +---------------------------+
  | Hacker part               |
  | (no new members)          |
  +---------------------------+




Case 1 -- Static variables are inherited:
  class Parent {                 class Child extends Parent {}
    static int x = 10;
  }                              public class Launch {
                                   public static void main(String[] args) {
                                     System.out.println(Child.x);
                                   }                // Output: 10
                                 }

Case 2 -- Static methods are inherited:
  class Parent {                 class Child extends Parent {}
    static void disp() {
      System.out.println(       public class Launch {
        "Parent method");          public static void main(String[] args) {
    }                                Child.disp();
  }                                }              // Output: Parent method
                                 }

Key Distinction:
  Instance methods --> can be OVERRIDDEN (runtime polymorphism)
  Static methods   --> can only be HIDDEN (method hiding, not overriding)
                       because they belong to the CLASS, not the object.



================================================================================
SUMMARY TABLE -- ALL 10 RULES
================================================================================

  +------+------------------------+-------------------------------------------+
  | Rule | Type                   | Permitted in Java?                        |
  +------+------------------------+-------------------------------------------+
  |  1   | Single                 | YES                                       |
  |  2   | Multilevel             | YES                                       |
  |  3   | Hierarchical           | YES                                       |
  |  4   | Multiple               | NO  (Diamond Problem / Ambiguity)         |
  |  5   | Hybrid                 | CONDITIONALLY (not if multiple involved)  |
  |  6   | Cyclic                 | NO  (Infinite loop)                       |
  |  7   | Memory Allocation      | Child object contains parent data too     |
  |  8   | Private Members        | Inherited but NOT directly accessible     |
  |  9   | Constructors           | NOT inherited, but executed via super()   |
  | 10   | Static Members         | Inherited, belong to CLASS not object     |
  +------+------------------------+-------------------------------------------+




class Parent {

    static void show() {
        System.out.println("Parent");
    }
}

class Child extends Parent {

    static void show() {
        System.out.println("Child");
    }
}


class Parent {

    static int x = 10;

    static void display() {
        System.out.println("Parent static");
    }

    void show() {
        System.out.println("Parent instance");
    }
}

class Child extends Parent {

    static int x = 20;

    static void display() {
        System.out.println("Child static");
    }

    @Override
    void show() {
        System.out.println("Child instance");
    }
}

public class Main {

    public static void main(String[] args) {

        Parent p = new Child();

        System.out.println(p.x);

        p.display();

        p.show();
    }
}



class Animal {
    String name = "Animal";
}
class Dog extends Animal {
    String name = "Dog";
    void show() {
        System.out.println(super.name);  // "Animal"
        System.out.println(this.name);   // "Dog"
    }
}

class Animal {
    void sound() { System.out.println("Generic sound"); }
}
class Dog extends Animal {
    void sound() {
        super.sound();  // calls Animal's sound()
        System.out.println("Bark");
    }
}

class Animal {
    Animal(String name) {
        System.out.println("Animal: " + name);
    }
}
class Dog extends Animal {
    Dog(String name) {
        super(name);    // <-- MUST be first statement
        System.out.println("Dog: " + name);
    }
}

When a child object is created, constructors run TOP-DOWN.

class A { A() { print("A"); } }
class B extends A { B() { print("B"); } }
class C extends B { C() { print("C"); } }

new C()  -->  Output:
            A constructor      <-- parent first
            B constructor
            C constructor      <-- child last

Flow diagram:
-------------

    new C()
        |
        v
    C() calls super()  -->  B() calls super()  -->  A() runs first
                                                        |
                                                    B() body runs
                                                        |
                                                    C() body runs



class Animal {
    void sound() { System.out.println("Some sound"); }
}
class Dog extends Animal {
    @Override
    void sound() { System.out.println("Bark"); }
}



    Rules for Overriding:
    ─────────────────────
  +──────────────────────────┬────────────────────────────────────────────+
  |  Rule                    |  Detail                                    |
  +──────────────────────────┼────────────────────────────────────────────+
  |  Same method signature   |  Name + parameters must match exactly      |
  |  Access modifier         |  Same or WIDER  (protected -> public OK)   |
  |                          |  Cannot NARROW  (public -> protected BAD)  |
  |  Return type             |  Same OR covariant (subtype allowed)       |
  |  static methods          |  Cannot override -- they are HIDDEN        |
  |  final methods           |  Cannot override -- locked                 |
  |  private methods         |  Cannot override                           |
  +──────────────────────────┴────────────────────────────────────────────+

Covariant Return Type:
──────────────────────
class Animal {
    Animal getInstance() { return new Animal(); }
}
class Dog extends Animal {
    @Override
    Dog getInstance() { return new Dog(); } 
    // Dog is subtype -> OK
}


   @Override ANNOTATION                                                    

  Tells compiler: "this intentionally overrides a parent method."
  If no matching method in parent --> COMPILE ERROR (safety net).

      @Override
      void sond() { } // typo --> compile error caught immediately
      // correction method is void sound()

  Without @Override, a typo creates a NEW method silently

  ┌──────────────────────────────────────────────┐
  │   Upcasting -- implicit, always SAFE         │
  └──────────────────────────────────────────────┘
      Animal a = new Dog();   // Dog stored in Animal reference
                              // happens automatically

      [Dog object] <── referenced by ── Animal a
        ↑
        actual type

  ┌──────────────────────────────────────────────┐
  │  Downcasting -- explicit, can FAIL           │
  └──────────────────────────────────────────────┘

      Animal a = new Dog();
      Dog d = (Dog) a;   //  safe -- actual object IS Dog
      d.bark();         //  works

      Animal a2 = new Cat();
      Dog d2 = (Dog) a2;  //  RUNTIME ClassCastException!

  ┌──────────────────────────────────────────────┐
  │  instanceof -- check before downcasting      │
  └──────────────────────────────────────────────┘

      if (a instanceof Dog) {
          Dog d = (Dog) a;
          d.bark();
      }

  ┌──────────────────────────────────────────────┐
  │  Pattern Matching instanceof  (Java 16+)     │
  └──────────────────────────────────────────────┘
      if (a instanceof Dog d) { // declares AND casts in one step
          d.bark();
      }

  Memory view of upcasting:
  ─────────────────────────
      Stack               Heap
      ─────               ────
      a  ─────────> [ Dog Object          ]
                    [ name   = "Rex"      ]
                    [ breed  = "Labrador" ]   <-- all Dog fields exist
                                                  in memory, but Animal
                                                  reference can't see them


```
```java

class Animal {

    void eat() {
        System.out.println("Eat");
    }
}

class Dog extends Animal {

    void bark() {
        System.out.println("Bark");
    }
}

public class Main {

    public static void main(String[] args) {

        Animal a = new Dog();

        a.eat();

        a.bark(); // ERROR
    }
}
```

---

## Example Covering All Cases

```java id="jlwm2b"

class Animal {

    void eat() {
        System.out.println("Eat");
    }
    void sound() {
        System.out.println("Animal Sound");
    }
}

class Dog extends Animal {

    @Override
    void sound() {
        System.out.println("Dog Bark");
    }
    void bark() {
        System.out.println("Bark");
    }
}

public class Main {

    public static void main(String[] args) {

        Animal a = new Dog();

        a.eat();    // Parent method
        a.sound();  // Overridden method
        a.bark();   // ERROR
    }
}



  +───────────────┬──────────────────────────────┬───────────────────────+
  |               |  Overloading                 |  Overriding           |
  +───────────────┼──────────────────────────────┼───────────────────────+
  |  Where        |  Same class                  |  Parent + Child       |
  |  Signature    |  Different parameters        |  Identical            |
  |  Resolved at  |  Compile time                |  Runtime              |
  |  Also called  |  Static polymorphism         |  Dynamic polymorphism |
  +───────────────┴──────────────────────────────┴───────────────────────+

  +─────────────┬────────────┬──────────────┬──────────┬────────────+
  |  Modifier   | Same Class | Same Package | Subclass | Everywhere |
  +─────────────┼────────────┼──────────────┼──────────┼────────────+
  |  private    |    YES     |     NO       |   NO     |    NO      |
  |  default    |    YES     |     YES      |   NO*    |    NO      |
  |  protected  |    YES     |     YES      |   YES    |    NO      |
  |  public     |    YES     |     YES      |   YES    |    YES     |
  +─────────────┴────────────┴──────────────┴──────────┴────────────+

  * default is accessible in subclass ONLY IF in the same package.

  [!] private members are NOT inherited.
      They exist in memory but child CANNOT access them directly.
      Use getter/setter methods to access private parent fields.
```
```java

  +─────────────────┬──────────────────────────────────────────────+
  |  Usage          |  Effect                                      |
  +─────────────────┼──────────────────────────────────────────────+
  |  final class    |  Cannot be extended  (e.g. String class)     |
  |  final method   |  Cannot be overridden in child class         |
  |  final variable |  Constant -- cannot be reassigned            |
  +─────────────────┴──────────────────────────────────────────────+

  final class MathUtils { }     // no class can extend this
      // class MyMath extends MathUtils { }  → ❌ ERROR

  class Parent {
      final void show() { System.out.println("Parent"); }
  }
  class Child extends Parent {
      // void show() { }  → ❌ Cannot override final method
  }


Real-life analogy (Parent --> Child):
  +------------------+        +---------------------------+
  |     Parent       |        |          Child            |
  +------------------+        +---------------------------+
  | height           |------> | height       } Inherited  |
  | skin-color       |------> | skin-color   }            |
  |                  |        |                           |
  | nose             |------> | nose         }            |
  | eyes             |------> | eyes         } Overridden |
  | hair             |------> | hair         }            |
  | teeth            |------> | teeth        }            |
  |                  |        |                           |
  |                  |        | code         }            |
  |                  |        | rain         } Specialized|
  |                  |        | dance        }            |
  |                  |        | paint        }            |
  |                  |        | kickboxing   }            |
  +------------------+        +---------------------------+


  +---------------------+--------------------------------------------------+
  | Method Type         | Description                                      |
  +---------------------+--------------------------------------------------+
  | Inherited           | Copied from parent, used WITHOUT modification.   |
  |                     | Advantage: Code Reusability                      |
  +---------------------+--------------------------------------------------+
  | Overridden          | Copied from parent, but MODIFIED in child class. |
  |                     | Advantage: Behavior changes per child class      |
  +---------------------+--------------------------------------------------+
  | Specialized         | Brand new method, exists ONLY in child class.    |
  |                     | Advantage: Enhances child class functionality    |
  +---------------------+--------------------------------------------------+


  Components of a class:
  +-------------------------------+
  |           class               |
  |                               |
  | static variables  }           |
  | static blocks     } --> Associated with the TYPE (class)
  | static methods    }           |
  |                               |
  | non-static variables }        |
  | non-static blocks    } --> Associated with the OBJECT (instance)
  | non-static methods   }        |
  |                               |
  | constructors                  |
  +-------------------------------+

--------------------------------------------------------------------------------
1) CLASS LOADER SUBSYSTEM
--------------------------------------------------------------------------------
Performs 3 activities:

  a) LOADING -- Loads class files into the metaspace
     i)   Bootstrap class loader  --> Loads standard JDK classes
     ii)  Extension class loader  --> Loads classes that are extension
                                      of standard core Java classes
     iii) Application/System class loader --> Loads application-specific classes

     * Class loaders work on the DELEGATION HIERARCHY MODEL:
       - Request to load a class is FIRST delegated to its parent class loader
       - It only loads the class if the parent does not find and load it

  b) LINKING -- Performs verification, preparation, and (optionally) resolution
     i)   Verify  --> Bytecode verifier verifies if generated bytecode is proper
                      If class fails verification, a verify error is thrown
     ii)  Prepare --> Memory allocated for static variables, default values assigned
     iii) Resolve --> All symbolic memory references replaced with actual references
                      from method area

  c) INITIALIZATION -- Static variables assigned their original values,
                       static blocks are executed


--------------------------------------------------------------------------------
2) RUNTIME DATA AREA (5 areas)
--------------------------------------------------------------------------------

  1) Method Area    -- class metadata, code for methods/constructors
  2) Heap Area      -- objects, instance variables, static members
  3) Stack Area     -- stack frames for methods, local variables
  4) PC Register    -- address of current instruction being executed
  5) Native Method Stack -- native method information

--------------------------------------------------------------------------------
3) EXECUTION ENGINE (3 components)
--------------------------------------------------------------------------------

The JVM invokes the main() method of the class and executes it using the
execution engine. The execution engine executes the bytecodes loaded into
the memory area using an interpreter and JIT compiler.

  1) Java Interpreter -- Interprets non-hotspot bytecodes to machine code
  2) JIT Compiler     -- Compiles hotspot bytecodes to machine code (faster)
  3) Garbage Collector -- Collects and removes unreferenced objects



class Demo
  {
    static int a = 10, b = 20, c = 30;
    static
    {
      s.o.p("Inside static block");
      a = 100; b = 200; c = 300;
    }
    public static void disp1()
    {
      s.o.p("Inside static method");
      s.o.p(a); s.o.p(b); s.o.p(c);
    }
    int x = 40, y = 50, z = 60;
    {
      s.o.p("Inside non-static block");
      x = 45; y = 55; z = 65;
    }
    public void disp2()
    {
      s.o.p("Inside non-static method");
      s.o.p(a); s.o.p(b); s.o.p(c);
      s.o.p(x); s.o.p(y); s.o.p(z);
    }
     public Demo()
    {
      s.o.p("Inside constructor");
      x = 400; y = 500; z = 600;
    }
    public static void main(String[] args)
    {
      s.o.p("Inside main() method");
      disp1();
    }
  }

```

```java 



class Demo {
    static int a = 10, b = 20, c = 30;
    static {
        System.out.println("Inside static block");
        a = 100;
        b = 200;
        c = 300;
    }
    public static void disp1() {
        System.out.println("Inside static method");
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
    }
    int x = 40, y = 50, z = 60;
    {
        System.out.println("Inside non-static block");
        x = 45;
        y = 55;
        z = 65;
    }
    public void disp2() {
        System.out.println("Inside non-static block");
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        System.out.println(x);
        System.out.println(y);
        System.out.println(z);
        System.out.println("");
    }

    public Demo() {
        System.out.println("Inside constructor");
        x = 400;
        y = 500;
        z = 600;
    }

    public static void main(String[] args) {
        System.out.println("Inside main() method");
        Demo
    }
}

  /*
  Output: 
  Inside static block
  Inside main() method
  Inside static method
  100
  200
  300
  */



class Demo {
    int x = 10;
    {
        System.out.println("Non-static block");
    }
    Demo() {
        System.out.println("Constructor");
    }
    void show() {
        System.out.println("Method");
    }

    public static void main(String[] args) {
        Demo d = new Demo();
        d.show();
    }
}

Steps:
1	Object creation starts
2	x gets default value 0
3	x gets explicit value 10
4	Non-static block executes
5	Constructor executes
6	Object ready
7	show() method executes



  Before Compilation:            After Compilation:
  class Demo                     class Demo extends Object
  {                              {
    {                              public Demo()
      s.o.p("Inside              {
        non-static block");          super();
    }                                s.o.p("Inside non-static block");
    public Demo()                    s.o.p("Inside constructor");
    {                              }
      s.o.p("Inside            }
        constructor");
    }
  }

+-----------------------------+----------------------------------+
  | Static Methods              | Instance Methods                 |
  +-----------------------------+----------------------------------+
  | Do NOT require an object    | Require an object of a class     |
  | to be called. Can be called | to be called. Called ONLY using  |
  | via class name OR object    | object reference.                |
  +-----------------------------+----------------------------------+
  | Can access ONLY static      | Can directly access BOTH static  |
  | variables & methods. Cannot | AND non-static members.          |
  | directly access non-static  |                                  |
  | members.                    |                                  |
  +-----------------------------+----------------------------------+
  | this & super keywords       | this & super keywords CAN be     |
  | CANNOT be used              | used                             |
  +-----------------------------+----------------------------------+
  | Resolved using COMPILE-TIME | Resolved using RUNTIME binding   |
  | (early) binding             | (late binding)                   |
  +-----------------------------+----------------------------------+
  | Generic methods (code that  | Specific methods (code that      |
  | can be shared across all    | operates on instance variables   |
  | instances) -- UTILITY       | of an object) -- INSTANCE        |
  | METHODS                     | METHODS                          |
  | e.g. String.join("-",       | e.g. String str = new String()   |
  |       "Raja","Ram")         |      str.indexOf('u'); // 3      |
  | output: Raja-Ram            |                                  |
  +-----------------------------+----------------------------------+



  +-----------------------------+----------------------------------+
  | Static Variables            | Non-Static Variables             |
  | (Class Variables)           | (Instance Variables / Fields)    |
  +-----------------------------+----------------------------------+
  | Declared within a class,    | Declared within a class, but     |
  | outside a method,           | outside a method, constructor    |
  | constructor, or any block   | or any block WITHOUT the static  |
  | WITH the static keyword     | keyword                          |
  +-----------------------------+----------------------------------+
  | Allocated memory at CLASS   | Allocated memory at OBJECT       |
  | LOADING time. Deallocated   | CREATION time. Deallocated once  |
  | once the class is unloaded  | the object is destroyed          |
  +-----------------------------+----------------------------------+
  | Allocated memory ONLY ONCE  | Allocated memory EVERY TIME an   |
  | throughout the program      | object is created                |
  +-----------------------------+----------------------------------+
  | Accessed WITHOUT creating   | Can ONLY be accessed by creating |
  | an object, by using class   | an object of a class             |
  | name                        |                                  |
  +-----------------------------+----------------------------------+
  | Can be accessed within      | Can be accessed ONLY within      |
  | BOTH static AND non-static  | non-static members of a class    |
  | members                     |                                  |
  +-----------------------------+----------------------------------+
  | Should be SHARED among      | Specific to THAT instance of     |
  | all instances of a class    | the class                        |
  +-----------------------------+----------------------------------+


  +------------------------+----------------------------------+
  | Static Blocks (SIB)    | Instance Blocks (IIB)            |
  +------------------------+----------------------------------+
  | Also called Static     | Also called Instance             |
  | Initialization Block   | Initialization Block             |
  +------------------------+----------------------------------+
  | Executed at CLASS      | Executed at OBJECT CREATION      |
  | LOADING time           | time, before constructor         |
  +------------------------+----------------------------------+
  | Executed ONLY ONCE     | Executed EVERY TIME an object    |
  |                        | is created                       |
  +------------------------+----------------------------------+
  | Can access only STATIC | Can access BOTH static AND       |
  | variables & methods    | non-static members               |
  +------------------------+----------------------------------+
  | super & this keywords  | super & this keywords CAN be     |
  | CANNOT be used         | used                             |
  +------------------------+----------------------------------+
  | Used to initialize     | Used to initialize instance      |
  | static variables &     | variables & execute code every   |
  | execute code before    | time an object is created,       |
  | main()                 | through which constructor        |
  +------------------------+----------------------------------+



class Demo {
    private Demo() {
        System.out.println("Constructor");
    }

    public static void main(String[] args) {
        Demo d = new Demo(); // VALID
    }
}

public class Main {

    public static void main(String[] args) {

        Demo d = new Demo(); // ERROR
    }
}

  class Dog
  {
    private String breed;
    private float age;
    private int price;
    private Dog()   // private constructor
    {
      breed = "Pug"; age = 4.5f; price = 6666;
    }
    public static Dog getInstance()  // factory method (static)
    {
      Dog d = new Dog(); // creates object INSIDE class (allowed)
      return d;
    }
  }

  // In main():
  Dog d = new Dog();          // COMPILE ERROR -- constructor is private
  Dog m = Dog.getInstance();  // OK -- using factory method
  Dog n = Dog.getInstance();  // m and n point to DIFFERENT objects



class Demo {
    private static Demo obj = new Demo();
    private Demo() {
        System.out.println("Object Created");
    }
    public static Demo getObject() {
        return obj;
    }
}

public class Main {
    public static void main(String[] args) {

        Demo d1 = Demo.getObject();

        Demo d2 = Demo.getObject();

        System.out.println(d1 == d2); // true
    }
}
/*
Output:
Object Created
true
*/




```


## Association
```java

  +------------------+-----------------------------------------------+
  | Type             | Description                                   |
  +------------------+-----------------------------------------------+
  | One to One       | 1 object of A  ---->  1 object of B           |
  | One to Many      | 1 object of A  ----> many objects of B        |
  | Many to One      | Many objects of A ---->  1 object of B        |
  | Many to Many     | Many objects of A ----> many objects of B     |
  +------------------+-----------------------------------------------+


Target Object / Main Object / Container Object
-----------------------------------------------
        * The object that HOLDS reference to another object

Dependent Object / Helper Object / Contained Object
----------------------------------------------------
        * The object that is HELD INSIDE the target object



DEPENDENCY INJECTION 
---------------------

   Two ways to perform DEPENDENCY INJECTION:
  +-------------------------+------------------------------------------------+
  | Type                    | When to Use                                    |
  +-------------------------+------------------------------------------------+
  | Constructor Injection   | Dependent object is READY at target creation   |
  | Setter Injection        | Dependent object is NOT READY at creation time |
  +-------------------------+------------------------------------------------+

  Both types can:
    -> Inject a primitive value into an object
    -> Inject an object into another object



ONE-TO-ONE ASSOCIATION   
=======================
In a One-to-One (1:1) Association:
   ->  One object is associated with exactly one object.
   ->  The other object is also associated with exactly one object.

One Person  ------> One Passport
One Passport ------> One Person

Person <--one-to-one-----> Passport

class Passport {
    String passportNumber;
    Passport(String passportNumber) { // construction
        this.passportNumber = passportNumber;
    }
    void displayPassport() {
        System.out.println("Passport Number : "
                            + passportNumber);
    }
}

class Person {
    String name;
    Passport passport;
    Person(String name, Passport passport) {
        this.name = name;
        this.passport = passport;
    }
    void displayPerson() {

        System.out.println("Name : " + name);

        passport.displayPassport();
    }
}


public class Test {
    public static void main(String[] args) {
        Passport p1 = new Passport("IND12345"); 
                // dependent object is ready


        // Constrctor Injection
        Person person = new Person("Rahul", p1);

        person.displayPerson();
    }
}

class Employee {

    String name;
    Address address;
}

class Address {

    String city;
    Employee employee;
}

MANY-TO-ONE ASSOCIATION       
=======================
Definition:
    MANY objects of one entity map to ONE object of another entity.

Real Life Example:
Many Employees  ------> One Department
Many Students   ------> One College
Many Customers  ------> One Bank
Many Citizens   ------> One Country


Rahul  ---------+
                |
Amit   ---------|-----> IT Department
                |
Rohan  ---------+


class Department {
    int deptId;
    String deptName;

    Department(int deptId, String deptName) {
        this.deptId = deptId;
        this.deptName = deptName;
    }

    void displayDepartment() {
        System.out.println("Department Id   : " + deptId);
        System.out.println("Department Name : " + deptName);
    }
}

class Employee {
    int empId;
    String empName;
    Department department;

    Employee(int empId,
             String empName,
             Department department) {

        this.empId = empId;
        this.empName = empName;
        this.department = department;
    }

    void displayEmployee() {

        System.out.println("Employee Id   : " + empId);
        System.out.println("Employee Name : " + empName);
        System.out.println("Department Details");
        department.displayDepartment();
    }
}

public class ManyToOneDemo {

    public static void main(String[] args) {

        Department d1 =
                new Department(101, "IT");
        Employee e1 =
                new Employee(1, "Rahul", d1);
        Employee e2 =
                new Employee(2, "Amit", d1);
        Employee e3 =
                new Employee(3, "Rohan", d1);
        e1.displayEmployee();

        System.out.println();
        e2.displayEmployee();

        System.out.println();
        e3.displayEmployee();
    }
}

ONE-TO-MANY ASSOCIATION  
=======================
Definition:
    One object of one entity is mapped to MANY objects of another entity.

                 Department
                      |
        +-------------+-------------+
        |             |             |
     Employee1    Employee2    Employee3

    One Department contains many Employees.


class Employee {
    int empId;
    String empName;

    Employee(int empId, String empName) {
        this.empId = empId;
        this.empName = empName;
    }

    void displayEmployee() {
        System.out.println("Employee Id   : " + empId);
        System.out.println("Employee Name : " + empName);
    }
}


class Department {
    int deptId;
    String deptName;
    Employee[] employees;

    Department(int deptId,
               String deptName,
               Employee[] employees) {

        this.deptId = deptId;
        this.deptName = deptName;
        this.employees = employees;
    }

    void displayDepartment() {
        System.out.println("Department Id   : " + deptId);
        System.out.println("Department Name : " + deptName);
        System.out.println("\nEmployee Details:");

        for(Employee emp : employees) {
            emp.displayEmployee();
            System.out.println();
        }
    }
}






public class OneToManyDemo {
    public static void main(String[] args) {
        Employee e1 =
            new Employee(101, "Rahul");
        Employee e2 =
            new Employee(102, "Amit");
        Employee e3 =
            new Employee(103, "Rohan");
        Employee[] empArray = {e1, e2, e3};

        Department dept =
            new Department(
                10,
                "IT",
                empArray
            );
        dept.displayDepartment();
    }
}


MANY-TO-MANY ASSOCIATION    
=========================
Definition:
    MANY objects of one entity map to MANY objects of another entity.

Student1 ----+
             |
             +------ Java
             |
Student2 ----+
             |
             +------ Python
             |
Student3 ----+

import java.util.ArrayList;
import java.util.List;

class Student {

    int studentId;
    String studentName;

    List<Course> courses;

    Student(int studentId, String studentName) {
        this.studentId = studentId;
        this.studentName = studentName;
        this.courses = new ArrayList<>();
    }
}

class Course {

    int courseId;
    String courseName;

    List<Student> students;

    Course(int courseId, String courseName) {
        this.courseId = courseId;
        this.courseName = courseName;
        this.students = new ArrayList<>();
    }
}

public class ManyToManyDemo {
    public static void main(String[] args) {
        Student s1 =
            new Student(1, "Rahul");
        Student s2 =
            new Student(2, "Amit");
        Course c1 =
            new Course(101, "Java");
        Course c2 =
            new Course(102, "Python");
        // Association
        s1.courses.add(c1);
        s1.courses.add(c2);

        s2.courses.add(c1);

        c1.students.add(s1);
        c1.students.add(s2);

        c2.students.add(s1);

        // Display

        System.out.println("Courses of Rahul");
        for(Course c : s1.courses) {
            System.out.println(c.courseName);
        }
        System.out.println();

        System.out.println("Students in Java Course");
        for(Student s : c1.students) {
            System.out.println(s.studentName);
        }
    }
}


                          +-------------+
                          | Association |
                          +-------------+
                           /           \
                     Weak /             \ Strong
                         /               \
               +--------------+     +-------------+
               | Aggregation  |     | Composition |
               +--------------+     +-------------+
               (Loose-bound)         (Tight-bound)
               Container obj         Contained obj
               can exist alone       dies with container


 COMPOSITION (Tight-bound Has-A):
  ----------------------------------
    * Contained object is CREATED INSIDE the container
    * If container is destroyed -> contained object ALSO destroyed
    * Container and contained have SAME lifetime

    Example: Student HAS-A Heart, Student HAS-A Brain
    (Heart/Brain cannot exist without Student)

    +---------+       +-------+
    | Student  |◆------| Heart |  (filled diamond = Composition)
    |          |◆------| Brain |
    +----------+       +-------+

    class Student {
        // Composite objects (created INSIDE Student)
        public Heart heart = new Heart(72, 932);
        public Brain brain = new Brain("gray", 150);
    }

AGGREGATION (Loose-bound Has-A):
  ----------------------------------
    * Contained object is CREATED OUTSIDE the container
    * If container is destroyed -> contained object STILL accessible
    * Injected via setter (loose connection)

    Example: Student HAS-A Bike, Student HAS-A Book
    (Bike/Book can exist without Student)

    +-----------+        +------+
    | Student   |◇-------| Bike |  (empty diamond = Aggregation)
    |           |◇-------| Book |
    +-----------+        +------+

    class Student {
        // Aggregate objects (created OUTSIDE, injected)
        public Bike bike;
        public Book book;

        public void setBike(Bike bike) { this.bike = bike; }
        public void setBook(Book book) { this.book = book; }
    }

Definition:
    * Delegation = handing over RESPONSIBILITY for a task to another
      class or method
    * An object EXPRESSES certain behaviour to the outside world
      but DELEGATES the actual implementation to an associated object

    
Flow:
    +-------------+  wash()   +------------+  wash()   +--------+
    | Boss/Owner  |---------->| Supervisor |---------->| Worker |
    |             |  delegate |            |  delegate |        |
    +-------------+           +------------+           +--------+
                               (delegates                (actual
                                the work)                 work done)


class Owner {
        public static void main(String[] args) {
            Supervisor s = new Supervisor();
            s.wash();    // Owner calls Supervisor
            s.dust();
            s.clean();
        }
    }
    class Supervisor {
        Worker w = new Worker();   // Has-A variable

        public void wash()  { w.wash();  }  // delegates to Worker
        public void dust()  { w.dust();  }
        public void clean() { w.clean(); }
    }

    class Worker {
        public void wash()  { s.o.p("Washing...");  }
        public void dust()  { s.o.p("Dusting...");  }
        public void clean() { s.o.p("Cleaning..."); }
    }

  Output:
    Washing...
    Dusting...
    Cleaning...



  +--------------------+---------------------------+------------------------+
  | Concept            | Key Point                 | How Achieved           |
  +--------------------+---------------------------+------------------------+
  | Has-A              | Association via variable  | has-a variable         |
  | Is-A               | Inheritance               | extends keyword        |
  | Constructor Inject | Inject at creation time   | parameterized constr.  |
  | Setter Inject      | Inject after creation     | setter method          |
  | One-to-One         | 1 ref variable            | Account acc;           |
  | One-to-Many        | Array of refs in target   | Employee[] employees;  |
  | Many-to-One        | Many share 1 dependent    | same obj passed to all |
  | Many-to-Many       | Arrays on both sides      | Project[] / varargs    |
  | Composition        | Tight-bound, same lifetime| new inside class       |
  | Aggregation        | Loose-bound, independent  | setter injection       |
  | Delegation         | Pass responsibility on    | Has-A + method call    |
  +--------------------+---------------------------+------------------------+



  

```


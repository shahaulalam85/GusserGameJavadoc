## 1.
```java

public class Test {
    static int x = 5;
    
    public static void main(String[] args) {
        Test t1 = new Test();
        Test t2 = new Test();
        t1.x = 10;
        t2.x = 20;
        System.out.println(t1.x + " " + t2.x);
    }
}

A) 10 20
B) 5 5
C) 20 20
D) Compile Error


// Why? x is static — there is only ONE copy shared by all objects. When t2.x = 20 runs, it overwrites the same memory location that t1.x points to. Both print 20.

// ⚠️ This is exactly why accessing static variables via object references (t1.x) is misleading and bad practice. Always use Test.x.

✅ Q1 — C) 20 20 — CORRECT

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
## 2.
```java

public class Test {
    int a = 10;
    
    void show() {
        int a = 20;
        System.out.println(a + " " + this.a);
    }
    
    public static void main(String[] args) {
        new Test().show();
    }
}

A) 10 10
B) 20 10
C) 10 20
D) 20 20

// Why? The local variable a = 20 shadows the instance variable a = 10 inside the method. this.a explicitly refers to the instance variable, bypassing the shadow.

✅ Q2 — B) 20 10 — CORRECT

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

## 3.
```java

public class Test {
    static int count;
    
    public static void main(String[] args) {
        System.out.println(count);
    }
}

A) Compile Error — uninitialized variable
B) Runtime Error
C) Prints 0
D) Prints null

// Why? count is a static variable, not a local variable. Static and instance variables are always auto-initialized by the JVM. Only local variables require manual initialization.

✅ Q3 — C) Prints 0 — CORRECT

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

## 4.
```java

public class Test {
    int x = 10;
    
    static void modify(Test obj) {
        obj.x = 99;
        obj = new Test();
        obj.x = 500;
    }
    
    public static void main(String[] args) {
        Test t = new Test();
        modify(t);
        System.out.println(t.x);
    }
}

A) 10
B) 99
C) 500
D) Compile Error

//Why? Java passes object references by value. obj = new Test() only changes the local copy of the reference inside modify(). The original t in main() still points to the object where x = 99.
Before:  t ──────────▶ [x=10]
After modify:
         t ──────────▶ [x=99]      ← t still points here
         obj ─────────▶ [x=500]    ← new object, t doesn't know about it


✅ Q4 — B) 99 — CORRECT

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

## 5.
```java

public class Test {
    static int i = 0;
    
    public static void main(String[] args) {
        for (int i = 0; i < 3; i++) {
            Test.i += i;
        }
        System.out.println(i + " " + Test.i);
    }
}

A) 3 3
B) 0 3
C) 3 0
D) Compile Error

//

✅ Q5 — A) 3 3 - CORRECT

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

## 6.
```java

public class Test {
    int val;
    
    Test(int val) {
        val = val;      // ⚠️ Notice: no 'this'
    }
    
    public static void main(String[] args) {
        Test t = new Test(42);
        System.out.println(t.val);
    }
}

A) 42
B) 0
C) null
D) Compile Error

//Why? This compiles perfectly fine — no error. But it's a silent logical bug. val = val assigns the parameter to itself. The instance variable this.val is never touched, so it keeps its default value of 0.

// What was intended:
this.val = val;   // instance ← parameter

// What was written:
val = val;        // parameter ← parameter (useless!)

This is one of the most common and dangerous bugs in Java — no warning, no error, just wrong behavior.

✅ Correct Answer: B) 0

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

## 7.
```java

public class Test {
    static int x = 10;
    
    public static void main(String[] args) {
        int x = x + 5;      // ⚠️ Tricky
        System.out.println(x);
    }
}

A) 15
B) 10
C) 5
D) Compile Error

@ Explanation

int x = x + 5;   // ❌ trying to read 'x' before it is initialized
// Why? When the compiler sees int x = x + 5, it creates a new local variable x that immediately shadows the static x. But then it tries to read this new local x on the right-hand side before it has been assigned — compile error.

// The compiler sees this as:
int x;           // new local x (shadows static x)
x = x + 5;      // ❌ reading local x before initialization → ERROR

✅ Q7 — D) Compile Error — CORRECT

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

## 8.
```java

public class Test {
    int x = 100;
    
    void method() {
        int x = 200;
        {
            int y = 300;
            System.out.println(x + " " + y);
        }
        // System.out.println(y);   // commented out
        System.out.println(x);
    }
    
    public static void main(String[] args) {
        new Test().method();
    }
}

A) 200 300 then 200
B) 100 300 then 100
C) 200 300 then 100
D) Compile Error



✅ Q8 — A) 200 300 then 200 — CORRECT

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

## 9.
```java

public class Test {
    static int a = 10;
    int b = 20;
    
    static void display() {
        System.out.println(a);
        System.out.println(b);    // ⚠️
    }
    
    public static void main(String[] args) {
        display();
    }
}

A) 10 then 20
B) 10 then 0
C) Compile Error
D) Runtime Error

@ Explanation -------------
static void display() {
    System.out.println(a);   // ✅ static accessing static — fine
    System.out.println(b);   // ❌ static accessing instance variable — ERROR
}

//Why? A static method has no this reference — it exists at class level, independent of any object. Instance variable b belongs to an object, and without an object there is no b to access

static method ──▶ knows about: static variables ✅
static method ──▶ does NOT know about: instance variables ❌

✅ Q8 — A) 200 300 then 200 — CORRECT

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

## 10.
```java

public class Test {
    static int num = 5;
    
    public static void main(String[] args) {
        System.out.println(num++);   // line 1
        System.out.println(++num);   // line 2
        System.out.println(num--);   // line 3
        System.out.println(num);     // line 4
    }
}

A) 5 7 7 6
B) 5 6 7 6
C) 6 7 7 6
D) 5 7 8 7


✅ Q10 — A) 5 7 7 6 — CORRECT

```

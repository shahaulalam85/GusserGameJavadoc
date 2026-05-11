
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

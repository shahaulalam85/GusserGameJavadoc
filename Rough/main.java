
abstract class Car {

    void start() {
        System.out.println("Car has started");
    }

    abstract void acclerate();

    abstract void drive();

    void stop() {
        System.out.println("Car has stoped");
    }
}

abstract class Maruti800 extends Car {

    void acclerate() {
        System.out.println("Car is accelerated at 180km");
    }

    void drive() {
        System.out.println("Manual Gear");
    }

    void combustion() {
        System.out.println("Petrol Engine");
    }
}

abstract class Innova extends Car {

    void acclerate() {
        System.out.println("Car is accelerated at 240km");
    }

    void drive() {
        System.out.println("Automatic Gear");
    }

    void combustion() {
        System.out.println("Disel Engine");
    }
}

class Ferrari extends Car {

    void acclerate() {
        System.out.println("Car is accelerated at 340km");
    }

    void drive() {
        System.out.println("Tarbo gear system");
    }

    void combustion() {
        System.out.println("White Petrol Engine");
    }
}

class Road {

    void Permit() {

    }
}

class main {

    public static void main(String[] args) {

    }
}

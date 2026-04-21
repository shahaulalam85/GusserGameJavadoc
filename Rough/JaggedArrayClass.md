## Marks of 5 students
```java

class main {

    public static void main(String[] args) {
        int[] a = new int[5];
        a[0] = 80;
        a[1] = 90;
        a[2] = 100;
        a[3] = 70;
        a[4] = 60;
        for (int i = 0; i < a.length; i++) {
            System.out.println(a[i]);
        }
        System.out.println("Length of the array is: " + a.length);
    }
}

```

## Marks of 5 Students each in 3 Classroom

```java 
class main {

    public static void main(String[] args) {
        int[][] a = new int[3][5];
        a[0][0] = 1;
        a[0][1] = 2;
        a[0][2] = 3;
        a[0][3] = 4;
        a[0][4] = 5;
        a[1][0] = 6;
        a[1][1] = 7;
        a[1][2] = 8;
        a[1][3] = 9;
        a[1][4] = 10;
        a[2][0] = 11;
        a[2][1] = 12;
        a[2][2] = 13;
        a[2][3] = 14;
        a[2][4] = 15;
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[i].length; j++) {
                System.out.println(a[i][j]);
            }
        }
        System.out.println("Length of the outer array is: " + a.length);
        System.out.println("Length of the inner array is: " + a[0].length);
    }
}

```

## Marks of 5 Students each in 3 Classroom each in 2 School

```java


class main {

    public static void main(String[] args) {
        int[][][] a = new int[2][3][5];
        a[0][0][0] = 30;
        a[0][0][1] = 40;
        a[0][0][2] = 50;
        a[0][0][3] = 60;
        a[0][0][4] = 70;

        a[0][1][0] = 35;
        a[0][1][1] = 45;
        a[0][1][2] = 55;
        a[0][1][3] = 65;
        a[0][1][4] = 75;

        a[0][2][0] = 36;
        a[0][2][1] = 46;
        a[0][2][2] = 56;
        a[0][2][3] = 66;
        a[0][2][4] = 76;

        a[1][0][0] = 37;
        a[1][0][1] = 47;
        a[1][0][2] = 57;
        a[1][0][3] = 67;
        a[1][0][4] = 77;

        a[1][1][0] = 38;
        a[1][1][1] = 48;
        a[1][1][2] = 58;
        a[1][1][3] = 68;
        a[1][1][4] = 78;

        a[1][2][0] = 39;
        a[1][2][1] = 49;
        a[1][2][2] = 59;
        a[1][2][3] = 69;
        a[1][2][4] = 79;

        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[i].length; j++) {
                for (int k = 0; k < a[i][j].length; k++) {
                    System.out.println(a[i][j][k]);
                }
            }
        }

    }
}


```

## Marks of 5 Students each in 3 Classroom each in 2 School each in 2 Cities

```java


import java.util.Scanner;

class main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter number of cities");
        int cities = scan.nextInt();
        System.out.println("Enter number of school");
        int school = scan.nextInt();
        System.out.println("Enter number of classroom");
        int classroom = scan.nextInt();
        System.out.println("Enter number of students");
        int students = scan.nextInt();
        int[][][][] a = new int[cities][school][classroom][students];
        // Scanning Input
        for (int i = 0; i < cities; i++) {
            for (int j = 0; j < school; j++) {
                for (int k = 0; k < classroom; k++) {
                    for (int l = 0; l < students; l++) {
                        a[i][j][k][l] = scan.nextInt();
                    }
                }
            }
        }

        // Printing output
        for (int i = 0; i < cities; i++) {
            for (int j = 0; j < school; j++) {
                for (int k = 0; k < classroom; k++) {
                    for (int l = 0; l < students; l++) {
                        System.out.println(a[i][j][k][l] + " ");
                    }
                    System.out.println("");
                }
                System.out.println("");
            }
            System.out.println("");
        }

    }
}

```

## jagged array
```java


import java.util.Scanner;

class main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter number of Classrooms: ");
        int classroom = scan.nextInt();
        int[][] a = new int[classroom][];
        for (int i = 0; i < classroom; i++) {
            System.out.println("Number of student in classroom no. " + i);
            int students = scan.nextInt();
            a[i] = new int[students];
        }

        // Input of arrays
        for (int i = 0; i < classroom; i++) {
            for (int j = 0; j < a[i].length; j++) {
                a[i][j] = scan.nextInt();
            }
        }

        // Printing the array
        for (int i = 0; i < classroom; i++) {
            System.err.print("Classroom " + i + ": ");
            for (int j = 0; j < a[i].length; j++) {
                System.out.print(a[i][j] + " ");
            }
            System.err.println("");
        }
    }
}

```

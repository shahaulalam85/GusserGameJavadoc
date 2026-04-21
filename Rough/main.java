
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

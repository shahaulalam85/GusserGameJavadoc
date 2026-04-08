import java.util.*;

public class NewGame {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            Umpire u = new Umpire(sc);
            u.collectNumFromGuesser();
            u.collectNumFromPlayers();
            u.compare();

            System.out.println("\nDo you want to play again? (yes/no)");
            String choice = sc.next();

            if (!choice.equalsIgnoreCase("yes")) {
                System.out.println("Thanks for playing!");
                break;
            }
        }

        sc.close();
    }

    // ------------------ Guesser ------------------
    static class Guesser {
        int guessNum;
        Scanner sc;

        Guesser(Scanner sc) {
            this.sc = sc;
        }

        int guessingNum() {
            System.out.print("Guesser, enter a number: ");
            guessNum = sc.nextInt();
            return guessNum;
        }
    }

    // ------------------ Player ------------------
    static class Player {
        int playerNum;
        Scanner sc;
        int playerId;

        Player(Scanner sc, int id) {
            this.sc = sc;
            this.playerId = id;
        }

        int predictingNum() {
            System.out.print("Player " + playerId + ", enter your guess: ");
            playerNum = sc.nextInt();
            return playerNum;
        }
    }

    // ------------------ Umpire ------------------
    static class Umpire {
        int numFromGuesser;
        int[] playerGuesses;
        Scanner sc;

        Umpire(Scanner sc) {
            this.sc = sc;
        }

        void collectNumFromGuesser() {
            Guesser g = new Guesser(sc);
            numFromGuesser = g.guessingNum();
        }

        void collectNumFromPlayers() {
            System.out.print("Enter number of players: ");
            int n = sc.nextInt();

            playerGuesses = new int[n];

            for (int i = 0; i < n; i++) {
                Player p = new Player(sc, i + 1);
                playerGuesses[i] = p.predictingNum();
            }
        }

        void compare() {
            boolean winnerFound = false;

            for (int i = 0; i < playerGuesses.length; i++) {
                if (playerGuesses[i] == numFromGuesser) {
                    System.out.println("🎉 Player " + (i + 1) + " guessed correctly!");
                    winnerFound = true;
                }
            }

            if (!winnerFound) {
                System.out.println("❌ No one guessed correctly. Try again!");
            }
        }
    }
}
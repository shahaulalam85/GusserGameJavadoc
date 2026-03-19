import java.util.*;
public class NewGame
{
    public static void main(String[] args){
        Umpire u = new Umpire();
        u.collectNumFromGuesser();
        u.collectNumFromPlayer();
        u.comparing();
    }
    static class Guesser
    {
        int guessNum;
        int guessingNum()
        {
            Scanner sc = new Scanner(System.in);
            System.out.println("Guesser, kindly guess the number! ");
            guessNum = sc.nextInt();
            return guessNum;
        }
    }
    static class Player
    {
        int playerNum;
        int predictingNum()
        {
            Scanner sc = new Scanner(System.in);
            System.out.println("Player, kindly guess the number! ");
            playerNum = sc.nextInt();
            return playerNum;
        }
    }
    static class Umpire
    {
        int numFromGuesser;
        int numFromPlayer1;
        int numFromPlayer2;
        int numFromPlayer3;


        void collectNumFromGuesser()
        {
            Guesser g = new Guesser();
            numFromGuesser = g.guessingNum();
        }
        void collectNumFromPlayer()
        {
            Player p1 = new Player();
            Player p2 = new Player();
            Player p3 = new Player();

            numFromPlayer1 = p1.predictingNum();
            numFromPlayer2 = p2.predictingNum();
            numFromPlayer3 = p3.predictingNum();

        }
        void comparing()
        {
            if(numFromGuesser == numFromPlayer1)
            {
                System.out.println("Congratulations! Player1 won the game!");
            }
            else if(numFromGuesser == numFromPlayer2)
            {
                System.out.println("Congratulations! Player2 won the game!");
            }
            else if(numFromGuesser == numFromPlayer3)
            {
                System.out.println("Congratulations! Player3 won the game!");
            }
            else
            {
                System.out.println("Sorry! You lost the game! Try again.");
            }
        }
    }
    
}
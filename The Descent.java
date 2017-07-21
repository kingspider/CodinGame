import java.util.*;
import java.io.*;
import java.math.*;

/**
 * The while loop represents the game.
 * Each iteration represents a turn of the game
 * where you are given inputs (the heights of the mountains)
 * and where you have to print an output (the index of the mountain to fire on)
 * The inputs you are given are automatically updated according to your last actions.
 **/

 
class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        
        ArrayList<Integer> mountain = new ArrayList<Integer>();
        ArrayList<Integer> mountainSorted = new ArrayList<Integer>();

        // game loop
        while (true) {
            for (int i = 0; i < 8; i++) {
                int mountainH = in.nextInt(); // represents the height of one mountain.
                mountain.add(mountainH);
                //System.err.println(mountain);
                mountainSorted.add(mountainH);
                //System.err.println(mountainSorted);
            }

            // Write an action using System.out.println()
            // To debug: System.err.println("Debug messages...");
            
        Collections.sort(mountainSorted, Collections.reverseOrder());
        System.err.println("Sorted list: " + mountainSorted);
        System.out.println(mountain.indexOf(mountainSorted.get(0)));
        mountain.clear();
        mountainSorted.clear();
            
          
        }
    }
}
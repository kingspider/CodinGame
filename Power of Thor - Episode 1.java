import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/

 
class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int lightX = in.nextInt(); // the X position of the light of power
        int lightY = in.nextInt(); // the Y position of the light of power
        int initialTX = in.nextInt(); // Thor's starting X position
        int initialTY = in.nextInt(); // Thor's starting Y position
        String direction = "";
        // game loop
        while (true) {
            int remainingTurns = in.nextInt(); // The remaining amount of turns Thor can move. Do not remove this line.
            
                if (initialTY > lightY) {
                    
                        initialTY -= 1;
                        direction += "N";
                }
                
                if (initialTY < lightY) {
                    
                        initialTY += 1;
                        direction += "S";
                }else{
                    
                }            
                
                if (initialTX > lightX) {
                    
                        initialTX -= 1;                   
                        direction += "W";
                        
                }
                if (initialTX < lightX) {
                    
                        initialTX += 1;
                        direction += "E";
                }else{
                
                }
                        
                
            System.out.println(direction);
            direction = "";

        }
    }
}
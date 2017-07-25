import java.util.*;
import java.io.*;
import java.math.*;

class Solution {
    
    public Integer closeZero(ArrayList<Integer> temperatures) {
        
     ArrayList<Integer> negTemps = new ArrayList<>();
     ArrayList<Integer> posTemps = new ArrayList<>();
     
     for ( Integer temps: temperatures) {
         
        if (temps < 0 ){
            
            negTemps.add(temps);
            
            } else {
                
            posTemps.add(temps);
            
        }   
    }
    
    Collections.sort(posTemps);
    System.err.println(posTemps);
    Collections.sort(negTemps, Collections.reverseOrder());
    System.err.println(negTemps);
    
    
    if( negTemps.size() == 0) {
            return posTemps.get(0);
        }
    if( posTemps.size() == 0){
            return negTemps.get(0);
        }    
    if ( Math.abs(negTemps.get(0)) == posTemps.get(0) ){
            return posTemps.get(0);
        }
    if ( posTemps.get(0) < Math.abs(negTemps.get(0)) ) {
            return posTemps.get(0);
        } 
    else {
            return negTemps.get(0);
        }    
            
    }

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(); // the number of temperatures to analyse
        if (in.hasNextLine()) {
            in.nextLine();
        }
        
        ArrayList<Integer> tempArray = new ArrayList<>();
        String[] temps = in.nextLine().split(" "); // the n temperatures expressed as integers ranging from -273 to 5526
        Solution program = new Solution();
        boolean empty = false;
            
            for(String temp: temps){
                    if( temp.isEmpty() ){
                        empty = true;
                        System.out.println(0);
                        break;
                        } 
                    else {
                        tempArray.add(Integer.valueOf(temp));
                        }
                    
            }
          if(!empty){
           System.out.println(program.closeZero(tempArray));
          } 
    }
}
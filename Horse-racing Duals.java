import java.util.*;
import java.io.*;
import java.math.*;

class Solution {

    public Integer getDist(int item1, int item2){
        return (item1 - item2);
    }
         
    public static void main(String args[]) {
        
        Solution program = new Solution();
        int lowest = 10000;
        ArrayList<Integer> horses = new ArrayList<>();
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        for (int i = 0; i < N; i++) {
            int pi = in.nextInt();
            horses.add(pi);
    }

        Collections.sort(horses, Collections.reverseOrder());
        
        for(int horse = 0; horse < horses.size() - 1; horse++){
            int horseOne = horses.get(horse);
            int horseTwo = horses.get(horse + 1);
            if (program.getDist(horseOne, horseTwo) < lowest){
                    lowest = program.getDist(horseOne, horseTwo);
                }
            }
        System.out.println(lowest);
    }
}


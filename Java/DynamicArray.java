import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;



public class DynamicArray {
    public static void main(String[] args) throws IOException {
        Scanner sc=new Scanner(System.in);
        int N=sc.nextInt();
        int Q=sc.nextInt();
        int lastAns=0;
        ArrayList<ArrayList<Integer>> lists=new ArrayList();
        for(int i=0;i<N;i++){
            lists.add(new ArrayList<Integer>());
        }
        for(int i=0;i<Q;i++){
            int q=sc.nextInt();
            int x=sc.nextInt();
            int y=sc.nextInt();
            ArrayList<Integer> seq=lists.get((x^lastAns)%N);
            if(q==1){
                seq.add(y);
            }
            else if(q==2){
                lastAns=seq.get(y%seq.size());
                System.out.println(lastAns);
            }
        }
    }
}

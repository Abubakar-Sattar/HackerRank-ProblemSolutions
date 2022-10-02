// Name: Hemant Singh
// Date: 10/02/2022


import java.io.*;
import java.util.*;

public class JavaList {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        ArrayList<Integer> l=new ArrayList<Integer>();
        String s="";
        int q,n,i;
        n=sc.nextInt();
        for(i=0;i<n;i++)
            l.add(sc.nextInt());
        
        q=sc.nextInt();
        for(i=0;i<q;i++){
            s=sc.next();
            if(s.compareTo("Insert")==0){
                int x=sc.nextInt();
                int y=sc.nextInt();
                l.add(x,y);
            }
            else{
                int x=sc.nextInt();
                l.remove(x);
            }
        }
        for(int j:l){
            System.out.print(j+" ");
        }
    }
}

//Name:Nikhil Srivastava
//Date:16/10/2022
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        //taking string as input from user
        String A=sc.next();
        //Make an empty string to store the input string in reverse order
        String B="";
        
        //Traverse the input string from last index and store characters in reverse order in string B
        for(int i=A.length()-1;i>=0;i--)
            B=B+A.charAt(i);
            
            
            //compare A and B if both are equal print yes else print no
            if(A.compareTo(B)==0)
            System.out.println("Yes");
            else
            System.out.println("No");
    }
}




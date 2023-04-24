//Name:Nikhil Srivastava
//Date:21/10/2022

import java.util.*;

public class Solution {

    public static void main(String[] args) {
	   
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
         //Declaring an integer array a of size n
         int[] a=new int[n];
         
         //Using for loop to store n integers in the array.
         for(int i=0;i<n;i++)
         a[i]=scan.nextInt();
        scan.close();

        // Prints each sequential element in array a
        for (int i = 0; i < a.length; i++) {
            System.out.println(a[i]);
        }
    }
}
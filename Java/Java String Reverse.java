/*  Name: Akshat Bokdia
    Date: 22/10/2022 */

import java.util.*;

public class Solution {
    
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        A = A.toLowerCase();
        StringBuffer B = new StringBuffer(A);   
        B.reverse();
        String C = new String(B);
        
        if(A.compareTo(C) == 0)
            System.out.println(A + " is a palindrome.");
        else
            System.out.println(A + " is NOT a palindrome.");
        sc.close();
    }
}

//Name:Nikhil Srivastava
//Date:16/10/2022
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        //Taking string as input from the user
        String S = in.next();
        //Take start and end index as input from user
        int start = in.nextInt();
        int end = in.nextInt();
        
        //print the substring from start to end using inbuilt substring function
        System.out.println(S.substring(start, end));
    }
}
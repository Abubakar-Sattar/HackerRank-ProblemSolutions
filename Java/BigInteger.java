import java.io.*;
import java.util.*;
import java.math.*;

public class Solution {

    public static void main(String[] args) {
    Scanner input=new Scanner(System.in);
    
    BigInteger a=new BigInteger(input.next());
    BigInteger b=new BigInteger(input.next());
    
    BigInteger c,d;
    c=a.add(b);
    d=a.multiply(b);
    System.out.println(c);
    System.out.println(d);
    
    }
}

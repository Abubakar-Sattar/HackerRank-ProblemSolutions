// Name: Sura Karthikeya
// Date: 28/10/2022


import java.util.*;

class JavaStack {
	
	public static void main(String[] args) {
        
		Scanner sc = new Scanner(System.in);

        while (sc.hasNext()) {
            String input = sc.next();
            // Complete the code
            Stack<Character> stack = new Stack<>(); // Creates an empty Stack
            boolean flag = true; // Boolean to Validate brackets
            for (int i = 0; i < input.length(); i++) {
                char bracket = input.charAt(i);
                if (bracket == '(' || bracket == '{' || bracket == '[') // Push if 'open brackets'
                    stack.push(bracket);
                else {
                    if (stack.isEmpty()) {
                        flag = false; break;
                    } else {
                        char top = stack.pop(); // Pop if 'closed brackets'
                        if ((top == '(' && bracket != ')') || (top == '{' && bracket != '}') || (top == '[' && bracket != ']')) { // Check incorrect bracket pairs
                            flag = false; break;
                        }
                    }
                }
            }

            // Output Result
            if (flag && stack.isEmpty()) System.out.println("true");
            else System.out.println("false");
        }
		
	}
}
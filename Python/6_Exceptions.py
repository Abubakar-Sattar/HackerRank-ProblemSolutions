# Name: ILYAS AHMED
# Date: 10/28/2022

# Enter your code here. Read input from STDIN. Print output to STDOUT        
x = int(input());   
for i in range(x):
    try:
        a, b = input().split()
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code:",e);
    except ValueError as v:
        print("Error Code:",v);

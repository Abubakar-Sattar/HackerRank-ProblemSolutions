# Name: ILYAS AHMED
# Date: 10/21/2022

# Find the runner up score 

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr))[-2])
    # below is another way to find runner up score 
    # print(sorted(set(arr), reverse=True)[2])

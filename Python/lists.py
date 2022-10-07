# Question source: https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':

    N = int(input())
    l = []
    for i in range(N):
        op = input().split()

        if op[0] == 'insert':
            l.insert(int(op[1]), int(op[2]))
        elif op[0] == 'append':
            l.append(int(op[1]))
        elif op[0] == 'remove':
            l.remove(int(op[1]))
        elif op[0] == 'print':
            print(l)
        elif op[0] == 'pop':
            l.pop()
        elif op[0] == 'sort':
            l.sort()
        elif op[0] == 'reverse':
            l.reverse()

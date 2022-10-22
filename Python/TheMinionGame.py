# Name: cocomo
# Date: 10/4/2022

#!/bin/python3

def minion_game(string):
    vowels = 'AEIOU'
    stuart = 0
    kevin = 0
    len_string = len(string)
        
    for i, j in enumerate(string):
        if j in vowels:
            kevin += len_string - i
        else:
            stuart += len_string - i
            
    if stuart > kevin:
        print('Stuart', stuart)
    elif kevin > stuart:
        print('Kevin', kevin)
    else:
        print('Draw')
        
if __name__ == '__main__':
    s = input()
    minion_game(s)
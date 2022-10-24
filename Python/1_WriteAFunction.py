# Name : Akshat Bokdia
# Date : 24/10/2022

def is_leap(year):
    leap = False
    
    if ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)):
        leap = True
    return leap

if __name__ == "__main__":    
    while True:
        year = int(input("Enter a year: "))
        if year < 0:
            print("Invalid input!!")
        else:
            break
    print(is_leap(year))

// Name: Syed Hamza Hoda
// Date: 10/2/2022

def count_substring(string, sub_string):
    
    res = [i for i in range(len(string)) if string.startswith(sub_string, i)]
   
    return len(res)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

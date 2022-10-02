// Name: Abubakar Sattar
// Date: 10/2/2022

#include <bits/stdc++.h>

using namespace std;


int main() {
int in;
string num[10] = {"Greater than 9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

cin >> in;

if(in > 9){
    cout << num[0];
}
else{
    cout << num[in];
}

return 0;
}

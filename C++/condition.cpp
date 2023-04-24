#include <bits/stdc++.h>
#include <vector>
using namespace std;


int main()
{
    int n;
    const vector<std::string> numbers {
        "one", "two", "three", "four", "five", 
        "six", "seven", "eight", "nine"
    };
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    if(n > 9) {
        cout << "Greater than 9" << endl;
    } else {
        cout << numbers.at(n-1) << endl;
    }
    return 0;
}

#include<bits/stdc++.h>
using namespace std;

void process_input(int n);
int largest_proper_divisor(int n);

int main() {
    int n;
    cin >> n;
    process_input(n);
    return 0;
}


void process_input(int n) {
    try {
        int d = largest_proper_divisor(n);
        cout << "result=" << d << endl;   
    } catch(exception &e) {
        cout << e.what() << endl;
    }
    cout << "returning control flow to caller" << endl;
}

int largest_proper_divisor(int n) {
    if (n == 0) {
        throw invalid_argument("largest proper divisor is not defined for n=0");
    }
    if (n == 1) {
        throw invalid_argument("largest proper divisor is not defined for n=1");
    }
    for (int i = n/2; i >= 1; --i) {
        if (n % i == 0) {
            return i;
        }
    }
    return -1;
}

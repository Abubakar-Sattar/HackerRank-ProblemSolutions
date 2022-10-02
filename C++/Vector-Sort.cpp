#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */     int N;
    cin>>N;
    vector<int>vec;
    int x;
    for(int i=0;i<N;i++){
        cin>>x;
        vec.push_back(x);
    }
    sort(vec.begin(),vec.end());
    for(auto i:vec){
        cout<< i<<" ";
    }
    return 0;
}

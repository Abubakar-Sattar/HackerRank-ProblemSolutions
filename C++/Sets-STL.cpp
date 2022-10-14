//Name:Nikhil Srivastava
//Date:14/10/2022

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    //declaring the set "s" 
    set<long> s;
    // declaring q which is number of queries and taking q as input from user
    long q;
    cin>>q;
    
    while(q--)
    {   
        //declaring x,y where y is query type and x is integer and then taking x,y as input from user
        int x,y;
        cin>>y>>x;
        
        if(y==1)
        s.insert(x);//insert x in set if y=1
        else if(y==2)
        {
         auto p=s.find(x); //find position of x,if x is present in set then iterator to the position will be returned and get stored in p else s.end() will be returned and stored in p
         if(s.find(x)!=s.end()) //if x is present delete it from set
         s.erase(p);
        }
        else {
          if(s.find(x)!=s.end())//if x is present print yes else print no
          cout<<"Yes"<<endl;
          else 
          cout<<"No"<<endl;
        }
    }
    return 0;
}

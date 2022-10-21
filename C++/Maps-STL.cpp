  //Name:Nikhil Srivastava
  //Date:16/10/2022
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    //Declaring q which is number of queries and taking input from user 
    long q;
    cin>>q;
    map<string,long> mp;//declaring a map named mp
    while(q--)
    {   
        string x;
        long type,y;
        cin>>type;//taking input from user,here type is query type
        
        if(type==1)
        {   
            //if query is of type 1 then take x and y as input
            cin>>x;
            cin>>y;
            if(mp.find(x)!=mp.end())//if a student named x exist then add y marks to previous marks obtained by x 
            mp[x]=mp[x]+y;
            else
            //if no student named x exists then create a student named x and save y as its marks
            mp[x]=y;
        }
        else if(type==2)
        {   //if query is of type 2 make marks of x=0
            cin>>x;
            mp[x]=0;
        }
        else {
         cin>>x;
         //if a student named x exists then print marks of x else print 0
         if(mp.find(x)!=mp.end())
         cout<<mp[x]<<endl;
         else
         cout<<"0"<<endl;
        }
    }  
    return 0;
}




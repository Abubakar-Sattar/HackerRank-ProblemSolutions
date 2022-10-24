#include<iostream>
#include<cstdlib>
#include<ctime>
using namespace std;

int main()
{
	start:
	int n1;

	srand(time(0));
	int n=rand()%3;
	 n1=rand()%3;
	
	cout<<"0:paper"<<endl;
	cout<<"1:scissor"<<endl;
	cout<<"2:rock"<<endl;
	
	    cout<<"enter your choice:"<<endl;
	    cin>>n1;

	    if(n1==n)
	    {
	    	cout<<"Match Drawn "<<endl;
		}
		else if(n1==0 && n==1)
	
		{
			cout<<"You choose Paper \n Computer Choose scissor "<<endl;
			cout<<"Computer Wins "<<endl;
		}
		else if(n1==0 && n==2)
		{
			cout<<"You choose Paper \n Computer Choose rock "<<endl;
			cout<<"You Win"<<endl;
		}
		else if(n1==1 && n==2)
		{
			cout<<"You choose scissor \n Computer Chose rock "<<endl;
			cout<<"Computer Wins"<<endl;
		}
		
		else if(n1==1 && n==0)
		{
			cout<<"You choose scissor \n Computer Chose paper "<<endl;
			cout<<"You Win"<<endl;
		}
		
		else if(n1==2 && n==1)
		{
			cout<<"You choose rock \n Computer Chose scissor "<<endl;
			cout<<"You Win"<<endl;
		}
		
		else if(n1==2 && n==0)
		{
			cout<<"You choose rock \n Computer Chose paper "<<endl;
			cout<<"Computer Wins"<<endl;
		}
		else 
		{
			cout<<"Invalid Value"<<endl;
		}
		
		goto start;
}

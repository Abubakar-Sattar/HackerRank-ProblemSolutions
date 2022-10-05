#include <iostream>
#include <string.h>
#include <cctype>
#include <cstdlib>
#include"LinkedStack.h"
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
void numberConversion(int num);
void SymbolBalancing(string text);
void postfixEvaluation(string number);

int main(int argc, char** argv) {
	int option;
	
	do{
	cout<<"For Number conversion, Press 1"<<endl;
	cout<<"For Symbol Balancing, Press 2"<<endl;
	cout<<"For PostFix Evaluation, Press 3"<<endl;
	cout<<"To Exit, Press 0"<<endl;
	cin>>option;
	
	switch(option)
	{
		case 0:
			exit(-1);
			break;
		case 1:
			cout<<"Enter a number to convert: "<<endl;
			int num;
			cin>>num;
			numberConversion(num);
			break;
		case 2:
			cout<<"Enter sequence of symbols: ";
			string text;
			cin>>text;
			//getline(cin,text);
			SymbolBalancing(text);
			break;
		case 3:
			cout<<"Enter the sequence of equation: ";
			string number;
			cin>>number;
			postfixEvaluation(number);
			break;
    }
	
}while(true);

}

void numberConversion(int num){
	LinkedStack<int> s1;
	while(num>=1){
		s1.push(num%2);
		num=num/2;
	}
	
	s1.removeAll();
	cout<<endl;
}

void SymbolBalancing(string text){
	
	LinkedStack<char> stack;//1
	for(int i=0;i<text.size();i++)//2
	{
		if(text[i]=='[' || text[i]=='{' || text[i]=='(' || text[i]=='<')//2.1
		{
			stack.push(text[i]);
		}
		else if(text[i]==']' || text[i]=='}' || text[i]==')' || text[i]=='>')//2.2
		{
			if(stack.isEmpty())//2.2.1
			{
				cerr<<"Opening Symbol Missing!";
				return;
			}
			else //2.2.2
			{
				char popped=stack.pop();
				if((popped=='[' && text[i]!=']') || (popped=='{' && text[i]!='}') || (popped=='(' && text[i]!=')') || (popped=='<' && text[i]!='>'))
				{
					cerr<<"Symbol mismatch";
					return;
				}
			}
		}
	}
	
	if(!stack.isEmpty())//3
	{
		cerr<<"Closing Symbol Missing";
		return;
	}
	
	else
	{
		cout<<"Valid Sequence || Balanced Symbols"<<endl;
	}
}//SymbolBalancing


void postfixEvaluation(string number){
	LinkedStack<double> stack; //1
	
	for(int i=0;i<number.size();i++)//2
	{
		if(isdigit(number[i])){
			char c = number[i];
			double d = atof(&c);
			stack.push(d);
		}
		else if(number[i]== '+' || number[i]== '-' || number[i]== '*' || number[i]== '/') //2.2
		{
			double a = stack.pop();
			double b = stack.pop();
			if(number[i]=='+'){
				stack.push(a+b);
			}
			else if(number[i]=='-'){
				stack.push(a-b);
			}
			else if(number[i]=='*'){
				stack.push(a*b);
			}
			else if(number[i]=='/'){
				stack.push(a/b);
			}
			
		}
	}
	
	stack.removeAll(); //3
}//postfixEvaluation

#include<iostream>
#include<string>
#include"Node.h"
using namespace std;
template <class T>
class LinkedStack
{
	private:
		Node<T> *top;
	public:
	    LinkedStack()
		{
			top=0;
		}	
			
		void push (T element);//addToHead
		T pop();//removeFromHead
		bool isEmpty();	
		T topValue();
		void removeAll();		
};

template <class T>
void LinkedStack<T>::push(T element)
{	
	Node<T> *ptr=new Node<T>(element);
	//ptr->setInfo(item)	
	if(top==0)//stack is empty
	{
		top=ptr;	
	}
	else //non empty
	{
		ptr->setNext(top);
		top=ptr;
	}
}//push

template <class T>
T LinkedStack<T>::pop()
{
	if(top==0)//empty
	{
		cerr<<"nothing to delete"<<endl;
	}
	else if(top->getNext()==0)//there is only one element
	{
		Node<T> *temp=top; 
		top=0;
		T tempInfo=temp->getInfo();
		delete temp;
		return tempInfo;
	}
	else//more than one element
	{
		Node<T> *temp=top;
		top=temp->getNext();
		T tempInfo=temp->getInfo();
		delete temp;
		return tempInfo;
	}
}//pop

template <class T>
bool LinkedStack<T>::isEmpty()
{
	return top==0;
}//isEmpty

template <class T>
T LinkedStack<T>::topValue()
{
	return top->getInfo();
}//topValue

template <class T>
void LinkedStack<T>::removeAll()
{
	//string elements="";
	while(top!=0)
	{
		//cout<<topValue();
		//elements+=to_string(topValue());//concatenate
		cout<<pop();
	}
	//return elements;
}//removeAll


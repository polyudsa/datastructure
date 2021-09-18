#include<iostream>
using namespace std;
#include "LinkList.h"

template <class T>
LinkList<T>::LinkList()
{
	first=NULL;
	last=NULL;
	length=0;
}

template <class T>
LinkList<T>::LinkList(T a[],int n)
{
	length=n;
	Node<T> *r=NULL,*s=NULL;
	first=NULL;
	if(length==0) {
		last=first;
		return;
	}
	first=new Node<T>;
	first->data=a[0];
	first->next=NULL;
	if(length==1) {
		last=first;
		return;	
	}
	r=first;
	for(int i=1;i<length;i++)
	{
		s=new Node<T>;
		s->data=a[i];
		r->next=s;
		r=s;
	}
	r->next=NULL;
	last=r;
}

template <class T>
LinkList<T>::~LinkList()
{
	Node<T> *q=first,*p=NULL;
	while(q!=NULL)
	{
		p=q;
		q=q->next;
		delete p;
	}
}

template <class T>
void LinkList<T>::Add(T x)
{
	Node<T> *s=new Node<T>;
	s->data=x;
	s->next=NULL;
	last->next=s;
	last=s;
	length++; 
}

template <class T>
void LinkList<T>::Insert(int i,T x)
{
	i++;
	if(i==length){
		Add(x);
		return;
	}
	Node<T> *p=first,*s=NULL;
	if(i==1)
	{
		s=new Node<T>;
		s->data=x;
		s->next=first;
		first=s;
		length++;
		return;
	 } 
	int count=1;
	while(p!=NULL&&count<i-1)
	{
		p=p->next;
		count++;
	}
	if(p==NULL) throw "位置";
	else{
		s=new Node<T>;
		s->data=x;
		s->next=p->next;
		p->next=s;
		length++;
	}
}

template <class T>
T LinkList<T>::Delete(int i)
{
	i++; 
	Node<T> *p=first,*q=NULL;
	T x;
	if(i==1)
	{
		if(p==NULL) throw "位置非法";
		else
		x=p->data;
		first=p->next;
		delete p;
		return x;
	}
	int count=1;
	while(p!=NULL&&count<i-1)
	{
		p=p->next;
		count++;
	}
	if(p==NULL||p->next==NULL)
	throw "位置非法";
	else
	{
		q=p->next;
		x=q->data;
		p->next=q->next;
		delete q;
		length--;
		return x;
	}
}

template <class T>
int LinkList<T>::Locate(T x)
{
	Node<T> *p=first;
	int count=1;
	while(p!=NULL)
	{
		if(p->data==x) return count-1;
		p=p->next;
		count++;
	}
	return 0;
}

template <class T>
void LinkList<T>::PrintList()
{
	Node<T> *p=first;
	if(p!=NULL) cout<<p->data;
	else return;
	while(p->next!=NULL)
	{
		cout<<"->"<<p->next->data;
		p=p->next;
	}
	cout<<endl;
}

template <class T>
int LinkList<T>::Length()
{
	return length;
 } 
#ifndef LinkList_H
#define LinkList_H

template <class T>
struct Node
{
	T data;
	Node<T> *next;
 };
 
template <class T>
class LinkList
{
	public:
		LinkList();
		LinkList(T a[],int n);
		~LinkList();
		int Locate(T x);
		void Add(T x);
		void Insert(int i,T x);
		T Delete(int i);
		void PrintList();
		int Length(); 
	private:
	    Node<T> *first; 
	    Node<T> *last; 
	    int length;
 };
#endif 

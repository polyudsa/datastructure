#include<iostream>
using namespace std;
#include "ArrayStack.h"

template <class T>
ArrayStack<T>::ArrayStack(){
    //Ĭ�Ϲ���һ���������Ϊ10��ջ
    dlength=10;
    dtop=-1;
    data=new T[10];
}

template <class T>
ArrayStack<T>::ArrayStack(int n){
    dlength=n;
    dtop=-1;
    data=new T[n];
}

template <class T>
ArrayStack<T>::~ArrayStack(){
    delete[] data;
}

template <class T>
bool ArrayStack<T>::isEmpty(){
    if(dtop==-1) return true;
    return false;
}

template<class T>
bool ArrayStack<T>::isFull(){
    if(dtop==dlength-1) return true;
    return false;
}

template<class T>
void ArrayStack<T>::push(T x){
    if(isFull()) throw "�Ѿ��ﵽջ����󴢴�ֵ";
    dtop++;
    data[dtop]=x;
}

template<class T>
T ArrayStack<T>::top(){
    if(isEmpty()) throw "ջ��û��Ԫ��";
    T res=data[dtop];
    return res;
}

template<class T>
T ArrayStack<T>::pop(){
    if(isEmpty()) throw "ջ��û��Ԫ��";
    T res=data[dtop];
    dtop--;
    return res;
}

template<class T>
int ArrayStack<T>::length(){
    return dtop+1;
}

template<class T>
int ArrayStack<T>::size(){
    return dlength;
}

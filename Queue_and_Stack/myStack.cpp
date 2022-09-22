/*
 * @author: Zhexuan Gu
 * @Date: 2022-09-21 16:00:28
 * @LastEditTime: 2022-09-22 13:11:55
 * @FilePath: /CPPprojects/PolyU_DSA_datastructure_database/Queue_and_Stack/myStack.cpp
 * @Description: Please implement
 */
#ifndef _MYSTACK_CPP_J
#define _MYSTACK_CPP_J

#include "myStack.h"

namespace gzx_simple_stl{
    template<typename T>
    MyStack<T>::MyStack(int capacity)
    {
        _top = nullptr;
        _capacity = capacity;
        _maximum = capacity;
    }


    template<typename T>
    MyStack<T>::MyStack(LinkNode<T>* head, int capacity)
    {
        _capacity = capacity;
        _maximum = capacity;
        _top = head;
    }

    template<typename T>
    MyStack<T>::MyStack(const MyStack<T>& anotherStack)
    {
        this->_capacity = anotherStack._capacity;
        this->_maximum = anotherStack._maximum;
        LinkNode<T> *ptr1, *ptr2;
        //case1 如果穿进来的栈本身为空
        if(anotherStack._top == nullptr){
            this->_top = nullptr;
        }
        else{
            _top = new LinkNode<T>(anotherStack._top->_data);
            ptr1 = anotherStack._top->next;
            ptr2 = this->_top;
            while(ptr1 != nullptr)
            {
                LinkNode<T>* tempPtr = new LinkNode<T>(ptr1->_data);
                ptr2->next = tempPtr;
                ptr2 = tempPtr;
                ptr1 = ptr1->next;
            }
        }
    }

    template<typename T>
    bool MyStack<T>::Push(T data)
    {
        if(IsFull())
            return false;
        
        LinkNode<T>* item = new LinkNode<T>(data);
        item->next = _top;
        _top = item;
        _capacity --;
        return true;
    }

    template<typename T>
    bool MyStack<T>::Pop(T& data)
    {
        if(IsEmpty())
            return false;
        data = _top->_data;
        LinkNode<T>* tempPtr = _top;
        _top = _top->next;
        delete tempPtr;
        _capacity ++;
        return true;
    }

    template<typename T>
    bool MyStack<T>::IsEmpty() const
    {
        return _capacity == _maximum;
    }

    template<typename T>
    bool MyStack<T>::IsFull() const
    {
        return _capacity == 0;
    }
    
    template<typename T>
    void MyStack<T>::MakeEmpty()
    {
        LinkNode<T>* tempPtr;
        while(_top != nullptr)
        {
            tempPtr = _top;
            _top = _top->next;
            delete tempPtr;
        }
        _capacity = _maximum;
    }

    /**
     * @description: notice the difference between shallow copy and deep copy
     * @event: 
     * @return void
     */    
    template<typename T>
    void MyStack<T>::Copy(MyStack<T> oldStack, MyStack<T>& copy)
    {
        /*
        for shallow copy, the oldStack is going to be empty. That's can be really bad
        because after pop function, all the elements in oldStack have been eliminated
        */
       /*
       MyStack<T> tempStack;
       T data;
       while(!oldStack.IsEmpty())
       {
            oldStack.Pop(data);
            tempStack.Push(data);
       }
       while(!tempStack.IsEmpty()){
            tempStack.Pop(data);
            copy.Push(data);
       }
       */
        
        /* 标准的拷贝代码，写入拷贝构造中 */
    }
    
    
    template<typename T>
    MyStack<T>::~MyStack<T>()
    {
        MakeEmpty();
    }
};

#endif
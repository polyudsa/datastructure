/*
 * @author: Zhexuan Gu
 * @Date: 2022-09-21 23:30:02
 * @LastEditTime: 2022-09-22 13:24:50
 * @FilePath: /CPPprojects/PolyU_DSA_datastructure_database/Queue_and_Stack/myQueue.cpp
 * @Description: Please implement
 */

#ifndef _MYQUEUE_CPP_J
#define _MYQUEUE_CPP_J

#include "myQueue.h"
#include <iostream>
using namespace std;

namespace gzx_simple_stl{
    template<typename T>
    MyQueue<T>::MyQueue(int capacity)
    {
        front = rear = nullptr;
        _capacity = _maximum = capacity;
    }

    template<typename T>
    MyQueue<T>::MyQueue(const MyQueue<T>& anotherQueue)
    {
        _maximum = anotherQueue._maximum;
        _capacity = anotherQueue._capacity;
        if(anotherQueue.front == nullptr)
        {
            front = rear = nullptr;
        }
        else
        {
            front = new LinkNode<T>(anotherQueue.front->_data);
            LinkNode<T>* ptr1 = anotherQueue.front->next;
            LinkNode<T>* ptr2 = this->front;
            while(ptr1)
            {
                LinkNode<T>* tempPtr = new LinkNode<T>(ptr1->_data);
                ptr2->next = tempPtr;
                ptr2 = ptr2->next;
                ptr1 = ptr1->next;
            }
            rear = ptr2;
        }
    }

    template<typename T>
    bool MyQueue<T>::Enqueue(T data)
    {
        if(IsFull())
            return false;
        if(IsEmpty())
        {
            front = new LinkNode<T>(data);
            rear = front;
        }
        else
        {
            LinkNode<T>* tempPtr = new LinkNode<T>(data);
            rear->next = tempPtr;
            rear = tempPtr;
        }
        _capacity --;
        return true;
    }

    template<typename T>
    bool MyQueue<T>::Dequeue(T& data)
    {
        if(IsEmpty())
            return false;
        data = front->_data;
        LinkNode<T>* tempPtr = front;
        front = front->next;
        if(front == nullptr)
            rear = nullptr;
        delete tempPtr;
        _capacity += 1;
        return true;
    }

    template<typename T>
    bool MyQueue<T>::IsEmpty() const
    {
        return _capacity == _maximum;
    }

    template<typename T>
    bool MyQueue<T>::IsFull() const
    {
        return _capacity == 0;
    }

    template<typename T>
    void MyQueue<T>::MakeEmpty()
    {
        LinkNode<T>* tempPtr;
        while(front)
        {
            tempPtr = front;
            front = front->next;
            delete tempPtr;
        }
        rear = nullptr;
        _capacity = _maximum;
    }

    template<typename T>
    MyQueue<T>::~MyQueue()
    {
        MakeEmpty();
    }
};

#endif
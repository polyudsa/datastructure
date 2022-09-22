/*
 * @author: Zhexuan Gu
 * @Date: 2022-09-21 23:29:55
 * @LastEditTime: 2022-09-22 15:04:21
 * @FilePath: /CPPprojects/PolyU_DSA_datastructure_database/Queue_and_Stack/myQueue.h
 * @Description: A simple definition of LinkList based Queue
 */

#ifndef _MYQUEUE_H_J
#define _MYQUEUE_H_J

#include "LinkNode.h"

/*
    关于capacity的解释，在myStack.h中做了解释
*/

namespace gzx_simple_stl{
    template <typename T>
    class MyQueue
    {
    private:
        LinkNode<T>* front;
        LinkNode<T>* rear;
        int _capacity;
        int _maximum;   
    public:
        MyQueue(int capacity);
        MyQueue(const MyQueue<T>& anotherQueue);
        bool Enqueue(T data);
        bool Dequeue(T& data);
        bool IsEmpty() const;
        bool IsFull() const;
        void MakeEmpty();
        ~MyQueue();
    };
    
    
};

#endif


/*
 * @author: Zhexuan Gu
 * @Date: 2022-09-21 15:37:05
 * @LastEditTime: 2022-09-22 15:03:46
 * @FilePath: /CPPprojects/PolyU_DSA_datastructure_database/Queue_and_Stack/myStack.h
 * @Description: a simple definition of stack
 */
#ifndef _MYSTACK_H_J
#define _MYSTACK_H_J
#include "LinkNode.h"

/*
    Robert PPT是表示可以一直Push，直到没内存空间才算放满。。。
    个人感觉没必要，就擅自加了capacity来管理空间大小
*/

namespace gzx_simple_stl{
    template<typename T>
    class MyStack
    {
    private:
        /* data */
        LinkNode<T>* _top;
        int _capacity;
        int _maximum;
        // for the array based situation, left to be done
    public:
        MyStack(int capacity);
        MyStack(LinkNode<T>* head, int capacity);
        MyStack(const MyStack<T>& anotherStack);
        ~MyStack();
        void MakeEmpty();
        bool IsEmpty() const;
        bool IsFull() const;
        bool Push(T data);
        bool Pop(T& data);
        // copy function
        void Copy(MyStack<T> oldStack, MyStack<T>& copy);
    };
};

#endif
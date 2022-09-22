/*
 * @author: Zhexuan Gu
 * @Date: 2022-09-21 17:36:52
 * @LastEditTime: 2022-09-22 13:34:41
 * @FilePath: /CPPprojects/PolyU_DSA_datastructure_database/Queue_and_Stack/test.cpp
 * @Description: Please implement
 */


#include <iostream>
#include "myStack.h"
#include "myStack.cpp"
#include "myQueue.h"
#include "myQueue.cpp"

using namespace std;
using namespace gzx_simple_stl;

void test_stack()
{
    MyStack<int> obj(5);
    int a = 3, b = 4, c = 5;
    int t;
    obj.Push(a);
    obj.Push(c);
    obj.Pop(t);
    cout << t << endl;
    obj.Push(b);
    obj.Pop(t);
    cout << t << endl;
    const MyStack<int> temp = static_cast<const MyStack<int>>(obj);
    cout << "Is obj empty? " << boolalpha << obj.IsEmpty() << endl;
    MyStack<int> obj2(temp);
    cout << "Is obj2 empty ? " << boolalpha << obj2.IsEmpty() << endl;
    obj2.Pop(t);
    cout << t << endl;
}

void test_queue()
{
    MyQueue<int> obj(5);
    int a = 3, b = 4, c = 5;
    int t;
    obj.Enqueue(a);
    obj.Enqueue(c);
    obj.Dequeue(t);
    cout << t << endl;
    obj.Enqueue(b);
    obj.Dequeue(t);
    cout << t << endl;
    const MyQueue<int> temp = static_cast<const MyQueue<int>>(obj);
    cout << "Is obj empty? " << boolalpha << obj.IsEmpty() << endl;
    MyQueue<int> obj2(temp);
    cout << "Is obj2 empty ? " << boolalpha << obj2.IsEmpty() << endl;
    obj2.Dequeue(t);
    cout << t << endl;
}

int main(){
    cout << "--------start testing--------\n";
    test_stack();
    cout << "----------seperator----------\n";
    test_queue();
    cout << "----------seperator----------\n";
    cout << "After testing, it's verified!\n";
    return 0;
}
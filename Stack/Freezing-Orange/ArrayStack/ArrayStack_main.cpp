#include<iostream>
using namespace std;
#include "ArrayStack.cpp"

int main(){
    ArrayStack<int>s(20);
    cout<<"栈初始化成功，最大储存空间为："<<s.size()<<endl;
    cout<<"栈是否为空：";
    if(s.isEmpty()) cout<<"是"<<endl;
    else cout<<"否"<<endl;
    s.push(1);
    s.push(2);
    s.push(3);
    cout<<"栈是否满：";
    if(s.isFull()) cout<<"是"<<endl;
    else cout<<"否"<<endl;
    cout<<"此时栈中有"<<s.length()<<"个元素，栈顶元素为"<<s.top()<<endl;
    s.pop();
    cout<<"弹出一次栈顶元素后，栈顶元素为"<<s.top()<<endl;
    return 0;
}
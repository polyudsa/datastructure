#include<iostream>
using namespace std;
#include "ArrayStack.cpp"

int main(){
    ArrayStack<int>s(20);
    cout<<"ջ��ʼ���ɹ�����󴢴�ռ�Ϊ��"<<s.size()<<endl;
    cout<<"ջ�Ƿ�Ϊ�գ�";
    if(s.isEmpty()) cout<<"��"<<endl;
    else cout<<"��"<<endl;
    s.push(1);
    s.push(2);
    s.push(3);
    cout<<"ջ�Ƿ�����";
    if(s.isFull()) cout<<"��"<<endl;
    else cout<<"��"<<endl;
    cout<<"��ʱջ����"<<s.length()<<"��Ԫ�أ�ջ��Ԫ��Ϊ"<<s.top()<<endl;
    s.pop();
    cout<<"����һ��ջ��Ԫ�غ�ջ��Ԫ��Ϊ"<<s.top()<<endl;
    return 0;
}
#include<iostream>
using namespace std;
#include "LinkList.cpp"

int main()
{
	int r[5]={1,2,3,4,5};
	LinkList<int>L(r,5);
	cout<<"ִ�в������ǰ���ݳ���Ϊ��"<<L.Length()<<endl;
	cout<<"ִ�в������ǰ����Ϊ��"<<endl;
	L.PrintList();
	try
	{
		L.Insert(0,3);
	}
	catch(char *s)
	{
		cout<<s<<endl;
	}
	cout<<"ִ�в������������Ϊ��"<<endl;
	L.PrintList();
	cout<<"ֵΪ5��Ԫ��λ��Ϊ��"; 
	cout<<L.Locate(5)<<endl;
	cout<<"ִ��׷�Ӳ���ǰ������Ϊ��"<<endl;
	L.PrintList();
	L.Add(6);
	cout<<"ִ��׷�Ӳ����������Ϊ��"<<endl;
	L.PrintList();
	cout<<"��ʱ����Ϊ��"<<L.Length()<<endl;
	cout<<"ִ��ɾ������ǰ����Ϊ��"<<endl;
	L.PrintList();
	try
	{
		L.Delete(0);
	 } 
	catch(char *s)
	{
		cout<<s<<endl;
	}
	cout<<"ִ��ɾ������������Ϊ��"<<endl;
	L.PrintList();
	return 0;
  }  
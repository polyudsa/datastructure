#include<iostream>
using namespace std;
#include "LinkList.cpp"

int main()
{
	int r[5]={1,2,3,4,5};
	LinkList<int>L(r,5);
	cout<<"执行插入操作前数据长度为："<<L.Length()<<endl;
	cout<<"执行插入操作前数据为："<<endl;
	L.PrintList();
	try
	{
		L.Insert(0,3);
	}
	catch(char *s)
	{
		cout<<s<<endl;
	}
	cout<<"执行插入操作后数据为："<<endl;
	L.PrintList();
	cout<<"值为5的元素位置为："; 
	cout<<L.Locate(5)<<endl;
	cout<<"执行追加操作前的数据为："<<endl;
	L.PrintList();
	L.Add(6);
	cout<<"执行追加操作后的数据为："<<endl;
	L.PrintList();
	cout<<"此时长度为："<<L.Length()<<endl;
	cout<<"执行删除操作前数据为："<<endl;
	L.PrintList();
	try
	{
		L.Delete(0);
	 } 
	catch(char *s)
	{
		cout<<s<<endl;
	}
	cout<<"执行删除操作后数据为："<<endl;
	L.PrintList();
	return 0;
  }  
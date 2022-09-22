/*
 * @author: Zhexuan Gu
 * @Date: 2022-08-26 10:41:07
 * @LastEditTime: 2022-09-21 14:14:35
 * @FilePath: /CPPprojects/Leetcode/DataStructure_PolyU/MyPriorityQueue.cpp
 * @Description: Implement a STL(vector) based priority_queue 
 */

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// 突发奇想，简单实现int类型的优先队列          ----可以写成模板，即vector<T> vec,但请确保你的模板类T重载了比较符哦。
class MyPriorityQueue{
private:
    // 用容器vector作为构造完全二叉树的根基
    vector<int> vec;
    int sz;
public:
    static void make_heap(vector<int>& obj);
    static void heapify(vector<int>& obj, int len, int size);
    MyPriorityQueue(vector<int>& obj);
    void push(int val);
    int size();
    void pop();
    int top();
    bool empty();
};

void MyPriorityQueue::make_heap(vector<int>& obj){
    // 构造初始大顶堆
    // EXAMPLE: 1 2 3 4 5    5
    int ptr = obj.size() / 2 - 1;   // 从第一个非叶子结点开始 如例： 5 / 2 - 1 = 1，即 2 代表的是第一个非叶子结点
    int len = obj.size();
    for(int i = ptr ; i >= 0 ; i --){
        heapify(obj, i, len);
    }
}

void MyPriorityQueue::heapify(vector<int>& obj, int ptr, int size){
    for(int i = ptr ; i < size ; ){
        // 以 i 为根结点，去和自己的左右子树根结点中较大的一个进行交换【因为默认构造大顶堆】
        int left = 2 * i + 1;
        int right = left + 1;
        int swapptr = left;
        // left的可行性也需要判断，因为有可能节点不断交换到叶子结点
        if(left < size && right < size && obj[right] > obj[left]){
            swapptr ++;
        }
        if(obj[swapptr] > obj[i]){
            swap(obj[swapptr], obj[i]);
            i = swapptr;
        }
        else break; // 毋需交换的话直接退出
    }
}

MyPriorityQueue::MyPriorityQueue(vector<int>& obj){
    vec = obj;
    sz = obj.size();
    make_heap(vec);
}

int MyPriorityQueue::top(){
    if(!empty())
        return vec[0];
    else
        return -1;
        exit(1);
}

bool MyPriorityQueue::empty(){
    return this->sz == 0;
}

int MyPriorityQueue::size(){
    return this->sz;
}

void MyPriorityQueue::push(int val){
    // 先直接放到vector的末尾
    vec.push_back(val);
    // 找到堆中此元素的父结点
    int ptr = sz;
    int parent = (sz - 1) / 2;
    // 队列大小s
    sz ++;
    // 从父结点开始不断往上找，找的仍旧是父结点，寻找是否有需要交换的地方
    for(int i = ptr ; i > 0 ; ){
        if(val > vec[parent]){
            swap(vec[i], vec[parent]);
            i = parent;
            // 向上寻找
            parent = (parent - 1) / 2;
        }
        else break;
    }
    
}

void MyPriorityQueue::pop(){
    // 巧了，和算法导论提供的思路一致
    // 把vector的第一个元素和末尾元素交换，然后pop_back掉，然后重新调用建堆方法
    if(!empty()){
        swap(vec[0], vec[sz - 1]);
        vec.pop_back();
        sz --;
        make_heap(vec);
    }
    else
        exit(1);
}

int main(){
    //-----------!!!!!demo!!!!!-----------//
    vector<int> vec{23, 0, 30, 35, 24, 7, 11};
    MyPriorityQueue obj(vec);
    cout << obj.top() << endl;  // 选取vec中的最大值 35
    obj.pop();                  // 弹出35
    obj.pop();                  // 弹出30
    cout << obj.top() << endl;  // 最大为24
    obj.push(99);               // 插入99
    obj.push(87);               // 插入87
    cout << obj.top() << endl;  // 最大为99
    obj.pop();                  // 弹出99
    cout << obj.top() << endl;  // 最大为87
    return 0;
}
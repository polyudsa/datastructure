/*
 * @author: Zhexuan Gu
 * @Date: 2022-09-28 15:32:24
 * @LastEditTime: 2022-09-30 15:50:47
 * @FilePath: /CPPprojects/PolyU_DSA_datastructure_database/Sortings/DifferentSortAlgorithms.h
 * @Description: Please implement
 */
#ifndef _SORT_H_J
#define _SORT_H_J

#include "yourObject.h"
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

/**
 * @description: 边上课边写好了大部分，有点草率
 * @event: 
 * @return 菜鸡
 */
namespace gzx_simple_stl{
    template<typename T>
    class Sort{
    private:
        vector<T> unsorted;
        vector<T> sorted;
        size_t num;
    public:
        Sort(vector<T> arr);
        void SelectionSort();
        void InsertionSort();
        void BubbleSort();
        // the following 3 functions are all for mergesort
        void MergeSort(int left, int right);
        void Merge(int left, int mid, int right);
        // void copy();         % 把copy操作合并到merge里了 ----

        void QuickSort(int left, int right);

        void HeapSort();
        void Heapify(int index, int nums);
        

        void ShowSorted();
    };
};

#endif
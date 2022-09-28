/*
 * @author: Zhexuan Gu
 * @Date: 2022-09-28 15:32:35
 * @LastEditTime: 2022-09-28 18:06:53
 * @FilePath: /CPPprojects/PolyU_DSA_datastructure_database/Sortings/DifferentSortAlgorithms.cpp
 * @Description: Please implement
 */
#ifndef _SORT_CPP_J
#define _SORT_CPP_J
#include "DifferentSortAlgorithms.h"
namespace gzx_simple_stl{
    template<typename T> 
    Sort<T>::Sort(vector<T> arr)
    {
        unsorted = sorted = arr;
        num = arr.size();
    }

    template<typename T> 
    void Sort<T>::SelectionSort()
    {
        if(num < 2) return;
        size_t smallest;
        for(size_t i = 0 ; i < num - 1 ; i ++)
        {
            smallest = i;
            for(size_t j = i + 1 ; j < num ; j ++)
            {
                if(sorted[j] < sorted[smallest])
                {
                    smallest = j;
                }
            }
            swap(sorted[smallest], sorted[i]);
        }
        ShowSorted();
    }

    template<typename T> 
    void Sort<T>::InsertionSort()
    {
        if(num < 2) return;
        for(size_t i = 1 ; i < num ; i ++)
        {
            T item = sorted[i];
            // then find the appropriate position to insert
            for(size_t j = i ; j > 0 && sorted[j - 1] > item ; j --)
            {
                swap(sorted[j], sorted[j - 1]);
            }
        }
        ShowSorted();
    }

    template<typename T> 
    void Sort<T>::BubbleSort()
    {
        if(num < 2) return;
        for(size_t i = 0 ; i < num ; i ++)
        {
            bool swapped = false;
            // 与ppt上不同，这里多减去一个i，因为经过轮排序，最大的i个数已经呈有序排列在数组尾部了
            for(size_t j = 0 ; j < num - i - 1 ; j ++)
            {
                if(sorted[j] > sorted[j + 1])
                {
                    swap(sorted[j], sorted[j + 1]);
                    swapped = true;
                }
            }
            if(!swapped) break;
        }
        ShowSorted();
    }

    template<typename T> 
    void Sort<T>::MergeSort(int left, int right)
    {
        if(left < right)
        {
            int mid = (left + right) >> 1;
            MergeSort(left, mid);
            MergeSort(mid + 1, right);
            Merge(left, mid, right);
        }
    }

    template<typename T> 
    void Sort<T>::Merge(int left, int mid, int right)
    {
        int i = left, j = mid + 1;
        int ptr = left;
        while(i <= mid && j <= right)
        {
            if(unsorted[i] < unsorted[j])
            {
                sorted[ptr++] = unsorted[i ++];
            }
            else
            {
                sorted[ptr++] = unsorted[j ++];
            }
        }
        while(i <= mid)
            sorted[ptr ++] = unsorted[i ++];
        while(j <= right) 
            sorted[ptr ++] = unsorted[j ++];
        for(int k = left ; k <= right ; k ++)
        {
            unsorted[k] = sorted[k];
        }
    }

    template<typename T> 
    void Sort<T>::QuickSort(int left, int right)
    {
        T pivot = sorted[left];
        size_t i = left + 1, j = right;
        while(i <= j)
        {
            while(i <= j && sorted[i] <= pivot)
            {
                i ++;
            }
            if(i > j)
            {
                break;
            }
            else
                swap(sorted[i], sorted[j --]);
            while(i <= j && sorted[j] >= pivot)
            {
                j --;
            }
            if(i > j)
            {
                break;
            }
            else
                swap(sorted[j], sorted[i ++]);
        }
        swap(sorted[left], sorted[j]);
        if(j - left > 1)
            QuickSort(left, j - 1);
        if(right - j > 1)
            QuickSort(j + 1, right);
    }

    template<typename T> 
    void Sort<T>::ShowSorted()
    {
        for(size_t i = 0 ; i < num ; i ++)
        {
            cout << sorted[i] << " ";
        }
        cout << endl;
        // eliminate the effect to next round sort
        sorted = unsorted;
    }
};
#endif
/*
 * @author: Zhexuan Gu
 * @Date: 2022-09-28 15:32:40
 * @LastEditTime: 2022-09-30 15:56:45
 * @FilePath: /CPPprojects/PolyU_DSA_datastructure_database/Sortings/test.cpp
 * @Description: Please implement
 */
#include "DifferentSortAlgorithms.h"
#include "DifferentSortAlgorithms.cpp"
using namespace gzx_simple_stl;


int main()
{
    vector<int> vec{23, 30, 3, 0, 35, 77, 99, 13, 11, 2, 23333, 666, 5112};
    Sort<int> sort(vec);
    
    sort.SelectionSort();
    //sort.ShowSorted();
    sort.InsertionSort();
    //sort.ShowSorted();
    sort.BubbleSort();

    sort.QuickSort(0, vec.size() - 1);
    sort.ShowSorted();

    sort.HeapSort();
    
    //------Cautious: MergeSort will change the original unsorted array！----//
    sort.MergeSort(0, vec.size() - 1);
    sort.ShowSorted();
    return 0;
}
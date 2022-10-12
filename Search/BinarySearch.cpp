/*
 * @author: Zhexuan Gu
 * @Date: 2022-10-12 12:52:20
 * @LastEditTime: 2022-10-12 13:33:29
 * @FilePath: /CPPprojects/PolyU_DSA_datastructure_database/Search/BinarySearch.cpp
 * @Description: Please implement
 */
#ifndef _BSEARCH_CPP_J
#define _BSEARCH_CPP_J
#include "BinarySearch.h"

namespace gzx_simple_search{
    template<typename T> 
    bool BinarySearch(std::vector<T> arr, T target, size_t left, size_t right, size_t& location)
    {
        if(left > right) return false;
        size_t middle;
        middle = left + ((right - left) >> 1);              // 一个防溢出的好习惯。。 避免left + right溢出
        if(target == arr[middle]){
            location = middle;
            return true;
        }
        else if(target < arr[middle]){
            // search the left part
            // 和ppt上大同小异，个人感觉这种方式更好理解
            return BinarySearch(arr, target, left, middle - 1, location);
        }
        else{
            return BinarySearch(arr, target, middle + 1, right, location);
        }
    }
}
#endif
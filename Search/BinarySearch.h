/*
 * @author: Zhexuan Gu
 * @Date: 2022-10-12 12:53:15
 * @LastEditTime: 2022-10-12 15:06:11
 * @FilePath: /CPPprojects/PolyU_DSA_datastructure_database/Search/BinarySearch.h
 * @Description: Please implement
 */

#ifndef _BSEARCH_H_J
#define _BSEARCH_H_J
#include <iostream>
#include <vector>

namespace gzx_simple_search{
    template<typename T> 
    bool BinarySearch(std::vector<T> arr, T target, size_t left, size_t right, size_t& location);
}

#endif
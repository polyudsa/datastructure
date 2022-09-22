/*
 * @author: Zhexuan Gu
 * @Date: 2022-09-21 15:32:18
 * @LastEditTime: 2022-09-22 13:27:47
 * @FilePath: /CPPprojects/PolyU_DSA_datastructure_database/Queue_and_Stack/LinkNode.h
 * @Description: a simple node definition
 */

#ifndef _LINKNODE_H_J
#define _LINKNODE_H_J

#include <iostream>
using namespace std;
namespace gzx_simple_stl{
    template <typename T>
    struct LinkNode{
        /* data */
        T _data;
        LinkNode<T>* next;
        LinkNode(T data):_data(data), next(nullptr){}
        LinkNode(T data, LinkNode<T>* nextptr):_data(data), next(nextptr){}
        LinkNode<T> operator=(LinkNode<T>* tempPtr){
            this->_data = tempPtr->_data;
            this->next = tempPtr->next;
            return *this;
        };
    };
};

#endif
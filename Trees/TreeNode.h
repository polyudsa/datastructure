/*
 * @author: Zhexuan Gu
 * @Date: 2022-09-23 23:40:45
 * @LastEditTime: 2022-09-25 14:24:34
 * @FilePath: /CPPprojects/PolyU_DSA_datastructure_database/Trees/TreeNode.h
 * @Description: A simple definition of treenode
 */

#ifndef _TREENODE_H_J
#define _TREENODE_H_J

#include <iostream>

namespace gzx_simple_datastructure{
    template<typename T>
    struct TreeNode
    {
        T _data;
        TreeNode<T>* leftchild; // 左孩子，同样也是当前节点左子树的根节点
        TreeNode<T>* rightchild;// 同上，换成"右"
        TreeNode<T>* siblings;  // 本次代码中不会实现，只需知道什么是兄弟节点即可
        TreeNode<T>* parent;    // 本次代码也不跟踪父节点，因为没有使用的地方。。
        TreeNode(T data):_data(data), leftchild(nullptr), rightchild(nullptr), siblings(nullptr), parent(nullptr){};
        TreeNode<T>* operator=(TreeNode<T>* node){
            this->_data = node->_data;
            this->siblings = node->siblings;
            this->leftchild = node->leftchild;
            this->rightchild = node->rightchild;
            this->parent = node->parent;
            return this;
        };
    };
};

#endif

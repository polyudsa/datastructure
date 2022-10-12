/*
 * @author: Zhexuan Gu
 * @Date: 2022-09-23 23:41:15
 * @LastEditTime: 2022-10-12 11:56:50
 * @FilePath: /CPPprojects/PolyU_DSA_datastructure_database/Trees/Tree.cpp
 * @Description: a implementation of tree
 */

#ifndef _TREE_CPP_J
#define _TREE_CPP_J

/*------------------其实recursive版本的遍历是很简单的，最好能实现一下非递归版本------------------*/

#include "Tree.h"
namespace gzx_simple_datastructure{
    /**
     * @description: 三个构造函数这次加了点输出提示，可以debug看看继承后构造有没有出什么问题  ----  析构函数同理
     * @event: null
     * @return null
     */    
    template<typename T>
    Tree<T>::Tree()
    {
        _root = nullptr;
        cout << "create tree object by set root to nullptr\n";
    }

    template<typename T>
    Tree<T>::Tree(TreeNode<T>* root)
    {
        _root = root;
        cout << "create tree object by set root to the parameter root\n";
    }

    template<typename T>
    Tree<T>::Tree(vector<T> vec)
    {
        // 也是一种较为常见的建树方法，用一个数组建立
        // 下标为0的就设置为根节点，然后下标1为0的左孩子，2就是0的右孩子。  接着3又是1的左孩子 ......
        size_t initptr = 0;
        _root = createTreeByVector(vec, initptr);
        cout << "create tree object by vector\n";
    }

    template<typename T>
    TreeNode<T>* Tree<T>::createTreeByVector(vector<T> vec, size_t ptr)
    {
        if(ptr >= vec.size() || vec[ptr] == '0')
            return nullptr;
        TreeNode<T>* tempPtr = new TreeNode<T>(vec[ptr]);
        tempPtr->leftchild = createTreeByVector(vec, ptr * 2 + 1);
        tempPtr->rightchild = createTreeByVector(vec, 2 * ptr + 2);
        return tempPtr;
    }

    template<typename T>
    TreeNode<T>* Tree<T>::getRoot()
    {
        return _root;
    }

    template<typename T>
    void Tree<T>::preOrderTraverse(TreeNode<T>* root)
    {
        if(root)
        {
            // 先序遍历口诀 根左右
            cout << root->_data << " ";
            preOrderTraverse(root->leftchild);
            preOrderTraverse(root->rightchild);
        }
    }

    template<typename T>
    void Tree<T>::inOrderTraverse(TreeNode<T>* root)
    {
        if(root)
        {
            inOrderTraverse(root->leftchild);
            cout << root->_data << " ";
            inOrderTraverse(root->rightchild);
        }
    }

    template<typename T>
    void Tree<T>::postOrderTraverse(TreeNode<T>* root)
    {
        if(root)
        {
            postOrderTraverse(root->leftchild);
            postOrderTraverse(root->rightchild);
            cout << root->_data << " ";
        }
    }

    template<typename T>
    Tree<T>::~Tree()
    {
        cout << "delete tree object\n";
    }
};

#endif
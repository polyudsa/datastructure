/*
 * @author: Zhexuan Gu
 * @Date: 2022-09-23 23:41:49
 * @LastEditTime: 2022-09-25 14:05:32
 * @FilePath: /CPPprojects/PolyU_DSA_datastructure_database/Trees/BinarySearchTree.h
 * @Description: Please implement
 */
#ifndef _BINARYSEARCHTREE_H_J
#define _BINARYSEARCHTREE_H_J

#include "Tree.h"
#include <iostream>

namespace gzx_simple_datastructure{
    /**
     * @description: 二叉树用了继承，主要是避免了 tree traversal的重写
     * @event: null
     * @return null
     */    
    template<typename T>
    class BinarySearchTree : public Tree<T>
    {
    private:
        // root it just same as Tree Class
    public:
        BinarySearchTree(vector<T> data);
        TreeNode<T>* createTreeByVectorRecursive(TreeNode<T>* root, T data);
        bool Search(T data);
        void DeleteNode(T data);
        void LeafCondition(TreeNode<T>* parent, TreeNode<T>* Node);
        void OneChildCondition(TreeNode<T>* parent, TreeNode<T>* Node);
        void TwoChildrenCondition(TreeNode<T>* parent, TreeNode<T>* Node);
        T findMin();
        T findMax();
        ~BinarySearchTree();
    };
};

#endif
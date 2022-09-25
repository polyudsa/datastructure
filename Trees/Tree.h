/*
 * @author: Zhexuan Gu
 * @Date: 2022-09-23 23:41:38
 * @LastEditTime: 2022-09-25 14:05:25
 * @FilePath: /CPPprojects/PolyU_DSA_datastructure_database/Trees/Tree.h
 * @Description: a simple definition of tree
 */

#ifndef _TREE_H_J
#define _TREE_H_J

#include "TreeNode.h"
#include <vector>
using namespace std;

                      // ----------这里尤指 "Binary Tree" 二叉树(因为建森林懒得编数据)----------//

namespace gzx_simple_datastructure{
    template<typename T>
    class Tree
    {
    protected:
        TreeNode<T>* _root;
    public:
        Tree();
        Tree(vector<T> vec);
        Tree(TreeNode<T>* root);
        TreeNode<T>* createTreeByVector(vector<T> vec, size_t ptr);
        void preOrderTraverse(TreeNode<T>* root);
        void inOrderTraverse(TreeNode<T>* root);
        void postOrderTraverse(TreeNode<T>* root);
        TreeNode<T>* getRoot();
        virtual ~Tree();
    };
};

#endif
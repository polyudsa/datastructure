/*
 * @author: Zhexuan Gu
 * @Date: 2022-09-23 23:41:59
 * @LastEditTime: 2022-09-25 14:40:38
 * @FilePath: /CPPprojects/PolyU_DSA_datastructure_database/Trees/BinarySearchTree.cpp
 * @Description: a simple implementation of tree
 */
#ifndef _BINARYSEARCHTREE_CPP_J
#define _BINARYSEARCHTREE_CPP_J

#include "BinarySearchTree.h"

namespace gzx_simple_datastructure{
    template<typename T>
    BinarySearchTree<T>::BinarySearchTree(vector<T> data)
    {
        Tree<T>::_root = new TreeNode<T>(data[0]);
        for(size_t i = 1 ; i < data.size() ; i ++)
        {
            createTreeByVectorRecursive(Tree<T>::_root, data[i]);
        }
        cout << "create bst object by vector\n";
    }

    /**
     * @description: 函数名字起草率了，其实插入某个元素时也可以用这个function，但不打算改了
     * @event:  传入树的根节点，待插入数据
     * @return  insert one node to the tree, so the returned obj is not so important
     */    
    template<typename T>
    TreeNode<T>* BinarySearchTree<T>::createTreeByVectorRecursive(TreeNode<T>* root, T data)
    {
        if(!root)
            return new TreeNode<T>(data);
        else
        {
            if(data > root->_data)
                root->rightchild = createTreeByVectorRecursive(root->rightchild, data);
            else if(data < root->_data)
                root->leftchild = createTreeByVectorRecursive(root->leftchild, data);
            else
            {
                cout << "The element " << data << " has been in the tree, do not insert!" << endl;
                return nullptr;
            }
        }
        return root;
    }

    /**
     * @description: 不采用递归了，因为顺序来就不难
     * @event: judge whether element data is in the tree
     * @return boolean
     */    
    template<typename T>
    bool BinarySearchTree<T>::Search(T data)
    {
        TreeNode<T>* tempPtr = Tree<T>::_root;
        while(tempPtr && tempPtr->_data != data)
        {
            if(data > tempPtr->_data)
                tempPtr = tempPtr->rightchild;
            else
                tempPtr = tempPtr->leftchild;
        }
        return tempPtr && tempPtr->_data == data;
    }

    template<typename T> 
    void BinarySearchTree<T>::LeafCondition(TreeNode<T>* parent, TreeNode<T>* Node)
    {
        // simplest case, just delete Node is okay!
        // but first deal with parent node, or maybe in the future some behavior maybe not defined
        if(parent->leftchild == Node){
            parent->leftchild = nullptr;
        }
        else{
            parent->rightchild = nullptr;
        }
        delete Node;
    }

    template<typename T> 
    void BinarySearchTree<T>::OneChildCondition(TreeNode<T>* parent, TreeNode<T>* Node)
    {
        //this condition is also simple, we just use the only child to replace Node is okay!
        TreeNode<T>* childNode = Node->leftchild != nullptr ? Node->leftchild : Node->rightchild;
        if(parent->leftchild == Node)
            parent->leftchild = childNode;
        else parent->rightchild = childNode;
        delete Node;
    }

    template<typename T> 
    void BinarySearchTree<T>::TwoChildrenCondition(TreeNode<T>* parent, TreeNode<T>* Node)
    {
        // a little bit more complicated
        // we use the minimum key in the Node's right subtree to replace Node
        // then we just delete the minimum node in the right subtree and change the Key value of Node is Okay

        // first to find the minimum node
        TreeNode<T>* rightSubTree = Node->rightchild;
        TreeNode<T>* tempPtr = Node;    // to record the minimum node's parent
        while(rightSubTree->leftchild)
        {
            tempPtr = rightSubTree;
            rightSubTree = rightSubTree->leftchild;
        }

        // means the Node's rightchild is the chosen one to replace Node!!
        if(tempPtr->rightchild == rightSubTree)
        {
            tempPtr->rightchild = nullptr;
        }

        else
        {
            // the minimum Node may have right child
            // as the minimum node is chosen to replace Node, it finally should be deleted
            // the minimum node definitely has no leftsubtree, otherwise, it's not the minimum anymore
            // however, it may have right subtree, so if have, the right subtree is going to be the leftsubtree of the minimum node's parent
            tempPtr->leftchild = rightSubTree->rightchild;
        }

        // just change value
        Node->_data = rightSubTree->_data;

        // delete minimum node
        delete rightSubTree;
    }

    template<typename T>
    void BinarySearchTree<T>::DeleteNode(T data)
    {
        TreeNode<T>* parent, *tempPtr;           // parent指向被删除节点的父亲，tempPtr则直接指向被删除节点
        parent = nullptr, tempPtr = Tree<T>::_root;
        while(tempPtr && tempPtr-> _data != data)
        {
            parent = tempPtr;
            if(data > tempPtr->_data)
                tempPtr = tempPtr->rightchild;
            else
                tempPtr = tempPtr->leftchild;
        }
        // 用这个数量来区分ppt中涉及的三种情况
        int childrenNum = (tempPtr->leftchild != nullptr) + (tempPtr->rightchild != nullptr);
        switch (childrenNum)
        {
        case 0:
            LeafCondition(parent, tempPtr);
            break;
        case 1:
            OneChildCondition(parent, tempPtr);
            break;
        case 2:
            TwoChildrenCondition(parent, tempPtr);
            break;
        default:
            break;
        }
    }

    template<typename T>
    T BinarySearchTree<T>::findMin(){
        TreeNode<T>* tempPtr = Tree<T>::_root;
        while(tempPtr->leftchild){
            tempPtr = tempPtr->leftchild;
        }
        return tempPtr->_data;
    }

    template<typename T>
    T BinarySearchTree<T>::findMax(){
        TreeNode<T>* tempPtr = Tree<T>::_root;
        while(tempPtr->rightchild){
            tempPtr = tempPtr->rightchild;
        }
        return tempPtr->_data;
    }

    template<typename T>
    BinarySearchTree<T>::~BinarySearchTree()
    {
        cout << "delete binary search tree object\n";
    }
};

#endif
/*
 * @author: Zhexuan Gu
 * @Date: 2022-09-23 23:42:05
 * @LastEditTime: 2022-09-25 14:37:44
 * @FilePath: /CPPprojects/PolyU_DSA_datastructure_database/Trees/test.cpp
 * @Description: Please implement
 */
#include <iostream>
#include "Tree.h"
#include "Tree.cpp"
#include "BinarySearchTree.h"
#include "BinarySearchTree.cpp"

using namespace std;
using namespace gzx_simple_datastructure; 

void changeTree(TreeNode<char>* &oldroot, TreeNode<char>* newroot)
{
    oldroot = newroot;
}

void test_binarysearch_tree()
{
    vector<int> vec{6, 2, 8, 1, 4, 3};
    BinarySearchTree<int>* bst = new BinarySearchTree<int>(vec);
    TreeNode<int>* root = bst->getRoot();
    // 建立二叉搜索树，并利用中序遍历，可以发现输出了有序的插入数组(就是构造用的那个数组)
    bst->inOrderTraverse(root);
    cout << endl;
    
    // 二叉搜索树的搜索，插入，findMax，findMin和delete的测试
    // 1. 插入
    cout << "---------- inserting 5 into the tree ----------\n";
    bst->createTreeByVectorRecursive(root, 5);
    bst->inOrderTraverse(root);
    cout << endl;

    // 2.找最大最小
    cout << "the biggest element in the tree is: " << bst->findMax() << endl;
    cout << "the smallest element in the tree is: " << bst->findMin() << endl;

    // 3.搜索
    int data = 9;
    cout << "9 is in the tree ? " << boolalpha << bst->Search(data) << endl;
    data = 4;
    cout << "4 is in the tree ? " << boolalpha << bst->Search(data) << endl;

    // 4. 删除
    // 删除前可以先行判断一些这个值有没有在树中
    data = 4;
    if(bst->Search(data))
    {
        bst->DeleteNode(data);
        cout << "----------After deleting value " << data << " ,the binary search tree become----------\n";
        bst->inOrderTraverse(root);
        cout << endl;
    }
    else cout << "The Key Value is not in the tree, cannot delete!" << endl;

    delete bst;
}

void test_tree_traverse()
{
    // ‘0’代表空指针
    vector<char> vec{'+', '+', '*', 'a', '*', '+', 'g', '0', '0', 'b', 'c', '*', 'f', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'd', 'e'};
    Tree<char>* tree = new Tree<char>(vec);
    TreeNode<char>* root = tree->getRoot();         // 这里存在隐患，即外部修改root 会导致类内部的树也被损坏，有待改进
    //  一个无意的操作就会置空右子树，类里面的一并被改变了
    //root->rightchild = nullptr;         
    //root->_data = xxx   同样是危险的操作
    //
    cout << "Inorder Traverse: ";
    tree->inOrderTraverse(root);
    cout << endl;
    // 控制台会打印输出，未添加括号，将就着看吧......
    cout << "Prerder Traverse: ";
    tree->preOrderTraverse(root);
    cout << endl;

    cout << "Postrder Traverse: ";
    tree->postOrderTraverse(root);
    cout << endl;

    delete tree;
}

int main(){
    cout << "--------start testing--------\n";
    test_tree_traverse();
    cout << "----------seperator----------\n";
    test_binarysearch_tree();
    cout << "----------seperator----------\n";
    cout << "After testing, it's verified!\n";
    return 0;
}

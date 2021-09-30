package BinarySearchTrees.evil;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

/**
 * @Author: Twiss
 * @Date: 2021/9/3 10:23 下午
 */
public class BinaryTreeTest {

    @Test
    public void testInorder(){
        BinarySearchTree treeNode = createTree();
        TreeNode root = treeNode.getRootNode();
        int depth = treeNode.getTreeDepth(root);
        assertEquals(depth,5);
    }

    private BinarySearchTree createTree(){
        BinarySearchTree tree = new BinarySearchTree();
        tree.insert(9,9);
        tree.insert(2,2);
        tree.insert(1,1);
        tree.insert(6,6);
        tree.insert(3,3);
        tree.insert(8,8);
        tree.insert(4,4);
        return tree;
    }

}

package BinarySearchTrees.evil;

/**
 * @Author: Twiss
 * @Date: 2021/9/15 7:08 下午
 */
public abstract class AbstractBinaryTree {
    /**
     * 查找指定节点
     * @param key
     * @return
     */
    public abstract TreeNode find(int key);

    /**
     * 更新节点值
     * @param key
     * @param value
     * @return
     */
    public abstract Boolean update(int key, int value);

    /**
     * 插入节点
     * @param key
     * @param val
     */
    public abstract void insert(int key, int val);

    /**
     * 删除节点
     * @param key
     * @return
     */
    public abstract Boolean delete(int key);

    /**
     * 获取树的层数
     * @param root
     * @return
     */
    public abstract int getTreeDepth(TreeNode root);

    /**
     * 将树存入数组中
     * @param currNode
     * @param rowIndex
     * @param columnIndex
     * @param res
     * @param treeDepth
     */
    public abstract void writeArray(TreeNode currNode, int rowIndex, int columnIndex, String[][] res, int treeDepth);

    /**
     * 打印树
     * @param root
     */
    public abstract void show(TreeNode root);
    /**
     * 得到删除节点的中继后节点
     * @param delNode
     * @return
     */
    public abstract TreeNode getDelNodeSuccessor(TreeNode delNode);

    /**
     * 先序遍历
     * @param rootNode
     */
    public abstract void preOrder(TreeNode rootNode);
    /**
     * 中序遍历
     * @param rootNode
     */
    public abstract void inOrder(TreeNode rootNode);
    /**
     * 后序遍历
     * @param rootNode
     */
    public abstract void postOrder(TreeNode rootNode);
}

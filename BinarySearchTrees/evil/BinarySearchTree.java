package BinarySearchTrees.evil;

/**
 * 二叉搜索树
 *
 * @Author: Twiss
 * @Date: 2021/9/15 3:27 下午
 */
public class BinarySearchTree extends AbstractBinaryTree {

    private TreeNode rootNode;

    public TreeNode getRootNode() {
        return rootNode;
    }

    public void setRootNode(TreeNode rootNode) {
        this.rootNode = rootNode;
    }

    /**
     * 查找指定节点
     *
     * @param key
     * @return
     */
    @Override
    public TreeNode find(int key) {
        TreeNode currentNode = this.rootNode;
        while (currentNode != null && (currentNode.key != key)) {
            // 遵循左节点小于其父节点
            if (currentNode.key > key) {
                currentNode = currentNode.leftChild;
            } else {
                currentNode = currentNode.rightChild;
            }
        }
        return currentNode;
    }

    /**
     * 更新节点值
     *
     * @param key
     * @param value
     * @return
     */
    @Override
    public Boolean update(int key, int value) {
        return null;
    }

    /**
     * 插入节点
     *
     * @param key
     * @param val
     */
    @Override
    public void insert(int key, int val) {
        if (this.rootNode == null) {
            this.rootNode = new TreeNode(key, val);
            return;
        }
        TreeNode currentNode = this.rootNode;
        TreeNode parentNode = this.rootNode;
        boolean isLeftChild = false;
        while (currentNode != null && (currentNode.key != key)) {
            parentNode = currentNode;
            // 遵循左节点小于其父节点
            if (currentNode.key > key) {
                currentNode = currentNode.leftChild;
                isLeftChild = true;
            } else {
                currentNode = currentNode.rightChild;
                isLeftChild = false;
            }
        }
        // 插入节点
        if (parentNode != currentNode) {
            TreeNode newNode = new TreeNode(key, val);
            if (isLeftChild) {
                parentNode.leftChild = newNode;
            } else {
                parentNode.rightChild = newNode;
            }
        } else {
            currentNode.setVal(val);
        }
    }

    /**
     * 删除节点
     *
     * @param key
     * @return
     */
    @Override
    public Boolean delete(int key) {
        TreeNode currentNode = this.rootNode;
        TreeNode parentNode = this.rootNode;
        Boolean isLeftChild = true;
        while (currentNode != null && (currentNode.key != key)) {
            parentNode = currentNode;
            // 遵循左节点小于其父节点
            if (currentNode.key > key) {
                currentNode = currentNode.leftChild;
                isLeftChild = true;
            } else {
                currentNode = currentNode.rightChild;
                isLeftChild = false;
            }
        }
        if (currentNode==null){
            return false;
        }
        // 要删除的节点为叶子节点
        if ((currentNode.leftChild==null)&&(currentNode.rightChild)==null){
            if (currentNode==this.rootNode){
                this.rootNode = null;
            }else if (isLeftChild){
                currentNode.leftChild = null;
            }else {
                currentNode.rightChild = null;
            }
        }else if ((currentNode.rightChild==null)&&(currentNode.leftChild!=null)){
            if (currentNode==this.rootNode){
                this.rootNode = currentNode.leftChild;
            }else if (isLeftChild){
                parentNode.leftChild = currentNode.leftChild;
            }else {
                parentNode.rightChild = currentNode.leftChild;
            }
        }else if ((currentNode.rightChild!=null)&&(currentNode.leftChild==null)){
            if (currentNode==this.rootNode){
                this.rootNode = currentNode.rightChild;
            }else if (isLeftChild){
                parentNode.leftChild = currentNode.rightChild;
            }else {
                parentNode.leftChild = currentNode.rightChild;
            }
        }else {
            TreeNode directNode = this.getDelNodeSuccessor(currentNode);
            currentNode.key = directNode.key;
            currentNode.val = directNode.val;
        }
        return true;
    }

    /**
     * 得到删除节点的中继后节点
     *
     * @param delNode
     * @return
     */
    @Override
    public TreeNode getDelNodeSuccessor(TreeNode delNode) {
        TreeNode parentNode = delNode;
        TreeNode directPostNode = delNode;
        TreeNode current = delNode.rightChild;
        while (current!=null){
            parentNode = directPostNode;
            directPostNode = current;
            current = current.leftChild;
        }
        if (directPostNode!=delNode.rightChild){
            parentNode.leftChild = directPostNode.rightChild;;
            directPostNode.rightChild = null;
        }
        return directPostNode;
    }

    @Override
    public int getTreeDepth(TreeNode root) {
        return root == null ? 0 : (1 + Math.max(getTreeDepth(root.leftChild), getTreeDepth(root.rightChild)));
    }

    @Override
    public void writeArray(TreeNode currNode, int rowIndex, int columnIndex, String[][] res, int treeDepth) {
        // 保证输入的树不为空
        if (currNode == null) {
            return;
        }
        // 先将当前节点保存到二维数组中
        res[rowIndex][columnIndex] = String.valueOf(currNode.val);

        // 计算当前位于树的第几层
        int currLevel = ((rowIndex + 1) / 2);
        // 若到了最后一层，则返回
        if (currLevel == treeDepth) {
            return;
        }
        // 计算当前行到下一行，每个元素之间的间隔（下一行的列索引与当前元素的列索引之间的间隔）
        int gap = treeDepth - currLevel - 1;

        // 对左儿子进行判断，若有左儿子，则记录相应的"/"与左儿子的值
        if (currNode.leftChild != null) {
            res[rowIndex + 1][columnIndex - gap] = "/";
            writeArray(currNode.leftChild, rowIndex + 2, columnIndex - gap * 2, res, treeDepth);
        }

        // 对右儿子进行判断，若有右儿子，则记录相应的"\"与右儿子的值
        if (currNode.rightChild != null) {
            res[rowIndex + 1][columnIndex + gap] = "\\";
            writeArray(currNode.rightChild, rowIndex + 2, columnIndex + gap * 2, res, treeDepth);
        }
    }

    @Override
    public void show(TreeNode root) {
        if (root == null) {
            System.out.println("EMPTY!");
        }
        // 得到树的深度
        int treeDepth = getTreeDepth(root);

        // 最后一行的宽度为2的（n - 1）次方乘3，再加1
        // 作为整个二维数组的宽度
        int arrayHeight = treeDepth * 2 - 1;
        int arrayWidth = (2 << (treeDepth - 2)) * 3 + 1;
        // 用一个字符串数组来存储每个位置应显示的元素
        String[][] res = new String[arrayHeight][arrayWidth];
        // 对数组进行初始化，默认为一个空格
        for (int i = 0; i < arrayHeight; i ++) {
            for (int j = 0; j < arrayWidth; j ++) {
                res[i][j] = " ";
            }
        }

        // 从根节点开始，递归处理整个树
        // res[0][(arrayWidth + 1)/ 2] = (char)(root.val + '0');
        writeArray(root, 0, arrayWidth/ 2, res, treeDepth);

        // 此时，已经将所有需要显示的元素储存到了二维数组中，将其拼接并打印即可
        for (String[] line: res) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < line.length; i ++) {
                sb.append(line[i]);
                if (line[i].length() > 1 && i <= line.length - 1) {
                    i += line[i].length() > 4 ? 2: line[i].length() - 1;
                }
            }
            System.out.println(sb.toString());
        }
    }

    /**
     * 先序遍历
     *
     * @param rootNode
     */
    @Override
    public void preOrder(TreeNode rootNode) {
        if (rootNode != null) {
            System.out.println(rootNode.key + " " + rootNode.val);
            this.preOrder(rootNode.leftChild);
            this.preOrder(rootNode.rightChild);
        }
    }

    /**
     * 中序遍历
     *
     * @param rootNode
     */
    @Override
    public void inOrder(TreeNode rootNode) {
        if (rootNode != null) {
            this.inOrder(rootNode.leftChild);
            System.out.println(rootNode.key + " " + rootNode.val);
            this.inOrder(rootNode.rightChild);
        }
    }

    /**
     * 后序遍历
     *
     * @param rootNode
     */
    @Override
    public void postOrder(TreeNode rootNode) {
        if (rootNode != null) {
            this.postOrder(rootNode.leftChild);
            this.postOrder(rootNode.rightChild);
            System.out.println(rootNode.key + " " + rootNode.val);
        }
    }

    public static void main(String[] args) {
        BinarySearchTree tree = new BinarySearchTree();
        tree.insert(6,6);
        tree.insert(3,3);
        tree.insert(14,14);
        tree.insert(16,16);
        tree.insert(10,10);
        tree.insert(9,9);
        tree.insert(13,13);
        tree.insert(11,11);
        tree.insert(12,12);
        System.out.println("删除前是递增有序");
        tree.inOrder(tree.getRootNode());// 中序遍历操作
        tree.update(12, 200);
        System.out.println("更新节点值中序遍历结果  key=12的值");
        tree.inOrder(tree.getRootNode());
        System.out.println("删除节点10之后遍历结果");

        tree.delete(10);// 删除操作
        tree.inOrder(tree.getRootNode());

        BinarySearchTree tree2 = new BinarySearchTree();
        tree2.insert(9,9);
        tree2.insert(2,2);
        tree2.insert(1,1);
        tree2.insert(6,6);
        tree2.insert(3,3);
        tree2.insert(8,8);
        tree2.insert(4,4);
        System.out.println("删除前是递增有序2：");
        tree2.inOrder(tree2.getRootNode());// 中序遍历操作
        tree2.delete(9);
        tree2.inOrder(tree2.getRootNode());
        tree2.show(tree2.getRootNode());

        BinarySearchTree tree3 = new BinarySearchTree();
        tree3.insert(20,20);
        tree3.insert(1,1);
        tree3.insert(10,10);
        tree3.insert(19,19);
        tree3.insert(16,16);
        System.out.println("删除前是递增有序3：");
        tree3.inOrder(tree3.getRootNode());// 中序遍历操作
        tree3.delete(20);
        tree3.inOrder(tree3.getRootNode());
        tree3.show(tree3.getRootNode());
    }
}

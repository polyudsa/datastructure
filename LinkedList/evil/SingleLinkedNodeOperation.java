/**
 * 单向链表的增删改查操作
 *
 * @Author: Twiss
 * @Date: 2021/9/1 3:23 下午
 */
public class SingleLinkedNodeOperation {

    /**
     * 定义头节点
     */
    private LinkedNode root;

    /**
     * 添加节点操作
     *
     * @param val
     */
    public void addNode(String val) {
        LinkedNode newNode = new LinkedNode(val);
        if (this.root == null) {
            root = newNode;
        } else {
            // 如果有头节点则调自动增加
            this.root.add(newNode);
        }
    }

    /**
     * 删除节点
     *
     * @param val
     */
    public void removeNode(String val) {
        // 如果删除的节点是根节点
        if (root.val.equals(val)) {
            // 如跟节点后有其他节点，则需要把当前next节点赋值给root
            if (root.next != null) {
                root = root.next;
            } else {
                // 否则root赋值为null
                root = null;
            }
        } else {
            // 否则寻找下一个节点，直到找到该节点
            root.next.remove(this.root, val);
        }
    }

    /**
     * 打印节点
     */
    public void print() {
        if (root != null) {
            this.root.print();
        }
    }

    /**
     * 寻找节点
     *
     * @param val
     * @return
     */
    public boolean find(String val) {
        return root.find(val);
    }


    public static void main(String[] args) {
        // 1->2->3->4->5
        SingleLinkedNodeOperation node = new SingleLinkedNodeOperation();
        node.addNode("1");
        node.addNode("2");
        node.addNode("3");
        node.addNode("4");
        node.addNode("5");
        // 查看链表
        System.out.print("originNode:");
        node.print();
        // 查找链表
        System.out.println("find: " + node.find("3"));
        System.out.println("find: " + node.find("7"));
        // 删除链表
        node.removeNode("3");
        System.out.println("find: " + node.find("3"));
        System.out.print("remove:");
        node.print();

    }
}

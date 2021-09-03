/**
 * @Author: Twiss
 * @Date: 2021/9/2 6:36 下午
 */
public class DoubleLinkedNodeOperation {

    private DoubleLinkedNode head;
    private DoubleLinkedNode tail;
    private int len = 0;


    /**
     * 添加元素到头节点
     * @param val
     */
    public void addHead(String val){
        DoubleLinkedNode node;
        if (head==null){
            // 头节点为空，说明是一个空链表
            node = new DoubleLinkedNode(null, null, val);
            this.head = node;
            this.tail = node;
        }else {
            // 头节点不为空，说明是一个非空链表
            node = new DoubleLinkedNode(null, head, val);
            // 将旧head的pre指针指向node
            this.head.previous = node;
            // 将head指针指向新node节点
            this.head = node;
        }
        len++;
    }

    /**
     *  添加元素到尾节点
     * @param val
     */
    public void addTail(String val){
        DoubleLinkedNode node;
        if (tail==null){
            // 如果尾节点为空，说明是一个空链表
            node = new DoubleLinkedNode(null,null,val);
            this.head = node;
            this.tail = node;
        }else {
            // 尾节点不为空
            node = new DoubleLinkedNode(tail,null,val);
            this.tail.next = node;
            this.tail = node;
            len++;
        }
    }

    /**
     * 在referVal节点之前插入val节点
     * @param referVal
     * @param val
     */
    public void insertPrevious(String referVal, String val){
        DoubleLinkedNode node = this.head;
        while (node!=null){
            if (node.val.equals(referVal)){
                break;
            }
            node = node.next;
        }
        // 将referVal节点的前节点赋值给node
        DoubleLinkedNode valNode = new DoubleLinkedNode(node.previous,node,val);
        // 修改referVal节点前的节点的next指针指向valNode
        node.previous.next = valNode;
        // 修改referVal节点的前节点指针指向valNode
        node.previous = valNode;
        len++;
    }

    /**
     * 在referVal节点之后插入val节点
     * @param referVal
     * @param val
     */
    public void insertNext(String referVal, String val){
        DoubleLinkedNode node = this.head;
        while (node!=null){
            if (node.val.equals(referVal)){
                break;
            }
            node = node.next;
        }
        // 将referVal节点的之后节点赋值给node，val前节点是referVal
        DoubleLinkedNode valNode = new DoubleLinkedNode(node,node.next,val);
        // 修改referVal节点后的节点的pre指针指向valNode
        node.next.previous = valNode;
        // 修改referVal节点的后节点指针指向valNode
        node.next = valNode;
        len++;
    }

    /**
     * 删除指定节点
     * @param val
     */
    public void removeNode(String val){
        DoubleLinkedNode node = this.head;
        while (node!=null){
            if (node.val.equals(val)){
                break;
            }
            node = node.next;
        }
        // 将val的前一个节点的next指针指向val的next
        node.previous.next = node.next;
        // 将val的后一个节点的pre指针指向val的前一个节点
        node.next.previous = node.previous;
        len--;
    }

    public int getLen(){
        return len;
    }

    /**
     * 11->12->13->14
     * @param args
     */
    public static void main(String[] args) {
        DoubleLinkedNodeOperation node = new DoubleLinkedNodeOperation();
        node.addTail("11");
        node.addTail("12");
        node.addTail("13");
        node.addTail("14");
        System.out.print("originNode: ");
        node.head.print();

        node.addHead("10");
        System.out.print("add 10: ");
        node.head.print();

        node.insertNext("13","16");
        System.out.print("insertNext 13: ");
        node.head.print();
        node.insertPrevious("12","17");
        System.out.print("insertPrevious 12: ");
        node.head.print();

        node.removeNode("12");
        System.out.print("remove 12: ");
        node.head.print();
    }
}

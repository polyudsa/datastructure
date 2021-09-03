/**
 * @Author: Twiss
 * @Date: 2021/9/1 12:01 下午
 */
public class LinkedNode {
    public String val;
    public LinkedNode next;

    /**
     * 构造函数
     */
    public LinkedNode() {

    }

    /**
     * 构造函数
     */
    public LinkedNode(String x) {
        this.val = x;
    }

    /**
     * 构造函数
     */
    public LinkedNode(String x, LinkedNode next) {
        this.val = x;
        this.next = next;
    }

    /**
     * 正常来讲下一个节点为空，则为tail
     * @param node
     */
    public void add(LinkedNode node) {
        // 如果下一个节点为空，把新节点添加到next位置上
        if (this.next == null){
            this.next = node;
        }else {
            // 如果下一个节点不为空，则继续找next节点
            this.next.add(node);
        }
    }

    /**
     * 删除节点方法
     * @param node
     * @param val
     */
    public void remove(LinkedNode node, String val){
        // 如果当前节点的val与输入的val一致，则将当前的next节点赋值为node节点的next
        if (this.val.equals(val)){
            node.next = this.next;
        }else {
            // 如果当前的节点的val与输入的val不一致
            // 则对当前节点的next
            if (this.next!=null){
                this.next.remove(this,val);
            }
        }
    }

    /**
     * 查找
     * @param val
     * @return
     */
    public boolean find(String val){
        if (this.val.equals(val)){
            return true;
        }
        if (this.next!=null){
            return this.next.find(val);
        }else {
            return false;
        }
    }

    /**
     * 输出链表结果
     */
    public void print(){
        if (this.next!=null){
            System.out.print(this.val+"-->");
            this.next.print();
        }else {
            System.out.print(this.val+"\n");
        }
    }

}

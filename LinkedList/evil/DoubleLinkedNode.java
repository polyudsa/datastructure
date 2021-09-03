/**
 * @Author: Twiss
 * @Date: 2021/9/2 6:36 下午
 */
public class DoubleLinkedNode {
    public DoubleLinkedNode previous;
    public DoubleLinkedNode next;
    public String val;

    public DoubleLinkedNode(){

    }

    public DoubleLinkedNode(DoubleLinkedNode previous,
                            DoubleLinkedNode next, String val){
        this.previous = previous;
        this.next = next;
        this.val = val;
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

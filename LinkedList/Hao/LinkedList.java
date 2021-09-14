package Package1;

class LinkedList {
    String value;
    LinkedList next = null;
    public LinkedList(String val) {
        value = val;
    }
    public LinkedList(String val, LinkedList nextNode) {
        this.value = val;
        this.next = nextNode;
    }
    public void add(LinkedList node) {
        if(this.next == null) {
            this.next = node;
        }else {
            this.next.add(node);
        }
    }
    public LinkedList find(String nodeVal) {
        if(this.value == nodeVal)
            return this;
        else {
            if(this.next!=null)
                return this.next.find(nodeVal);
            else return null;
        }
    }
    private LinkedList findLast(String nodeVal) {
            if(this.next!=null) {
                if(this.next.value == nodeVal) {
                    return this;
                }else {
                    return this.next.findLast(nodeVal);
            }
        } else {
                return null;
            }
    }

    public boolean delete(String nodeVal) {
        if(this.value==nodeVal) {
            this.next = this.next.next;
            this.value = this.next.value;
        }
        if(find(nodeVal)==null){
            return false;
        }else {
            LinkedList lastNode = findLast(nodeVal);
            lastNode.next = lastNode.next.next;
            return true;
        }
    }


}
class TestClass {
    public static void main(String[] args) {
        LinkedList testList = new LinkedList("0",new LinkedList("1"));
        testList.add(new LinkedList("3"));
        LinkedList find1 = testList.find("1");
        boolean delete2 = testList.delete("2");
        boolean delete4 = testList.delete("3");
        System.out.println("find1: "+find1.value+" detele2: "+delete2+" delete4: "+delete4);
    }
}
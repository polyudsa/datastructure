package Package1;

import java.util.Stack;

class QueuebyArray {
    Integer value;
    Integer capacity = 10;
    Integer tailIndex=0;
    private int[] queue = new int[capacity];
    void enqueue(Integer num) {
        try {
            queue[tailIndex++] = num;
        }
        catch(ArrayIndexOutOfBoundsException e) {
            System.out.println("QueuebyArray out of range!");
        }
    }
    Integer dequeue() {
        if(tailIndex==0)
            return null;
        int topNum = queue[0];
        for(int i=1;i<tailIndex;i++) {
            queue[i-1] = queue[i];
        }
        return topNum;
    }
}
class CircleQueuebyArray {
    Integer capacity = 10;
    int[] circleQueue = new int[capacity];
    Integer firstIndex = 0;
    Integer lastIndex = 0;
    boolean enqueue(Integer num) {
         if((lastIndex+1)%capacity==firstIndex) {
             return false;
         }
         circleQueue[lastIndex] = num;
         lastIndex = (lastIndex+1)%capacity;
         return true;
    }
    Integer dequeue() {
        if(lastIndex==firstIndex)
            return null;
        int res = circleQueue[firstIndex];
        firstIndex = (firstIndex+1)%capacity;
        return res;
    }
}
public class Queue {
    public static void main(String[] args) {
        QueuebyArray queue1 = new QueuebyArray();
        queue1.enqueue(0);
        queue1.enqueue(1);
        queue1.enqueue(2);
        Integer queue1Top = queue1.dequeue();
        CircleQueuebyArray queue2 = new CircleQueuebyArray();
        queue2.enqueue(10);
        queue2.enqueue(9);
        queue2.enqueue(8);
        Integer queue2Top = queue2.dequeue();
        System.out.println("queue1Top: "+queue1Top+" queue2Top: "+ queue2Top);
    }
}
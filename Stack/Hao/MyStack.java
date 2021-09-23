package Package1;

import java.util.Arrays;

class StackbyArray {
    private int length = 1;
    private int frontIndex;
    private int[] stackVal = new int[length];
    StackbyArray(){
        frontIndex = 0;
    }
    public void pushStack(int val) {
        if(frontIndex >length-1) {
            length*=2;
            int[] tmp = new int[length];
            tmp = (int[]) Arrays.copyOf(stackVal,length);
            stackVal = tmp;
        }
        stackVal[frontIndex] =val;
        frontIndex++;
    }
    public int popStack(){
        frontIndex-=1;
        if(frontIndex<0) {
            frontIndex=0;
            return Integer.MIN_VALUE;
        }
        else return stackVal[frontIndex];
    }
}
class UnitTest {
    public static void main(String[] args) {
        StackbyArray myStack = new StackbyArray();
        myStack.pushStack(0);
        myStack.pushStack(1);
        myStack.pushStack(2);
        System.out.println(myStack.popStack());
        System.out.println(myStack.popStack());
        System.out.println(myStack.popStack());
        System.out.println(myStack.popStack());
    }

}

package Package1;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;

class HashTableUsingChain {
    private ArrayList<LinkedList<Integer>> hashTable = new ArrayList<LinkedList<Integer>>();
    HashTableUsingChain() {
        for(int i=0;i<11;i++){
            LinkedList<Integer> tmp = new LinkedList<Integer>();
            hashTable.add(tmp);
        }
    }
    void addHashTable(Integer num) {
        int hashNum = hashFunc(num);
        hashTable.get(hashNum).add(num);
    }
    int hashFunc(int num) {//h(k) = 2k+5 mod 11
        return (num*2+5)%11;
    }
    void printHashTable() {
        Iterator<LinkedList<Integer>> iterator = hashTable.iterator();
        while(iterator.hasNext()) {
            Iterator<Integer> iterator1 = iterator.next().iterator();
            if(!iterator1.hasNext()) {
                System.out.printf("null");
            }
            while(iterator1.hasNext()) {
                System.out.printf(iterator1.next()+"->");
            }
            System.out.printf("\n");
        }
    }
}
class HashTableUsingLinearProb {
    Integer[] hashTable = new Integer[11];
    int currentCapacity = 0;
    void addHashTable(int num) {
        currentCapacity++;
        int collisionTime = 0;
        boolean isCollision = true;
        while(isCollision) {
            if(hashTable[hashFunc(num,collisionTime)]!=null)
                collisionTime++;
            else {
                hashTable[hashFunc(num,collisionTime)] = num;
                isCollision=false;
            }
        }
    }
    Integer hashFunc(int num,int collisionTimes) {
        return (2*num+5+collisionTimes)%11;
    }
    void printHashTable() {
        System.out.println("----------HashTableUsingLinearProb----------");
        for(int i=0;i<11;i++) {
            System.out.printf(hashTable[i]+" ");
        }
    }
}
class HashTableUsingQuadraticProb {
    Integer[] hashTable = new Integer[11];
    int currentCapacity = 0;
    void addHashTable(int num) {
        currentCapacity++;
        int collisionTime = 0;
        boolean isCollision = true;
        while(isCollision) {
            if(hashTable[hashFunc(num,collisionTime)]!=null)
                collisionTime++;
            else {
                hashTable[hashFunc(num,collisionTime)] = num;
                isCollision=false;
            }
        }
    }
    Integer hashFunc(int num,int collisionTimes) {
        return (num+collisionTimes+collisionTimes*collisionTimes)%11;
    }
    void printHashTable() {
        System.out.println("-------------HashTableUsingQuadraticProb------------");
        for(int i=0;i<11;i++) {
            System.out.printf(hashTable[i]+" ");
        }
    }
}

class Test {
    public static void main(String[] args) {
        HashTableUsingChain testChain = new HashTableUsingChain();
        testChain.addHashTable(12);
        testChain.addHashTable(44);
        testChain.addHashTable(13);
        testChain.addHashTable(88);
        testChain.addHashTable(23);
        testChain.addHashTable(94);
        testChain.addHashTable(11);
        testChain.addHashTable(39);
        testChain.addHashTable(20);
        testChain.addHashTable(16);
        testChain.printHashTable();

        HashTableUsingLinearProb testLinearProb = new HashTableUsingLinearProb();
        testLinearProb.addHashTable(12);
        testLinearProb.addHashTable(44);
        testLinearProb.addHashTable(13);
        testLinearProb.addHashTable(88);
        testLinearProb.addHashTable(23);
        testLinearProb.addHashTable(94);
        testLinearProb.addHashTable(11);
        testLinearProb.addHashTable(39);
        testLinearProb.addHashTable(20);
        testLinearProb.printHashTable();

        HashTableUsingQuadraticProb testQuadraticProb = new HashTableUsingQuadraticProb();
        testQuadraticProb.addHashTable(12);
        testQuadraticProb.addHashTable(44);
        testQuadraticProb.addHashTable(13);
        testQuadraticProb.addHashTable(88);
        testQuadraticProb.addHashTable(23);
        testQuadraticProb.addHashTable(94);
        testQuadraticProb.addHashTable(11);
        testQuadraticProb.addHashTable(39);
        testQuadraticProb.addHashTable(20);
        testQuadraticProb.printHashTable();
    }
}

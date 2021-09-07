# LinkedQueue
class Empty(Exception):
    """Error attempting to access an element from an empth continer"""
    pass

class LinkedQueue:
    """LIFO stack implementation using a singly linked list for storage."""

    # ____________________ nested _Node class____________________
    class _Node:
        """
            storing a singly linked node.
            For the usefulness of the __slots__ function, please refer to the following article.
            https://blog.csdn.net/sxingming/article/details/52892640
        """
        ___slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, nextOne):
            self._element = element
            self._next = nextOne

    # ____________________  queue methods_______________________
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def _len_(self):
        """storing the length of the queue"""
        return self.size

    def is_empty(self):
        """Return True if the queue is empty"""
        return self.size == 0

    def push(self,e):
        """Add new element from the tail of the queue"""
        newest = self._Node(e,None)
        if self.is_empty():
            self.head = newest
            #self.size += 1
        else:
            self.tail._next = newest
        self.tail = newest
        self.size += 1

    def dequeue(self):
        """Remove the element from the head of the queue"""
        if self.is_empty():
            raise Empty("stack is empty")
        #answer = self.head._element
        self.head = self.head._next
        self.size -= 1
        #return answer

    def printElements(self):
        """Print the element from the head"""
        if self.is_empty():
            raise Empty("Stack is empty.")
        output = ''
        a = self.head
        while a is not None:
            output += (str(a._element)+" ")
            a = a._next
        print(output)

if __name__ == '__main__':
    # test2
    A = LinkedQueue()
    A.push(1)
    A.push(2)
    A.push(3)
    A.push(4)
    A.printElements()
    A.dequeue()
    A.dequeue()
    A.printElements()







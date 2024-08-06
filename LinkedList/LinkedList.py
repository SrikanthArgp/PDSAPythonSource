from heapq import merge
from typing import Tuple


class Node:
    """ A singly-linked node. """

    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def getHead(self):
        return self.head

    def append(self, data):
        # Encapsulate the data in a Node
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def delete_first_node (self): 
        current = self.head  
        if self.head is None:
            print("No data element to delete")
        elif current == self.head:
            self.head = current.next
            
          
    def delete_last_node (self): 
        current = self.head 
        prev = self.head
        while current:
            if current.next is None:
                prev.next = current.next 
                self.size -= 1
            prev = current
            current = current.next
            

    def delete(self, data): 
        current = self.head 
        prev = self.head 
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next 
                else:
                    prev.next = current.next 
                self.size -= 1
                return
            prev = current
            current = current.next

    def reverse(self):
        prev=None
        current=self.head
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev

    def reverse_list_recursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p = head.next
        head.next = None
        revrest = self.reverse_list_recursive(p)
        p.next = head
        return revrest

    def reverse_rec(self):
        self.head = self.reverse_list_recursive(self.head)

    def kth_to_last(self,head, k):
        """
        This is an optimal method using iteration.
        We move p1 k steps ahead into the list.
        Then we move p1 and p2 together until p1 hits the end.
        """
        if not (head or k > -1):
            return False
        p1 = head
        p2 = head
        for i in range(1, k+1):
            if p1 is None:
                # Went too far, k is not valid
                return None
            p1 = p1.next
        while p1:
            p1 = p1.next
            p2 = p2.next
        return p2.data

    def kth_from_last(self, k):
        return self.kth_to_last(self.head, k)

    def is_palindrome_stack(self):
        if not self.head or not self.head.next:
            return True

        # 1. Get the midpoint (slow)
        slow = fast = self.head
        stack = []
        while fast and fast.next:
            stack.append(slow.data)
            fast, slow = fast.next.next, slow.next

        if fast is not None:
            slow = slow.next

        # 2. Comparison
        while stack:
            if stack.pop() != slow.data:
                return False
            slow = slow.next

        return True

    def rotate_right(self, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not self.head or not self.head.next:
            return self.head
        current = self.head
        length = 1
        # count length of the list
        while current.next:
            current = current.next
            length += 1
        # make it circular
        current.next = self.head
        k = k % length
        # rotate until length-k
        for i in range(length-k):
            current = current.next
        self.head = current.next
        current.next = None

    def first_cyclic_node(self):
        """
        :type head: Node
        :rtype: Node
        """
        runner = walker = self.head
        while runner and runner.next:
            runner = runner.next.next
            walker = walker.next
            if runner is walker:
                break

        if runner is None or runner.next is None:
            return None

        walker = self.head
        while runner is not walker:
            runner, walker = runner.next, walker.next
        return runner
    
def merge_two_list(ll1, ll2):
    l1 = ll1.getHead()
    l2 = ll2.getHead()
    ret = cur = Node(0)
    while l1 and l2:
        if l1.data < l2.data:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return ret.next

def addTwoNumbers( l1: Node, l2: Node) -> Node:
        _ = l1.data + l2.data
        digit, carry = _ % 10, _ // 10
        answer = Node(digit)
        if any((l1.next, l2.next, carry)):
            l1 = l1.next if l1.next else Node(0)
            l2 = l2.next if l2.next else Node(0)
            l1.data += carry
            answer.next = addTwoNumbers(l1, l2)    
        return answer

def addTwoNumbers_reverse( l1: Node, l2: Node) -> Tuple[Node,int]:
        if l1 is None and l2 is None:
            return None,0
        else:
            ref, carry = addTwoNumbers_reverse(l1.next, l2.next)
            # if any((l1, l2, carry)):
            #     l1 = l1 if l1 else Node(0)
            #     l2 = l2 if l2 else Node(0)
            val = l1.data + l2.data + carry
            digit, carry = val % 10, val // 10
            n = Node(digit)
            n.next = ref
            # a,b = b,a    
            return n, carry



            
            
            
words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')
words.append('Jam')
words.append('scam')

for word in words.iter():
    print(word)

words.delete('scam')
print("After deletion : ")
for word in words.iter():
    print(word)

print("After Reversing")
words.reverse()
for word in words.iter():
    print(word)

print("After Reverse Recursive")
words.reverse_rec()
for word in words.iter():
    print(word)

print("Kth from Last : "+str(words.kth_from_last(1)))
words_pal = SinglyLinkedList()
words_pal.append('egg')
words_pal.append('ham')
words_pal.append('spam')
words_pal.append('ham')
words_pal.append('egg')

print("Is palindrome : "+str(words.is_palindrome_stack()))

print("After Rotating k steps : ")
words.rotate_right(1)
for word in words.iter():
    print(word)

ll1 = SinglyLinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)

ll2 = SinglyLinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(4)

mergeHead = merge_two_list(ll1, ll2)
while mergeHead is not None:
    print(mergeHead.data, end=" ")
    mergeHead = mergeHead.next
print()

ll3 = SinglyLinkedList()

ll3.append(6)
ll3.append(2)
ll3.append(2)

ll4 = SinglyLinkedList()

ll4.append(2)
ll4.append(2)
ll4.append(8)

print("Adding two LL: ")
sum = addTwoNumbers(ll3.getHead(), ll4.getHead())
while sum is not None:
    print(sum.data, end=" ")
    sum = sum.next
print()
print("Adding two LL reverse: ")
ref,car = addTwoNumbers_reverse(ll3.getHead(), ll4.getHead())
print(car, end=" ")
while ref is not None:
    print(revsum.data, end=" ")
    revsum = revsum.next

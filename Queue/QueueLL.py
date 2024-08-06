#Like for stacks, we need a node class which will contain the data and a pointer to the next node
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


#Next we need the Queue class itself which will contain a constructor initialising the queue and then the methods we require
class Queue():

#The 'first' pointer will always point to the front of the queue, the element which is to be removed next that is
#The 'last' pointer will always point to the end of the queue, i.e., the element which has last been entered
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

#Now comes the peek method which will return the element at the front of the queue
    def peek(self):
        if self.isEmpty():
            return None
        return self.first.data
    
    def isEmpty(self):
        return self.first is None and self.last is None

#The enqueue operation will add an element at the end of the queue
#If the queue is empty, it will make both the first and last pointer point to the new node
#Else, if will first make the next of the new node to point to the present last node and then it will update the last node to point to the new node
#Time complexity will be O(1)
    def enqueue(self, data):
        new_node = Node(data)
        if self.last == None:
            self.last = new_node
            self.first = self.last
            self.length += 1
            return
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1
            return


#Next comes the dequeue operation which removes the front element of the queue
#If the queue is empty, it will print an apropriate message
#Else, it will simply make the first pointer point to the next element of the first pointer.
    def dequeue(self):
        if self.last == None:
            print("Queue Empty")
            return None;
        else:
            temp =self.first
            if self.last == self.first:
                self.last = None
            self.first = self.first.next
            temp.next = None
            self.length -= 1
            return temp.data

#Finally we'll create the print method which prints the elements of the queue in, well, a queue like format
    def print_queue(self):
        if self.length == 0:
            print("Queue Empty")
            return
        else:
            current_pointer = self.first
            while(current_pointer!= None):
                if current_pointer.next == None:
                    print(current_pointer.data)
                else:
                    print(f'{current_pointer.data}  <<--  ', end='')
                current_pointer = current_pointer.next
            return
        
def reverse(q : Queue):
    if q.isEmpty():
        return
    else:
        temp  = q.dequeue()
        reverse(q)
        q.enqueue(temp)

my_queue = Queue()
my_queue.enqueue("This")
my_queue.enqueue("is")
my_queue.enqueue("a")
my_queue.enqueue("Queue")
my_queue.print_queue()
#This  <<--  is  <<--  a  <<--  Queue

reverse(my_queue)

print("Reversed Queue :")
my_queue.print_queue()

print(my_queue.peek())
#This

my_queue.dequeue()
my_queue.dequeue()
my_queue.print_queue()
#a  <<--  Queue

# print(my_queue.__dict__)
# #{'first': <__main__.Node object at 0x0000020CE99AED48>, 'last': <__main__.Node object at 0x0000020CE99AED88>, 'length': 2}
# print(my_queue.first)
# #<__main__.Node object at 0x000001A3F633ED48>
# print(my_queue.first.data)
#a

my_queue.dequeue()
my_queue.dequeue()
my_queue.print_queue()
#Queue Empty
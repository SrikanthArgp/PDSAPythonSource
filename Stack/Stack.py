class Node:  
    def __init__(self, data=None):  
        self.data = data  
        self.next = None  
       
      
      
class Stack:  
    def __init__(self):  
        self.top = None  
        self.size = 0  
        
    def push(self, data):  
    # create a new node 
        node = Node(data)  
        if self.top:  
            node.next = self.top  
            self.top = node                  
        else:  
            self.top = node  
        self.size += 1 
            
            
            
    def pop(self):  
        if self.top:  
            data = self.top.data  
            self.size -= 1   
            if self.top.next:  #check if there is more than one node. 
                self.top = self.top.next  
            else:  
                self.top = None  
            return data  
        else:  
            print("Stack is empty")             
        
        
    def peek(self):  
        if self.top:
            return self.top.data  
        else:  
            print("Stack is empty")          
        
    def traverse(self):
        if self.top:
            temp : Node = self.top
            while temp is not None:
                print(temp.data, end=" ")
                temp=temp.next
            print()
        else:
            print("Stack is empty")


words = Stack()
words.push('egg')
words.push('ham')
words.push('spam')

words.traverse()



print("Popping out .."+words.pop())




print("peeking in to .."+words.peek())
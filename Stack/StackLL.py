#Stacks are linear data-structures which can be implemented using either stacks or linked lists

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


#Now we create the Stack class

class Stack():
    def __init__(self):
        self.top = None
        self.length = 0


    def peek(self):
        if self.top is None:
            return None
        return self.top.data



#So time complexity is O(1)
    def push(self, data):
        new_node = Node(data)
        if self.top == None: #If the stack is empty, we make the top and bottom pointer both point to the new node
            self.top = new_node
        else: #Otherwise, we make the next of the new node, which was pointing to None, point to the present top and then update the top pointer
            new_node.next = self.top
            self.top = new_node
        self.length += 1


#Its time complexity is O(1) as well
    def pop(self):
        if self.top == None: #If the stack is empty, we print an appropriate message
            print("Stack empty")
        else: #Else we make the top pointer point to the next of the top pointer and decrease the length by 1, effectively deleting the top element.
            self.top = self.top.next
            self.length -= 1
           


    def print_stack(self):
        if self.top == None:
            print("Stack empty")
        else:
            current_pointer = self.top
            while(current_pointer!=None):
                print(current_pointer.data)
                current_pointer = current_pointer.next


my_stack = Stack()
print(my_stack.peek())
#None

my_stack.push('google')
my_stack.push('udemy')
my_stack.push('discord')
my_stack.print_stack()
#discord
#udemy
#google

print(my_stack.top.data)
#discord



my_stack.pop()
my_stack.print_stack()
#udemy
#google

my_stack.pop()
my_stack.pop()
my_stack.print_stack()
#Stack Empty
from tkinter import N


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        # Append an item at the end of the list.
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def append_at_start(self, data):
        # Append an item at beginning to the list.
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count += 1

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def contains(self, data):
        for node_data in self.iter():
            if data == node_data:
                print(" Data item is present in the list. ")
                return
        print(" Data item is not present in the list. ")
        return

    def traverse(self):
        if self.head is None:
             return
        else:
            current = self.head
            while current:
                print(current.data)
                current = current.next
    
    def delete(self, data):
        # Delete a node from the list. 
        current = self.head 
        node_deleted = False 
        if current is None:       #List is empty
            print("List is empty")
        elif current.data == data:   #Item to be deleted is found at starting of list
            self.head.prev = None 
            node_deleted = True 
            self.head = current.next

        elif self.tail.data == data:   #Item to be deleted is found at the end of list.
            self.tail = self.tail.prev  
            self.tail.next = None 
            node_deleted = True 

        else: 
            while current:          #search item to be deleted, and delete that node
                if current.data == data: 
                    current.prev.next = current.next  
                    current.next.prev = current.prev 
                    node_deleted = True 
                current = current.next 
            if node_deleted == False:   #Item to be deleted is not found in the list
                print("Item not found")
        if node_deleted: 
            self.count -= 1




words = DoublyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

print("Items in doubly linked list before add at start")

words.traverse()   
words.append_at_start('book')

print("Items in doubly linked list after add at start")
words.traverse()

words.delete('spam')
print("Items in doubly linked list after deletion")
words.traverse()



words.append('book')

print("Items in doubly linked list after adding element at end.")
words.traverse()
    





words = DoublyLinkedList()  
words.append('egg')  
words.append('ham')  
words.append('spam') 


words.contains("ham")  
words.contains("ham2") 
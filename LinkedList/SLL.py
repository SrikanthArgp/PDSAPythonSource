class Node:
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = None
        
    def get_data(self):
        return self.__data
    
    def get_next(self):
        return self.__next
    
    def set_data(self,data):
        self.__data= data
        
    def set_next(self,next):
        self.__next=next    

class LinkedList:
    def __init__(self, head=None):
        self.__head = head
        
    def isEmpty(self):
        return self.__head == None
        
    def append(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.__head = newNode
        else:
            temp = self.__head
            while temp.get_next() is not None:
                temp = temp.get_next()
            temp.set_next(newNode)
            
    def traverse(self):
        if self.isEmpty():
            return;
        else:
            temp = self.__head
            while temp is not None:
                print(" ",temp.get_data(), end=" ")
                temp = temp.get_next()

        
    def delete(self, data):
        if self.isEmpty(): return
        elif self.__head.get_data() == data:
            temp=self.__head
            self.__head = self.__head.get_next()
            temp.set_next(None)
            return
        else:
            prev=self.__head
            cur = self.__head.get_next()
            while cur is not None:
                if cur.get_data() == data:
                    prev.set_next(cur.get_next())
                    cur.set_next(None)
                    return
                else:
                    prev=cur
                    cur=cur.get_next()
                    
            print("Data Does not Exists: ")

    def getMiddle(self):
        fast=self.__head
        slow=fast
        while fast is not None and fast.get_next() is not None:
            slow = slow.get_next()
            fast = fast.get_next().get_next()
        return slow



            
  

l=LinkedList()
for i in range(1,11):
    l.append(i)
l.traverse()
print()
print(l.getMiddle().get_data())
l.delete(5)
l.traverse()

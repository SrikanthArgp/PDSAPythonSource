class BNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = BNode(data)
        if self.root is None:
            self.root = node
            return
        else:
            queue = []
            queue.append(self.root)
            while len(queue) !=0:
                temp : BNode  = queue.pop(0)
                if temp.left is None:
                    temp.left=node
                    return
                else:
                    queue.append(temp.left)

                if temp.right is None:
                    temp.right = node
                    return
                else:
                    queue.append(temp.right)


    def levelOder(self): 
        if self.root is None:
            return
        else:
            queue = []
            queue.append(self.root)
            while len(queue) !=0:
                temp : Node = queue.pop(0)
                print(" ", temp.data, end=" ")
                if temp.left is not None:
                    queue.append(temp.left)

                if temp.right is not None:
                    queue.append(temp.right)
            print()


    def inorder(self, root): 
        if root is None: 
            return
        else: 
            self.inorder(root.left) 
            print(root.data, end=" ") 
            self.inorder(root.right)

    def inOrder(self):
        self.inorder(self.root)
        print()

    def preorder(self, root): 
        if root is None: 
            return
        else: 
            print(root.data, end=" ") 
            self.preorder(root.left) 
            self.preorder(root.right)

    def preOrder(self):
        self.preorder(self.root)
        print()

    def postorder(self, root): 
        if root is None: 
            return
        else:  
            self.postorder(root.left) 
            self.postorder(root.right)
            print(root.data, end=" ")

    def postOrder(self):
        self.postorder(self.root)
        print()
    



btree = BinaryTree()
btree.insert(5)
btree.insert(2)
btree.insert(7)
btree.insert(9)
btree.insert(1)
btree.insert(18)
btree.insert(6)

print("Level order Traversal :")
btree.levelOder()
print("In order Traversal :")
btree.inOrder()
print("Pre order Traversal :")
btree.preOrder()
print("Post order Traversal :")
btree.postOrder()



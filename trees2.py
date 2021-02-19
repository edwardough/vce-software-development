# define classes and functions etc
class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.value == data:
            print("Data already present.")
            return False
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                print(data,"inserted.")
                return True
        elif self.value < data:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                print(data,"inserted.")
                return True

    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        elif self.value < data:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        # print(self)
        # The line above helped me realise you can't do "if self == True:"
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()
    
    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.value))

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            print(data,"set as root.")
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print("PreOrder")
        self.root.preorder()

    def postorder(self):
        print("PostOrder")
        self.root.postorder()

    def inorder(self):
        print("InOrder")
        self.root.inorder()

# actual program
bst = Tree()
bst.insert(14)
bst.insert(14)
bst.insert(10)
bst.insert(9)
bst.insert(61)
bst.insert(33)
bst.preorder()
bst.postorder()
bst.inorder()
print("So what's the difference between pre, post and in order traversal?")
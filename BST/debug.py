class BSTreeNode:
    def __init__(self, val):
        self.value = val 
        self.left, self.right = None, None
        
class BinaryST:
    def __init__(self):
        self.root = None
        
    def insert(self, val):
        self.root = self.insertHelp(val, self.root)
    

    def insertHelp(self, value, node):
        if node == None:
            node = BSTreeNode(value)
            return node
        
        
        if node.value > value:
            node.left = self.insertHelp(value, node.left)
        if node.value < value:
            node.right = self.insertHelp(value, node.right)
            
        return node
    
    def Sum(self):
        return self.sumHelp(self.root)

    def sumHelp(self, node):
        if node == None:
            return 0
        return node.value + self.sumHelp(node.left) + self.sumHelp(node.right)



    def display(self):
        self.displayHelper(self.root, "Root Node: ")


    def displayHelper(self, node, details):
        if node == None:
            return

        print(details, node.value)

        self.displayHelper(node.left, "left child of " + str(node.value) + ":")
        self.displayHelper(node.right, "right child of " + str(node.value) + ":")

        

# nums = [4, 5, 2, 7, 6, 1]
if __name__ == '__main__':
    bst = BinaryST()
    bst.insert(4)
    bst.insert(5)
    bst.insert(2)
    bst.insert(7)
    bst.insert(6)
    bst.display()
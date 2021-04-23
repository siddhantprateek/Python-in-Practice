class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def insert(self, val):
        self.root = self.insertHelper(val, self.root)


    def insertHelper(self, value, node):
        if node == None:
            node = TreeNode(value)
            return node

        if value < node.value:
            node.left = self.insertHelper(value, node.left)
        if value > node.value:
            node.right = self.insertHelper(value, node.right)

        return node

    def populated(self, nums):
        for num in nums:
            self.insert(num)



    def populatedWithSorted(self, nums):
        self.populatedWithSortedHelper(nums, 0, len(nums))

    def populatedWithSortedHelper(self, nums, start, end):
        if start >= end:
            return

        mid = (start + end) // 2
        self.insert(nums[mid])

        self.populatedWithSortedHelper(nums, start, mid)
        self.populatedWithSortedHelper(nums, mid + 1, end)


    def Height(self):
        return self.HeightHelper(self.root)

    def HeightHelper(self, node):
        if node == None:
            return 0
        return 1 + max(self.HeightHelper(node.left), self.HeightHelper(node.right))

    def balanced(self):
        if not self.root:
            return True
        return self.balancedHelp(self.root) and self.balanced(self.root.left) and self.balanced(self.root.right)

    def balancedHelp(self, node):
        if node == None:
            return

        left = self.HeightHelper(self.root.left)
        right  = self.HeightHelper(self.root.right)

        return abs(left - right) <= 1

    def search(self, value):
        return self.searchHelp(self.root, value)

    def searchHelp(self, node ,value):
        if node is None:
            return node
        if node.value == value:
            return "found"
        if node.value < value:
            self.searchHelp(node.right, value)
        return self.searchHelp(node.left, value)



    def sum(self):
        return self.sumHelper(self.root)

    def sumHelper(self, node):
        if node == None:
            return 0
        return node.value + self.sumHelper(node.left) + self.sumHelper(node.right)

    def rangeSumBST(self, root,low: int, high: int) -> int:
        if not root:
            return 0
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)




    def traversal(self):
        self.preOrder(self.root)
        self.inOrder(self.root)
        self.postOrder(self.root)

    # invert a Binary Tree
    def invertTree(self, root):
        if root is None:
            return

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # swapping
        root.left = right
        root.right = left
        return root



    def preOrder(self, node):
        if node == None:
            return

        print(node.value)
        self.preOrder(node.left)
        self.preOrder(node.right)

    def inOrder(self, node):
        if node == None:
            return


        self.inOrder(node.left)
        print(node.value)
        self.inOrder(node.right)

    def postOrder(self, node):
        if node == None:
            return

        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.value)

    def display(self):
        self.displayHelper(self.root, "Root Node: ")


    def displayHelper(self, node, details):
        if node == None:
            return

        print(details, node.value)

        self.displayHelper(node.left, "left child of " + str(node.value) + ":")
        self.displayHelper(node.right, "right child of " + str(node.value) + ":")


if __name__ == '__main__':
    bst = BST()
    # bst.insert(15)
    # bst.insert(10)
    # bst.insert(5)
    # bst.insert(5)
    # bst.insert(30)
    bst.populated([10,5,15,3,7,18])
    print(bst.search(1))
    # print(bst.rangeSumBST(7, 15))
    print(bst.balanced())
    # print(bst.sum())
    # bst.display()

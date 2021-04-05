from collections import deque
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

    def preOrder(self, node):
        if node == None:
            return

        print(node.value)
        self.preOrder(node.left)
        self.preOrder(node.left)

    def inOrder(self, node):
        if node == None:
            return


        self.inOrder(node.left)
        print(node.value)
        self.inOrder(node.left)

    def postOrder(self, node):
        if node == None:
            return

        self.postOrder(node.left)
        self.postOrder(node.left)
        print(node.value)

    def display(self):
        self.displayHelper(self.root, "Root Node: ")


    def displayHelper(self, node, details):
        if node == None:
            return

        print(details, node.value)

        self.displayHelper(node.left, "left child of " + str(node.value) + ":")
        self.displayHelper(node.right, "right child of " + str(node.value) + ":")

    def bfs(self):
        if self.isEmpty():
            return

        queue = deque()
        queue.append(self.root)

        while queue:
            # level size
            ls = len(queue)
            for _ in range(ls):
                popped = queue.popleft()
                print(popped.value, end=" ")
                # insert the children
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            print()


    def zigzag(self):
        ans = []

        if self.isEmpty():
            return ans

        queue = deque()
        queue.append(self.root)
        leftToRight = True
        while queue:
            # level size
            ls = len(queue)
            current = deque()
            for _ in range(ls):

                popped = queue.popleft()
                # print(popped.value, end=" ")

                if leftToRight:
                    current.append(popped.value)
                else:
                    current.appendleft(popped.value)
                # insert the childrens
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            ans.append(list(current))
            leftToRight = not leftToRight
        return ans





    def RightView(self):
        self.rightviewHelper(self.root)

    def rightviewHelper(self, node):
        if node == None:
            return
        print(node.val)
        if node.right:
            self.rightviewHelper(node.right)
        else:
            self.rightviewHelper(node.left)

# anothe way last element of all level
    def rightSideView(self):
        ans = []

        if self.isEmpty():
            return ans

        queue = deque()
        queue.append(self.root)
        leftToRight = True
        while queue:
            # level size
            ls = len(queue)
            current = deque()
            for _ in range(ls):

                popped = queue.popleft()
                # print(popped.value, end=" ")
                # insert the childrens
                if i == ls - 1:
                    ans.append(popped.left)

                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)

        return ans
    # def level_order_successor(self, key):
    #     if self.isEmpty():
    #         return None
    #
    #     queue = deque()
    #     queue.append(self.root)
    #     # level is not maintained
    #     while queue:

# make level average



# bottom view
    # def bottomView(self):
    #     ans = {}
    #
    #     if self.isEmpty():
    #         return






if __name__ == '__main__':
    bst = BST()
    # bst.insert(15)
    # bst.insert(10)
    # bst.insert(5)
    # bst.insert(5)
    # bst.insert(30)
    bst.populatedWithSorted([1, 2, 3, 4, 5, 6])
    # print(bst.search(1))
    # print(bst.rangeSumBST(7, 15))
    # print(bst.balanced())
    # print(bst.sum())
    # bst.display()
    bst.bfs()
    print(bst.zigzag())

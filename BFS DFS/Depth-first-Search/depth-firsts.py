from collections import deque

class TreeNode:
    def __init__(self, val):
        self.value = self.val
        self.left, self.right = None, None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self.inserting(self.root, val)

    def inserting(self, node, value):
        if node == None:
            node = TreeNode(value)
            return node

        if value < node.value:
            node.left = self.inserting(node.left, value)

        if value > node.value:
            node.right = self.inserting(node.right, value)

        return node

    def isEmpty(self):
        return self.root == None

    def popualatedWithSorted(self, nums):
        self.populatingbySort(nums, 0, len(nums))

    def populatingbySort(self, nums, start, end):

        if start >= end:
            return

        mid = start + (end - start) // 2
        self.insert(nums[mid])

        self.populatingbySort(nums, start, mid)
        self.populatingbySort(nums, mid + 1, end)


    def flatten(self):
        self.flattening(self.root)

    def flattening(self, node):

        if node is None:
            return


        if node.left is None and node.right is None:
            return node

        temp = node.right
        node.right = self.flattening(node.left)
        node.left = None

        prev = node
        while prev.right is not None:
            prev = prev.right
        prev.right = self.flatten(temp)

        return node

    def populatedWithSorted(self, nums):
        self.populatedWithSortedHelper(nums, 0, len(nums))

    def populatedWithSortedHelper(self, nums, start, end):

        if start >= end:
            return
        mid = (start + end) // 2
        self.insert(nums[mid])

        self.populatedWithSortedHelper(nums, start, mid)
        self.populatedWithSortedHelper(nums, mid + 1, end)



    def getLevelsList(self):

        if self.isEmpty():
            return



        queue = deque()
        queue.append(self.root)

        while queue:

            ls = len(queue)
            ans = []
            for _ in range(ls):

                popped = queue.popleft()
                ans.append(popped.val)

                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)

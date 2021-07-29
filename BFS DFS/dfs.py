class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = self.right = None

class Solution():
    def __init__(self):
        self.root = None
    def insert(self, val):
        self.insertHelper(self.root, val)

    def insertHelper(self, node, value):
        if node == None:
            node = TreeNode(value)
            return node

        if node.value > value:
            node.left = self.insertHelper(node.left, value)

        if node.value < value:
            node.right = self.insertHelper(node.right, value)
        return node

    def populatedWithSorted(self, nums):
        return populatedWithSortedHelper(nums, 0, len(nums))

    def populatedWithSortedHelper(self, nums, start, end):
        if start >= end:
            return

        mid = (start + end) // 2
        self.insert(nums[mid])
        self.populatedWithSortedHelper(nums, start, mid)
        self.populatedWithSortedHelper(nums, mid + 1, end)

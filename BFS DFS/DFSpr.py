from collections import deque

class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left, self.right = None, None

class BST():
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self.insertHelper(self.root, val)

    def insertHelper(self, node, value):
        if node == None:
            node = TreeNode(value)
            return node

        if value < node.value:
            node.left = self.insertHelper(node.left, value)
        if value > node.value:
            node.right = self.insertHelper(node.right, value)

        return node

    def isEmpty(self):
        return self.root == None

    def populatedWithSorted(self, nums):
        self.populatedWithSortedHelper(nums, 0, len(nums))

    def populatedWithSortedHelper(self, nums, start, end):

        if start >= end:
            return

        mid = (start + end) // 2
        self.insert(nums[mid])

        self.populatedWithSortedHelper(nums, start, mid)
        self.populatedWithSortedHelper(nums, mid + 1, end)

    def allPathSum(self, sum):
        result = []
        self.findallpaths(self.root, sum, [],result)

    def findallpaths(self, node, sum, currentList, result):
        if node == None:
            return

        currentList.append(node.value)
        if node.value == sum and node.left == None and node.right == None:
            result.append(list(currentList))
        else:
            self.findallpaths(node.left, sum - node.value, currentList, result)
            self.findallpaths(node.right, sum - node.value, currentList, result)

        # backtracking if solution is not found in that branch
        del  currentList[-1]



    def pathNumbersSum(self):
        return self.findPathNumberSum(self.root, 0)

    def findPathNumberSum(self, node, Prevsum):
        if node == None:
            return 0

        currentSum = node.value + Prevsum*10

        if node.left == None and node.right == None:
            return currentSum

        return self.findPathNumberSum(node.left, currentSum) + self.findPathNumberSum(node.right, currentSum)

    def countPath(self, sum):
        return self.PathCounter(self.root, sum, [])

    def PathCounter(self, node, sum , currentPath):

        if node == None:
            return 0

        currentPath.append(node.value)
        count = 0
        pathSum = 0
        for i in range(len(currentPath)- 1, -1, -1):
            pathSum += currentPath[i]
            if pathSum == sum:
                count += 1
        count += self.PathCounter(node.left, sum, currentPath) + self.PathCounter(node.right, sum, currentPath)


        del currentPath[-1]
        return count


if __name__ == '__main__':
    bst = BST()

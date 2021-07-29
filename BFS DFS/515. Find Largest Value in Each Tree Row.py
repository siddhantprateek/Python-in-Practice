# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        levelList = self.getLevels(root)
        maxlist = self.getMaxList(levelList)
        return maxlist

    def getMaxList(self, levels):

        largeVal = []
        for level in levels:
            maxInLevel = max(level)
            largeVal.append(maxInLevel)

        return largeVal

    def getLevels(self, node):

        ans = []
        if node == None:
            return ans

        from collections import deque

        queue= deque()
        queue.append(node)

        while queue:

            length = len(queue)
            current = deque()

            for _ in range(length):

                popped = queue.popleft()

                current.append(popped.val)

                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            ans.append(list(current))
        return ans

        

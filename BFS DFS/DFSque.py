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

#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
    # def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    #     if not nums:
    #         return None
    #
    #     mid = (len(nums))// 2
    #     root = TreeNode(nums[mid])
    #     root.left = self.sortedArrayToBST(nums[:mid])
    #     root.right = self.sortedArrayToBST(nums[mid + 1:])
    #     return root




    def bfs(self):
        if self.isEmpty():
            return


        queue = deque()
        queue.append(self.root)

        while queue:
            # level size
            ls = len(queue)

            for _ in range(ls):
                # we are popping the node not the value
                popped = queue.popleft()

                print(popped.value, end = " ")
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            print()

    def bfsList(self):
        ans = []
        if self.isEmpty():
            return

        queue = deque()
        queue.append(self.root)

        while queue:

            ls = len(queue)
            current = deque()
            for _ in range(ls):

                popped = queue.popleft()
                current.append(popped.value)

                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            ans.append(list(current))
        return ans

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
            # queue of that level
            current = deque()
            for i in range(ls):
                popped = queue.popleft()

                if leftToRight:
                    current.append(popped.value)
                else:
                    current.appendleft(popped.value)

                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            ans.append(list(current))
            leftToRight = not leftToRight
        return ans

    def rightView(self):
        ans = []
        if self.isEmpty():
            return ans

        queue = deque()
        queue.append(self.root)
        leftToRight = True
        while queue:

            # level size:
            ls = len(queue)

            for i in range(ls):
                popped = queue.popleft()
                # when we are at the end of queue
                # we will insert it in current
                if i == ls - 1:
                    ans.append(popped.value)

                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
        return ans

    # def bfs(self):
    #
    #     if self.isEmpty():
    #         return
    #
    #     queue = deque()
    #     queue.append(self.root)
    #
    #     while queue:
    #
    #         ls = len(queue)
    #
    #         for _ in range(ls):
    #
    #             popped = queue.popleft()
    #
    #             print(popped.value, end=" ")
    #             # will insert the childrens in another level
    #             if popped.left:
    #                 queue.append(popped.left)
    #             if popped.right:
    #                 queue.append(popped.right)
    #
    #         print()
    #
    #




    def nextNodeLevel(self, key):

        if self.isEmpty():
            return None

        queue = deque()
        queue.append(self.root)

        while queue:
            popped = queue.popleft()

            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)

            if popped.value == key:
                break

            if queue:
                return queue[0]
            return None

    # DFS
    def pathSum(self, sum):
        return self.pathSumHelper(self.root, sum)

    def pathSumHelper(self, node, sum):
        if node == None:
            return False

        # the node have no child and the node value is equal to the sum
        if node.value == sum and node.left == None and node.right == None:
            return True

        return self.pathSumHelper(node.left, sum - node.value) or self.pathSumHelper(node.right, sum - node.value)


    def allPathSum(self, sum):
        result = []
        self.findallpaths(self.root, sum, [], result)
        return result

    def findallpaths(self, node, sum, currentList, result):
        if node == None:
            return

        # when ever we are at the node we are adding the TreeNode

        currentList.append(node.value)
        if node.value == sum and node.left == None and node.right == None:
            result.append(list(currentList)) # O(n) in appending
            # O(n) accesing every node if we ignore it will be O(n) otherwise it will be O(n^2)
        else:
            self.findallpaths(node.left, sum - node.value, currentList, currentList)
            self.findallpaths(node.right, sum - node.value, currentList, currentList)

        # worst case the complexity will be its height O(NlogN)
        # worst case mein leaf tree mein leaf O(n+1/2)*logN  ~ O(Nlog(N))

        # backtracking
        del currentList[-1]

    def pathNumbersSum(self):
        return self.findPathNumberSum(self.root, 0)

    def findPathNumberSum(self, node, prevLevelSum):
        if node == None:
            return 0
        # before moving to node below *10
        currentSum = node.value + prevLevelSum*10

        if node.left == None and node.right == None:
            return currentSum

        # while moving to next node left and right add them both
        return self.findPathNumberSum(node.left, currentSum) + self.findPathNumberSum(node.right, currentSum)

    def checkSequence(self, seq):
        return self.checkingSequence(self.root, seq, 0)

    def checkingSequence(self, node, seq, index):
        if not node:
            return False

        # if node.value != seq[index]:
        #     return
        # time Comp == O(n)
        # space complexity = 1
        if index > len(seq) - 1:
            return True

        if node.value == seq[index]:
            return self.checkingSequence(node.left, seq, index + 1) or self.checkingSequence(node.right, seq, index + 1)
        # any node does not match return False
        return False






    def countPath(self, sum):
        return self.countPathrec(self.root, sum, [])

    def countPathrec(self, node, sum, currentPath):
        if node == None:
            return 0

        currentPath.append(node.value)
        count = 0
        pathSum = 0
        for i in range(len(currentPath) - 1, -1, -1):
            pathSum += currentPath[i]
            if pathSum == sum:
                count += 1
        count += self.countPathrec(node.left, sum, currentPath) + self.countPathrec(node.right, sum, currentPath)


        # time comp height of the tree NlogN
        # worst case N^2

        # backtracking
        del currentPath[-1]
        return count

    def diameterOfTree(self):
        self.dia = 0
        self.diaHeight(self.root)
        return self.dia

    def diaHeight(self, node):
        if node == None:
            return 0

        leftHeight = self.diaHeight(node.left)
        rightHeight = self.diaHeight(node.right)
        if leftHeight != None and rightHeight != None:
            diaofCurrentNode = leftHeight + rightHeight + 1
            # update the global
            self.dia = max(self.dia, diaofCurrentNode)

        return max(leftHeight, rightHeight) + 1

    def MaxPath(self):
        self.maximum = 0
        self.MaxPathCounter(self.root)
        return self.maximum

    def distanceFromRoot(self, target):
        return self.distanceFromRootHelper(self.root, target)

    def distanceFromRootHelper(self, node, target):
        if node == target:
            return 0
        elif node.value > target:
            return 1 + self.distanceFromRootHelper(node.left, target)
        return 1 + self.distanceFromRootHelper(node.right, target)

    # find distance between node
    def distancebetween2Node(self, a, b):
        return self.distancebetween2NodeHelper(self.root, a, b)

    def distancebetween2NodeHelper(self, node, a, b):

        if node == None:
            return 0

        if node.value  >  a and node.value > b:
            return self.distancebetween2NodeHelper(node.left, a, b)
        if node.value < a and node.value < b:
            return self.distancebetween2NodeHelper(node.right, a, b)

        if node.value >= a and node.value <= b:
            return self.distanceFromRootHelper(node, a) + self.distanceFromRootHelper(node, b)


    def MaxPathCounter(self, node):
        if node == None:
            return 0

        leftMax = max(self.MaxPathCounter(node.left), 0)
        rightMax = max(self.MaxPathCounter(node.right), 0)
        if leftMax != None and rightMax != None:
            Max = leftMax + rightMax + node.val
                # update the global
            self.maximum = max(self.maximum, Max)

        return max(leftMax, rightMax) + node.val

if __name__ == '__main__':
    bst = BST()
    bst.populatedWithSorted([1,2,3,4,5,6])
    bst.bfs()
    print(bst.zigzag())
    print(bst.rightView())
    bst.nextNodeLevel(6)
    print("bfs:", bst.bfsList())
    print(bst.pathSum(9))
    print("pathNumbersSum: ",bst.pathNumbersSum())
    print("allPathSum: ",bst.allPathSum(6))
    print(bst.countPath(2))
    print("seq Sum: ",bst.checkSequence([1, 2, 5]))

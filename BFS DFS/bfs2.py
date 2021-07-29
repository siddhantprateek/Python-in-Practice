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
    # left View

    # bottom View
    # top View

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

        return self.pathSumHelper(node.left, sum - node.value) or
         self.pathSumHelper(node.right, sum - node.value)


    def PathSum(self):
        pass

# linked List
# make a slow and fast
# the get the cycle length
# after that keep the fast at distance of cycle length
# when slow == fast then at that point the start of the cycle
    def getCycleStart():
        pass



if __name__ == '__main__':
    bst = BST()
    bst.populatedWithSorted([1,2,3,4,5,6])
    bst.bfs()
    print(bst.zigzag())
    print(bst.rightView())
    bst.nextNodeLevel(6)
    print(bst.pathSum(9))

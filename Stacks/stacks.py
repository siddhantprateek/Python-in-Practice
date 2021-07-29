class Stack:

    def __init__(self, size = 10):
        self.size = size
        self.top = -1
        self.data = [None for _ in range(size)]

    def isFull(self):
        return self.top == self.size - 1

    def isEmpty(self):
        return self.top == -1

#
    def push(self, item):
        if self.isFull():
            print('Stack is full')
            return False

        self.top += 1 
        self.data[self.top] = item
        return True

    def pop(self):
        if self.isEmpty():
            print('Stack is Empty')
            return False

        removed = self.data[self.top]
        self.top -= 1
        return removed


    def bbsort(self):
        for i in range(self.top):
            for j in range(self.top - i):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]




#

    def top(self):
        return self.data[self.top]


    def display(self):
        return self.data[:self.top + 1]


stack = Stack(20)

stack.push(5)
stack.push(12)
stack.push(4)
stack.push(7)
stack.push(8)
stack.push(2)
stack.push(3)
stack.push(1)
print(stack.display())

stack.pop()

print(stack.display())

stack.bbsort()
print(stack.display())



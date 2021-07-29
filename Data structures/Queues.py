# (FIFO) First in First Out

# Remove items from the beginning

# A module is a bucket with bunch of reusable code

from collections import deque  # deque is class
queue = deque([])  # list is passed deque object
queue.append(1)
queue.append(2)
queue.append(3)  # pop by itself pops from last in .
print(queue)
queue.popleft()
print(queue)
queue.pop()
print(queue)
queue.pop()
if not queue:
    print("Empty")

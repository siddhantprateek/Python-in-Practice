

# Implementation of Deque

* Deque() creates a new deque that is empty. It needs no parameters and returns an empty deque.
```python
def __init__(self):
	self.items = []
```
* addFront(item) adds a new item to the front of the deque. It needs the item and returns nothing.
```python
def addFront(self, item):
	self.items.append(item)
```
* addRear(item) adds a new item to the rear of the deque. It needs the item and returns nothing.
```python
def addRear(self, item):
	self.items.insert(0,item)
```
* removeFront() removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.
```python
def removeFront(self):
	return self.items.pop()
```
* removeRear() removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.
```python
def removeRear(self):
	return self.items.pop(0)
```
* isEmpty() tests to see whether the deque is empty. It needs no parameters and returns a boolean value.
```python
def isEmpty(self):
	return self.items == []
```
* size() returns the number of items in the deque. It needs no parameters and returns an integer
```python
def size(self):
	return len(self.items)
```

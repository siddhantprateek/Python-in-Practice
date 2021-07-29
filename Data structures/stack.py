# (LIFO) Last in First Out
# Imagine a stack of books last book you put on stack is the first book you can remove
# Same works in a browser when you press back botton we go to previous website


browsing_session = []
# Append() is used to add item to the top of the stack
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
# Pop() is used to remove item from the top of the stack
last = browsing_session.pop()
print(last)
print(browsing_session)
# we used index [-1] to to get item to the top of the stack
print("Redirect", browsing_session[-1])

# if the only one item in stack and your at the end


# if not browsing_session:
#  browsing_session[-1]

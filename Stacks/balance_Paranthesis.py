

def balance_check(s: str):

    # CHECK EVEN NUMBER OF BRACKETS
    if len(s)%2 != 0:
        return False

    opening = set('([{')

    matches = set([('(',')'),('[',']'),('{','}')])

    stack = []
    for paren in s:
        # the stack takes the opening parantheses present in s
        if paren in opening:
            stack.append(paren)
        else:
            # checks whether there are parantheses in the stack or not
            if len(stack) == 0:
                return False

            last_open = stack.pop()
            # to check whether the paren is closing bracket or not
            if (last_open, paren) not in matches:
                return False

    return len(stack) == 0

print(balance_check('[](){([[[]]])}'))
print(balance_check('()(){]}'))


# By using HashMap

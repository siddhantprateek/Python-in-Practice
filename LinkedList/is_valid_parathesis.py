def is_valid_paranthesis(s: str):

    left_char, lookup = [], {'(': ')', '[': ']', '{': '}' }

    for char in s:

        # check the opening brackets
        if char in lookup:
            left_char.append(char)
        # check the closing character
        # and check wheather the char that is popped is part value matching the key or not 
        elif not left_char or lookup[left_char.pop()] != char :
            return print(False)

    return print(not left_char)

is_valid_paranthesis("()")
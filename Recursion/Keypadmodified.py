def getkeys(num):

    keys = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    return list(keys[num])

def keypad(number, proc = "", index = 0, result= []):

    if index == len(number):
        result.append(proc)
        return

    # selecting each key at once
    key = int(number[index])
    # geting correspond keys to it.
    keys = getkeys(key)

    # if our key don't have any keys correspond to that the we must move to next key
    if keys == []:
        keypad(number, proc, index + 1, result)

    for item in keys:
        keypad(number, proc + item, index + 1, result)

    return result

print(keypad("12013"))

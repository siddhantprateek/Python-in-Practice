def getReverseElements(unproc, result = []):


    # if unproc == "":
    #     result.append(proc)
    #     return
    rev = []
    for i in range(len(unproc)):
        for j in range(i + 1,len(unproc)):
            item = unproc[i: j]
            result.append(item)
            rev.append(item[::-1])
    return print(result)

getReverseElements("abab")
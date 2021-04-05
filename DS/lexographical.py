def freqArr(word: str):
    freq_Arr = [0]*26

    for char in word:
        index = ord(char) - ord("a")
        freq_Arr[index] += 1

    return freq_Arr


def lexicographical(freq, wordsize, proc = "", solution = []):

    if len(proc) == wordsize:
        solution.append(proc)
        return


    for index in range(26):
        if freq[index] > 0:
            freq[index] -= 1
            lexicographical(freq, wordsize, proc + chr(ord("a") + index), solution)
            freq[index] += 1

    return solution


word = "hello"
freq = freqArr(word)

solution = lexicographical(freq, len(word))
print(solution)
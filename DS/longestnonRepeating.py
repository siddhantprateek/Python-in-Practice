def longestStringNoRepeatingChar(word):
    
    window_start, max_length = 0, 0
    char_index_map = {}
    
    for window_end in range(len(word)):
        
        right_char = word[window_end]
        if right_char in char_index_map:
            # compare window_start and prev position of repeating char finding max of them
            window_start = max(window_start, char_index_map[right_char] + 1)
            
        char_index_map[right_char] = window_end
        max_length= max(max_length, window_end -window_start+ 1)
    
    return print(max_length)

longestStringNoRepeatingChar("aabccbb")
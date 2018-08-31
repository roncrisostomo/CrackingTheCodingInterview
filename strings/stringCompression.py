def stringCompression(s):
    """
        s: a string
        
        Returns a compressed version of string using counts of repeated
        characters
    """
    if len(s) == 0:
        return ''
    
    result = ''
    # Initialize first run using first character
    curRunChar = s[0]
    curRun = 1
    # Iterate starting from second character
    for character in s[1:]:
        # If different from current run, update result and start new run
        if curRunChar != character:
            result += curRunChar + str(curRun)
            curRunChar = character
            curRun = 1
        # If same, update run length
        else:
            curRun += 1
    
    # Add the last run to result
    result += curRunChar + str(curRun)
        
    return result
    
s = 'a'             # Ans: a1
s = 'aabcccccaaa'   # Ans: a2b1c5a3
print(stringCompression(s))

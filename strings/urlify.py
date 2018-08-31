def urlify(s, l):
    """
    s: a string, with sufficient space at the end to hold additional characters
    l: "true" length of string, an int
    
    Replaces all spaces in string with '%20'
    """
    # Approach 1: Use string.split()
#    return '%20'.join(s.split())

    # Assume s is fixed array of characters, so approach 1 cannot be used
    
    # Approach 2: Iterate backwards from end of 'true' string--move characters
    #   to the end, replace space characters with '%20' before moving
    s2 = list(s)
    lastIndex = len(s) - 1
    for i in range(l - 1, -1, -1):
        if s[i] == ' ':
            s2[lastIndex - 2] = '%'
            s2[lastIndex - 1] = '2'
            s2[lastIndex] = '0'
            lastIndex -= 3
        else:
            s2[lastIndex] = s[i]
            lastIndex -= 1
            
    return ''.join(s2)

s = 'Mr John Smith    '
l = 13
# Ans: 'Mr%20John%20Smith'

print(urlify(s, l))

def checkPermutation(s1, s2):
    """
    s1, s2: strings
    
    Determine if one string is a permutation of the other
    """
    
    if len(s1) == 0 or len(s2) == 0:
        return False
    
    # Add letters of s1 in hash table
    s1Letters = {}
    for l in s1:
        if l in s1Letters:
            s1Letters[l] += 1
        else:
            s1Letters[l] = 1
    
    # For each letter in s2, find and remove similar letter in hash table
    # If letter is not found, strings are not permutations of each other
    for l in s2:
        if l in s1Letters and s1Letters[l] > 0:
            s1Letters[l] -= 1
        else:
            return False
        
    return True

#s1 = 'a'
#s2 = 'e'
#s1 = 'abcde'
#s2 = 'edcba'
s1 = 'tomcat'
s2 = 'cattom'
print(checkPermutation(s1, s2))

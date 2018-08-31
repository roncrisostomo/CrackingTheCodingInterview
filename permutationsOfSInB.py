def permutationsOfSInB(s, b):
    """
    s, b: strings, with s shorter than b
    
    Finds permutations of s in b
    
    Returns a list of locations of each permutation, i.e. int indices in b
    """
    
    # For each contiguous substring bSub in b of length len(s),
    #   if all letters in bSub are in s, then that is a valid answer
    # For the next bSub, no need to check the first len(s)-1 letters since
    #   they are checked in the previous bSub. Remove the first letter in
    #   previous bSub from letters to check, and add the last letter in current
    #   bSub instead.
    
    permutationLocations = []
    lettersToFind = list(s)
    # Dictionary of letters found in b that are in s, mapped to a list of
    #   their position indices in b
    usedLetterIndices = {}
    
    print("Start: Find", lettersToFind)
    
    for i in range(len(s)):
        print(i)
        if b[i] in lettersToFind:
            print("LettersToFind=" + str(lettersToFind) + " b[" + str(i) + "]=" + b[i])
            lettersToFind.remove(b[i])
            if b[i] in usedLetterIndices.keys():
                usedLetterIndices[b[i]].append(i)
            else:
                usedLetterIndices[b[i]] = [i]
    
    if len(lettersToFind) == 0:
        permutationLocations.append(0)
    
    print("Substring 0 Find", lettersToFind, \
          "Used", usedLetterIndices, \
          "Perms", permutationLocations)
    
    for startIndex in range(1, len(b) - len(s) + 1):
        prevLetterIndex = startIndex - 1
        lastLetterIndex = startIndex + len(s) - 1
        
        if b[prevLetterIndex] in usedLetterIndices.keys() and \
        prevLetterIndex in usedLetterIndices[b[prevLetterIndex]]:
            lettersToFind.append(b[prevLetterIndex])
            usedLetterIndices[b[prevLetterIndex]].remove(prevLetterIndex)
        
        if b[lastLetterIndex] in lettersToFind:
            lettersToFind.remove(b[lastLetterIndex])
            if b[lastLetterIndex] in usedLetterIndices.keys():
                usedLetterIndices[b[lastLetterIndex]].append(lastLetterIndex)
            else:
                usedLetterIndices[b[lastLetterIndex]] = [lastLetterIndex]
        
        if len(lettersToFind) == 0:
            permutationLocations.append(startIndex)
    
        print("Substring", startIndex, "Find", lettersToFind, \
              "Used", usedLetterIndices, \
              "Perms", permutationLocations)
    
    return permutationLocations

# Test cases
    
#s = 'ab'
#b = 'bafbab'
# Ans = [0, 3, 4]

#s = 'abb'
#b = 'bafbabba'
# Ans = [0, 3, 4, 5]

#s = 'abbc'
#b = 'cbabbabbac'
# Ans = []

s = 'abbc'
b = 'cbabadcbbabbcbabaabccbabc'
#    0123456789
# Ans = [0, 6, 9, 11, 12, 20, 21]

#s = 'abbc'
#b = 'ecbabadcbbabbcbabaabccbabc'
# Ans = [1, 7, 10, 12, 13, 21, 22]

print(permutationsOfSInB(s, b))

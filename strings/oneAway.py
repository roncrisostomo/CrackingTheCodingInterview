def oneAway(s1, s2):
    """
        s1, s2: strings
        
        Determines whether two strings are one edit (or zero edits) away,
        with possible edits being:
            1. insert a character
            2. remove a character
            3. replace a character
    """
    
    # Check lengths of strings
    # If same length, check edit case 3
    # If lengths differ by one, check edit cases 1 and 2
    # If lengths differ by more than one, then strings are not one edit away
    
    # Iterate over each index in both strings at the same time
    # If a difference is found at current index in both strings, set flag to
    #   note this difference. If another difference is found, then strings
    #   are not one edit away
    #   If checking cases 1 and 2, offset the index for the longer string by 1,
    #       i.e. compare shorter string from current index until end, with
    #       longer string from current index + 1 until end
    
    # Assign either string as longer or shorter, even if they have same length
    longerString = s1
    shorterString = s2
    if len(s2) > len(s1):
        longerString = s2
        shorterString = s1
    
    # If string lengths differ by more than one, then they are not one edit away
    lenDiff = len(longerString) - len(shorterString)
    if lenDiff > 1:
        return False
    
    # If string lengths differ by one, then they *may* be one insert/remove edit away
    checkInsertRemove = lenDiff == 1
    
    # Compare each letter at the same index in both strings
    for i in range(len(shorterString)):
        ithOfShorter = shorterString[i]
        ithOfLonger = longerString[i]
        
        # When a difference is found:
        if ithOfShorter != ithOfLonger:
            # Compare the remaining substrings
            remShorter = shorterString[i + 1:]
            remLonger = longerString[i + 1:]
            # If checking for an insert/remove edit, then include the current
            #   letter for shorter string in the comparison
            if checkInsertRemove:
                remShorter = ithOfShorter + remShorter
            
            # If the substrings are the same, then strings are one edit away
            return remShorter == remLonger
    
    # If no difference is found, then strings are zero edits away
    return True

#s1, s2 = 'pale', 'ple'      # True
#s1, s2 = 'pales', 'pale'    # True
#s1, s2 = 'pale', 'bale'     # True
#s1, s2 = 'pale', 'bake'     # False
s1, s2 = 'pale', 'pke'      # False
print(oneAway(s1, s2))

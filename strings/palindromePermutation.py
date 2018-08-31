def palindromePermutation(s):
    """
    s: a string
    
    Determine if string is a permutation of a palindrome, excluding spaces
    """
    
    # For a palindrome with even length, each letter must have an even number
    #   of occurrences in string
    # For odd length, there must be one letter with odd number of occurrences
    #   (the letter in the middle of palindrome)
    
    # Add letters of s to a hash table
    letterCounts = {}
    for letter in s.lower():
        if letter == ' ':
            continue
        if letter in letterCounts:
            letterCounts[letter] += 1
        else:
            letterCounts[letter] = 1
    
    print(letterCounts)
    
    # If length of string is even, then all letters must have even number of
    #   occurrences. If odd, there must be one letter with odd number of
    #   occurrences.
    maxOddAllowed = 0
    if sum(letterCounts.values()) % 2 == 1:
        maxOddAllowed = 1
    
    oddOccurrences = 0
    for letterCount in letterCounts.values():
        if letterCount % 2 == 1:
            oddOccurrences += 1
            if oddOccurrences > maxOddAllowed:
                return False
            
    return True

s = 'Tact Coa'
print(palindromePermutation(s))
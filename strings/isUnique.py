def isUnique(s):
    """
        s: a string
        
        Determines if string has all unique characters, without using
        data structures
        
        Returns True if all unique, false otherwise
    """
    
    # Approach 1: Use hash table--O(n), but breaks "no data structure" rule
#    letters = {}
#    for l in s:
#        if l in letters:
#            return False
#        else:
#            letters[l] = 1
#    
#    return True
    
    # Approach 2: Brute force without data structure--O(n^2)
#    for i in range(len(s)):
#        for j in range(i + 1, len(s)):
#            if s[i] == s[j]:
#                return False
#    
#    return True
    
    # Approach 3: Use special binary representation with bit set to 1 for a
    #   character's position in alphabet (can also be extended to ascii
    #   characters, but will need 256-bit variable, possible in Python)
    
    if len(s) == 0:
        return False
    
    if len(s) == 1:
        return True
    
    # Helper function: Converts character to binary format with a 1 at the
    #   position of character in alphabet, e.g. a=1, b=10, c=100, f=100000
    def convertToBinary(c):
        i = ord(c) - ord('a')
        s = '1' + '0' * i
        return int(s, 2)
    
    # Get sum of binary representations of each character
    binSum = convertToBinary(s[0])
    for l in s[1:]:
        binL = convertToBinary(l)
        newSum = binSum + binL
        
        # If there is carryover, then there is a repeated character
        # If there is no carryover, ANDing the sum and either binary addend
        #   should result in just the addend
        #   e.g. newSum =  110  
        #        binL   =  100 = newSum & binL
        #        binSum =   10 = newSum & binSum
        if binL & newSum != binL or binSum & newSum != binSum:
            return False
        
        binSum = newSum
    
    # If no carryover, all characters are unique
    return True


print(isUnique(''))
print(isUnique('ab'))
print(isUnique('abb'))
print(isUnique('abc'))
print(isUnique('z'))
print(isUnique('zb'))
print(isUnique('asdgbewrhe'))

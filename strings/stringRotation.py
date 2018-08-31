def stringRotation(s1, s2):
    """
    s1, s2: strings
    
    Determines if string s2 is a rotation of string s1 with only one call to
    method isSubstring
    """
    if len(s1) == 0 or len(s2) == 0 or len(s1) != len(s2):
        return False
    
    # Approach: If strings are of equal length and one string is a substring of
    #   the other appended to itself ('hello' -> 'hellohello'), then the two
    #   are rotations of each other--O(n), n = length of either string (equal)
    
    def isSubstring(s1, s2):
        return s1 in s2
    
    return isSubstring(s1, s2 * 2)

#s1, s2 = 'waterbottle', 'erbottlewat'   # True
#s1, s2 = 'waterbottle', 'erbottlewate'  # False
#s1, s2 = '', 'wat'                      # False
#s1, s2 = 'hail', 'ilha'                 # True
s1, s2 = 'hail', 'hailhail'             # False
print(stringRotation(s1, s2))

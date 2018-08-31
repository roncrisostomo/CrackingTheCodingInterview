def get_permutations(s):
    """
    Returns a list of all permutations of the given string
    """
    
    def perm(subStr, remaining, permutations):
        # If there are no more letters to assign, subStr is the complete string
        #   and one permutation of s
        if (len(remaining) == 0):
            permutations.append(subStr)
        else:
            # For each position in string, try assigning each letter
            for letterIndex in range(len(remaining)):
                perm(subStr + remaining[letterIndex],\
                     remaining[0:letterIndex] + remaining[letterIndex + 1:],\
                     permutations)
    
    permutations = []
    
    # Start with no substring and with all letters of s remaining
    perm('', s, permutations)
    
    return permutations

print(get_permutations("ABCD"))

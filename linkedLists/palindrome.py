from linkedLists import createSinglyLinkedList

def palindrome(sll):
    """ Return whether given linked list is a palindrome """
    # If empty list, then not a palindrome
    if sll.head == None:
        return False
    
    # Approach 1: Convert to list, then check if list is a palindrome--O(n)
#    l = []
#    curNode = sll.head
#    while curNode != None:
#        l.append(curNode.data)
#        curNode = curNode.next
#    
#    for i in range(len(l) // 2):
#        if l[i] != l[len(l) - 1 - i]:
#            return False
#    
#    return True
    
    # Approach 2: Use runner technique to get values of nodes up to the middle
    #   node in list, then compare each node in second half of list--O(n)
    doubleRunner = sll.head
    singleRunner = sll.head
    # 1 2 3 4       1 2 3 4 5
    # d             d
    # s             s
    #     d             d
    #   s             s
    #   mid = 2             d
    #                   s
    #                   mid = 3
    
    firstHalfValues = []
    while doubleRunner != None:
        firstHalfValues.append(singleRunner.data)
        if doubleRunner.next != None and doubleRunner.next.next != None:
            doubleRunner = doubleRunner.next.next
            singleRunner = singleRunner.next
    
    print(firstHalfValues)
    
    # At this point, singleRunner is at the middle node
    # For each node after the middle node, values must match firstHalfValues
    #   in reverse
    # Iterate through firstHalfValues in reverse
    for i in range(len(firstHalfValues) - 1, -1, -1):
        singleRunner = singleRunner.next
        # If values do not match those in second half,
        #   then list is not a palindrome
        print(firstHalfValues[i], singleRunner.data)
        if firstHalfValues[i] != singleRunner.data:
            return False
    
    return True

# Test cases
#a = [7, 1, 7]      # Ans: True
#a = [7, 1, 6]      # Ans: False
#a = [2, 1, 6, 5]   # Ans: False
a = [2, 1, 1, 2]    # Ans: True
    
# Create singly linked list for testing
sll = createSinglyLinkedList(a)

print(palindrome(sll))

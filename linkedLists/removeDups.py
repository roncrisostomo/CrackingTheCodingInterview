from linkedLists import createSinglyLinkedList

def removeDups(ll):
    """
    Remove duplicates from specified linked list without using a
    temporary buffer
    
    ll: an unsorted linked list
    
    Return nothing
    """
#    # Approach 1: Use temporary buffer first, a set--O(n)
#    # Add unique elements of linked list to set
#    data = set()
#    # Iterate through linked list
#    prevNode = None # Needed for singly-linked lists
#    curNode = ll.head
#    while curNode != None:
#        # If data is not in set, add it in
#        if curNode.data not in data:
#            data.add(curNode.data)
#            prevNode = curNode
#        # If data is in set, remove node from linked list
#        else:
#            # Point previous node to current node's next node
#            prevNode.next = curNode.next
#            
#        curNode = curNode.next

    # Approach 2: No temporary buffer, brute force--O(n^2)
    # For each node, check and remove other nodes with same data
    curNode = ll.head
    while curNode != None:
        prevNode = curNode # Needed for singly-linked lists
        compareNode = curNode.next
        # Compare curNode with each of the remaining nodes
        while compareNode != None:
            # If same data, remove compareNode
            if curNode.data == compareNode.data:
                # Point previous node to compareNode's next node
                prevNode.next = compareNode.next
            # Otherwise, update prevNode
            else:
                prevNode = compareNode
            
            compareNode = compareNode.next
        
        curNode = curNode.next

# Test cases
a = [3, 4, 3, 3, 1, 1, 6, 2]  # Ans: 3 4 1 6 2
#a = [3, 3, 1, 1]        # Ans: 3 1
#a = [1, 1, 1]           # Ans: 1

# Create unsorted linked list for testing
sll = createSinglyLinkedList(a)

print("Before:", sll)
removeDups(sll)
print("After:", sll)

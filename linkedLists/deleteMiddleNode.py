from linkedLists import createSinglyLinkedList

def deleteMiddleNode(n):
    """
    Delete the given node from the list
    
    n: a node somewhere in the middle of a singly linked list
    
    Return nothing
    """
    # Replace given node's data and next fields with those of the next node's
    n.data = n.next.data
    n.next = n.next.next
    
# Test cases
a, middleNodeIndex = [1, 2, 3, 4], 1    # Ans: 1 3 4
#a, middleNodeIndex = [3, 3, 1, 1], 2    # Ans: 3 3 1

# Create singly linked list for testing
sll = createSinglyLinkedList(a)

# Get middle node to confirm it gets deleted
middleNode = sll.head
curIndex = 0
while curIndex < middleNodeIndex:
    middleNode = middleNode.next
    curIndex += 1
print(middleNode)

# Delete middle node, and check resulting list
deleteMiddleNode(middleNode)
print(sll)

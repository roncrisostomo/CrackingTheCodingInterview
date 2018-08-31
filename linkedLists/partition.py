from linkedLists import createSinglyLinkedList

def partition(sll, p):
    """
    Partition the given singly linked list such that all values less than p
    come before all values greater than or equal to p
    
    n: a singly linked list
    p: partition value, an int
    """
    if sll.head == None:
        return
    
    # Iterate through list, appending values greater than p to the tail--O(n)
    
    # Find tail and length of list
    tail = sll.head
    lenSLL = 1
    while tail.next != None:
        tail = tail.next
        lenSLL += 1
    
    # Iterate through list
    prevNode = None
    curNode = sll.head
    for i in range(lenSLL):
        # If value is greater than or equal to p, append to tail
        if curNode.data >= p:
            if prevNode != None:
                prevNode.next = curNode.next
            # Append curNode to tail, and make it the new tail
            tail.next = curNode
            tail = curNode
            # Check the node next to curNode before it was moved to the end
            curNode = curNode.next
            # Set new tail node to have no next node
            tail.next = None
        # Otherwise, check next node
        else:
            prevNode = curNode
            curNode = curNode.next
    

# Test case
a, p = [3, 5, 8, 5, 10, 2, 1], 5    # Ans: 3 2 1 5 8 5 10 (Book answer: 3 1 2 10 5 5 8)

# Create singly linked list for testing
sll = createSinglyLinkedList(a)

partition(sll, p)
print(sll)

from linkedLists import createSinglyLinkedList

def returnKthToLast(sll, k):
    """
    Return the kth to last element of singly linked list
    
    sll: a singly linked list
    k: count from last element in singly linked list to element to find
    """
    # Minimum k is 1, i.e. 1st to last element ==last element
    if k < 1:
        return
    
    # Approach 1: Two runs, one to get length of list, another to get kth to
    #   last element in list--O(n)
    # Get length of linked list
    lenSLL = 0
    curNode = sll.head
    while curNode != None:
        lenSLL += 1
        curNode = curNode.next
    
    # Maximum k is length of list, i.e. nth to last element of list with
    #   length n == first element
    if k > lenSLL:
        return
    
    # Get ith element, where i is zero-based index of kth element from last item
    i = lenSLL - k
    index = 0
    curNode = sll.head
    while curNode != None:
        if i == index:
            return curNode
        curNode = curNode.next
        index += 1
    
# Test cases
a, k = [3, 4, 3, 3, 1, 1, 6, 2], 2  # Ans: 6
#a, k = [3, 3, 1, 1], 3        # Ans: 3
#a, k = [1, 1, 1], 1           # Ans: 1

# Create singly linked list for testing
sll = createSinglyLinkedList(a)

print(returnKthToLast(sll, k))

from linkedLists import createSinglyLinkedList, Node, appendToSinglyLinkedList

def intersection(sll1, sll2):
    """
    Return the node where 2 linked lists intersect, None if no intersection.
    
    sll1, sll2: singly-linked lists
    """
    # Approach: Add each node in both lists to a hash table. If a node already
    #   exists in table, then the 2 lists intersect at that node--
    #   O(n), where n is the sum of the lengths of the linked lists
    nodeSet = set()
    
    # Add all nodes from list 1
    curNode = sll1.head
    while curNode != None:
        nodeSet.add(curNode)
        curNode = curNode.next
    
    # Add nodes from list 2
    curNode = sll2.head
    while curNode != None:
        # If already in set, then the 2 lists intersect at curNode
        if curNode in nodeSet:
            return curNode
        else:
            nodeSet.add(curNode)
        curNode = curNode.next
    
    # No intersection
    return None


# Test cases
a1, a2 = [1, 2, 3], [4, 5]
    
# Create singly linked lists for testing
sll1 = createSinglyLinkedList(a1)
sll2 = createSinglyLinkedList(a2)

# Intersecting case: Add common node(s) to both lists. Ans: 100
n = Node(100)
# Non-intersecting case Ans: None
appendToSinglyLinkedList(sll1, n)
appendToSinglyLinkedList(sll2, n)

res = intersection(sll1, sll2)
if res != None:
    print(sll1, "and", sll2, "intersect at", res)
else:
    print("No intersection")

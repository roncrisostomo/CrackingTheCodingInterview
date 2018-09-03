from linkedLists import createSinglyLinkedList, Node, appendToSinglyLinkedList

def loopDetection(circularSLL):
    """
    circularSLL: a singly-linked list that contains a loop
    
    Return node where the loop starts
    """
    # Approach: Add nodes to hash table. If a node already exists in table,
    #   then loop begins at that node--O(n)
    nodeSet = set()
    curNode = circularSLL.head
    while curNode != None:
        if curNode in nodeSet:
            return curNode
        else:
            nodeSet.add(curNode)
        curNode = curNode.next
    
    return None


# Test cases
n2 = Node('B')
n3 = Node('C')
n4 = Node('D')
n5 = Node('E')

sll = createSinglyLinkedList('A')
appendToSinglyLinkedList(sll, n2)
appendToSinglyLinkedList(sll, n3)
appendToSinglyLinkedList(sll, n4)
appendToSinglyLinkedList(sll, n5)
appendToSinglyLinkedList(sll, n3) # Loop here. Ans: 'C' (n3)
   
print(loopDetection(sll))

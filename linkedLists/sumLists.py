from linkedLists import Node, SinglyLinkedList, createSinglyLinkedList

def sumLists(sll1, sll2, reverse):
    """
    Return the sum of the 2 digits represented by linked lists as another
    linked list containing digits of sum
    
    sll1, sll2: singly linked lists with each element being digits of a
        number in reverse order (i.e. head has least significant digit)
    reverse: whether digits in linked lists are in reverse order, a boolean
    """
    if sll1.head == None or sll2.head == None:
        return
    
    # Approach 1: Convert linked lists to numbers, get sum, then convert sum
    #   to linked list--O(n), where n is length of longer list
    
#    def toNumber(sll, reverse):
#        """
#        sll: singly linked list with each element being digits of a number
#        reverse: whether digits in linked list are in reverse order,
#            a boolean
#        """
#        curNode = sll.head
#        num = curNode.data
#        curIndex = 1
#        while curNode.next != None:
#            curNode = curNode.next
#            if reverse:
#                num += curNode.data * 10**curIndex
#                curIndex += 1
#            else:
#                num = curNode.data + num * 10
#        return num
#    
#    def toSinglyLinkedList(num, reverse):
#        """
#        num: an integer
#        reverse: whether to store digits to linked list in reverse order,
#            a boolean
#        """
#        sll = SinglyLinkedList()
#        prevNode = None
#        curNode = None
#        while num > 0:
#            digit = num % 10
#            if reverse:
#                if prevNode == None:
#                    sll.head = Node(digit)
#                    curNode = sll.head
#                else:
#                    curNode = Node(digit)
#                    prevNode.next = curNode
#            else:
#                curNode = Node(digit)
#                curNode.next = prevNode
#                sll.head = curNode
#            prevNode = curNode
#            num //= 10
#        return sll
#    
#    s = toNumber(sll1, reverse) + toNumber(sll2, reverse)
#    return toSinglyLinkedList(s, reverse)
    
    
    # Approach 2: Add each item at the same "index" (position relative to head)
    #   in each list, carry over to next index (if there is carryover)--O(n),
    #   where n is length of longer list
    sllSum = SinglyLinkedList()
    
    l1CurNode = sll1.head
    l2CurNode = sll2.head
    
    def reverseLinkedList(sll):
        """ Reverse the order of elements in the given linked list """
        # 1 2 3, head = 1, lastMoved = None
        # 2 3 | 1, head = 2, 1.next = None, lastMoved = 1, 3 not linked to 1
        # 3 | 2 1, head = 3, 2.next = 1, lastMoved = 2, 3 not linked to 2
        # 3 2 1, head = 3, 3.next = 2, lastMoved = 3
        # Stop when head == lastMoved
        lastMoved = None
        while sll.head != lastMoved:
            prevHead = sll.head
            if prevHead.next != None:
                sll.head = prevHead.next
            prevHead.next = lastMoved
            lastMoved = prevHead
    
    # If digits are listed in forward order, reverse the linked lists, do 
    #   procedure for summing numbers in reverse, then reverse again to restore
    #   linked lists to original state
    if not reverse:
        reverseLinkedList(sll1)
        reverseLinkedList(sll2)
        l1CurNode = sll1.head
        l2CurNode = sll2.head
    
    sumVal = 0
    prevSumNode = None
    while l1CurNode != None or l2CurNode != None or sumVal > 0:
        if l1CurNode != None:
            sumVal += l1CurNode.data
            l1CurNode = l1CurNode.next
            
        if l2CurNode != None:
            sumVal += l2CurNode.data
            l2CurNode = l2CurNode.next
        
        onesDigit = sumVal % 10
        sumVal //= 10
        sumNode = Node(onesDigit)
        
        if prevSumNode == None:
            sllSum.head = sumNode
        else:
            prevSumNode.next = sumNode
        
        prevSumNode = sumNode
    
    # Restore linked lists to original state, and return sum in forward order
    if not reverse:
        reverseLinkedList(sll1)
        reverseLinkedList(sll2)
        reverseLinkedList(sllSum)
    
    return sllSum

# Test cases
#a1, a2 = [7, 1, 6], [5, 9, 2]  # Ans: Reverse = 2 1 9, Forward = 1 3 0 8
#a1, a2 = [7, 1, 6], [0]        # Ans: Reverse = 7 1 6, Forward = 7 1 6
a1, a2 = [7, 1, 6], [8, 1]      # Ans: Reverse = 5 3 6, Forward = 7 9 7

# Create singly linked lists for testing
sll1 = createSinglyLinkedList(a1)
sll2 = createSinglyLinkedList(a2)

print(sll1, "+", sll2, "=", "[Reverse]", sumLists(sll1, sll2, True),
      "[Forward]", sumLists(sll1, sll2, False))

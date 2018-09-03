"""
Linked list implementations are kept as basic as possible on purpose, with only
a head node reference for singly-linked lists and head and tail node references
for doubly-linked lists. This is so that scripts using these lists would
contain all the code that could affect running time.

This file also provides helper functions intended for use in testing solutions.
"""

class Node:
    """
    Node of a linked list (either singly- or doubly- linked)
    """
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return str(self.data)
    
class SinglyLinkedList:
    def __init__(self, head = None):
        self.head = head
        
    def __str__(self):
        curNode = self.head
        s = ''
        while curNode != None:
            s += str(curNode.data) + ' '
            curNode = curNode.next
        return s
    
class DoublyLinkedList(SinglyLinkedList):
    def __init__(self, head = None, tail = None):
        super().__init__(head)
        self.tail = tail
    
    def reverseStr(self):
        curNode = self.tail
        s = ''
        while curNode != None:
            s += str(curNode.data) + ' '
            curNode = curNode.prev
        return s

def createSinglyLinkedList(dataList):
    """
    dataList: list of data to put into singly linked list
    """
    if len(dataList) == 0:
        return SinglyLinkedList()
    
    head = Node(dataList[0])
    sll = SinglyLinkedList(head)
    curNode = sll.head
    for data in dataList[1:]:
        curNode.next = Node(data)
        curNode = curNode.next
    
    return sll

def createDoublyLinkedList(dataList):
    """
    dataList: list of data to put into doubly linked list
    """
    if len(dataList) == 0:
        return DoublyLinkedList()
    
    head = Node(dataList[0])
    tail = Node(dataList[len(dataList) - 1])
    dll = DoublyLinkedList(head, tail)
    curNode = dll.head
    for data in dataList[1 : len(dataList) - 1]:
        curNode.next = Node(data)
        curNode.next.prev = curNode
        curNode = curNode.next
    curNode.next = dll.tail
    dll.tail.prev = curNode
    
    return dll

def appendToSinglyLinkedList(sll, newNode):
    """
    sll: singly-linked list to append to
    newNode: node to append
    """
    # Find the tail node
    curNode = sll.head
    while curNode.next != None:
        curNode = curNode.next
    # Append new node to tail
    curNode.next = newNode


if __name__ == "__main__":
    sll = createSinglyLinkedList([0, 1, 2, 3, 4])
    dll = createDoublyLinkedList([0, 1, 2, 3, 4])
    
    print(sll)
    print(dll)
    print(dll.reverseStr())
    
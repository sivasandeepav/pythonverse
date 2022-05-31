
class SinglyLinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None


class DoublyLinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


def addNodeS(headNode, value):
    temp = SinglyLinkedListNode(value)
    if headNode is None:
        print("headnode is new node")
        print(temp.value)
        headNode = temp
    else:
        p = headNode
        while p.next is not None:
            p = p.next
        p.next = temp
    return headNode


def addNodeD(headNode, value):
    temp = DoublyLinkedListNode(value)
    if headNode is None:
        headNode = temp
    else:
        p = headNode
        while p.next is not None:
            p = p.next
        p.next = temp
        temp.prev = p
    return headNode


def deleteNodeS(node):
    if node is None or node.next is None:
        pass
    node.value = node.next.value
    node.next = node.next.next


if __name__ == "__main__":

    # Singly Linked List operations
    headNodeS = SinglyLinkedListNode(None)

    addNodeS(headNodeS, 23)
    addNodeS(headNodeS, 24)
    addNodeS(headNodeS, 25)
    addNodeS(headNodeS, 26)
    addNodeS(headNodeS, 27)
    addNodeS(headNodeS, 28)
    addNodeS(headNodeS, 29)
    addNodeS(headNodeS, 30)

    headNodeS = headNodeS.next
    temp = headNodeS

    # Print full sequence once after adding all nodes
    print("Full Sequence after adding all nodes : ")
    while temp.next is not None:
        print(temp.value)
        temp = temp.next
        if temp.next is None:
            print(temp.value)

    # Deleting a node
    to_del = headNodeS.next.next.next
    deleteNodeS(to_del)

    # After a node is deleted
    print("After deleting one node : ")
    temp = headNodeS
    while temp.next is not None:
        print(temp.value)
        temp = temp.next
        if temp.next is None:
            print(temp.value)

    # Doubly Linked LIst operations
    headNodeD = DoublyLinkedListNode(None)

    print(addNodeD(headNodeD, 100))
    print(addNodeD(headNodeD, 101))
    print(addNodeD(headNodeD, 102))
    print(addNodeD(headNodeD, 103))
    print(addNodeD(headNodeD, 104))
    print(addNodeD(headNodeD, 105))
    print(addNodeD(headNodeD, 106))
    print(addNodeD(headNodeD, 107))

    headNodeD = headNodeD.next
    # Printing in forward order
    print("Forward order of Doubly Linked List :")
    tempD = headNodeD
    while tempD.next is not None:
        print(tempD.value)
        tempD = tempD.next
        if tempD.next is None:
            print(tempD.value)

    # Printing in reverse order
    print("Reverse order of Doubly Linked List :")
    while tempD.prev is not None:
        print(tempD.value)
        tempD = tempD.prev

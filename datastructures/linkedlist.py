
class SinglyLinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None


def addNode(headNode, value):
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
    print(headNode)
    return headNode


def deleteNode(node):
    if node is None or node.next is None:
        pass
    node.value = node.next.value
    node.next = node.next.next


if __name__ == "__main__":
    headNode = SinglyLinkedListNode(None)

    print(addNode(headNode, 23))
    print(addNode(headNode, 24))
    print(addNode(headNode, 25))
    print(addNode(headNode, 26))
    print(addNode(headNode, 27))
    print(addNode(headNode, 28))
    print(addNode(headNode, 29))
    print(addNode(headNode, 30))

    temp = headNode
    while temp.next is not None:
        print(temp.value)
        temp = temp.next

    to_del = headNode.next.next.next
    deleteNode(to_del)

    temp = headNode
    while temp.next is not None:
        print(temp.value)
        temp = temp.next

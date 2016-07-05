# # palindrome

from LinkedList import Node


def checkIntersect(head, head2):
    n = head
    m = head2
    len1 = 0
    len2 = 0

    while n != None:
        len1+=1
        n = n.next

    while m != None:
        len2 += 1
        m = m.next

    diff = 0
    n = head
    m = head2
    if len1 > len2:
        diff = len1 - len2
        #chop n
        for i in range(0,diff):
            n = n.next
    elif len2 > len1:
        diff = len2 - len1
        # chop m
        for i in range(0, diff):
            m = m.next

    # are same lengths now, compare
    while n != None:
        if n == m:
            return n
        n = n.next
        m = m.next

    return None



head = Node("c")
head2 = Node("c")
head2.appendToTail("a")
head2.appendToTail("r")

head3 = Node("b")
head3.appendToTail("u")
head3.appendToTail("s")

head.appendNode(head2)
head3.appendNode(head2)

head.printLL()
head3.printLL()
result = checkIntersect(head, head3)
if result != None:
    print(result.data)
else:
    print(False)
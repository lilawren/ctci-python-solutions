# palindrome

from LinkedList import Node


def checkPalin(head):
    mystr = ""
    n = head
    while n != None:
        mystr += str(n.data)
        n = n.next

    mystr2 = mystr[::-1]
    if mystr == mystr2:
        return True
    else:
        return False



head = Node("r")
head.appendToTail("a")
head.appendToTail("c")
head.appendToTail("e")
head.appendToTail("c")
head.appendToTail("a")
head.appendToTail("r")

head.printLL()
print(checkPalin(head))
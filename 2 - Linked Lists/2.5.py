# add two numbers stored in reverse as linked list

from LinkedList import Node

def sumLL(h1, h2):
    n = h1
    m = h2
    num_n = ""
    num_m = ""
    while(n != None): #while not at end yet
        num_n = str(n.data) + num_n
        n = n.next
    while (m != None):  # while not at end yet
        num_m = str(m.data) + num_m
        m = m.next

    #construct the linked list
    numstr = str(int(num_n) + int(num_m))

    if len(numstr) < 1:
        return None
    head = Node(numstr[0])
    for i in range(1,len(numstr)):
        head.appendToTail(numstr[i])

    return head



#follow up: if in forward order
'''
    n = h1
    m = h2
    num_n = ""
    num_m = ""
    while (n != None):  # while not at end yet
        num_n =  num_n + str(n.data)
        n = n.next
    while (m != None):  # while not at end yet
        num_m = num_m + str(m.data)
        m = m.next

    # construct the linked list
    numstr = str(int(num_n) + int(num_m))

    if len(numstr) < 1:
        return None
    head = Node(numstr[0])
    for i in range(1, len(numstr)):
        head.appendToTail(numstr[i])

    return head
'''

n1 = Node(7)
n1.appendToTail(1)
n1.appendToTail(6)

n2 = Node(5)
n2.appendToTail(9)
n2.appendToTail(2)

n1.printLL()
n2.printLL()
result = sumLL(n1, n2)
result.printLL()
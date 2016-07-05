# # palindrome

from LinkedList import Node


def detectLoop(head):
    fast = head
    slow = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if fast == None or fast.next == None: #do not meet
        return None

    #move slow to head, keep fast at meeting point
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return fast


head = Node("a")
head.appendToTail("b")
head.appendToTail("c")
head.appendToTail("d")
tmp = Node("e")
tmp.next = head.next.next
head.appendNode(tmp)

result = detectLoop(head)
print(result.data)
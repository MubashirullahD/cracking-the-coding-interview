"""
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list. 
Hints: #8, #25, #47, #67, # 726
"""
from linkedlist import linkedlist

def kth_last(linkedlist, kth):
    """
    2N approach
    """
    node = linkedlist.head
    count = 1   # Assume one node does exist

    while(node.next is not None):
        node = node.next
        count += 1
    # if there are 10 total elements and we get asked 3rd to last (k=3)
    # what do we do? 10-3 = 7 
    # 10 last, 9 second, 8 third (add 1)
    want_node = count - kth + 1

    if want_node <= 0 or want_node > count:
        raise Exception("Number beyound size of linked list.", count)

    node = linkedlist.head
    count = 1
    if count == want_node:
        print("Kth to last,", node.data)

    while(node.next is not None):
        node = node.next
        count += 1
        if count == want_node:
            print("Kth to last,", node.data)


def kth_last_recursive(node, kth):
    """
    O(N)
    """
    if node.next is None:
        if kth == 1:
            print("Kth to last", node.data)
        return 1
        
    count = kth_last_recursive(node.next, kth) + 1
    if count == kth:
        print("Kth to last", node.data)
    return count

    # We should write another function where we call this one.
    # This way we can give the head node reference and check if k is a valid input
    # Interesting, invalid inputs dont return anything with this implementation

def kth_last_two_pointer(linkedlist, kth):
    """
    O(N)
    """
    p1 = linkedlist.head
    p2 = linkedlist.head
    for _ in range(kth):
        p2 = p2.next

    if p2 is None:
        print("Kth to last,,", p1.data)
        return

    while(p2.next is not None):
        p1 = p1.next
        p2 = p2.next
        
    p1 = p1.next # This has to do with the definition of kth to last. We added 1 in the other methods too
    print("Kth to last,,", p1.data)
    




if __name__ == "__main__":
    test_list = linkedlist(10)
    test_list.head.append_to_tail(20)
    test_list.head.append_to_tail(30) 
    test_list.head.append_to_tail(40) 
    test_list.head.append_to_tail(50)
    kth_last(test_list, 1)
    kth_last_recursive(test_list.head, 1)
    kth_last_two_pointer(test_list, 1)
    

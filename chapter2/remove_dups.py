"""
Remove Dups: Write code to remove duplicates from an unsorted linked list. 
FOLLOW UP 
How would you solve this problem if a temporary buffer is not allowed?
"""
from linkedlist import linkedlist


def remove_dup(linked_list):
    placeholder = dict()
    pointer1 = linked_list.head         # This guy deletes the dublicate nodes
    pointer2 = linked_list.head.next    # This guy finds the nodes to delete

    if pointer2 is None:                # Only one variable
        return 
    placeholder[pointer1.data] = 1

    while(pointer2.next is not None):
        
        placeholder[pointer2.data] = placeholder.get(pointer2.data, 0) + 1

        if placeholder[pointer2.data] > 1:
            pointer1.next = pointer2.next
            pointer2 = pointer2.next
        else:
            pointer1 = pointer2
            pointer2 = pointer2.next
    
    # Last node case
    placeholder[pointer2.data] = placeholder.get(pointer2.data, 0) + 1

    if placeholder[pointer2.data] > 1:
        pointer1.next = pointer2.next

def _sort(linked_list):
    #bubble sort
    sorted = False

    while(not sorted):
        node = linked_list.head
        sorted = True
        while(node.next is not None):
            if node.data > node.next.data:
                sorted = False
                tmp = node.data
                node.data = node.next.data
                node.next.data = tmp
            node = node.next
    


def remove_dub_no_buff(linked_list):
    # We may have to sort
    _sort(linked_list)
    pointer1 = linked_list.head
    
    while (pointer1.next is not None):
        if (pointer1.data == pointer1.next.data):
            pointer1.next = pointer1.next.next
        else:
            pointer1 = pointer1.next




if __name__ == "__main__":
    test_list = linkedlist(10)
    test_list.head.append_to_tail(20)
    test_list.head.append_to_tail(30)
    test_list.head.append_to_tail(20) #
    test_list.head.append_to_tail(40)
    test_list.head.append_to_tail(20) #
    test_list.head.append_to_tail(50)
    test_list.head.append_to_tail(40) #
    test_list.head.append_to_tail(50) #
    print("Before removing ")
    test_list.print_all()
    remove_dub_no_buff(test_list)
    print("After removing ")
    test_list.print_all()



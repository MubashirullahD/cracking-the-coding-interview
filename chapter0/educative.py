def remove_even_integers(_array: list) -> list:
    """
     Remove Even Integers from Array
    """
    new_arrays = [number for number in _array if number % 2]
    return new_arrays


def merge_sorted_arrays(list1: list, list2: list) -> list:
    """
    Merge Two Sorted Arrays:
    """
    index1 = 0
    index2 = 0
    merged_array = []

    while index1 < len(list1) and index2 < len(list2):
        tmp1 = list1[index1]
        tmp2 = list2[index2]
        if tmp1 < tmp2:
            merged_array.append(tmp1)
            index1 += 1
        elif tmp2 < tmp1:
            merged_array.append(tmp2)
            index2 += 1
        else:
            merged_array.extend([tmp1, tmp2])
            index1 += 1
            index2 += 1

    if index1 < len(list1):
        while index1 < len(list1):
            merged_array.append(list1[index1])
            index1 += 1
    elif index2 < len(list2):
        while index2 < len(list2):
            merged_array.append(list2[index2])
            index2 += 1
    return merged_array


from chapter2.linkedlist import linkedlist


def length_of_linkedlist(linkedlist):
    """
    Find Length of Linked List
    """
    node = linkedlist.head
    count = 1

    while node.next is not None:
        count += 1
        node = node.next
    return count


def search_linkedlist(linkedlist, item):
    """
    Search in Singly Linked List
    """
    node = linkedlist.head
    if node.data == item:
        print("Item found")
        return True
    while node.next is not None:
        node = node.next
        if node.data == item:
            print("Item found")
            return True
    print("Item NOT found")
    return False

from chapter3.stack import Stack

def sort_stack(stack: Stack):
    """
    Sort values in Stack
    """
    # Build a binary search tree from values of stack pops and then do an in-order traveral add to the stack
    # Other approach
    _list = []
    while not stack.is_empty():
        _list.append(stack.pop())
    print("stack items before sorting", _list)
    for values in sorted(_list, reverse=True):
        stack.push(values)


from chapter4.tree import BinarySearchTree, BinaryTreeNode


def smallest_in_BST_iterative(bst: BinarySearchTree):
    node = bst.root
    while node.left is not None:
        node = node.left
    print(node.data)
    return node.data

from chapter4.tree import MinHeap, MaxHeap

def k_smallest_element(_list: list, k):
    """
    Find k smallest elements in a list
    """
    MH = MinHeap(_list[0])
    for val in _list[1:]:
        MH.insert(val)

    return_list = []
    for _ in range(k):
        return_list.append(MH.extract_min())
    return return_list


def k_largest_element(_list: list, k):
    """
    Find k largest elements in an array
    """
    MH = MaxHeap(_list[0])
    for val in _list[1:]:
        MH.insert(val)

    return_list = []
    for _ in range(k):
        return_list.append(MH.extract_max())
    return return_list

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_array = remove_even_integers(array)
    print("Remove even integers from array")
    print("Old array", array)
    print("New array", new_array)
    print("Merge sorted arrays")
    merged_array = merge_sorted_arrays(array, new_array)
    print('merged array', merged_array)
    print("Find length of linked list")
    test_linkedlist = linkedlist(10)
    test_linkedlist.head.append_to_tail(20)
    test_linkedlist.head.append_to_tail(30)
    print("Size of linkedlist", length_of_linkedlist(test_linkedlist))
    print("Search linkedlist returned", search_linkedlist(test_linkedlist, 30))
    print("Search linkedlist returned", search_linkedlist(test_linkedlist, 0))
    test_stack = Stack(50)
    test_stack.push(40)
    test_stack.push(30)
    test_stack.push(10)
    test_stack.push(20)
    sort_stack(test_stack)
    stack_dump = []
    while not test_stack.is_empty():
        stack_dump.append(test_stack.pop())
    print("Stack items", stack_dump)
    print("Smallest number in BST")
    _list = [8, 4, 10, 2, 6, 20]
    BST = BinarySearchTree(_list[0])
    inc = 1
    while inc < len(_list):
        BST.add(_list[inc])
        inc +=1
    smallest_in_BST_iterative(BST)

    _list = [4, 50, 7, 55, 90, 87]
    print("Finding k smallest and largest values in this list", _list)
    print("3 smallest values are:", k_smallest_element(_list, 3))
    print("3 largest values are:", k_largest_element(_list, 3))


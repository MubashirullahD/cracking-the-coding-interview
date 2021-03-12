class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def append_to_tail(self, data):
        end_node = Node(data)
        node = self
        while(node.next != None):
            node = node.next
        node.next = end_node  


class linkedlist:
    def __init__(self, data):
        self.head = Node(data)

    def delete_node(self, data):
        node = self.head

        if (node.data == data):
            self.head = self.head.next
            return

        while(node.next != None):
            if node.next.data == data:
                node.next = node.next.next
                return
            node = node.next
        
        return
        
    def print_all(self):
        node = self.head
        while(node.next is not None):
            print(node.data)
            node = node.next
        print(node.data) # Last node
            
        


if __name__ == "__main__":
    test = linkedlist(10)
    print(test.head.data)
    test.head.append_to_tail(20)
    print(test.head.next.data)
    test.delete_node(20)
    print(test.head.data)
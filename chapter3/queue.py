class Queue:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self, data: int):
        self.first = self.Node(data)
        self.last  = self.first

    def add(self, item):
        if self.last is None:
            self.last = self.Node(item)
            self.first = self.last
        else:
            item = self.Node(item)
            self.last.next = item
            self.last = item

    def remove(self):
        if self.first is None:
            print("Nothing to remove")
            return None
        item = self.first.data
        self.first = self.first.next

        if self.first is None:
            self.last = None
        return item

    def peek(self):
        return self.first.data if self.first is not None else None

    def is_empty(self):
        return self.first is None


if __name__ == "__main__":
    test = Queue(10)
    print(test.remove())
    print(test.remove())
    test.add(20)
    print(test.peek())
    test.add(30)
    print(test.remove())
    print(test.remove())
    print(test.is_empty())





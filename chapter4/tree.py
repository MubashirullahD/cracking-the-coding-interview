class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.top = None

class BinarySearchTree:
    def __init__(self, data):
        self.root = BinaryTreeNode(data)

    def add(self, data):
        node = self.root
        while True:
            if data <= node.data:
                if node.left is not None:
                    node = node.left
                    continue
                else:
                    node.left = BinaryTreeNode(data)
                    break
            else:
                if node.right is not None:
                    node = node.right
                    continue
                else:
                    node.right = BinaryTreeNode(data)
                    break

    def p_in_order(self, node):
        if node is not None:
            self.p_in_order(node.left)
            print(node.data)
            self.p_in_order(node.right)

    def p_pre_order(self, node):
        if node is not None:
            print(node.data)
            self.p_pre_order(node.left)
            self.p_pre_order(node.right)

    def p_post_order(self, node):
        if node is not None:
            self.p_post_order(node.left)
            self.p_post_order(node.right)
            print(node.data)


from queue import Queue


class MinHeap:
    def __init__(self, data):
        self.root = BinaryTreeNode(data)

    def insert(self, data):
        # Part 1 insert in right place
        queue = Queue(0)
        queue.put(self.root)
        while not queue.empty():
            node = queue.get()
            if node.left is None:
                node.left = BinaryTreeNode(data)
                node.left.top = node
                node = node.left
                break
            elif node.right is None:
                node.right = BinaryTreeNode(data)
                node.right.top = node
                node = node.right
                break
            else:
                queue.put(node.left)
                queue.put(node.right)

        # Part 2 bubble to right place
        while node.top is not None:
            if node.data <= node.top.data:
                node.data, node.top.data = node.top.data, node.data
                node = node.top
            else:
                break

    def extract_min(self):
        # Part 1 take data
        if self.root is None:
            print("Nothing left")
            return
        data = self.root.data
        # Part 2 fix the tree
        # Finding the bottommost, rightmost element
        # Last item on Queue
        queue = Queue(0)
        queue.put(self.root)
        while not queue.empty():
            node = queue.get()
            if node.left is not None:
                queue.put(node.left)
            if node.right is not None:
                queue.put(node.right)
        # switch to the top
        self.root.data = node.data

        # Cut that node
        node = node.top
        if node.right is not None and self.root.data == node.right.data:
            node.right = None
        elif node.left is not None and self.root.data == node.left.data:
            node.left = None

        # Bubble down
        node = self.root
        while True:
            left_data = node.left.data if node.left is not None else float("inf")
            right_data = node.right.data if node.right is not None else float("inf")
            # print("left", left_data)
            # print("right", right_data)

            if left_data <= right_data:
                # print("left < right")
                if node.data >= left_data:
                    # print("exchange happened")
                    node.data, node.left.data = node.left.data, node.data
                    node = node.left
                else:
                    break
            else:
                # print("right < left")
                if node.data >= right_data:
                    # print("exchange happened")
                    node.data, node.right.data = node.right.data, node.data
                    node = node.right
                else:
                    break

        return data


class MaxHeap:
    def __init__(self, data):
        self.root = BinaryTreeNode(data)

    def insert(self, data):
        # Part 1 insert in right place
        queue = Queue(0)
        queue.put(self.root)
        while not queue.empty():
            node = queue.get()
            if node.left is None:
                node.left = BinaryTreeNode(data)
                node.left.top = node
                node = node.left
                break
            elif node.right is None:
                node.right = BinaryTreeNode(data)
                node.right.top = node
                node = node.right
                break
            else:
                queue.put(node.left)
                queue.put(node.right)

        # Part 2 bubble to right place
        while node.top is not None:
            if node.data >= node.top.data:
                node.data, node.top.data = node.top.data, node.data
                node = node.top
            else:
                break

    def extract_max(self):
        # Part 1 take data
        if self.root is None:
            print("Nothing left")
            return
        data = self.root.data
        # Part 2 fix the tree
        # Finding the bottommost, rightmost element
        # Last item on Queue
        queue = Queue(0)
        queue.put(self.root)
        while not queue.empty():
            node = queue.get()
            if node.left is not None:
                queue.put(node.left)
            if node.right is not None:
                queue.put(node.right)
        # switch to the top
        self.root.data = node.data

        # Cut that node
        node = node.top
        if node.right is not None and self.root.data == node.right.data:
            node.right = None
        elif node.left is not None and self.root.data == node.left.data:
            node.left = None

        # Bubble down
        node = self.root
        while True:
            left_data = node.left.data if node.left is not None else 0
            right_data = node.right.data if node.right is not None else 0
            # print("left", left_data)
            # print("right", right_data)

            if left_data >= right_data:
                # print("left > right")
                if node.data <= left_data:
                    # print("exchange happened")
                    node.data, node.left.data = node.left.data, node.data
                    node = node.left
                else:
                    break
            else:
                # print("right > left")
                if node.data <= right_data:
                    # print("exchange happened")
                    node.data, node.right.data = node.right.data, node.data
                    node = node.right
                else:
                    break

        return data


class TrieNode:
    def __init__(self):
        self.children = {}

    def add(self, data):
        if data not in self.children.keys():
            self.children[data] = TrieNode()


import string


class Trie:
    KEYS = {letter for letter in string.ascii_lowercase}

    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for letter in word.lower():
            if letter in self.KEYS:
                node.add(letter)
                node = node.children[letter]
        node.add("*") # for full stop

    def all_words(self):
        words = []

        def _recursively_get_words(node, word):
            for letter in node.children.keys():
                if letter == "*":
                    words.append(word)
                else:
                    _recursively_get_words(node.children[letter], word + letter)

        _recursively_get_words(self.root, "")
        return words

    def count_words(self):
        return len(self.all_words())


if __name__ == "__main__":
    _list = [8, 4, 10, 2, 6, 20]
    BST = BinarySearchTree(_list[0])
    inc = 1
    while inc < len(_list):
        BST.add(_list[inc])
        inc +=1
    print("manual")
    print("root", BST.root.data)
    print("root.left", BST.root.left.data)
    print("4's child.left", BST.root.left.left.data)
    print("4's child.right", BST.root.left.right.data)
    print("root.right", BST.root.right.data)
    # print("10's child.left", BST.root.right.left.data) No left child of 10
    print("10's child.right", BST.root.right.right.data)
    print("In order")
    BST.p_in_order(BST.root)
    print("Pre order")
    BST.p_pre_order(BST.root)
    print("Post order")
    BST.p_post_order(BST.root)

    _list = [4, 50, 7, 55, 90, 87]
    MH = MinHeap(_list[0])
    inc = 1
    while inc < len(_list):
        MH.insert(_list[inc])
        inc += 1
    print("Manual MinHeap checking")
    print("root", MH.root.data)
    print("root.left", MH.root.left.data)
    print("50's child.left", MH.root.left.left.data)
    print("50's child.right", MH.root.left.right.data)
    print("root.right", MH.root.right.data)
    print("7's child.left", MH.root.right.left.data)
    #print("7's child.right", MH.root.right.right.data) Does not exist at the moment
    MH.insert(2)
    print("Manual MinHeap checking after inserting 2")
    print("root", MH.root.data)
    print("root.left", MH.root.left.data)
    print("50's child.left", MH.root.left.left.data)
    print("50's child.right", MH.root.left.right.data)
    print("root.right", MH.root.right.data)
    print("4's child.left", MH.root.right.left.data)
    print("4's child.right", MH.root.right.right.data)
    print("Extract minimum")
    print("minimum =", MH.extract_min())
    print("new root", MH.root.data)
    print("root.left", MH.root.left.data)
    print("50's child.left", MH.root.left.left.data)
    print("50's child.right", MH.root.left.right.data)
    print("root.right", MH.root.right.data)
    print("7's child.left", MH.root.right.left.data)
    # print("7's child.right", MH.root.right.right.data) Got cut

    words = ["Hello", "World", "Practice", "Makes", "Perfect"]
    print("Trie words we have", words)
    trie_test = Trie()
    for word in words:
        trie_test.add(word)
    print("Return all words", trie_test.all_words())
    print("Count of all words", trie_test.count_words())








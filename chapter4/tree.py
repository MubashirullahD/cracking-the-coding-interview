class Node:
    def __init__(self, data):
        self.item = data
        self.children = []


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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





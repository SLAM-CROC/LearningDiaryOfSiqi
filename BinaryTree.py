class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree():
    def __init__(self):
        self.root = None
        self.queue = []

    def add(self, value):
        new_node = Node(value)
        self.queue.append(new_node)
        if self.root is None:
            self.root = new_node
        else:
            tree_node = self.queue[0]
            if tree_node.left is None:
                tree_node.left = new_node
            else:
                tree_node.right = new_node
                self.queue.pop(0)

    def recursive_pre_order(self, root):
        if root is None:
            return
        print(root.value, end='')
        self.recursive_pre_order(root.left)
        self.recursive_pre_order(root.right)

    def stack_pre_order(self, root):
        if root is None:
            return
        stack = []
        node = root
        while stack or node:
            while node:
                print(node.value, end='')
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right

    def recursive_in_order(self, root):
        if root is None:
            return
        self.recursive_in_order(root.left)
        print(root.value, end='')
        self.recursive_in_order(root.right)

    def stack_in_order(self, root):
        if root is None:
            return
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            print(node.value, end='')
            node = node.right

    def recursive_post_order(self, root):
        if root is None:
            return
        self.recursive_post_order(root.left)
        self.recursive_post_order(root.right)
        print(root.value, end='')

    def stack_post_order(self, root):
        if root is None:
            return
        stack1 = []
        stack2 = []
        node = root
        while stack1 or node:
            while node:
                stack2.append(node)
                stack1.append(node)
                node = node.right
            node = stack1.pop()
            node = node.left
        while stack2:
            print(stack2.pop().value, end='')

    def bfs(self):
        queue = []
        current = self.root
        queue.append(current)
        while queue:
            current = queue.pop(0)
            print(current.value, end='')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)


if __name__ == "__main__":
    values = range(10)
    tree = Tree()
    for value in values:
        tree.add(value)
    print("Recursive pre order Traversal")
    tree.recursive_pre_order(tree.root)
    print("\n==========================")
    print("Pre order Traversal by Stack")
    tree.stack_pre_order(tree.root)
    print("\n==========================")
    print("Recursive in order Traversal")
    tree.recursive_in_order(tree.root)
    print("\n==========================")
    print("In order Traversal by Stack")
    tree.stack_in_order(tree.root)
    print("\n==========================")
    print("Recursive post order Traversal")
    tree.recursive_post_order(tree.root)
    print("\n==========================")
    print("Post order Traversal by Stack")
    tree.stack_post_order(tree.root)
    print("\n==========================")
    print("Breadth-First Search")
    tree.bfs()



""" Tree class. """

from ete3 import Tree as EteTree

from function import Function
from node import Node
from terminal import Terminal

class Tree(object):
    def __init__(self, node, children=None):
        self.node = node
        self.children = children

    def get_children(self):
        return self.children

    def entry(self):
        return self.node

    def is_leaf(self):
        return bool(self.children)

    def add_child(self, child):
        if self.children:
            self.children.append(child)
        else:
            self.children = [child]

    @staticmethod
    def create_full_tree(depth):
        """ Creates a tree using the full method with depth `depth`.

        Args:
            depth: int

        Returns:
            Tree instance
        """
        if depth == 0:
            terminal = Terminal.random_terminal()
            node = Node("terminal", terminal)
            return Tree(node)
        else:
            function = Function.random_function()
            root_node = Node("function", function)
            result = Tree(root_node)
            for _ in range(2):  #function.arity()
                result.add_child(Tree.create_full_tree(depth - 1))
            return result

    @staticmethod
    def create_grow_tree(depth):
        """ Creates a tree using the grow method with depth `depth`. Note
        that since grow ends when all leaf nodes are 0-arity, it is
        possible that the tree generated by this method has a depth
        less than `depth`.

        Args:
            depth: int

        Returns:
            Tree instance
        """
        # TODO
        return

    def __str__(self):
        if self.children:
            s = "({0});".format(",".join([str(child) for child in self.children]))
            return str(EteTree(s))
        else:
            return str(self.node.value.num)

if __name__ == "__main__":
    tree = Tree.create_full_tree(2)
    print(tree)
"""
Binary Tree

Any and all nodes at any given time can only point to two nodes MAX

Terminology

    - Root: The topmost node in the tree.
    - Child: A node directly connected to another node when moving away from the root node.
    - Parent: A node directly connected to another node when mving towards the root node
    - Siblings: Nodes that share the same parent are considered siblings
    - Leaf: A node that does NOT have any children of its own

Binary Search Trees maintain the following structure...

For any given node, all values on the left subtree are less than ort equal to the value of the parent / value at the given node.
For the right subtree all the values are greater than or equal to the value of the parent / value at the given node.

=====================================================================================================================================

Checking for a value in a BST

    - check root: see if root is less than or equal to the value passed
        if the current node is greater than the value move to the left
            update current node to be a step down on the left subtree
        else
            update current node to be a steop down on the right side


Questions

    - How would inserting into a binary search tree work? How would it differ from the contains example?
    - In the contains example (Up above), out of all the elements in the binary search tree, how man elments were actually checked?
        how does this compare to the number of elements we would have to check if we were checking for a vlue in an array or linked list
    - Is inserting into a binary search tree more or less work than inserting into an arrya or linked list? Why?

Pros and Cons

    - PRO: Searching for an element in a binary search tree is sugnificantly more efficient
        than searching through an array or linked list. (Why is this)

    - CON: As a tradeoff, it is not as efficient to insert into a binary search tree (why)

    - CON: The performance of a binary search tree depends on quite a lot on if the tree
        is balanced or not. Is this generally a good assumption to make?
        When would this assumption be incorrect?
"""


# Example BST class

class BinarySearchTree:
    def __init__(self, vlaue, left_subtree=None, right_subtree=None):
        self.value = vlaue
        self.left = left_subtree
        self.right = right_subtree

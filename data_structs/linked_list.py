# Class used to create nodes in the linked list

"""
Every node has 2 parts:

- Data
- A pointer to the next node

The first node is konwn as the root node, we will always keep a variable to the root node in the linked list
so that we can always access the first node in a list

The last node in a list will NOT have a pointer to then next node since there is no other node.
Instead we will point to None / Null so that we know we are at the end of a linked list
"""


class Node:
    def __init__(self, data=None):
        self.node_value = data
        self.next_node = None


"""
Operations we want to be able to do with our linked list

- get_size(): reurn the size, create a var called size that will keep a tally on how big the list is
    every time that we add a node we will add 1 to the current size.

- find(data): we will start at the root and compare its data to the value we are looking for.
    If the root / current node data does not match the value we are looking for then we will goto the next node
    once we find matching data return it
    if we get to the end of the list and still have not made a match we will return None / false

- add(data): Create a new node, set the next node pointer to the current root / head node
    then change root pointer to the newly added node

- remove(data): Start at the root, compare data if it doesnt match move on.
    Once the data is matched, we change the next pointer of our previous node to the next of the current node

"""
# Class used to start a linked list


class LinkedList:
    def __init__(self):
        self.head_value = None
        self.length = 0

    # add a new node to the front of the list
    def push(self, data):

        # create
        new_node = Node(data)
        # connect
        new_node.next_node = self.head_value
        # change / update
        self.head_value = new_node
        # increase the count on the list
        self.length += 1

    # add a new node to the end of a list
    def append(self, data):

        new_node = Node(data)
        cur_node = self.head_value

        while cur_node:
            if cur_node.next_node is not None:
                cur_node = cur_node.next_node
            elif cur_node.next_node is None:
                cur_node.next_node = new_node
                self.length += 1
                break

    # return the current size of the linked list
    def get_size(self):
        return self.length

    # print out all the values in the list
    def get_values(self):

        current_node = self.head_value

        while current_node:
            if current_node.next_node is not None:
                print(current_node.node_value)
                current_node = current_node.next_node
            else:
                print(current_node.node_value)
                break

    # Reverse a linked list
    def rev_lsit(self):
        prev = None
        current = self.head_value
        while current is not None:
            # Store the next node in a temp holder
            temp = current.next_node
            # make the current node point to previous node / value
            current.next_node = prev
            # move the prev pointer to the current node / value
            prev = current
            # make the current node the next node
            current = temp
        # move the head pointer to the last node in the list
        self.head_value = prev
        self.get_values()


my_list = LinkedList()
# print("The starting length is: {}".format(my_list.length))
my_list.push(5)
my_list.append(18)
my_list.append(50)
# print("The head value is: {}".format(my_list.head_value.node_value))
# print("The new length is: {}".format(my_list.length))
# print("vvvv All the values in the list vvvv")
# my_list.get_values()
my_list.rev_lsit()

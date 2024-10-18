"""
This program creates a simple linked list data structure where nodes are 
added at the beginning and can be removed by value. The list can also 
be printed (stringified) to visualize the values in the nodes.

The following tasks are accomplished:
1. Create nodes and add them to the linked list.
2. Print the linked list.
3. Remove a node (by value) from the list.
4. Print the list again to confirm the node removal.
"""

# Node class represents each element (node) in the linked list.
class Node:
    def __init__(self, value, next_node=None):
        """
        Initialize a new Node.
        :param value: The value to store in this node.
        :param next_node: The next node in the list (default is None).
        """
        self.value = value
        self.next_node = next_node

    def get_node_value(self):
        """
        Returns the value stored in the node.
        :return: Value of the node.
        """
        return self.value

    def get_next_node(self):
        """
        Returns the next node in the list.
        :return: The next node.
        """
        return self.next_node

    def set_next_node(self, next_node):
        """
        Sets the next node in the list.
        :param next_node: The next node to link to.
        """
        self.next_node = next_node


# LinkedList class manages a list of nodes.
class LinkedList:
    def __init__(self, value):
        """
        Initialize the linked list with a head node.
        :param value: The value of the first (head) node in the list.
        """
        self.head_node = Node(value)

    def get_head_node(self):
        """
        Returns the head (first) node in the linked list.
        :return: The head node.
        """
        return self.head_node

    def add_node_to_beginning(self, add_value):
        """
        Adds a new node at the beginning of the linked list.
        :param add_value: The value of the new node to add.
        """
        new_node = Node(add_value)  # Create a new node
        new_node.set_next_node(self.head_node)  # Link the new node to the current head
        self.head_node = new_node  # Update the head to the new node

    def node_to_list(self):
        """
        Converts the linked list into a string representation.
        :return: A string of node values separated by arrows (->).
        """
        node_list = ""
        current_node = self.head_node

        while current_node:
            node_list += str(current_node.get_node_value()) + " -> "  # Append node value to string
            current_node = current_node.get_next_node()  # Move to the next node

        node_list += "None"  # End of the list
        return node_list

    def remove_node(self, remove_value):
        """
        Removes the first occurrence of a node with the given value.
        :param remove_value: The value of the node to remove.
        """
        current_node = self.head_node

        # Special case: if the head node is the one to remove
        if current_node.get_node_value() == remove_value:
            self.head_node = current_node.get_next_node()  # Move the head to the next node
            current_node = self.head_node  # Update the current node

        # Traverse the list to find and remove the target node
        while current_node is not None:
            next_node = current_node.get_next_node()

            # Check if the next node holds the value to remove
            if next_node is not None and next_node.get_node_value() == remove_value:
                current_node.set_next_node(next_node.get_next_node())  # Bypass the node to remove
            current_node = current_node.get_next_node()  # Move to the next node


# Example usage:

# Create a new linked list and add nodes
linked_list = LinkedList(90)
linked_list.add_node_to_beginning(500)
linked_list.add_node_to_beginning("hello")

# Print the linked list before removing any nodes
print("Before removal:")
print(linked_list.node_to_list())  # Output: hello -> 500 -> 90 -> None

# Remove a node by value ("hello")
linked_list.remove_node("hello")

# Print the linked list after removing the node
print("After removal:")
print(linked_list.node_to_list())  # Output: 500 -> 90 -> None


# Import the unittest module
import unittest

# Import the LinkedList class from your file
from LinkedList import LinkedList, LinkedListNode

# Define a test class that inherits from unittest.TestCase
class TestLinkedList(unittest.TestCase):

    # Define a setUp method that runs before each test case
    def setUp(self):
        # Create an empty list
        self.empty_list = LinkedList(None)
        # Create a list with one node
        self.one_node_list = LinkedList(LinkedListNode(1))
        # Create a list with three nodes
        self.three_node_list = LinkedList(LinkedListNode(1))
        self.three_node_list.append(2)
        self.three_node_list.append(3)

    # Define a test case for the append method
    def test_append(self):
        # Append a node to the empty list
        self.empty_list.append(1)
        # Check that the head node has the correct value
        self.assertEqual(self.empty_list.head.value, 1)
        # Check that the next node is None
        self.assertIsNone(self.empty_list.head.next)
        # Append a node to the one node list
        self.one_node_list.append(2)
        # Check that the head node has the correct value
        self.assertEqual(self.one_node_list.head.value, 1)
        # Check that the next node has the correct value
        self.assertEqual(self.one_node_list.head.next.value, 2)
        # Check that the next next node is None
        self.assertIsNone(self.one_node_list.head.next.next)

    # Define a test case for the prepend method
    def test_prepend(self):
        # Prepend a node to the empty list
        self.empty_list.prepend(1)
        # Check that the head node has the correct value
        self.assertEqual(self.empty_list.head.value, 1)
        # Check that the next node is None
        self.assertIsNone(self.empty_list.head.next)
        # Prepend a node to the one node list
        self.one_node_list.prepend(0)
        # Check that the head node has the correct value
        self.assertEqual(self.one_node_list.head.value, 0)
        # Check that the next node has the correct value
        self.assertEqual(self.one_node_list.head.next.value, 1)
        # Check that the next next node is None
        self.assertIsNone(self.one_node_list.head.next.next)

    # Define a test case for the insert method
    def test_insert(self):
        # Insert a node at index 0 in the empty list
        self.empty_list.insert(0, 1)
        # Check that the head node has the correct value
        self.assertEqual(self.empty_list.head.value, 1)
        # Check that the next node is None
        self.assertIsNone(self.empty_list.head.next)
        # Insert a node at index 0 in the one node list
        self.one_node_list.insert(0, 0)
        # Check that the head node has the correct value
        self.assertEqual(self.one_node_list.head.value, 0)
        # Check that the next node has the correct value
        self.assertEqual(self.one_node_list.head.next.value, 1)
        # Check that the next next node is None
        self.assertIsNone(self.one_node_list.head.next.next)
        # Insert a node at index 1 in the three node list
        self.three_node_list.insert(1, 4)
        # Check that the head node has the correct value
        self.assertEqual(self.three_node_list.head.value, 1)
        # Check that the next node has the correct value
        self.assertEqual(self.three_node_list.head.next.value, 4)
        # Check that the next next node has the correct value
        self.assertEqual(self.three_node_list.head.next.next.value, 2)
        # Check that the next next next node has the correct value
        self.assertEqual(self.three_node_list.head.next.next.next.value, 3)
        # Check that the next next next next node is None
        self.assertIsNone(self.three_node_list.head.next.next.next.next)

    # Define a test case for the remove method
    def test_remove(self):
        # Remove a node with value 1 from the one node list
        self.one_node_list.remove(1)
        # Check that the head node is None
        self.assertIsNone(self.one_node_list.head)
        # Remove a node with value 2 from the three node list
        self.three_node_list.remove(2)
        # Check that the head node has the correct value
        self.assertEqual(self.three_node_list.head.value, 1)
        # Check that the next node has the correct value
        self.assertEqual(self.three_node_list.head.next.value, 3)
        # Check that the next next node is None
        self.assertIsNone(self.three_node_list.head.next.next)

    # Run the tests
    if __name__ == "__main__":
        unittest.main()

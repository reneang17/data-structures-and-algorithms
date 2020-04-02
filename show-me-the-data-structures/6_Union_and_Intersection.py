from data_structures import BinaryTree

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

# Reference https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# My leetcode solution to Flatten a binary tree
def flatten(root):
    """
    Approach depth search first, port order
    """
    if root is None:
        return None

    flatten(root.left)

    flatten(root.right)

    head = root.left
    tail = root.left
    if tail:
        while tail and tail.right:
            tail = tail.right

        tail.right = root.right
        root.right = head
        root.left = None


def union(llist_1, llist_2):
    # Insert elements of llist_1 into linked llist_1
    bt1 = BinaryTree()
    node = llist_1.head
    while node:
        bt1.insert(node.value)
        node = node.next

    # Fist turn elements of llist_2 into the same btree
    node = llist_2.head
    while node:
        bt1.insert(node.value)
        node = node.next

    # Flatten the binary tree
    flatten(bt1.get_root())

    # Empty btree into llist and return
    llist =  LinkedList()
    node = bt1.get_root()
    while node:
        llist.append(node.value)
        node = node.right
    return llist


def intersection(llist_1, llist_2):

    #edge cases
    if llist_1.size()==0 or llist_2.size() ==0:
        return LinkedList()

    # Insert elements of llist_1 into bt1
    bt1 = BinaryTree()
    node = llist_1.head
    while node:
        bt1.insert(node.value)
        node = node.next

    # Insert elements of llist_2 into bt2
    bt2 = BinaryTree()
    node = llist_2.head
    while node:
        bt2.insert(node.value)
        tail2 = node
        node = node.next

    #link head of llist1 to the tail of llist2
    tail2.next = llist_1.head
    node = llist_2.head
    bt = BinaryTree()
    while node:
        if bt1.search(node.value) and bt2.search(node.value):
            bt.insert(node.value)
        node = node.next

    flatten(bt.get_root())

    # Empty btree into llist and return
    llist =  LinkedList()
    node = bt.get_root()
    while node:
        llist.append(node.value)
        node = node.right
    return llist

if __name__ == '__main__':
    # Aux test functions

# Test case 1

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print (union(linked_list_1,linked_list_2))
    print (intersection(linked_list_1,linked_list_2))

    # Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print (union(linked_list_3,linked_list_4))
    print (intersection(linked_list_3,linked_list_4))

    #Below there is test module

    def list_intersection(arr1, arr2):
        return set(arr1) & set(arr2)


    def list_union(arr1, arr2):
        return set(arr1+arr2)


    def llist_to_set(llist):
        s = set()
        size= llist.size()
        node= llist.head
        while node:
            s.add(node.value)
            node = node.next
        assert len(s) == size , 'Fail'
        return s

    def make_llist(arr):
        llist = LinkedList()
        for i in arr:
            llist.append(i)
        return llist

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    def test_intersection(arr1, arr2):
        arr_union = list_union(arr1, arr2)
        arr_inter = list_intersection(arr1, arr2)

        llist1 = make_llist(arr1)
        llist2 = make_llist(arr2)

        llist_union = llist_to_set(union(llist1, llist2))
        llist_inter = llist_to_set(intersection(llist1, llist2))

        assert llist_inter == arr_inter, 'Fail'
        assert llist_union == arr_union, 'Fail'

    test_intersection(element_1, element_2)


    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]

    test_intersection(element_1, element_2)

    element_1 = []
    element_2 = [1]

    test_intersection(element_1, element_2)

    element_1 = [1]
    element_2 = []

    test_intersection(element_1, element_2)


    element_1 = [1,2,3]
    element_2 = [1,2,4]

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    #print('Llist_1:', linked_list_1)
    #print('Llist_2:', linked_list_2)

    #print('Intersection: ', intersection(linked_list_1,linked_list_2))
    #print('Union: ', union(linked_list_1, linked_list_2))

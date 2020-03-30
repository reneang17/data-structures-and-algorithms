from Hash_map import HashMap
from Linked_list import LinkedList
from Queue import Queue
from Stack import Stack
from Tree import Tree as Node

def test_hash():
    hash_map = HashMap()
    hash_map.put("one", 1)
    hash_map.put("two", 2)
    hash_map.put("three", 3)
    hash_map.put("neo", 11)

    assert hash_map.size() == 4, 'Incorrect size'
    assert hash_map.get("one") == 1, 'Check get'
    assert hash_map.get("neo") == 11, 'Check get'
    assert hash_map.get("three") == 3, 'Check get'

    hash_map.delete("one")

    assert hash_map.get("one") == None, 'Check delete'

    assert hash_map.size() == 3, 'Incorrect size'

# executing test
test_hash()



def test_hash():
    # Test prepend
    linked_list = LinkedList()
    linked_list.prepend(1)
    assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
    linked_list.append(3)
    linked_list.prepend(2)
    assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

    # Test append
    linked_list = LinkedList()
    linked_list.append(1)
    assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
    linked_list.append(3)
    assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

    # Test search
    linked_list.prepend(2)
    linked_list.prepend(1)
    linked_list.append(4)
    linked_list.append(3)
    assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
    assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

    # Test remove
    linked_list.remove(1)
    assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
    linked_list.remove(3)
    assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
    linked_list.remove(3)
    assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

    # Test pop
    value = linked_list.pop()
    assert value == 2, f"list contents: {linked_list.to_list()}"
    assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

    # Test insert
    linked_list.insert(5, 0)
    assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
    linked_list.insert(2, 1)
    assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
    linked_list.insert(3, 6)
    assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

    # Test size
    assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"

test_hash()

def test_queue():
    # Setup
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    # Test size
    assert q.size() == 3, 'Fail'

    # Test dequeue
    assert q.dequeue() == 1, 'Fail'

    # Test enqueue
    q.enqueue(4)
    assert q.dequeue() == 2, 'Fail'
    assert q.dequeue() == 3, 'Fail'
    assert q.dequeue() == 4, 'Fail'
    q.enqueue(5)
    assert (q.size() == 1) , "Fail"

test_queue()

def test_stack():
    foo = Stack()
    for i in range(1,12):
        foo.push(i)

    assert foo.size() == 11,  "Fail"
    assert len(foo.arr) == 20,  "Fail"
    assert foo.is_empty()== False, 'Fail'
    foo.push("Test")
    assert foo.pop() == "Test", 'Fail'

test_stack()

def test_Tree():
    node0 = Node("apple")
    node1 = Node("banana")
    node2 = Node("orange")

    assert node0.has_left_child() == False, 'Fail'
    assert node0.has_right_child() == False, 'Fail'

    node0.set_left_child(node1)
    node0.set_right_child(node2)

    assert node0.has_left_child(), 'Fail'
    assert node0.has_right_child(), 'Fail'

test_Tree()

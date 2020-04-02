from data_structures import HashMap, Node

class LRU_Cache(HashMap):

    def __init__(self, capacity):
        # Initialize class variables
        HashMap.__init__(self, initial_size = capacity)
        self.capacity = capacity

        self.cache_head = Node(-1)
        self.cache_tail = self.head_cache
        self.cache = HashMap(initial_size = capacity)
        self.cache_size = 0



    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        key_str= str(key)

        val = HashMap.get(self, key_str)

        if val != None:
            # Remove node from cache_linked_list
            #node = self.hash_cache.get(key_str)
            #if node.next.next:
            #    node.val = node.next.val
            #    node.next = node.next.next
            #else:
            #    node.val = None
            val = val.value
        elif val == None:
            val = -1
        return val

    def set(self, key, value):
        # Set the value if the key is not present in the cache.
        #If the cache is at capacity remove the oldest item.
        key_str = str(key)
        aux = curr
        if len(cash_dict)== 5 and i != aux[0].value:
            key_to_deleted = head.next.value
            head.next = head.next.next

            del cash_dict[key_to_deleted]
            del hashmap[key_to_deleted]

            node = Node(i)
            cash_dict[i] = node
            aux[0].next = node
            aux[0] = aux[0].next
        hashmap[i]= value




def test_LRU_Cache():

    our_cache = LRU_Cache(5)
    for i in range(1,5):
        our_cache.set(i, i)

    assert our_cache.get(1) == 1       # returns 1
    assert our_cache.get(2) == 2      # returns 2

    # returns -1 because 9 is not present in the cache
    assert our_cache.get(9) ==-1, 'Failed'

    our_cache.set(5, 5)
    our_cache.set(6, 6)
    print(our_cache.hash_cache)

    # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    print(our_cache.get(3))

test_LRU_Cache()

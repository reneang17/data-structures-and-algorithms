


#####################################################
#  Implementation of LRU hashed map
#  Least recurrent used (LRU) with O(1) time complexity
#  Data structures used:
#  1.- Hashmap (dictionary) to store key, values
#  2.- Linked list of Least recurrent key stores in nodes
#  3.- Hash maps to store nodes with keys and recorder in O(1)
####################################################

# Each node will have value a key, and will be linked
# previous and last used
class Node:
    def __init__(self, x):
        self.value = x
        self.next = None
        self.prev = None


class LRU_Cache():
    def __init__(self, capacity = 5):
        # if input capacity is wrong set to 5
        if capacity<0 or type(capacity) != 'int':
            self.capacity = 5
        else:
            self.capacity = capacity

        self.hashmap = {}

        #Cache will be store in linked list
        self.head = Node(-1)
        self.tail = self.head
        #To get O(1) access to Node we store these on HashMap (dictionary)
        self.cache_dict = {}



    def set(self, key, value):


        # Move to tail if key exists
        if key in self.hashmap:
            self.move_to_cache_tail(key)

        # Remove LRU if key is new
        else:
            if len(self.cache_dict) == self.capacity:
                key_to_be_removed = self.head.next.value
                del self.cache_dict[key_to_be_removed]
                del self.hashmap[key_to_be_removed]

                #Remove also from linked list
                self.head.next, self.head.next.prev = \
                self.head.next.next, self.head



            node = Node(key)
            self.cache_dict[key] = node
            self.tail.next = node
            node.prev =  self.tail
            self.tail = self.tail.next



        #Create/Update in any case
        self.hashmap[key]= value


    def get(self, key):

        if key in self.hashmap: # if cache hit move key to cache tail
            self.move_to_cache_tail(key)
            return self.hashmap[key]
        else: # if cache hit
            return -1

    def move_to_cache_tail(self, key):
        # If not already on tail
        if self.cache_dict[key].next is not None:

            # Unlink  self.cache_dict[key], join prev with next
            previous = self.cache_dict[key].prev
            previous.next = self.cache_dict[key].next
            self.cache_dict[key].next.prev = previous
            self.cache_dict[key].next = None

            # Link self.cache_dict[key] on tail
            self.tail.next = self.cache_dict[key]
            self.cache_dict[key].prev =  self.tail
            self.tail = self.tail.next

if __name__ == '__main__':
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
        our_cache.set(6, 6)



        # returns -1 because the cache reached it's
        #capacity and 3 was the least recently used entry
        assert our_cache.get(3) == -1, 'Failed'

        # Test edge cases:

        #Zero capacity
        our_cache = LRU_Cache(0.)
        assert our_cache.capacity == 5, 'Fail'

        #One capacity
        our_cache = LRU_Cache(1)
        our_cache.set(1, 1)
        our_cache.set(2, 2)
        assert our_cache.get(2) == 2


    test_LRU_Cache()

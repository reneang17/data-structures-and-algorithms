import sys
from data_structures import Tree, Queue, Stack


class Node(object):

    def __init__(self, freq = None, char = None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def get_freq(self):
        return self.freq

    def get_char(self):
        return self.char

    def set_left_child(self,left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    def __repr__(self):
        return f"{self.freq} {self.char}"

class HTree():
    def __init__(self, node = None):
        self.root = node


    def set_root(self,value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def get_freq(self):
        return self.root.get_freq()

    def get_char(self):
        return self.root.get_char()

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enqueue( (node,level) )

        while q.size() > 0:
            node, level = q.dequeue()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enqueue( (node.get_left_child(), level +1 ))
            else:
                q.enqueue( (None, level +1) )

            if node.has_right_child():
                q.enqueue( (node.get_right_child(), level +1 ))
            else:
                q.enqueue( (None, level +1) )

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level

        return s



class Huffman():
    def __init__(self, data =None):
        if data is not None:
            self.data = data
            self.preprocess_data()
        self.huffman_tree= None


    def preprocess_data(self):
        self.data = self.data.lower()
        self.data = self.data.replace(' ', '.')

    def sort_frequencies(self):

        freq_dict ={i:0 for i in set(self.data)}
        for i in self.data:
            freq_dict[i]+=1

        sorted_freq = sorted(freq_dict.items(), #Sort: more frequent first
            key=lambda x: (x[1],x[0]), reverse=True)

        stack = Stack() #Push most frequent firts

        [stack.push(Node(freq = x[1], char= x[0]))  for x in sorted_freq]
        #print(stack.arr)
        #print('top stack:', stack.top())

        return stack

    def insert_node(self, node):
        lessFreq_stack = Stack()

        while self.stack.num_elements>0 and self.stack.top().get_freq() < node.get_freq():
            lessFreq_stack.push(self.stack.pop())

        self.stack.push(node)

        while lessFreq_stack.num_elements>0:
            self.stack.push(lessFreq_stack.pop())

    def build_codes(self, node, bin_code):
        if node.left is None and node.right is None:
            key = node.get_char()
            self.code[key] = bin_code

        if node.left is not None:
            self.build_codes(node.left, bin_code+'0')

        if node.right is not None:
            self.build_codes(node.right, bin_code+'1')

    def huffman_encode(self):
        #Address trivial cases
        if len(self.data) == 0:
            self.huffman_tree = HTree()
            self.encoded = ''
            return self.encoded, self.huffman_tree

        if len(set(self.data)) == 1:
            root = Node(freq = len(self.data), char= None)
            self.huffman_tree = HTree(root)
            node = Node(freq = len(self.data), char =self.data[0])
            root.set_left_child(node)
            self.huffman_tree
            self.encoded = '0'*len(self.data)
            return self.encoded , self.huffman_tree

        #stack stack with more frequent at the bottom.
        self.stack = self.sort_frequencies()

        #Build tree from stack
        while self.stack.num_elements > 1:
            t1 =  self.stack.pop()
            t2 =  self.stack.pop()
            #Grow tree by creating a new node an attaching
            #lesf frequent nodes
            new_node= Node(freq= t1.get_freq()+ t2.get_freq() , char = None)
            new_node.set_left_child(t1)
            new_node.set_right_child(t2)

            self.insert_node(new_node)

        root_node= self.stack.pop()
        self.huffman_tree = HTree(node = root_node)

        self.code = {}
        self.build_codes(root_node, '') # Filles fictionary

        encoded_list = [self.code[c] for c in self.data]
        self.encoded = "".join(encoded_list)

        return self.encoded, self.huffman_tree


    def huffman_decode(self):
        decoded_list = []
        node= self.huffman_tree.get_root()
        for i in self.encoded:
            if i =="0":
                node = node.left
            elif i =="1":
                node = node.right

            if node.left is None and node.right is None:
                decoded_list.append(node.get_char())
                node = self.huffman_tree.get_root()

        return ''.join(decoded_list)


def _huffman_encoding(data):
    huffman = Huffman(data)
    encoded, huffman_tree = huffman_encode()
    return encoded, huffman_tree


def _huffman_decoding(data, tree):
    decoded_list = []
    node= tree.get_root()
    for i in data:
        if i =="0":
            node = node.left
        elif i =="1":
            node = node.right

        if node.left is None and node.right is None:
            decoded_list.append(node.get_char())
            node = tree.get_root()

    return ''.join(decoded_list)





#huffman = Huffman('bccabbddaeccbbaeddcc')
#huffman.huffman_encode()
#print(huffman.data)
#print(huffman.huffman_tree)
#print(huffman.code)
#print(huffman.encoded)
#decoded = huffman.huffman_decode()
#print(decoded == huffman.data)




if __name__ == "__main__":


    a_great_sentence = "The bird is the word"

    huffman= Huffman()

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    huffman.data= a_great_sentence

    encoded_data, tree = huffman.huffman_encode()

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman.huffman_decode()

    assert decoded_data == a_great_sentence, 'Decoding changes input'

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    def test_edges():
        huffman = Huffman('')
        huffman.huffman_encode()
        assert huffman.huffman_decode() == huffman.data, 'Decoding changes input'

        huffman.data= 'aaa'
        huffman.huffman_encode()
        assert huffman.huffman_decode() == huffman.data, 'Decoding changes input'

    test_edges()




#def huffman_decoding(data,tree):
#    pass

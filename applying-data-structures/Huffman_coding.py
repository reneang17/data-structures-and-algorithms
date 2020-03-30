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

    def __repr__(self):
        return f"{self.freq} {self.char}"


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
    def __init__(self, data):
        self.data = data
        self.preprocess_data()


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
        print(stack.arr)
        print('top stack:', stack.top())

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
            self.codes[key] = bin_code

        if node.left is not None:
            self.build_codes(node.left, bin_code+'0')

        if node.right is not None:
            self.build_codes(node.right, bin_code+'1')






    def huffman_encode(self):
        #Address trivial cases
        if len(self.data) == 0:
            return -1,-1,-1
        if len(set(self.data)) == 1:
            return '1'*len(self.data), [1]*len(self.data), self.data[0]

        #stack stack with more frequent at the bottom.
        self.stack = self.sort_frequencies()

        #Build tree from stack
        while self.stack.num_elements > 1:
            t1 =  self.stack.pop()
            t2 =  self.stack.pop()
            #Build tree
            grow_node= Node(freq= t1.get_freq()+ t2.get_freq() , char = None)
            grow_node.set_left_child(t1)
            grow_node.set_right_child(t2)

            self.insert_node(grow_node)

        root_node= self.stack.pop()
        self.huffman_tree = HTree(node = root_node)

        self.codes = {}
        self.build_codes(root_node, '')






huffman = Huffman('bccabbddaeccbbaeddcc')
huffman.huffman_encode()
print(huffman.huffman_tree)

print(huffman.codes)


#    while s.num_elements > 1:
#        a = s.pop()
#        b = s.pop()
#        #create a tree
#        t = Tree()
#        t.set_root(_node_specific_freq(a) + _node_specific_freq(b))
#        #print('root: ', a.get_freq() + b.get_freq(), t.get_root().get_freq())
#        if _node_specific_freq(a) < t.get_root().get_freq():
#            t.get_root().set_left_child(a)
#            t.get_root().set_right_child(b)
#        else:
#            t.get_root().set_left_child(a)
#            t.get_root().set_right_child(b)
#        #add to stack
#        top = s.top()
#        #node
#        #if type(top).__name__ == 'Node':
#        if _node_specific_freq(top) != None and _node_specific_freq(top) >= t.get_root().get_freq():
#            s.push(t)
#            #print('pushing on top')
#        else:#pop lighter nodes
#            tmp_stack = []
#            while _node_specific_freq(top) != None and  _node_specific_freq(top) < t.get_root().get_freq():
#                tmp_stack.append(s.pop())
#                top = s.top()
#                #print('val: ', _node_specific_freq(top), t.get_root().get_freq())
#                if _node_specific_freq(top) == None:
#                    break
#            s.push(t)
#            #print('size of lighter nodes: ', len(tmp_stack))
#            for tt in list(reversed(tmp_stack)):
#                s.push(tt)
#        #break
#        #encode_data(data, s.top())
#        #get codes for each character
#        visit_order, codes = pre_order_with_stack(s.top())#s.top() is the tree
#        '''print(visit_order)
#        for c in codes.keys():
#        print(c, codes[c])'''









#def huffman_decoding(data,tree):
#    pass

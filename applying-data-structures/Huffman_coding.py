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

class HTree(Tree):
    def __init__(self, node):
        Tree.__init__(self, value = node)

    def get_freq(self):
        return self.value.get_freq()

    def get_char(self):
        return self.value.get_char()



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

        stack = Stack() #Push most frequent
        [stack.push(Node(freq = x[1], char= x[0])) for x in sorted_freq]

        return stack

    def insert_node(self, node):
        lessFreq_stack = Stack()

        while self.stack.num_elements>0 and self.stack.top().get_freq() < node.get_freq():
            lessFreq_stack.push(self.stack.pop())

        self.stack.push(node)

        while lessFreq_stack.num_elements>0 is not None:
            self.stack.push(lessFreq_stack.pop())


    def huffman_encode(self):
        #Address trivial cases
        if len(self.data) == 0:
            return -1,-1,-1
        if len(set(self.data)) == 1:
            return '1'*len(self.data), [1]*len(self.data), self.data[0]

        #stack stack with more prequent at the bottom.
        self.stack = self.sort_frequencies()

        while self.stack.num_elements > 1:
            n1 =  self.stack.pop()
            n2 =  self.stack.pop()
            new_node= Node(freq= n1.get_freq()+ n2.get_freq() , char = None)
            tree = HTree(new_node)
            tree.left , tree.right = n1, n2

            self.insert_node(tree)




huffman = Huffman('abbccccc')
huffman.huffman_encode()

#huffman.insert_node(Node(freq= 4, char = None))
while huffman.stack.num_elements>0:
    node = huffman.stack.pop()
    print(node.get_char() , node.get_freq())


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

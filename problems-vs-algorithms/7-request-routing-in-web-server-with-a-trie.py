
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler=handler)


    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node= self.root
        for token in path:
            if token not in current_node.children:
                current_node.insert(token)
            current_node = current_node.children[token]
        current_node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        current_node = self.root
        if path == ['']:
            return self.root

        for token in path:
            if token not in current_node.children:

                return None
            current_node = current_node.children[token]
        return current_node


class Router:
    def __init__(self, handler=None, not_found_handler = None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.route_trie = RouteTrie(handler=handler)
        self.not_found_handler = not_found_handler


    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path = self.split_path(path)
        current_node = self.route_trie.insert(path, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handle
        path =self.split_path(path)
        handler_node = self.route_trie.find(path)

        if handler_node is None:
            return self.not_found_handler
        else:
            if handler_node.handler is not None:
                return handler_node.handler
            else:
                return self.not_found_handler


    def get_subpaths(self, path = ''):
        "List all "
        path_to_look =self.split_path(path)
        node = self.route_trie.find(path_to_look)
        subpaths = node.get_subpaths()
        subpaths = [path+i for i in subpaths]
        return subpaths



    def split_path(self, path = ''):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if len(path)>0 and path[-1] == '/':
            path = path[:-1]
        return path.split('/')


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, token):
        if token not in self.children:
            self.children[token] = RouteTrieNode()


    def get_subpaths(self, suffix = ''):

        suffix_list = []
        for char in self.children:
            if self.children[char].handler is not None:
                suffix_list.append(suffix+char+'/')
            suffix_list+=self.children[char].get_subpaths(suffix = suffix+char+'/')
        return suffix_list


if __name__ == '__main__':
    def test_Rourter():
        router = Router("root handler", "not found handler")
        router.add_handler("/home/about", "about handler")

        assert router.lookup("/") == "root handler"
        assert router.lookup("/home") == "not found handler"
        assert router.lookup("/home/about") == 'about handler'
        assert router.lookup("/home/about/") == 'about handler'
        assert router.lookup("/home/about/me") == "not found handler"

        #Other edge cases
        assert router.lookup("") == "root handler"
        assert router.lookup("//") == "not found handler"

        #Industrial testing
        for i in range(1,10):
            path= ''.join('/'+str(i) for i in range(1,i+1))
            router.add_handler(path, i)
        for i in range(1,10):
            path= ''.join('/'+str(i) for i in range(1,i+1))
            assert router.lookup(path) == i

        #Bonus: Testing if get_subpaths function works as expected
        router = Router("root handler", "not found handler")
        router.add_handler("/home/about", "about handler")
        for i in range(1,5):
            path= ''.join('/'+str(i) for i in range(1,i+1))
            router.add_handler(path, i)
        assert router.get_subpaths('/1/2/') == ['/1/2/3/', '/1/2/3/4/']
        assert router.get_subpaths() == ['/home/about/', '/1/', '/1/2/', '/1/2/3/', '/1/2/3/4/']

        print('All tests passed!')

    test_Rourter()

import hashlib
from datetime import datetime
import datetime

class Block():
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.prev = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        s = ''
        s += "Timestamp: " + str(self.timestamp) + "\n"
        s += "Data: " + str(self.data) + "\n"
        s += "SHA256 Hash: " + str(self.hash) + "\n"
        s += "Prev_Hash: " + str(self.previous_hash) + "\n"
        assert type(s)== str
        return s

class Blockchain():
    def __init__(self): # initialize when creating a chain
        self.chain_head = self.block_zero()
        self.size = 1

    def block_zero(self):
        return Block(datetime.datetime.utcnow(),
                            'First', '0')

    def chain_block(self, data):
        new_block = Block(datetime.datetime.utcnow(), data,
                self.chain_head.hash)
        new_block.prev = self.chain_head
        self.chain_head = new_block
        self.size+=1

    def get_chain_size(self): # exclude genesis block
        return self.size

    def is_chain_consistent(self):
        head= self.chain_head
        flag = True
        idx  = self.size -1
        while head.prev is not None :
            if head.prev.hash != head.previous_hash:
                flag = False
                print(f'Blocks {idx} and {idx-1} are inconsistent')
            if head.hash != head.calc_hash():
                flag = False
                print('Block {idx} hash not consistent')
            if head.prev.timestamp >= head.timestamp:
                flag = False
                print(f'Worng timestamp at block {idx}')
            idx-=1
            head=head.prev
        return flag

    def print_block(self):
        head= self.chain_head
        while head.prev is not None:
             print('-'*20)
             print(head)
             print('-'*20)
             head= head.prev




if __name__ == '__main__':

    def test_blockchain(block_chain):
        block_chain.is_chain_consistent()


    block_chain = Blockchain()
    for i in range(1,3):
        block_chain.chain_block(data = f'Test block {i}')
    test_blockchain(block_chain)

    block_chain.print_block()


    #Aditional testing
    # 1 same data
    block_chain = Blockchain()
    for i in range(1,3):
        block_chain.chain_block(data = f'Test block')
    test_blockchain(block_chain)

    # 2 Empty chain
    block_chain = Blockchain()
    test_blockchain(block_chain)

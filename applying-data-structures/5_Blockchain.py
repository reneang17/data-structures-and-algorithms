import hashlib
from datetime import datetime
import datetime

class Block():
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

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
        self.block_chain = [self.block_zero()]

    def block_zero(self):
        return Block(datetime.datetime.utcnow(),
                            'First', '0')

    def chain_block(self, data):
        self.block_chain.append(Block(datetime.datetime.utcnow(), data,
                                        self.block_chain[len(self.block_chain)-1].hash))
    def get_chain_size(self): # exclude genesis block
        return len(self.block_chain)-1

    def is_chain_consistent(self):
        flag = True
        for i in range(1,len(self.block_chain)):
            if self.block_chain[i-1].hash != self.block_chain[i].previous_hash:
                flag = False
                print(f'Blocks {i} and {i-1} are inconsistent')
            if self.block_chain[i].hash != self.block_chain[i].calc_hash():
                flag = False
                print('Block {i} hash not consistent')
            if self.block_chain[i-1].timestamp >= self.block_chain[i].timestamp:
                flag = False
                print(f'Worng timestamp at block {i}')
        return flag

    def print_block(self):
        for b in self.block_chain:
             print('-'*20)
             print(b)
             print('-'*20)




if __name__ == '__main__':

    def test_blockchain(block_chain):
        block_chain.is_chain_consistent()

    block_chain = Blockchain()
    for i in range(1,3):
        block_chain.chain_block(data = f'Test block {i}')

    test_blockchain(block_chain)
    block_chain.print_block()

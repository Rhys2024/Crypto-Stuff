import hashlib, datetime

class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    prev_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data) -> None:
        self.data = data
    

    def hash(self):
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode('Utf-8')+
            str(self.data).encode('Utf-8')+
            str(self.prev_hash).encode('Utf-8')+
            str(self.timestamp).encode('Utf-8')+
            str(self.blockNo).encode('Utf-8')
        )
        return h.hexdigest()
    
    def __str__(self) -> str:
        return "Block Hash" + str(self.hash()) + "\nblock number:" + str(self.blockNo)


class Blockchain:

    diff = 20
    maxNonce = 2**32
    target = 2 ** (256-diff)


    block = Block("Genesis")
    dummy = head = block

    def add(self,block):
        block.prev_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self,block):

        for i in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

blockchain = Blockchain()

for i in range(10):
    blockchain.mine(Block("Block: " + str(i+1)))


while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next
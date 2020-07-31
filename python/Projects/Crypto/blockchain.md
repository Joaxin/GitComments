## Blockchain

> ​	In more general terms, it’s a public database where new data are stored in a container called a block and are added to an immutable chain (hence blockchain) with data added in the past. In the case of Bitcoin and other cryptocurrencies, these data are groups of transactions. But, the data can be of any type, of course.
>
> 一般而言，它是一个公共数据库，新数据存储在一个称为块的容器中，并与过去添加的数据一起添加到不可变链（区块链）中。 对于比特币和其他加密货币来说，这些数据是一组交易记录。 当然，数据可以是任意类型。



We’ll start by first defining what our blocks will look like. In blockchain, each block is stored with a timestamp and, optionally, an index. In SnakeCoin, we’re going to store both. 

And to help ensure integrity throughout the blockchain, each block will have a self-identifying hash. Like Bitcoin, each block’s hash will be a cryptographic hash of the block’s index, timestamp, data, and the hash of the previous block’s hash. Oh, and the data can be anything you want.

首先我们定义一下区块，在一个区块中，存储着一个时间戳和一个（可选的）索引。为了保证整个区块链的完整性，每个区块有一个标记自己身份的哈希值，像莱特币，每个区块的哈希值都是由一个密码学算法根据区块的索引、时间戳、数据以及前一个区块的哈希值生成的。区块的数据可以是任何你想要的东西。

```python
import hashlib as hasher

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index) + 
                   str(self.timestamp) + 
                   str(self.data) + 
                   str(self.previous_hash))
    return sha.hexdigest()
```

Awesome! We have our block structure, but we’re creating a block**chain**. We need to start adding blocks to the actual chain. As I mentioned earlier, each block requires information from the previous block. But with that being said, a question arises: **how does the first block in the blockchain get there?** Well, the first block, or *genesis block,* is a special block. In many cases, it’s added manually or has unique logic allowing it to be added.

太棒了！我们有自己的区块结构了，但我们需要创建一个区块链啊。我们需要开始把区块附加到实际的链条上。前面提到过，每个区块需要前面区块的信息，那么问题来了：区块链里的第一个区块是怎么来的？好吧，第一个区块，或者说创世区块，是一个特殊的区块，在许多情况下，这是通过手工或者一个唯一的逻辑添加上去的。





这里我们创建一个函数，为了简化起见，简单地返回一个创世区块。这个区块的索引是0，它的数据值和previous hash参数是任意指定的。

We’ll create a function that simply returns a genesis block to make things easy. This block is of index 0, and it has an arbitrary data value and an arbitrary value in the “previous hash” parameter.

```python
import datetime as date

def create_genesis_block():
  # Manually construct a block with
  # index zero and arbitrary previous hash
  return Block(0, date.datetime.now(), "Genesis Block", "0")
```

Now that we’re able to create a genesis block, we need a function that will generate succeeding blocks in the blockchain. This function will take the previous block in the chain as a parameter, create the data for the block to be generated, and return the new block with its appropriate data. When new blocks hash information from previous blocks, the integrity of the blockchain increases with each new block. If we didn’t do this, it would be easier for an outside party to “change the past” and replace our chain with an entirely new one of their own. This chain of hashes acts as cryptographic proof and helps ensure that once a block is added to the blockchain it cannot be replaced or removed.

现在，我们能够创建一个创世区块了，接下来我们需要一个函数来生成区块链里的后续区块，这个函数将链条中的前一个区块作为参数，为新的区块创建数据，并返回带有一个带有合适的数据的新区块。当新的区块哈希来自前面的区块的信息，伴随着新区块的加入，区块链的完整性也得以增强。如果我们不这么做的话，那么外界就很容易用他们的新区块来替换我们的链条里的区块，以达到“篡改历史”的目的。



这个哈希值的链条起到了密码学证据的作用，并确保一旦一个区块加入了区块链，它就不能被替换和修改。

```python
def next_block(last_block):
  this_index = last_block.index + 1
  this_timestamp = date.datetime.now()
  this_data = "Hey! I'm block " + str(this_index)
  this_hash = last_block.hash
  return Block(this_index, this_timestamp, this_data, this_hash)
```



That’s the majority of the hard work. Now, we can create our blockchain! In our case, the blockchain itself is a simple Python list. The first element of the list is the genesis block. And of course, we need to add the succeeding blocks. Because SnakeCoin is the tiniest blockchain, we’ll only add 20 new blocks. We can do this with a for loop.

这就是主要的工作了，现在我们可以创建我们的区块链了。在我们这个例子里，区块链本身是一个简单的Python list。list的第一个元素就是创世区块，当然，我们需要继续添加区块。因为SnakeCoin是一个最简区块链，只有20个新的区块，我们可以在一个for循环里搞定。

```python
# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# How many blocks should we add to the chain
# after the genesis block
num_of_blocks_to_add = 20

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
  block_to_add = next_block(previous_block)
  blockchain.append(block_to_add)
  previous_block = block_to_add
  # Tell everyone about it!
  print "Block #{} has been added to the blockchain!".format(block_to_add.index)
  print "Hash: {}\n".format(block_to_add.hash) 
```


Let’s test what we’ve made so far.

![img](https://miro.medium.com/max/50/1*njl6-UdLUWTLRFsHc4D-tA.png?q=20)

![img](https://miro.medium.com/max/1020/1*njl6-UdLUWTLRFsHc4D-tA.png)

Don’t worry. It goes up to 20.

That’s about all that SnakeCoin has to offer. To make SnakeCoin scale to the size of today’s production blockchains, we’d have to add more features like a server layer to track changes to the chain on multiple machines and a [proof-of-work algorithm](https://en.bitcoin.it/wiki/Proof_of_work) to limit the amount of blocks added in a given time period.

The tiniest blockchain was extremely simple, and it was relatively easy to make. But, with its simplicity came a few flaws. First, SnakeCoin only ran on one single machine, so it was far from distributed, let alone decentralized. Second, blocks could be added to the chain as fast as the host computer could create a Python object and add it to a list. In the case of a simple blockchain, that’s not a problem, but we’re now going to let SnakeCoin be an actual cryptocurrency so we’ll need control the amount of blocks (and coins) that can be created at a time.

From now on, SnakeCoin’s data will be transactions, so each block’s data field will be a list of some transactions. We’ll define a transaction as follows. Each transaction will be a JSON object detailing the sender of the coin, the receiver of the coin, and the amount of SnakeCoin that is being transferred. *Note: Transactions are in JSON format for a reason I’ll detail shortly.*

```
{
  "from": "71238uqirbfh894-random-public-key-a-alkjdflakjfewn204ij",
  "to": "93j4ivnqiopvh43-random-public-key-b-qjrgvnoeirbnferinfo",
  "amount": 3
}
```

Now that we know what our transactions will look like, we need a way to add them to one of the computers in our blockchain network, called a node. To do that, we’ll create a simple HTTP server so that any user can let our nodes know that a new transaction has occurred. A node will be able to accept a POST request with a transaction (like above) as the request body. This is why transactions are JSON formatted; we need them to be transmitted to our server in a request body.

```
pip install flask # Install our web server framework first
```

```python
from flask import Flask
from flask import request
node = Flask(__name__)

# Store the transactions that
# this node has in a list
this_nodes_transactions = []

@node.route('/txion', methods=['POST'])
def transaction():
  if request.method == 'POST':
    # On each new POST request,
    # we extract the transaction data
    new_txion = request.get_json()
    # Then we add the transaction to our list
    this_nodes_transactions.append(new_txion)
    # Because the transaction was successfully
    # submitted, we log it to our console
    print "New transaction"
    print "FROM: {}".format(new_txion['from'])
    print "TO: {}".format(new_txion['to'])
    print "AMOUNT: {}\n".format(new_txion['amount'])
    # Then we let the client know it worked out
    return "Transaction submission successful\n"

node.run()
```

Awesome! Now we have a way to keep a record of users when they send SnakeCoins to each other. This is why people refer to blockchains as public, distributed ledgers: all transactions are stored for all to see and are stored on every node in the network.

But, a question arises: *where do people get SnakeCoins from?* Nowhere, yet. There’s no such thing as a SnakeCoin yet, because not one coin has been created and issued yet. To create new coins, people have to *mine* new blocks of SnakeCoin. When they successfully mine new blocks, a new SnakeCoin is created and rewarded to the person who mined the block. The coin then gets circulated once the miner sends the SnakeCoin to another person.

We don’t want it to be too easy to mine new SnakeCoin blocks, because that will create too many SnakeCoins and they will have little value. Conversely, we don’t want it to be too hard to mine new blocks, because there wouldn’t be enough coins for everyone to spend, and they would be too expensive for our liking. To control the difficulty of mining new SnakeCoins, we’ll implement a [Proof-of-Work](https://en.bitcoin.it/wiki/Proof_of_work) (PoW) algorithm. A Proof-of-Work algorithm is essentially an algorithm that generates an item that is difficult to create but easy to verify. The item is called the proof and, as it sounds, it is proof that a computer performed a certain amount of work.

In SnakeCoin, we’ll create a somewhat simple Proof-of-Work algorithm. To create a new block, a miner’s computer will have to increment a number. When that number is divisible by 9 (the number of letters in “SnakeCoin”) and the proof number of the last block, a new SnakeCoin block will be mined and the miner will be given a brand new SnakeCoin.

```python
 ...blockchain
# ...Block class definition

miner_address = "q3nf394hjg-random-miner-address-34nf3i4nflkn3oi"

def proof_of_work(last_proof):
  # Create a variable that we will use to find
  # our next proof of work
  incrementor = last_proof + 1
  # Keep incrementing the incrementor until
  # it's equal to a number divisible by 9
  # and the proof of work of the previous
  # block in the chain
  while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
    incrementor += 1
  # Once that number is found,
  # we can return it as a proof
  # of our work
  return incrementor

@node.route('/mine', methods = ['GET'])
def mine():
  # Get the last proof of work
  last_block = blockchain[len(blockchain) - 1]
  last_proof = last_block.data['proof-of-work']
  # Find the proof of work for
  # the current block being mined
  # Note: The program will hang here until a new
  #       proof of work is found
  proof = proof_of_work(last_proof)
  # Once we find a valid proof of work,
  # we know we can mine a block so 
  # we reward the miner by adding a transaction
  this_nodes_transactions.append(
    { "from": "network", "to": miner_address, "amount": 1 }
  )
  # Now we can gather the data needed
  # to create the new block
  new_block_data = {
    "proof-of-work": proof,
    "transactions": list(this_nodes_transactions)
  }
  new_block_index = last_block.index + 1
  new_block_timestamp = this_timestamp = date.datetime.now()
  last_block_hash = last_block.hash
  # Empty transaction list
  this_nodes_transactions[:] = []
  # Now create the
  # new block!
  mined_block = Block(
    new_block_index,
    new_block_timestamp,
    new_block_data,
    last_block_hash
  )
  blockchain.append(mined_block)
  # Let the client know we mined a block
  return json.dumps({
      "index": new_block_index,
      "timestamp": str(new_block_timestamp),
      "data": new_block_data,
      "hash": last_block_hash
  }) + "\n"
```

Now, we can control the number of blocks mined in a certain time period, and we can issue new coins for people in the network to send to each other. But like we said, we’re only doing this on one computer. *If blockchains are decentralized, how do we make sure that the same chain is on every node?* To do this, we make each node broadcast its version of the chain to the others and allow them to receive the chains of other nodes. After that, each node has to verify the other nodes’ chains so that the every node in the network can come to a *consensus* of what the resulting blockchain will look like. This is called a [consensus algorithm](https://en.wikipedia.org/wiki/Consensus_(computer_science)).

Our consensus algorithm will be rather simple: if a node’s chain is different from another’s (i.e. there is a conflict), then the longest chain in the network stays and all shorter chains will be deleted. If there is no conflict between the chains in our network, then we carry on.

```python
@node.route('/blocks', methods=['GET'])
def get_blocks():
  chain_to_send = blockchain
  # Convert our blocks into dictionaries
  # so we can send them as json objects later
  for block in chain_to_send:
    block_index = str(block.index)
    block_timestamp = str(block.timestamp)
    block_data = str(block.data)
    block_hash = block.hash
    block = {
      "index": block_index,
      "timestamp": block_timestamp,
      "data": block_data,
      "hash": block_hash
    }
  # Send our chain to whomever requested it
  chain_to_send = json.dumps(chain_to_send)
  return chain_to_send

def find_new_chains():
  # Get the blockchains of every
  # other node
  other_chains = []
  for node_url in peer_nodes:
    # Get their chains using a GET request
    block = requests.get(node_url + "/blocks").content
    # Convert the JSON object to a Python dictionary
    block = json.loads(block)
    # Add it to our list
    other_chains.append(block)
  return other_chains

def consensus():
  # Get the blocks from other nodes
  other_chains = find_new_chains()
  # If our chain isn't longest,
  # then we store the longest chain
  longest_chain = blockchain
  for chain in other_chains:
    if len(longest_chain) < len(chain):
      longest_chain = chain
  # If the longest chain wasn't ours,
  # then we set our chain to the longest
  blockchain = longest_chain
```

We’re just about done now. After running [the full SnakeCoin server code](https://gist.github.com/aunyks/47d157f8bc7d1829a729c2a6a919c173), run the following commands in your terminal. *Assuming you have cURL installed.*

1. Create a transaction.

   ```
   curl "localhost:5000/txion" \
        -H "Content-Type: application/json" \
        -d '{"from": "akjflw", "to":"fjlakdj", "amount": 3}'
   ```

\2. Mine a new block.

```
curl localhost:5000/mine
```

\3. Check out the results. From the client window, we see this.

![img](https://miro.medium.com/max/60/1*qCaWQM7Rzj-gJrJB_J0uJw.png?q=20)

![img](https://miro.medium.com/max/2848/1*qCaWQM7Rzj-gJrJB_J0uJw.png)

With a little bit of pretty printing we see that after mining we get some cool information on our new block.

```
{
  "index": 2,
  "data": {
    "transactions": [
      {
        "to": "fjlakdj",
        "amount": 3,
        "from": "akjflw"
      },
      {
        "to": "q3nf394hjg-random-miner-address-34nf3i4nflkn3oi",
        "amount": 1,
        "from": "network"
      }
    ],
    "proof-of-work": 36
  },
  "hash": "151edd3ef6af2e7eb8272245cb8ea91b4ecfc3e60af22d8518ef0bba8b4a6b18",
  "timestamp": "2017-07-23 11:23:10.140996"
}
```

And that’s it! We’ve made a fairly sized blockchain at this point. Now, SnakeCoin can be launched on multiple machines to create a network, and real SnakeCoins can be mined. Please feel free to tinker with [the SnakeCoin server code](https://gist.github.com/aunyks/47d157f8bc7d1829a729c2a6a919c173) as much as you’d like, and ask as many questions as you need! **In the next part, we’ll discuss creating a SnakeCoin wallet, so users can send, receive, and store their SnakeCoins.**

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/18 10:10
# @Author  : Yann
# @File    : snakeCoin2.py
# @Software: PyCharm
# 既然要用到哈希算法，首先导入哈希包
import hashlib
 
 
# 创建区块类
class Block:
    # 做构造函数，包含索引号、时间戳、数据、上一区块哈希值
    def __init__(self, index, timestamp, data, previous_hash):
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp
        self.index = index
        # 打上本区块的哈希值
        self.hash = self.hash_block()
 
    # 求区块的哈希值函数
    def hash_block(self):
        # 导入sha256这个哈希算法
        sha256 = hashlib.sha256()
        # 计算哈希值
        sha256.update((
                              str(self.index) +
                              str(self.timestamp) +
                              str(self.data) +
                              # 这一步是为了避免编码问题
                              str(self.previous_hash)).encode("utf-8")
                      )
        # 返回哈希值
        return sha256.hexdigest()
 
 
# 任何区块链，总有一个区块是创世区块，制作它
# 导入时间包
import datetime
 
 
def create_genesis_block():
    return Block(0, datetime.datetime.now(), "宝宝是创世区块", "0")
 
 
# 制作下一个区块的函数，所带的形参是上一个区块
def next_block(last_block):
    next_block_index = last_block.index + 1
    next_block_timestamp = datetime.datetime.now()
    next_block_data = "大家好，宝宝是第" + str(next_block_index) + "个区块"
    next_block_hash = last_block.hash
    # 返回制作好的下一个区块
    return Block(next_block_index, next_block_timestamp, next_block_data, next_block_hash)
 
 
# 制作区块链，新建一个数组，先填入创世区块
blockChain = [create_genesis_block()]
# 这里为第二个区块标识出上一个区块
previous_block = blockChain[0]
# 创世区块之后，加入说我们要把100个区块放入一个链中，则有
num_of_block = 100
# 在链中增加区块
for i in range(num_of_block):
    # 这里标识第二个区块
    block_to_add = next_block(previous_block)
    # 把第二个区块附加上去，到链中
    blockChain.append(block_to_add)
    # 将下一个区块（本来标识的第二个区块）改为新的区块，现在标识第三个区块
    previous_block = block_to_add
    # 打印出来瞧一瞧区块链
    # 这里是区块内容基本信息
    print("index:" + str(block_to_add.index) +
          "timestamp:" + str(block_to_add.timestamp) +
          "data:" + str(block_to_add.data) +
          "hash:" + str(block_to_add.previous_hash)
          )
    # 这里是区块的哈希值
    print("Hash:" + str(block_to_add.hash) + "\n")
```













## REFERENCES

- https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b
- https://medium.com/crypto-currently/lets-make-the-tiniest-blockchain-bigger-ac360a328f4d
- https://cloud.tencent.com/developer/ask/38629
- https://www.cnblogs.com/pyxiaomangshe/p/8110497.html
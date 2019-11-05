import sys
sys.path.append('..')
from blockchain_parser.blockchain import Blockchain
#sys.argv.append('~/../../media/wintermute/Mass_Storage/Bitcoin/data/blocks')
# Instantiate the Blockchain by giving the path to the directory 
# containing the .blk files created by bitcoind
blockchain = Blockchain("../../../../../../media/wintermute/Mass_Storage/Bitcoin/data/blocks/")

# To get the blocks ordered by height, you need to provide the path of the
# `index` directory (LevelDB index) being maintained by bitcoind. It contains
# # .ldb files and is present inside the `blocks` directory
# for block in blockchain.get_ordered_blocks('../../../../../../media/wintermute/Mass_Storage/Bitcoin/data/blocks/index', end=10,cache='test'):
#     print("height=%d block=%s" % (block.height, block.hash))
for block in blockchain.get_ordered_blocks('../../../../../../media/wintermute/Mass_Storage/Bitcoin/data/blocks/index',end=1000000,cache='test'):
    print("height=%d block=%s" % (block.height, block.hash))
    for transaction in block.transactions:
        print(transaction)
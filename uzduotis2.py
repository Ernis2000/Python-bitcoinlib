from bitcoin.rpc import RawProxy
import hashlib

p = RawProxy()

def swap(mem):
    sz = bytearray.fromhex(mem)
    sz.reverse()
    return (''.join(format(a, '02x') for a in sz))

blockheight = 277316

block_hash = p.getblockhash(blockheight)
block = p.getblock(block_hash)
versionHex = swap(block["versionHex"])
previousblockhash = swap(block["previousblockhash"])
merkleroot = swap(block["merkleroot"])
time = swap('{:02x}'.format(block["time"]))
bits = swap(block["bits"])
nonce = swap('{:02x}'.format(block["nonce"]))
head = (versionHex + previousblockhash + merkleroot + time + bits + nonce)

head_bin = head.decode('hex')
hash = hashlib.sha256(hashlib.sha256(head_bin).digest()).digest()

print("Correct hash: ")
print hash[::-1].encode('hex_codec')
print("Current hash: ")
print block['hash']
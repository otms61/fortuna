from hashlib import sha256
from Crypto.Cipher import AES
import math

def encrypt(key, c):
    return AES.new(key=key).encrypt(c.to_bytes(16, 'big'))

class Generator(object):
    def __init__(self):
        # XXX: Fix here
        # self.K = b''
        self.K = b'0123456789abcdef0123456789abcdef'
        self.C = 0
        
    def reseed(self, G, s):
        # G: Generator state, G = (K, C)
        # s: New or additional seed
        g = sha256(self.K + s).digest()
        self.C += 1

    def generate_blocks(self, k):
        # k: Nmber of blocks to generate
        r = b''
        for i in range(k):
            r += encrypt(self.K, self.C)
            self.C += 1
        return r

    def pseudo_randomdata(self, n):
        # n: Number of bytes of random data to generate
        assert 0 <= n <= 2**20
        r = self.generate_blocks(math.ceil(n / 16))[:n]
        self.K = self.generate_blocks(2)
        return r




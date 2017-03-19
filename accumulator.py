from hashlib import sha256
from Crypto.Cipher import AES
import math

from generator import Generator

MINPOOLSIZE = 64

class Accumulator(object):
    def __init__(self):
        self.P = [b''] * 32
        self.reseedcnt = 0
        self.generator = Generator()
        self.last_seed = 0

    def randomdata(self, n):
        # n: Number of bytes of random data to generate
        if len(self.P[0]) >= MINPOOLSIZE and self.last_seed > 100:
            self.reseedcnt += 1
            s = b''
            for i in range(32):
                if 2**i % self.reseedcnt == 0:
                    # XXX: Is this correct?
                    s += sha256(self.P[i]).digest()
                    self.P[i] = b''
            self.generator.reseed(s)

        # XXX: FIX here
        # if self.reseedcnt == 0:
        #     print("Generate error, PRNG not seeded yet")
        #     raise

        return self.generator.pseudo_randomdata(n)

    def write_seedfile(self, f):
        with open(f, 'wb') as fp:
            fp.write(self.randomdata(64))

    def update_seedfile(self, f):
        s = open(f).read()
        assert len(s) == 64
        self.generator.reseed(s)
        with open(f, 'wb') as fp:
            fp.write(self.randomdata(64))
        

a = Accumulator()
print(a.randomdata((4)))
print(a.randomdata((4)))
print(a.randomdata((4)))

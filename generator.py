import math
from hashlib import sha256

from cryptography.hazmat.primitives import ciphers


def encrypt(key: bytes, c: int):
    cipher = ciphers.Cipher(ciphers.algorithms.AES(key), mode=ciphers.modes.ECB())
    encryptor = cipher.encryptor()
    return encryptor.update(c.to_bytes(16, "little"))


def sha_double_256(data):
    return sha256(sha256(data).digest()).digest()


class Generator(object):
    def __init__(self):
        self.K = b"\x00" * 32
        self.C = 0

    def reseed(self, s: bytes):
        """
        G: Generator state, G = (K, C)
        s: New or additional seed
        """
        self.K = sha_double_256(self.K + s)
        self.C += 1

    def generate_blocks(self, k: int):
        """
        k: Nmber of blocks to generate
        """
        r = bytearray()
        for i in range(k):
            r += encrypt(self.K, self.C)
            self.C += 1
        return r

    def pseudo_randomdata(self, n: int):
        """
        n: Number of bytes of random data to generate
        """
        assert 0 <= n <= 2**20
        r = self.generate_blocks(math.ceil(n / 16))[:n]
        self.K = self.generate_blocks(2)
        return r

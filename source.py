class Source(object):
    def __init__(self, accumulator):
        self.accumulator = accumulator
        
    def add_randomevent(self, s, i, e):
        # s: Source number in range(256)
        # i: Pool number in range(32)
        # e: Event data
        assert 1 <= len(e) <= 32
        assert 0 <= s <= 255
        assert 0 <= i <= 31
        self.accumulator.P[i] = self.accumulator.P[i] + s + len(e).to_bytes(1, 'big') + e

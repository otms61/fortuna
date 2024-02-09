from generator import Generator


def test():
    """ "
    test copied from https://github.com/pycrypto/pycrypto/blob/65b43bd4ffe2a48bdedae986b1a291f5a2cc7df7/lib/Crypto/SelfTest/Random/Fortuna/test_FortunaGenerator.py#L42
    """
    g = Generator()

    g.reseed(b"Hello")
    assert g.K == bytes.fromhex(
        "0ea6919d4361551364242a4ba890f8f073676e82cf1a52bb880f7e496648b565"
    )
    assert g.C == 1

    assert g.pseudo_randomdata(32) == bytes.fromhex(
        "7cbe2c17684ac223d08969ee8b565616"  # counter = 1
        "717661c0d2f4758bd6ba140bf3791abd"  # counter = 2
    )

    # Meanwhile, the generator will have re-keyed itself and incremented its counter
    assert g.K == bytes.fromhex(
        "33a1bb21987859caf2bbfc5615bef56d"  # counter=3
        "e6b71ff9f37112d0c193a135160862b7"  # counter=4
    )
    assert g.C == 5

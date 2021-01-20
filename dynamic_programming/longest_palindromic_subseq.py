from utils import assert_equal


def lps(string):
    pass


def run_lps():
    assert_equal(lps("a"), 1)
    assert_equal(lps("aa"), 2)
    assert_equal(lps("aba"), 3)
    assert_equal(lps("abcbaf"), 5)
    assert_equal(lps("racecar"), 7)
    assert_equal(lps("yracecarxx"), 7)


if __name__ == '__main__':
    run_lps()

from utils import assert_equal


def total_3_chains(string):
    pass


def run_total_3_chains():
    assert_equal(total_3_chains([10, 13, 7, 8, 14, 11]), 5)
    assert_equal(total_3_chains([10, 7, 7, 7, 7, 11]), 5)
    assert_equal(total_3_chains([5, 3, 15]), 0)
    assert_equal(total_3_chains([5, 15]), 0)
    assert_equal(total_3_chains([10, 13, 16]), 1)


if __name__ == '__main__':
    run_total_3_chains()

from utils import assert_equal


def lis_length(numbers):
    log = [1 for idx in range(len(numbers))]

    for j in range(1, len(numbers)):
        for i in range(j):
            if numbers[i] < numbers[j]:
                if log[j] < log[i] + 1:
                    log[j] = log[i] + 1

    return max(log)


def lis(numbers):
    log = [1 for _ in range(len(numbers))]
    prevs = [None for _ in range(len(numbers))]

    for j in range(1, len(numbers)):
        for i in range(j):
            if numbers[i] < numbers[j]:
                if log[j] < log[i] + 1:
                    log[j] = log[i] + 1
                    prevs[j] = i

    max_ind = log.index(max(log))
    seq = [numbers[max_ind]]
    prev = prevs[max_ind]
    while prev is not None:
        seq.insert(0, numbers[prev])
        prev = prevs[prev]

    return seq


def lcs_length(alpha, beta):
    if alpha is "" or beta is "":
        return 0

    if alpha[-1] is beta[-1]:
        return 1 + lcs_length(alpha[:-1], beta[:-1])
    else:
        return max(lcs_length(alpha[:-1], beta), lcs_length(alpha, beta[:-1]))


def run_lis_length():
    assert_equal(lis_length([10, 9, 2, 5, 3, 7, 19, 18]), 4)

    assert_equal(lis_length([0, 1, 0, 3, 2, 3]), 4)

    assert_equal(lis_length([3, 10, 2, 1, 20]), 3)

    assert_equal(lis_length([3, 2, 1]), 1)

    assert_equal(lis_length([10, 22, 9, 33, 21, 50, 41, 60, 80]), 6)

    assert_equal(lis_length([7, 7, 7, 7, 7, 7, 7]), 1)

    assert_equal(lis_length([2, 8, 1, 0, 4, 7, 10]), 4)

    assert_equal(lis_length([50, 3, 10, 7, 40, 80]), 4)


def run_lis():
    assert_equal(lis([10, 9, 2, 5, 3, 7, 19, 18]), [2, 5, 7, 19])

    assert_equal(lis([0, 1, 0, 3, 2, 3]), [0, 1, 2, 3])

    assert_equal(lis([3, 10, 2, 1, 20]), [3, 10, 20])

    assert_equal(lis([3, 2, 1]), [3])

    assert_equal(lis([10, 22, 9, 33, 21, 50, 41, 60, 80]), [10, 22, 33, 50, 60, 80])

    assert_equal(lis([7, 7, 7, 7, 7, 7, 7]), [7])

    assert_equal(lis([2, 8, 1, 0, 4, 7, 10]), [2, 4, 7, 10])

    assert_equal(lis([50, 3, 10, 7, 40, 80]), [3, 10, 40, 80])


def run_lcs_length():
    assert_equal(lcs_length("aza", "aaa"), 2)

    assert_equal(lcs_length("abcdefgh", "xxbxdxexhxx"), 4)


if __name__ == "__main__":
    run_lcs_length()

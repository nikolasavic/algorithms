from utils import assert_equal


def lis_length(numbers):
    log = [1] * len(numbers)

    for j in range(1, len(numbers)):
        for i in range(j):
            if numbers[i] < numbers[j]:
                if log[j] < log[i] + 1:
                    log[j] = log[i] + 1

    return max(log)


def run_lis_length():
    assert_equal(lis_length([10, 9, 2, 5, 3, 7, 19, 18]), 4)

    assert_equal(lis_length([0, 1, 0, 3, 2, 3]), 4)

    assert_equal(lis_length([3, 10, 2, 1, 20]), 3)

    assert_equal(lis_length([3, 2, 1]), 1)

    assert_equal(lis_length([10, 22, 9, 33, 21, 50, 41, 60, 80]), 6)

    assert_equal(lis_length([7, 7, 7, 7, 7, 7, 7]), 1)

    assert_equal(lis_length([2, 8, 1, 0, 4, 7, 10]), 4)

    assert_equal(lis_length([50, 3, 10, 7, 40, 80]), 4)


if __name__ == "__main__":
    run_lis_length()

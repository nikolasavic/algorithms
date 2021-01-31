from utils import assert_equal


def lis(numbers):
    n = len(numbers)
    T = [1 for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, i):
            if numbers[j - 1] < numbers[i - 1]:  # Not 1-based index
                if T[i] < T[j] + 1:
                    T[i] = T[j] + 1

    return max(T)


def run_lis():
    assert_equal(lis([10, 9, 2, 5, 3, 7, 19, 18]), 4)
    assert_equal(lis([0, 1, 0, 3, 2, 3]), 4)
    assert_equal(lis([3, 10, 2, 1, 20]), 3)
    assert_equal(lis([3, 2, 1]), 1)
    assert_equal(lis([10, 22, 9, 33, 21, 50, 41, 60, 80]), 6)
    assert_equal(lis([7, 7, 7, 7, 7, 7, 7]), 1)
    assert_equal(lis([2, 8, 1, 0, 4, 7, 10]), 4)
    assert_equal(lis([50, 3, 10, 7, 40, 80]), 4)


if __name__ == "__main__":
    run_lis()

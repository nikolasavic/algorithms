# Given a target, return whether it's possible to create a combination of numbers provided
# that sum to the target
# Example:
# target: 7, numbers: [2,3,5]
# output: true
from utils import assert_equal


def can_sum_memo(target, numbers, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]

    if target == 0:
        return True
    if target < 0:
        return False

    for n in numbers:
        remainder = target - n
        if can_sum_memo(remainder, numbers, memo):
            memo[remainder] = True
            return True

    memo[target] = False
    return False


def has_sum_memo(target, numbers, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]

    if target == 0:
        return []
    if target < 0:
        return None

    for n in numbers:
        remainder = target - n
        result = has_sum_memo(remainder, numbers, memo)
        if result is not None:
            memo[remainder] = result
            return [*result, n]

    memo[target] = None
    return None


def best_sum_memo(target, numbers, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]

    if target == 0:
        return []
    if target < 0:
        return None

    shortest = None
    for n in numbers:
        remainder = target - n
        result = best_sum_memo(remainder, numbers, memo)
        if result is not None:
            attempt = [*result, n]
            if shortest is None or len(attempt) < len(shortest):
                shortest = attempt

    memo[target] = shortest
    return shortest


def run_can_sum():
    assert_equal(can_sum_memo(5, [3, 4]), False)
    assert_equal(can_sum_memo(7, [2, 3, 5, 7]), True)
    assert_equal(can_sum_memo(8, [2, 3, 5, 7]), True)
    assert_equal(can_sum_memo(13, [2, 3, 5, 7]), True)
    assert_equal(can_sum_memo(7, [2, 4]), False)
    assert_equal(can_sum_memo(300, [7, 14]), False)


def run_has_sum():
    assert_equal(has_sum_memo(5, [3, 4]), None)
    assert_equal(has_sum_memo(7, [2, 3, 5, 7]), [3, 2, 2])
    assert_equal(has_sum_memo(8, [2, 3, 5, 7]), [2, 2, 2, 2])
    assert_equal(has_sum_memo(13, [3, 5, 7]), [7, 3, 3])
    assert_equal(has_sum_memo(7, [2, 4]), None)
    assert_equal(has_sum_memo(300, [7, 14]), None)
    assert_equal(has_sum_memo(100, [10, 25]), [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])


def run_best_sum():
    assert_equal(best_sum_memo(5, [3, 4]), None)
    assert_equal(best_sum_memo(7, [2, 3, 5, 7]), [7])
    assert_equal(best_sum_memo(8, [2, 3, 5, 7]), [5, 3])
    assert_equal(best_sum_memo(8, [1, 4, 5]), [4, 4])
    assert_equal(best_sum_memo(13, [3, 5, 7]), [7, 3, 3])
    assert_equal(best_sum_memo(7, [2, 4]), None)
    assert_equal(best_sum_memo(300, [7, 14]), None)
    assert_equal(best_sum_memo(100, [1, 5, 10, 15, 25]), [25, 25, 25, 25])


if __name__ == "__main__":
    run_can_sum()
    run_has_sum()
    run_best_sum()

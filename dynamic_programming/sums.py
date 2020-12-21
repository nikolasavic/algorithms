# Given a target, return whether it's possible to create a combination of numbers provided
# that sum to the target
# Example:
# target: 7, numbers: [2,3,5]
# output: true
from utils import assert_equal


def can_sum(target, numbers, memo=None):
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
        if can_sum(remainder, numbers, memo):
            memo[remainder] = True
            return True

    memo[target] = False
    return False


def has_sum(target, numbers, memo=None):
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
        result = has_sum(remainder, numbers, memo)
        if result is not None:
            memo[remainder] = result
            return [*result, n]

    memo[target] = None
    return None


def best_sum(target, numbers, memo=None):
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
        result = best_sum(remainder, numbers, memo)
        if result is not None:
            attempt = [*result, n]
            if shortest is None or len(attempt) < len(shortest):
                shortest = attempt

    memo[target] = shortest
    return shortest


def run_can_sum():
    assert_equal(can_sum(5, [3, 4]), False)
    assert_equal(can_sum(7, [2, 3, 5, 7]), True)
    assert_equal(can_sum(8, [2, 3, 5, 7]), True)
    assert_equal(can_sum(13, [2, 3, 5, 7]), True)
    assert_equal(can_sum(7, [2, 4]), False)
    assert_equal(can_sum(300, [7, 14]), False)


def run_has_sum():
    assert_equal(has_sum(5, [3, 4]), None)
    assert_equal(has_sum(7, [2, 3, 5, 7]), [3, 2, 2])
    assert_equal(has_sum(8, [2, 3, 5, 7]), [2, 2, 2, 2])
    assert_equal(has_sum(13, [3, 5, 7]), [7, 3, 3])
    assert_equal(has_sum(7, [2, 4]), None)
    assert_equal(has_sum(300, [7, 14]), None)
    assert_equal(has_sum(100, [1, 5, 10, 25]), [25, 25, 25, 25])


def run_best_sum():
    assert_equal(best_sum(5, [3, 4]), None)
    assert_equal(best_sum(7, [2, 3, 5, 7]), [7])
    assert_equal(best_sum(8, [2, 3, 5, 7]), [5, 3])
    assert_equal(best_sum(8, [1, 4, 5]), [4, 4])
    assert_equal(best_sum(13, [3, 5, 7]), [7, 3, 3])
    assert_equal(best_sum(7, [2, 4]), None)
    assert_equal(best_sum(300, [7, 14]), None)


if __name__ == "__main__":
    run_best_sum()

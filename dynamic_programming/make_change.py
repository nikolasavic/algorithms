from utils import assert_equal


def can_make_change_iter(target, coins):
    dp = [False for _ in range(target + 1)]
    dp[0] = True

    for i in range(len(dp)):
        if dp[i] is True:
            for c in coins:
                if i + c < len(dp):
                    dp[i + c] = True

    return dp[target]


def can_make_change_memo(target, coins, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]

    if target == 0:
        return True
    if target < 0:
        return False

    for c in coins:
        remainder = target - c
        if can_make_change_memo(remainder, coins, memo):
            memo[remainder] = True
            return True

    memo[target] = False
    return False


def has_make_change_iter(target, coins):
    dp = [None for _ in range(target + 1)]
    dp[0] = []

    for i in range(len(dp)):
        if dp[i] is not None:
            for c in coins:
                attempt = [*dp[i], c]
                if i + c < len(dp):
                    if dp[i + c] is None:
                        dp[i + c] = attempt
    return dp[target]


def has_make_change_memo(target, coins, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]

    if target == 0:
        return []
    if target < 0:
        return None

    for c in coins:
        remainder = target - c
        result = has_make_change_memo(remainder, coins, memo)
        if result is not None:
            memo[remainder] = result
            return [*result, c]

    memo[target] = None
    return None


def best_make_change_iter(target, coins):
    dp = [None for _ in range(target + 1)]
    dp[0] = []

    for i in range(len(dp)):
        if dp[i] is not None:
            for c in coins:
                if i + c < len(dp):
                    attempt = [*dp[i], c]
                    if dp[i + c] is None or len(attempt) < len(dp[i + c]):
                        dp[i + c] = attempt

    return dp[target]


def best_make_change_memo(target, coins, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]

    if target == 0:
        return []
    if target < 0:
        return None

    shortest = None
    for c in coins:
        remainder = target - c
        result = best_make_change_memo(remainder, coins, memo)
        if result is not None:
            attempt = [*result, c]
            if shortest is None or len(attempt) < len(shortest):
                shortest = attempt

    memo[target] = shortest
    return shortest


def run_can_sum():
    assert_equal(can_make_change_iter(5, [3, 4]), False)
    assert_equal(can_make_change_iter(7, [2, 3, 5, 7]), True)
    assert_equal(can_make_change_iter(8, [2, 3, 5, 7]), True)
    assert_equal(can_make_change_iter(13, [2, 3, 5, 7]), True)
    assert_equal(can_make_change_iter(7, [2, 4]), False)
    assert_equal(can_make_change_iter(300, [7, 14]), False)

    assert_equal(can_make_change_memo(5, [3, 4]), False)
    assert_equal(can_make_change_memo(7, [2, 3, 5, 7]), True)
    assert_equal(can_make_change_memo(8, [2, 3, 5, 7]), True)
    assert_equal(can_make_change_memo(13, [2, 3, 5, 7]), True)
    assert_equal(can_make_change_memo(7, [2, 4]), False)
    assert_equal(can_make_change_memo(300, [7, 14]), False)


def run_has_sum():
    assert_equal(has_make_change_iter(5, [3, 4]), None)
    assert_equal(has_make_change_iter(7, [2, 3, 5, 7]), [7])
    assert_equal(has_make_change_iter(8, [2, 3, 5, 7]), [3, 5])
    assert_equal(has_make_change_iter(13, [3, 5, 7]), [3, 3, 7])
    assert_equal(has_make_change_iter(7, [2, 4]), None)
    assert_equal(has_make_change_iter(300, [7, 14]), None)
    assert_equal(has_make_change_iter(100, [1, 10, 15, 25, 20, 5]), [25, 25, 25, 25])
    assert_equal(has_make_change_iter(8, [1, 4, 5]), [1, 1, 1, 5])

    assert_equal(has_make_change_memo(5, [3, 4]), None)
    assert_equal(has_make_change_memo(7, [2, 3, 5, 7]), [3, 2, 2])
    assert_equal(has_make_change_memo(8, [2, 3, 5, 7]), [2, 2, 2, 2])
    assert_equal(has_make_change_memo(13, [3, 5, 7]), [7, 3, 3])
    assert_equal(has_make_change_memo(7, [2, 4]), None)
    assert_equal(has_make_change_memo(300, [7, 14]), None)
    assert_equal(has_make_change_memo(100, [1, 10, 15, 25, 20, 5]), [1 for _ in range(100)])
    assert_equal(has_make_change_memo(8, [1, 4, 5]), [1, 1, 1, 1, 1, 1, 1, 1])


def run_best_sum():
    assert_equal(best_make_change_iter(5, [3, 4]), None)
    assert_equal(best_make_change_iter(7, [2, 3, 5, 7]), [7])
    assert_equal(best_make_change_iter(8, [2, 3, 5, 7]), [3, 5])
    assert_equal(best_make_change_iter(8, [1, 4, 5]), [4, 4])
    assert_equal(best_make_change_iter(13, [3, 5, 7]), [3, 3, 7])
    assert_equal(best_make_change_iter(7, [2, 4]), None)
    assert_equal(best_make_change_iter(300, [7, 14]), None)
    assert_equal(best_make_change_iter(100, [1, 5, 10, 15, 25]), [25, 25, 25, 25])
    assert_equal(best_make_change_iter(8, [1, 4, 5]), [4, 4])

    assert_equal(best_make_change_memo(5, [3, 4]), None)
    assert_equal(best_make_change_memo(7, [2, 3, 5, 7]), [7])
    assert_equal(best_make_change_memo(8, [2, 3, 5, 7]), [5, 3])
    assert_equal(best_make_change_memo(8, [1, 4, 5]), [4, 4])
    assert_equal(best_make_change_memo(13, [3, 5, 7]), [7, 3, 3])
    assert_equal(best_make_change_memo(7, [2, 4]), None)
    assert_equal(best_make_change_memo(300, [7, 14]), None)
    assert_equal(best_make_change_memo(100, [1, 5, 10, 15, 25]), [25, 25, 25, 25])
    assert_equal(best_make_change_memo(8, [1, 4, 5]), [4, 4])


if __name__ == "__main__":
    run_can_sum()
    run_has_sum()
    run_best_sum()

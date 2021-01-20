from utils import assert_equal


def can_make_change(target, coins):
    dp = [False for _ in range(target + 1)]
    dp[0] = True

    for i in range(len(dp)):
        if dp[i] is True:
            for c in coins:
                if i + c < len(dp):
                    dp[i + c] = True

    return dp[target]


def best_make_change(target, coins):
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


def run_can_sum():
    assert_equal(can_make_change(5, [3, 4]), False)
    assert_equal(can_make_change(7, [2, 3, 5, 7]), True)
    assert_equal(can_make_change(8, [2, 3, 5, 7]), True)
    assert_equal(can_make_change(13, [2, 3, 5, 7]), True)
    assert_equal(can_make_change(7, [2, 4]), False)
    assert_equal(can_make_change(300, [7, 14]), False)


def run_best_sum():
    assert_equal(best_make_change(5, [3, 4]), None)
    assert_equal(best_make_change(7, [2, 3, 5, 7]), [7])
    assert_equal(best_make_change(8, [2, 3, 5, 7]), [3, 5])
    assert_equal(best_make_change(8, [1, 4, 5]), [4, 4])
    assert_equal(best_make_change(13, [3, 5, 7]), [3, 3, 7])
    assert_equal(best_make_change(7, [2, 4]), None)
    assert_equal(best_make_change(300, [7, 14]), None)
    assert_equal(best_make_change(100, [1, 5, 10, 15, 25]), [25, 25, 25, 25])
    assert_equal(best_make_change(8, [1, 4, 5]), [4, 4])


if __name__ == "__main__":
    run_can_sum()
    run_best_sum()

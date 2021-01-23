from utils import assert_equal


def total_3_chains(arr):
    n = len(arr)
    dp = [0 for _ in range(n)]

    for i in range(1, n - 1):
        for j in range(i):
            if abs(arr[i] - arr[j]) <= 3 and abs(arr[i] - arr[n - 1]) <= 3:
                dp[i] = 1 + dp[j]

    if abs(arr[0] - arr[n - 1]) <= 3:
        dp[0] = 1

    return sum(dp)


def run_total_3_chains():
    assert_equal(total_3_chains([4, 10, 9, 3, 6, 15, 10, 8, 11, 10]), 4)
    assert_equal(total_3_chains([6, 3, 7, 11, 1, 2, 14, 9, 2, 6]), 5)

    assert_equal(total_3_chains([2, 10, 12, 13, 11, 9, 4, 5, 12, 5]), 4)
    assert_equal(total_3_chains([10, 13, 7, 8, 14, 11]), 5)
    assert_equal(total_3_chains([7, 10, 13]), 1)
    assert_equal(total_3_chains([5, 3, 15]), 0)
    assert_equal(total_3_chains([5, 15]), 0)
    assert_equal(total_3_chains([5, 6]), 1)


if __name__ == "__main__":
    run_total_3_chains()

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
# Example 2:
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
from utils import assert_equal


def climb_stairs_iter(n):
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1

    for i in range(len(dp)):
        if i + 1 < len(dp):
            dp[i + 1] += dp[i]

        if i + 2 < len(dp):
            dp[i + 2] += dp[i]

    return dp[n]


def climb_stairs_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]

    if n == 0:
        return 1
    if n <= 0:
        return 0

    memo[n] = climb_stairs_memo(n - 1, memo=memo) + climb_stairs_memo(n - 2, memo=memo)

    return memo[n]


if __name__ == "__main__":
    assert_equal(climb_stairs_memo(5), 8)
    assert_equal(climb_stairs_memo(45), 1836311903)
    assert_equal(climb_stairs_iter(5), 8)
    assert_equal(climb_stairs_iter(45), 1836311903)

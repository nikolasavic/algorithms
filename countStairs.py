class Solution:
    def climbStairs(self, n: int, memo={}) -> int:
        if n in memo:
            return memo[n]

        if n == 0:
            return 1

        if n <= 0:
            return 0

        memo[n] = self.climbStairs(n - 1, memo=memo) + self.climbStairs(
            n - 2, memo=memo
        )

        return memo[n]


if __name__ == "__main__":
    assert Solution().climbStairs(5) == 8
    assert Solution().climbStairs(45) == 1836311903

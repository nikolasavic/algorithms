from utils import assert_equal


def lps(string):
    n = len(string)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for x in range(n):
        dp[x][x] = 1

    for seq_len in range(2, n + 1):
        for i in range(n - seq_len + 1):
            j = i + seq_len - 1
            if string[i] == string[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


def run_lps():
    assert_equal(lps("a"), 1)
    assert_equal(lps("aa"), 2)
    assert_equal(lps("aba"), 3)
    assert_equal(lps("abcbaf"), 5)
    assert_equal(lps("racecar"), 7)
    assert_equal(lps("yracecarxx"), 7)


if __name__ == "__main__":
    run_lps()

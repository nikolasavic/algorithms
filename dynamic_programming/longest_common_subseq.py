from utils import assert_equal


def lcs_length_iter(alpha, beta):
    dp = [[0 for _ in range(len(beta) + 1)] for _ in range(len(alpha) + 1)]

    for a in range(1, len(alpha) + 1):
        for b in range(1, len(beta) + 1):
            if alpha[a - 1] == beta[b - 1]:
                dp[a][b] = 1 + dp[a - 1][b - 1]
            else:
                dp[a][b] = max(dp[a - 1][b], dp[a][b - 1])

    return dp[-1][-1]


def lcs_length_recursive(alpha, beta):
    if alpha == "" or beta == "":
        return 0

    if alpha[0] == beta[0]:
        return 1 + lcs_length_recursive(alpha[1:], beta[1:])
    else:
        return max(
            lcs_length_recursive(alpha, beta[1:]),
            lcs_length_recursive(alpha[1:], beta),
        )


def run_lcs_length():
    assert_equal(lcs_length_recursive("aza", "aaa"), 2)
    assert_equal(lcs_length_recursive("abcdefgh", "xxbxdxexhxx"), 4)
    assert_equal(lcs_length_recursive("xxooxxoooxx", "YoxYxoYoxxYYY"), 7)
    assert_equal(lcs_length_recursive("abcdexxxabcxxx", "yyyyxxxabde"), 5)
    assert_equal(lcs_length_recursive("xxxxxXX", "yyyyyXX"), 2)
    assert_equal(lcs_length_recursive("xxxxxXxxX", "yyyyyXyyX"), 2)
    assert_equal(lcs_length_recursive("xxXxxXxxxX", "yyXyyyXyyX"), 3)
    assert_equal(lcs_length_recursive("axxxa", "ayyya"), 2)

    assert_equal(lcs_length_iter("aza", "aaa"), 2)
    assert_equal(lcs_length_iter("abcdefgh", "xxbxdxexhxx"), 4)
    assert_equal(lcs_length_iter("xxooxxoooxx", "YoxYxoYoxxYYY"), 7)
    assert_equal(lcs_length_iter("abcdexxxabcxxx", "yyyyxxxabde"), 5)
    assert_equal(lcs_length_iter("xxxxxXX", "yyyyyXX"), 2)
    assert_equal(lcs_length_iter("xxxxxXxxX", "yyyyyXyyX"), 2)
    assert_equal(lcs_length_iter("xxXxxXxxxX", "yyXyyyXyyX"), 3)
    assert_equal(lcs_length_iter("axxxa", "ayyya"), 2)


if __name__ == "__main__":
    run_lcs_length()

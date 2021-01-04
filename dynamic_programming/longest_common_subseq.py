from utils import assert_equal


def lcs_length_iter(alpha, beta):
    dp = [[0 for _ in range(len(beta))] for _ in range(len(alpha))]

    for a in range(1, len(alpha)):
        for b in range(1, len(beta)):
            if alpha[a] == beta[b]:
                dp[a][b] = 1 + max(dp[a - 1][b], dp[a][b - 1])
            else:
                dp[a][b] = max(dp[a - 1][b], dp[a][b - 1])

    return dp[-1][-1]


def lcs_length_recursive(alpha, beta):
    if alpha == "" or beta == "":
        return 0

    if alpha[-1:] == beta[-1:]:
        return 1 + lcs_length_recursive(alpha[:-1], beta[:-1])
    else:
        return max(
            lcs_length_recursive(alpha, beta[:-1]),
            lcs_length_recursive(alpha[:-1], beta),
        )


def run_lcs_length():
    assert_equal(lcs_length_recursive("aza", "aaa"), 2)
    assert_equal(lcs_length_recursive("abcdefgh", "xxbxdxexhxx"), 4)

    assert_equal(lcs_length_iter("aza", "aaa"), 2)
    assert_equal(lcs_length_iter("abcdefgh", "xxbxdxexhxx"), 4)


if __name__ == "__main__":
    run_lcs_length()

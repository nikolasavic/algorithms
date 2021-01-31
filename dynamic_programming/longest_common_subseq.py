from utils import assert_equal


def lcs(alpha, beta):
    T = [[0 for _ in range(len(beta) + 1)] for _ in range(len(alpha) + 1)]

    for a in range(1, len(alpha) + 1):
        for b in range(1, len(beta) + 1):
            if alpha[a - 1] == beta[b - 1]:  # Not 1-based index
                T[a][b] = 1 + T[a - 1][b - 1]
            else:
                T[a][b] = max(T[a - 1][b], T[a][b - 1])

    return T[-1][-1]


def run_lcs():
    assert_equal(lcs("aza", "aaa"), 2)
    assert_equal(lcs("abcdefgh", "xxbxdxexhxx"), 4)
    assert_equal(lcs("xxooxxoooxx", "YoxYxoYoxxYYY"), 7)
    assert_equal(lcs("abcdexxxabcxxx", "yyyyxxxabde"), 5)
    assert_equal(lcs("xxxxxXX", "yyyyyXX"), 2)
    assert_equal(lcs("xxxxxXxxX", "yyyyyXyyX"), 2)
    assert_equal(lcs("xxXxxXxxxX", "yyXyyyXyyX"), 3)
    assert_equal(lcs("axxxa", "ayyya"), 2)


if __name__ == "__main__":
    run_lcs()

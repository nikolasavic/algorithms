from utils import assert_equal


def can_make_change(target, coins):
    T = [False for _ in range(target + 1)]
    T[0] = True

    for i in range(1, target + 1):
        for c in coins:
            if c <= target:
                T[i] = T[i] or T[i - c]

    return T[target]


def can_make_change_k_coins(target, coins, k):
    pass


def best_make_change(target, coins):
    T = [None for _ in range(target + 1)]
    T[0] = []

    for i in range(len(T)):
        if T[i] is not None:
            for c in coins:
                if i + c < len(T):
                    attempt = [*T[i], c]
                    if T[i + c] is None or len(attempt) < len(T[i + c]):
                        T[i + c] = attempt

    return T[target]


def run_can_make_change():
    assert_equal(can_make_change(5, [3, 4]), False)
    assert_equal(can_make_change(7, [2, 3, 5, 7]), True)
    assert_equal(can_make_change(8, [2, 3, 5, 7]), True)
    assert_equal(can_make_change(13, [2, 3, 5, 7]), True)
    assert_equal(can_make_change(7, [2, 4]), False)
    assert_equal(can_make_change(300, [7, 14]), False)


def run_best_make_change():
    assert_equal(best_make_change(5, [3, 4]), None)
    assert_equal(best_make_change(7, [2, 3, 5, 7]), [7])
    assert_equal(best_make_change(8, [2, 3, 5, 7]), [3, 5])
    assert_equal(best_make_change(8, [1, 4, 5]), [4, 4])
    assert_equal(best_make_change(13, [3, 5, 7]), [3, 3, 7])
    assert_equal(best_make_change(7, [2, 4]), None)
    assert_equal(best_make_change(300, [7, 14]), None)
    assert_equal(best_make_change(100, [1, 5, 10, 15, 25]), [25, 25, 25, 25])
    assert_equal(best_make_change(8, [1, 4, 5]), [4, 4])


def run_can_make_change_k_coins():
    pass


if __name__ == "__main__":
    run_can_make_change()
    run_best_make_change()
    run_can_make_change_k_coins()

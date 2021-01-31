from utils import assert_equal


def linear_frog(n):
    # Jumps:
    # i -> i + 1
    # i -> i + 4
    T = [0 for _ in range(n + 1)]
    T[1] = 1

    for i in range(2, n + 1):
        T[i] = T[i - 1]

        if i > 4:
            T[i] = T[i] + T[i - 4]

    return T[n]


def grid_frog(n):
    # Jumps:
    # i, j -> i + 1, j + 2
    # i, j -> i + 2, j + 1
    T = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    T[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i > 1 and j > 1:
                T[i][j] = T[i - 1][j - 2] + T[i - 2][j - 1]

    return T[n][n]


def run_linear_frog():
    assert_equal(linear_frog(3), 1)
    assert_equal(linear_frog(5), 2)
    assert_equal(linear_frog(6), 3)
    assert_equal(linear_frog(7), 4)


def run_grid_frog():
    assert_equal(grid_frog(3), 0)
    assert_equal(grid_frog(4), 2)
    assert_equal(grid_frog(7), 6)
    assert_equal(grid_frog(10), 20)
    assert_equal(grid_frog(11), 0)
    assert_equal(grid_frog(13), 70)
    assert_equal(grid_frog(16), 252)
    assert_equal(grid_frog(19), 924)
    assert_equal(grid_frog(31), 184756)


if __name__ == "__main__":
    run_linear_frog()
    run_grid_frog()

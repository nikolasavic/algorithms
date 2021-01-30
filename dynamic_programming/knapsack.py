from utils import assert_equal


def knapsack(W, values, weights):
    T = [[0 for _ in range(W + 1)] for _ in range(len(weights) + 1)]

    for i in range(1, len(T)):
        for w in range(1, len(T[0])):
            value = values[i - 1]
            weight = weights[i - 1]
            if weight <= w:
                use = T[i - 1][w - weight] + value
                dont_use = T[i - 1][w]
                T[i][w] = max(use, dont_use)
            else:
                T[i][w] = T[i - 1][w]

    return T[-1][-1]


def run_knapsack():
    assert_equal(knapsack(10, [8, 5, 4], [9, 5, 4]), 9)
    assert_equal(knapsack(15, [60, 80, 70], [7, 8, 6]), 150)
    assert_equal(knapsack(10, [10, 40, 30, 50], [5, 4, 6, 3]), 90)
    assert_equal(knapsack(50, [60, 100, 120], [10, 20, 30]), 220)
    assert_equal(knapsack(25, [24, 18, 18, 10], [24, 10, 10, 7]), 36)
    assert_equal(knapsack(60, [100, 280, 120], [10, 40, 20]), 400)


if __name__ == "__main__":
    run_knapsack()

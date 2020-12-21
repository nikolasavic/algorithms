# Given a target, return whether it's possible to create a combination of numbers provided
# that sum to the target
# Example:
# target: 7, numbers: [2,3,5]
# output: true


def can_sum(target, numbers, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]

    if target == 0:
        return True
    if target < 0:
        return False

    for n in numbers:
        remainder = target - n
        if can_sum(remainder, numbers, memo):   
            memo[remainder] = True
            return True

    memo[target] = False
    return False


def run_can_sum():
    assert can_sum(5, [3, 4]) == False
    assert can_sum(7, [2, 3, 5, 7]) == True
    assert can_sum(8, [2, 3, 5, 7]) == True
    assert can_sum(13, [2, 3, 5, 7]) == True
    assert can_sum(7, [2, 4]) == False
    assert can_sum(300, [7, 14]) == False


if __name__ == "__main__":
    run_can_sum()

def can_sum(target, numbers):
    if target == 0:
        return True

    if target < 0:
        return False

    for n in numbers:
        remainder = target - n
        if can_sum(remainder, numbers):
            return True

    return False


if __name__ == "__main__":
    assert can_sum(5, [3, 4]) == False
    assert can_sum(7, [2, 3, 5, 7]) == True
    assert can_sum(8, [2, 3, 5, 7]) == True
    assert can_sum(13, [2, 3, 5, 7]) == True
    assert can_sum(7, [2, 4]) == False
    # assert can_sum(300, [7, 14]) == False

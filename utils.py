def assert_equal(result, expected):
    if result == expected:
        return True
    else:
        print(f"expected: {expected}")
        print(f"received: {result}")
        return False

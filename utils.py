def assert_equal(result, expected, prob=[1]):
    if result == expected:
        print(f"#{len(prob)}  ✅")
        prob.append(1)
        return True
    else:
        print(f"#{len(prob)}  ❌")
        print(f"  expected: {expected}")
        print(f"  received: {result}")
        prob.append(1)
        return False

from utils import assert_equal


def has_construct(word, word_bank, memo=None):
    if memo is None:
        memo = {}
    if word in memo:
        return memo[word]

    if word is "":
        return []
    if word is None:
        return None

    for w in word_bank:
        if word.startswith(w):
            remainder = word[len(w) :]
            result = has_construct(remainder, word_bank, memo)
            if result is not None:
                memo[remainder] = result
                return [w, *result]

    memo[word] = None
    return None


def best_construct(word, word_bank, memo=None):
    if memo is None:
        memo = {}
    if word in memo:
        return memo[word]

    if word is "":
        return []
    if word is None:
        return None

    best = None
    for w in word_bank:
        if word.startswith(w):
            remainder = word[len(w) :]
            result = best_construct(remainder, word_bank, memo)
            if result is not None:
                if best is None or len(result) < len(best):
                    best = [w, *result]

    memo[word] = best
    return best


def run_has_construct():
    assert_equal(
        has_construct("apple", ["a", "ap", "app", "p", "pl", "le", "e"]),
        ["a", "p", "p", "le"],
    )

    assert_equal(
        has_construct(
            "abcdefgh", ["a", "ab", "cdef", "bcde", "abcdef", "f", "gh", "fgh"]
        ),
        ["a", "bcde", "f", "gh"],
    )

    assert_equal(
        has_construct("skateboard", ["ska", "ate", "kateb", "boar"]),
        None,
    )

    assert_equal(
        has_construct(
            "aaaaaaaaaaaaaaaaaaaaaaaz",
            ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaaaa", "aaaaaaaaaaa"],
        ),
        None,
    )


def run_best_construct():
    assert_equal(
        best_construct("apple", ["a", "ap", "app", "p", "pl", "le", "e"]),
        ["app", "le"],
    )

    assert_equal(
        best_construct(
            "abcdefgh", ["a", "ab", "cdef", "bcde", "abcdef", "f", "gh", "fgh"]
        ),
        ["abcdef", "gh"],
    )
    assert_equal(
        best_construct("skateboard", ["ska", "ate", "kateb", "boar"]),
        None,
    )

    assert_equal(
        best_construct(
            "aaaaaaaaaaaaaaaaaaaaaaaz",
            ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaaaa", "aaaaaaaaaaa"],
        ),
        None,
    )


if __name__ == "__main__":
    run_best_construct()

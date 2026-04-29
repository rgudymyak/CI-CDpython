from hello import sum


def test_sum():
    assert sum(2,3) == 5, "2 + 3 should be equal 5"
    assert sum(-1, 1) == 0, "-1 + 1 should be equal 0"
    print(" all test passed")

if __name__ == "__main__":
    test_sum()
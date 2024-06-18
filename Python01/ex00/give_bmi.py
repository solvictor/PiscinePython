def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """Get BMIs from heights and weights

    Args:
        height (list[int | float]): List of heights
        weight (list[int | float]): List of weights

    Returns:
        list[int | float]: List of BMIs
    """

    assert isinstance(height, list) and isinstance(weight, list)
    assert len(height) == len(weight)
    assert all(isinstance(h, (int, float)) for h in height)
    assert all(isinstance(w, (int, float)) for w in weight)
    return [w / (h * h) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Get a list of bools which indicates whether the corresponding BMI
    if strictly greater than limit

    Args:
        bmi (list[int | float]): BMIs to check
        limit (int): Limit for a BMI

    Returns:
        list[bool]: List of check results
    """

    assert isinstance(bmi, list) and isinstance(limit, int)
    assert all(isinstance(b, (int, float)) for b in bmi)
    return [b > limit for b in bmi]


def main():
    """Test this file's functions"""

    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()

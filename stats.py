"""Tiny helpers used only to check that Copilot code review runs on this account."""


def average(values):
    """Return the mean of a non-empty list of numbers."""
    if not values:
        raise ValueError("average() needs at least one value")
    return sum(values) / len(values)


def median(values):
    """Return the median of a non-empty list of numbers."""
    ordered = sorted(values)
    middle = len(ordered) // 2
    return ordered[middle]

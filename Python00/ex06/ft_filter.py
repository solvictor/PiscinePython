def default_filter(e):
    """Default filtering function

    Args:
        e (Any): element

    Returns:
        Any: the element
    """
    return e


def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    if function is None:
        function = default_filter

    return (e for e in iterable if function(e))

from itertools import accumulate


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    if not sequence:
        return []

    try:
        for i, _sum in enumerate(accumulate(sequence)):
            yield round(_sum / (i+1), 2)

    except StopIteration:
        pass
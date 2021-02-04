import data_manip as dm


def median_seq(sequence):
    """Find the median of an unsorted sequence of real numbers of length n."""

    sequence.sort()
    n = len(sequence)

    # Division with no remainder
    pos = (n - 1) // 2

    # Remainder == 0 (even) => False
    # Remainder == 1 (odd) => True
    if n % 2:
        return sequence[pos]

    return (sequence[pos] + sequence[pos + 1]) / 2


dm.write_output(
    input_filename="sequence.txt",
    function=median_seq,
    output_filename="out_median.txt"
)

print("Successfully calculated the median.")

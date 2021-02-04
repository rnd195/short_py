import data_manip as dm


def bubble_sort(sequence, order="A"):
    """Sorts a sequence of numbers using the bubble sort algorithm in
    ascending or descending order.
    """
    seq_len = len(sequence)
    runs = 0

    # Always true for a non-trivial case
    while seq_len > 1:
        switch = False
        for i in range(seq_len - runs - 1):
            if sequence[i] > sequence[i + 1]:
                sequence[i], sequence[i + 1] = sequence[i + 1], sequence[i]
                switch = True
        runs += 1
        if switch is False:
            break

    if order != "A":
        sequence.reverse()

    return sequence


print("Do you want to sort the sequence in ascending or descending order?")
# The prompt is repeated until the user chooses A/D (or a/d)
while True:
    asc_desc = input("\nType A for ascending or D for descending order: ")
    asc_desc = asc_desc.upper()

    if asc_desc not in ("A", "D"):
        print("\nWrong input.")
        continue
    break

# Create an anonymous argument x using the lambda function to pass "order"
dm.write_output(
    input_filename="sequence.txt",
    function=lambda x: bubble_sort(x, asc_desc),
    output_filename="sorted_sequence_bbl.txt"
)

print("Successfully sorted the sequence.")

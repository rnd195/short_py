import data_manip as dm


def insertion_sort(sequence, order="A"):
    """Sorts a sequence using the iterative insertion sort algorithm in
    ascending or descending order.
    """

    for index in range(1, len(sequence)):
        # Use different indices in each loop for clarity
        pos = index

        while sequence[pos - 1] > sequence[pos] and pos > 0:
            sequence[pos - 1], sequence[pos] = sequence[pos], sequence[pos - 1]
            pos -= 1

    # User selects ascending / descending order
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
    function=lambda x: insertion_sort(x, asc_desc),
    output_filename="sorted_sequence_ins.txt"
)

print("Successfully sorted the sequence.")

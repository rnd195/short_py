from sys import exit


def load_sequence(filename):
    """Loads a sequence of numbers from a text file, where each number is
    separated by a line break."""

    try:
        with open(filename, "r", encoding="UTF-8") as f:
            txtfile = f.readlines()
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        exit()
    except PermissionError:
        print(f"The program does not have access to {filename}.",)
        exit()

    # Save each line as an item in a list without line breaks
    stripped = [line.strip() for line in txtfile]
    try:
        if len(stripped) == 0:
            print(f"The file {filename} is empty.")
            exit()
        # Convert strings into floats
        seq = list(map(float, stripped))

    except ValueError:
        print(
            f"The file {filename} contains non-numerical values.\n"
            "Make sure that each number is on its own line "
            "and uses decimal points instead of commas."
        )
        exit()

    return seq


def write_output(input_filename, function, output_filename="output.txt"):
    """Applies a specified function to the input text file and writes the
    output of the function into a new (text) file."""

    # In this case, the output is either a single (float) value or a list
    output = function(load_sequence(input_filename))

    with open(output_filename, "w", encoding="UTF-8") as out:
        if type(output) == list:
            # Each item in a list is separated by a line break
            return print(*output, sep="\n", file=out)

        return out.write(str(output))

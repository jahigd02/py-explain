# fileLines is a list of tuples: the first element in a tuple is the line string, and the second element is a list of
# all tokens from the line.
fileLines = []

# Pretty print
def pp(line_number, line_str, message):
    print(f"{line_number} | \"{line_str}\" -> ")
    print(f"\t{message}\n")


def read_file(filepath):
    with open(filepath) as file:
        for line in file:
            line = line.replace("\n", "")
            fileLines.append((line, [token for token in line.split(" ")]))


def import_statement(line_split):
    if line_split[0] == "import":
        return f"Imports the {line_split[1]} module."
    elif line_split[0] == "from":
        return f"Imports the {line_split[3]} section from the {line_split[1]} module."

method_dict = {
    'import_statement': import_statement,
}

def analyze(line_split):
    if line_split[0] == "import" or line_split[0] == "from":
        return method_dict["import_statement"](line_split)


def parseInstructions(fileLines):
    for line_number, line_tup in enumerate(fileLines):
        line_str = line_tup[0]
        line_split = line_tup[1]

        if len(line_str.strip()) == 0:
            pp(line_number, "", "Empty line.")
        else:
            message = analyze(line_split)
            pp(line_number, line_str, message)

read_file("dummy-files/dummy1.py")
parseInstructions(fileLines)
def parse_input(file_num, delimiter, sample=False):
    if sample:
        filename = f"input/input{file_num}_sample.txt"
    else:
        filename = f"input/input{file_num}.txt"
    file = open(filename, "r")
    input_text = file.read()
    return input_text.split(delimiter)
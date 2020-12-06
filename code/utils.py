def parse_input(file_num, delimiter):
    file = open(f"input/input{file_num}.txt", "r")
    input_text = file.read()
    return input_text.split(delimiter)
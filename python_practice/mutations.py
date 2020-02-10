def mutate_string(string, position, character):
    new_string = list(string)
    new_string[position] = character
    string = "".join(new_string)
    return string

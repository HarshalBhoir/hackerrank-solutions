def split_and_join(line):
    # write your code here
    list_line = line.split()
    result_string = "-".join(list_line)
    return result_string


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
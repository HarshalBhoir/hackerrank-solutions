def count_substring(string, sub_string):
    count_all = 0
    start = 0
    for three in string:
        new_string = (string[start:len(sub_string)+start])
        if sub_string == new_string:
            count_all+=1
        start+=1
    return count_all

def swap_case(s):
    new_s = ""
    for i in s:
        if i == i.upper():
            i = i.lower()
        elif i == i.lower():
            i = i.upper()
        new_s+=i

    return new_s

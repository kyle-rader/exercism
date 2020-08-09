def decode(string):
    string = string or ""
    i = 0
    cnt_str = ""
    output = ""
    while i < len(string):
        while string[i].isdigit():
            cnt_str += string[i]
            i += 1
        output += (int(cnt_str) if len(cnt_str) > 0 else 1) * string[i]
        cnt_str = ""
        i+=1
    return output

def encode(string):
    from itertools import groupby

    string = string or ""
    output = ""

    for char, group in groupby(string):
        cnt = sum([1 for _ in group])
        prefix = str(cnt) if cnt > 1 else ""
        output += prefix + char

    return output

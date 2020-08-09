def decode(string):
    if string is None or string == "":
        return ""

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
    if string is None or string == "":
        return ""

    output = ""
    last = string[0]
    cnt = 1
    for cur in string[1:]:
        if cur != last:
            if cnt > 1:
                output += str(cnt)
            output += last
            last = cur
            cnt = 1
        else:
            cnt += 1

    if cnt > 1:
        output += str(cnt)
    output += string[-1]

    return output

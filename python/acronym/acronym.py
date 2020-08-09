from re import split

def abbreviate(words):
    groups = split(' |_|,|-', words) # Need the | (or) operators to match any of the given chars
    return "".join([w[0].upper() for w in groups if len(w) > 0])

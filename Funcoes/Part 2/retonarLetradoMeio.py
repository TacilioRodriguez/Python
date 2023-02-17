import math

def mid(string_1):
    if len(string_1) % 2 == 0:
        pass
    else:
        string_1 = string_1[math.floor(len(string_1)/2)]
    return string_1


print(mid("abced"))
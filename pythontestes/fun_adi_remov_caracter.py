nome = "test"

def add_dots(msg):
    formatted_msg = ''
    for i, c in enumerate(msg):
        if i < len(msg) - 1:
            formatted_msg += c + '.'
        else:
            formatted_msg += c
    return formatted_msg


def remove_dots(msg):
    return msg.replace('.', '')


def add(s):
    return ".".join(s)

def remove_dots(s):
    return s.replace(".", "")

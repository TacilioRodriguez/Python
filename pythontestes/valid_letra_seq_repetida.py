nome = "hello"

def double_letters(msg):
    for i in range(len(msg) - 1):
        if msg[i] == msg[i + 1]:
            return True
    return False


print(double_letters(nome))

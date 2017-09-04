import random
import string

#激活码中的字符和数字

field = string.ascii_letters+string.digits

def get_code():
    return "".join(random.sample(field,4))

def concatenate(group):
    return "-".join([get_code() for i in range(group)])

def generate(n):
    return [concatenate(4) for i in range(n)]

if __name__ == '__main__':
    print(generate(10))
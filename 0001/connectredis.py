import random
import string
import redis


r = redis.Redis(host='127.0.0.1',port=6379,db=0)


field = string.ascii_letters+string.digits

def get_code():
    return "".join(random.sample(field,4))

def concatenate(group):
    return "-".join([get_code() for i in range(group)])

def generate(n):
    return [concatenate(4) for i in range(n)]

if __name__ == '__main__':
    #print(generate(10))
    for key in generate(10):
        r.lpush('key',key)
        key_list = r.lrange('key',0,-1)
        for key in key_list:
            print(key)



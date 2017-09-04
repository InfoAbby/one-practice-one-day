import random
import string
from sqlalchemy import Column,String,create_engine
import pymysql.cursors
from config import config
#激活码中的字符和数字

db = pymysql.connect("localhost","root","748134","practice")
cursor = db.cursor()






field = string.ascii_letters+string.digits

def get_code():
    return "".join(random.sample(field,4))

def concatenate(group):
    return "-".join([get_code() for i in range(group)])

def generate(n):
    return [concatenate(4) for i in range(n)]

if __name__ == '__main__':
    print(generate(10))
    for g in generate(10):
        sql = "INSERT INTO p0001(code) VALUES ('%s')" % g
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


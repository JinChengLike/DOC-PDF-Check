#coding=utf-8
import MySQLdb
import time


def db_insert(id, name, result, test):
    conn = MySQLdb.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        passwd="jackjin820",
        db="test",
        charset='utf8'
    )
    cursor = conn.cursor()
    datatime = time.strftime('%Y-%m-%d-%T', time.localtime(time.time()))
    id = str(id)
    name = name
    result = result
    test = test
    sql = "INSERT INTO text_check (id, name, result, datatime, test) VALUES (" + id + ", '" + name + "', '" + result + "', '" + datatime + "', '" + test + "');"
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print e
        conn.rollback()
    cursor.close()
    conn.close()


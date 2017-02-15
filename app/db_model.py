#coding=utf-8
import MySQLdb
import time
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def db_insert(id, name, test):
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
    test = test
    sql = "INSERT INTO text_check (id, name, datatime, test) VALUES ("
    sql = sql + id + ", '" + name + "', '" + datatime + "', '" + test + "');"
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print e
        conn.rollback()
    cursor.close()
    conn.close()


def db_select_history():
    conn = MySQLdb.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        passwd="jackjin820",
        db="test",
        charset='utf8'
    )
    cursor = conn.cursor()
    sql = "select * from text_check ORDER BY NO DESC"
    cursor.execute(sql)
    his_num = 3
    rs = cursor.fetchmany(his_num)
    his = []
    i = 0
    while(i < his_num):
        his_str = rs[i][3] + ' ' + rs[i][2] + ' 检查了 ' + rs[i][4]
        his.append(his_str)
        i += 1
    cursor.close()
    conn.close()
    return his

if __name__ == "__main__":
    print db_select_history()

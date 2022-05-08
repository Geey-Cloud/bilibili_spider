import pymysql
import sys


def connect():
    try:
        conn = pymysql.Connect(host='localhost', user='root', passwd='200714', db='userDB', port=3306,
                               charset='utf8')
        cur = conn.cursor()
    except pymysql.err.InternalError as err:
        print("MySQL连接失败:%r" % err)
        sys.exit()
    except pymysql.err.OperationalError as err:
        print("MySQL连接失败:%r" % err)
        sys.exit()
    return [conn, cur]


def execute_sql(sql, data):
    """
    执行sql语句
    @param data: 插入的数据
    @param sql: sql语句
    """
    conn, cur = connect()
    try:
        cur.execute(sql, data)
        conn.commit()
    except:
        print("失败，请检查SQL语句。")

    cur.close()
    conn.close()


def show():
    """
    打印user_info的所有数据
    @rtype: object
    """
    conn, cur = connect()
    try:
        cur.execute('select * from user_info')
        print(cur.fetchall())
    except:
        print("查询列表数据失败")
    cur.close()
    conn.close()


def clear():
    """
    清空表user_info
    @rtype: object
    """
    conn, cur = connect()
    try:
        cur.execute('truncate user_info')
    except:
        print('清空表失败')
    cur.close()
    conn.close()

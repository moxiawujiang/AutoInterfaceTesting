#coding:utf-8
import pymysql


class OperaMysql:
    def __init__(self):
        # 打开数据库连接
        self._db = pymysql.connect("47.95.195.3", "root", "root", "")
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self._db.cursor()

    def get_all_db_data(self,sql):
        # 使用 execute()  方法执行 SQL 查询
        self.cursor.execute(sql)
        # 使用 fetchone() 方法获取单条数据.
        _data = self.cursor.fetchall()
        # 关闭数据库连接
        self._db.close()
        return _data


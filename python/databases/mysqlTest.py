#!/usr/bin/python3
# _*_ coding: utf-8 _*_
 

import pymysql as mysql
# pip install PyMySQL Python3的安装方式
#引入python中的traceback模块，跟踪错误
import traceback
#引入sys模块
import sys
 
class MysqlUtil():
    def __init__(self):
        pass
 
    """
        获取数据库的连接
    """
    def getConnect(self):
        # 参数依次是：IP地址,数据库登录名，数据库密码，数据库实体名称,指定字符集 （未指定可能出现中文乱码）
        db = mysql.connect("localhost","root","go2mysql","python_test",charset='utf8')
        return db
 
    '''
        创建数据表
        tableName：数据表名称
        sql： 数据表的创建sql语句
    '''
    def createTable(self,tableName,sql):
        # 获取数据库连接
        db = self.getConnect()
        #使用cursor() 方法创建一个游标对象 cursor
        cursor =  db.cursor()
        # 使用execute()方法执行sql ，如果表存在则删除
        cursor.execute("drop table if exists %s" %(tableName))
        # 使用预处理语句创建表
        cursor.execute(sql)

        # 关闭数据库连接
        db.close()
    '''
        插入数据库
        sql:插入数据库的sql语句
    '''
    def insertTable(self,sql):
        #获取数据库连接
        db = self.getConnect()
        #使用cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
 
        try:
            #执行sql语句
            cursor.execute(sql)
            #提交到数据库执行
            db.commit()
        except Exception: #方法一：捕获所有异常
            #如果发生异常，则回滚
            print("发生异常",Exception)
            db.rollback()
        finally:
            #最终关闭数据库连接
            db.close()
 
    '''
        查询数据库：单个结果集
        fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
    '''
    def fetchone(self,sql):
        result = "";
        # 获取数据库连接
        db = self.getConnect()
        # 使用cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        try:
            # 执行sql语句
            cursor.execute(sql)
            result = cursor.fetchone()
        except: #方法二：采用traceback模块查看异常
            #输出异常信息
            traceback.print_exc()
            # 如果发生异常，则回滚
            db.rollback()
        finally:
            # 最终关闭数据库连接
            db.close()
        return result
 
    '''
        查询数据库：多个结果集
        fetchall(): 接收全部的返回结果行.
    '''
    def fetchall(self,sql):
        results = "";
        # 获取数据库连接
        db = self.getConnect()
        # 使用cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        try:
            # 执行sql语句
            cursor.execute(sql)
            results = cursor.fetchall()
        except: #方法三：采用sys模块回溯最后的异常
            #输出异常信息
            info = sys.exc_info()
            print( info[0], ":", info[1])
            # 如果发生异常，则回滚

            db.rollback()
        finally:
            # 最终关闭数据库连接
            db.close()
        return results
 
    '''
        删除结果集
    '''
    def delete(self,sql):
        # 获取数据库连接
        db = self.getConnect()
        # 使用cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        try:
            # 执行sql语句
            cursor.execute(sql)
            db.commit()
        except: #如果你还想把这些异常保存到一个日志文件中，来分析这些异常
            #将错误日志输入到目录文件中
            f = open("c:log.txt", 'a')
            traceback.print_exc(file=f)
            f.flush()
            f.close()
            # 如果发生异常，则回滚
            db.rollback()
        finally:
            # 最终关闭数据库连接

            db.close()
 
    '''
        更新结果集
    '''
    def update(self,sql):
        # 获取数据库连接
        db = self.getConnect()
        # 使用cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        try:
            # 执行sql语句
            cursor.execute(sql)
            db.commit()
        except:
            # 如果发生异常，则回滚
            db.rollback()
        finally:
            # 最终关闭数据库连接
            db.close()
 
 
 
 
app = MysqlUtil()
#======================创建表结构==============================
#表名称
tableName = "user"
#见表语句
tableSql = """
    CREATE  table user(
        id bigint(20) NOT NULL AUTO_INCREMENT,
        name varchar(50) NOT NULL,
        sex varchar(2) NOT NULL,
        age int,
        PRIMARY KEY (`id`)
    )
"""
#调用创建表语句
#app.createTable(tableName,tableSql)
#====================================================
 
#=======================插入数据库=============================
 
insertSql = "INSERT INTO user(name,sex,age) \
       VALUES ('%s', '%s', '%d')" % \
       ('jack', '女', 18)
app.insertTable(insertSql)
 
#=======================查询单个数据库=============================
 
fetchoneSql = "SELECT * FROM user  WHERE id = '%d'" % (1)
user = app.fetchone(fetchoneSql)
print(user)
 
#=======================查询多个数据库=============================
 
fetchallSql = "SELECT * FROM user  WHERE id > '%d'" % (0)
users = app.fetchall(fetchallSql)
print(users)

 
#=======================更新数据库=============================
 
updateSql = "update  user  set age = age + 1 ,sex = '%s' where id = '%d'" % ('未知',1)
app.update(updateSql)
 
 
#=======================删除数据库=============================
delSql = "delete from user where id = '%d'" % (1)
app.delete(delSql)
fetchoneSql = "SELECT * FROM user  WHERE id = '%d'" % (1)
user = app.fetchone(fetchoneSql)
print(user)


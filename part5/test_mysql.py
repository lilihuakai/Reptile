import pymysql

id = '20120001'
user ='Bob'
age = 20
data = {
    'id': '20120005',
    'name':'Bob',
    'age': 20
}

db = pymysql.connect(host='localhost', user='root', password='123654', port=3306, db='spiders')
cursor = db.cursor()


# 查询数据
tabel = 'students'
sql = "SELECT * FROM {tabel} WHERE age >= 20".format(tabel=tabel)
try:
    cursor.execute(sql)
    print("Count:", cursor.rowcount)
    one = cursor.fetchone()
    print("One:", one)
    while one:
        one = cursor.fetchone()
        print("One:", one)
        pass
    # results = cursor.fetchall()
    # print("Results:", results)
    # print("Results Type:", type(results))
    # for row in results:
    #     print(row)
except Exception as e:
    print('Error')
    db.rollback()


# 删除数据
# tabel = 'students'
# condition = 'age > 20'

# sql = 'DELETE FROM {tabel} WHERE {condition}'.format(tabel=tabel, condition=condition)
# try:
#     if cursor.execute(sql):
#         print('Successfu')
#         db.commit()
# except Exception as e:
#     print('Failed')
#     db.rollback()


# 更新数据
# tabel = 'students'
# keys = ', '.join(data.keys())
# values = ', '.join(['%s'] * len(data))

# sql = "INSERT INTO {tabel}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE".format(tabel=tabel, keys=keys, values=values)
# update = ','.join([" {key} = %s".format(key=key) for key in data])
# sql += update
# # sql = "UPDATE students SET age = %s WHERE name = %s"
# try:
#     if cursor.execute(sql, tuple(data.values()) * 2):
#         print('Successfu')
#         db.commit()
#     # cursor.execute(sql, (25, 'Bob'))
#     # db.commit()
# except Exception as e:
#     print('Failed')
#     db.rollback()


# 插入数据
# tabel = 'students'
# keys = ', '.join(data.keys())
# values = ', '.join(['%s'] * len(data))

# sql = "INSERT INTO {tabel}({keys}) VALUES ({values})".format(tabel=tabel, keys=keys, values=values)
# # sql = "INSERT INTO students(id, name, age) values(%s, %s, %s)"
# try:
#     if cursor.execute(sql, tuple(data.values())):
#         print('Successfu')
#         db.commit()
#     # cursor.execute(sql, (id, user, age))
#     # db.commit()
# except Exception as e:
#     print('Failed')
#     db.rollback()


# 创建表
# sql = "CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, \
#         age INT NOT NULL, PRIMARY KEY (id))"
# cursor.execute(sql)


# 创建数据库
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version:', data)
# # cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')
cursor.close()

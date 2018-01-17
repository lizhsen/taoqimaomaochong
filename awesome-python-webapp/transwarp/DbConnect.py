# coding=utf-8


import mysql.connector

conn = mysql.connector.connect(host='localhost',
                               port=3306,
                               user='root',
                               passwd='817924',
                               db='test',
                               )
cur = conn.cursor(cursor_class=mysql.connector.cursor.MySQLCursorDict)

cur.execute("insert into student values('4','Tommy','3 year 2 class','9')")
cur.execute("update student set class='3 year 1 class' where name = 'Tommy'")
query=("select * from student")
cur.execute(query)
columns=cur.column_names

 #取出全部数据
result=cur.fetchall()
print '数据表字段名称：{0}'.format(columns)
print '查询结果：{0}'.format(result)



cur.close()
conn.commit()
conn.close()

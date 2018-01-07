# coding=utf-8


import mysql.connector

conn = mysql.connector.connect(host='localhost',
                               port=3306,
                               user='root',
                               passwd='lee817924',
                               db='test',
                               )
cur = conn.cursor()
cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")
cur.execute("insert into student values('2','Tom','3 year 2 class','9')")
cur.execute("update student set class='3 year 1 class' where name = 'Tom'")
cur.execute("delete from student where age='9'")

cur.close()
conn.commit()
conn.close()

#!/usr/bin/python3
# _*_ coding: utf-8 _*_
 
import sqlite3

conn = sqlite3.connect("spider.db");

if conn:
	print("sqlite connect success");
else:
	print("sqlite connection error")

c = conn.cursor()
res = '';
try:
	res = c.execute('''CREATE table company
			(ID INT primary key not null,
			name text not null,
			age int not null,
			address char(50),
			salary	real);''');
except:
	print("create databases error");
else:
	print("create datebases success");

try:
	c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
	      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

	c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
	      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

	c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
	      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

	c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
	      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
except:
	print("insert error")
else:
	print("insert success");


try:
	cursor = c.execute("select id,name,address,salary from company")
	for row in cursor:
		print("ID = %s"%row[0])
		print("name = %s"%row[1])
		print("address = %s"%row[2])
		print("salary = %s"%row[3])
except:
	print("db select execute error")
else:
	print("db select execute success")

conn.commit()
conn.close()

#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="database_name")

# you must create a Cursor object. It will let you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM sm_products")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row[0]

db.close()
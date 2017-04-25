import MySQLdb
from contextlib import closing

db  = MySQLdb.connect("127.0.0.1","root","root","database_name", port=3306)

cur = db.cursor()
cur.execute("SELECT name, price FROM sm_products")

for (name, price) in cur:
  print "Product name = %s, Product price = %s" % (name, price)
  
  #Writing it into csv file
  with open('teste.csv', 'a') as file:
    file.write('%s;%s\n' % (name, price))

db.close()

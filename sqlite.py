import sqlite3

connection=sqlite3.connect('student.db')

cursor=connection.cursor()  #responsible for going through all the  records

table_info= """ Create table student (name varchar(15),class varchar(15), section varchar (5))"""

cursor.execute(table_info)

cursor.execute("""Insert into student (name,class,section) values ('vaibhav' ,'Data Science' , 'A'),
              ('Rob' ,'Data Science' , 'B') ,
               ('Ilia' ,'MERN' , 'C'),
               ('Jon' ,'ML' , 'A') ,
               ('Dricus' ,'Data Science' , 'B')""")


print('the records has been inserted')
data=cursor.execute('Select * from student')

for row in data:
    print(row)


connection.commit()
connection.close()
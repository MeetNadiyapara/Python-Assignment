import sqlite3

try:
    database=sqlite3.connect("firstdatabadse.db")
    print("Database Created.....")

except Exception as  error:
    print(error)
 
table="create table website(id int primary key,username text,password text,contact int)"
try:
    database.execute(table)
    print("Table Created....")

except Exception as error:
    print(error)
insert="insert into website values(1,'m','465sxh',79846320),(2,'met','465sh',7984651320),(3,'met','465',51320),(4,'meet','465h',79846320)"
try:
    database.execute(insert)
    database.commit()
    print("Value Added....")

except Exception as error:
    print(error)

update="update website set contact=1324657980 where id=1"
try:
    database.execute(update)
    database.commit()
    print("Value Updated....")

except Exception as error:
    print(error)

delete="delete from website where id=4"
try:
    database.execute(delete)
    database.commit()
    print("Value Deleted.....")

except Exception as error:
    print(error)

select="select * from website"
cursor=database.cursor()
try:

    cursor.execute(select)
    sotre=cursor.fetchall()
    #sotre=cursor.fetchone()
    #sotre=cursor.fetchmany(2)
    #database.commit()
    for i in sotre:
        print(i[1])

except Exception as error:
    print(error)
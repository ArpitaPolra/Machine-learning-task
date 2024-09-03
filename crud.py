import mysql.connector as c
con=c.connect(host="localhost",user="root",password="root",database="biawork")
cursor=con.cursor()

# courser.execute("create table tblcust(cid int primary key,cname varchar(30),quantity int,price int)")
# con.close()

# insert data
while True:
    cid=int(input("Enter Customer Id:"))
    cname=input("Enter Customer Name:")
    quantity=int(input("Enter Quntity:"))
    price=int(input("Enter Price:"))
    query="insert into tblcust values({},'{}',{},{})" .format(cid,cname,quantity,price)
    cursor.execute(query)
    con.commit()
    print("Data Inserted Successfully..")
    x=int(input("1->Enter more\n2->Exit\nEnter choice:"))
    if x==2:
        break 

# update data
cid=int(input("Enter Customer Id:"))
quantity=int(input("Enter Quntity:"))
query="update tblcust set quantity={} where cid={}".format(cid,quantity)
cursor.execute(query)
con.commit()
if cursor.rowcount>0:
    print("Data Updated Successfully..")
else:
    print("No Data Found.")


# delete data
cid=int(input("Enter Customer Id:"))
query="delete from tblcust where cid={}".format(cid)
cursor.execute(query)
con.commit()
if cursor.rowcount>0:
    print("Deletion successfull..")
else:
    print("Customer id not Found")

# read data
cursor.execute("select *from tblcust")
record=cursor.fetchall()
for i in record:
    print(i)
print("Total number of records=",cursor.rowcount)
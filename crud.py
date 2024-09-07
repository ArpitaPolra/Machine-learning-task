import mysql.connector as c
con=c.connect(host="localhost",user="root",password="root",database="biawork")
cursor=con.cursor()

# cursor.execute("create table tblcust(cid int primary key,cname varchar(30),quantity int,price int)")
# con.close()

# insert data
def insert_data():
    
    while True:
        cid=int(input("Enter Customer Id:"))
        

        cursor.execute("SELECT COUNT(*) FROM tblcust WHERE cid = %s", (cid,))
        row_count = cursor.fetchone()[0]

        if row_count > 0:
            print("Record already exists.")
        else:
            # cid=int(input("Enter Customer Id:")
            cname=input("Enter Customer Name:")
            quantity=int(input("Enter Quantity:"))
            price=int(input("Enter Price:"))
            query="insert into tblcust values({},'{}',{},{})" .format(cid,cname,quantity,price)
            cursor.execute(query)
            con.commit()
            print("Data Inserted Successfully..")

        x = int(input("1->more data\n2->exit\n Enter your choice:"))
        if x == 2:
            print("Perform next operation")
            break
        else:
            print("Enter data:")

    


# update data
def update_data():
    cid=int(input("Enter Customer Id:"))
    quantity=int(input("Enter Quntity:"))
    query="update tblcust set quantity={} where cid={}".format(quantity,cid)
    cursor.execute(query)
    con.commit()
    if cursor.rowcount>0:
        print("Data Updated Successfully..")
    else:
        print("No Data Found.")




# delete data
def delete_data():
    cid=int(input("Enter Customer Id:"))
    query="delete from tblcust where cid={}".format(cid)
    cursor.execute(query)
    con.commit()
    if cursor.rowcount>0:
        print("Deletion successfull..")
    else:
        print("Customer id not Found")
    


# read data
def read_data():
    cursor.execute("select *from tblcust")
    record=cursor.fetchall()
    for i in record:
         print(i)
    print("Total number of records=",cursor.rowcount)
    


while True:
    print("\nOptions:")
    print("1. Insert Data")
    print("2. Read Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        insert_data()
    elif choice == '2':
        read_data()
    elif choice == '3':
        update_data()
    elif choice == '4':
        delete_data()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
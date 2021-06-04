def show_product(conn,stmt):
    #conn=pymysql.connect(host="localhost", user="root", passwd="shree", db="shopping")
    #stmt=conn.cursor()
    p=int(input("Enter Product ID: "))
    stmt.execute ("SELECT * from products where prod_id=%d" %p)
    row=stmt.fetchone()
    if row==None:
        print ("Sorry no Product found with ID %d" %p)
    else:
        print ("Information of the product with ID %d is as follows:" %p)
        print ("Product ID: %d, Product Name: %s, Quantity: %d, Price: %f" %(row[0], row[1], row[2], row[3]))
    #stmt.close()
    #conn.close()

def show_products(conn,stmt):   
    #conn=pymysql.connect(host="localhost", user="root", passwd="shree", db="shopping")
    #stmt=conn.cursor()
    try:
        stmt.execute ("SELECT * from products")
        print ("Product ID\tProduct Name\tQuantity\tPrice")
        rows=stmt.fetchall()
        for row in rows:
            print ("%d\t\t%s\t\t%d\t\t%f"  %(row[0], row[1], row[2], row[3]))
    except pymysql.Error:
        print ("Error in fetching rows")
        sys.exit(1)    
    #stmt.close()
    #conn.close()


def insert_products(conn,stmt):
    
    #conn=pymysql.connect(host="localhost", user="root", passwd="shree", db="shopping")
    #stmt=conn.cursor()
    k="YES"
    while k.upper()=="YES" :
        pid=int(input("Enter Product ID: ")) # 100, 200
        pname=input("Enter Product Name: ")  # nuts, bolts
        qty=int(input("Enter Quantity: "))   # 200, 300
        price=float(input("Enter Price: "))  # 10.48 14.13
        try:
            stmt.execute("""
            INSERT INTO products (prod_id, prod_name, quantity, price)
            VALUES (%d, '%s', %d, %f)
            """  %(pid, pname, qty, price))
            conn.commit()
            k=input("Want to insert more products, yes/no: ") # YeS,yes,YEs,NO,nO,no
        except:
            conn.rollback()
            sys.exit(1)
    #stmt.close()
    #conn.close()

    
def delete_products(conn,stmt):
    #conn=pymysql.connect(host="localhost", user="root", passwd="shree", db="shopping")
    #stmt=conn.cursor()
    p=int(input("Enter Product ID: "))
    stmt.execute ("SELECT * from products where prod_id=%d" %p)
    row=stmt.fetchone()
    if row==None:
        print ("Sorry no Product found with ID %d" %p)
    else:
        print ("Information of the product with ID %d is as follows:" %p)
        print ("Product ID: %d, Product Name: %s, Quantity: %d, Price: %f" %(row[0], row[1], row[2], row[3]))
        k=input("Confirm, Want to delete this record, yes/no: ")
        if k.upper()=="YES":
            stmt.execute ("DELETE from products where prod_id=%d" %p)
            print("Product with ID %d is deleted" %p)
    #stmt.close()
    conn.commit()
    #conn.close()



    
def update_products(conn,stmt):
    
    #conn=pymysql.connect(host="localhost", user="root", passwd="shree", db="shopping")
    #stmt=conn.cursor()
    p=int(input("Enter Product ID: "))
    stmt.execute ("SELECT * from products where prod_id=%d" %p)
    row=stmt.fetchone()
    if row==None:
        print ("Sorry no Product found with ID %d" %p)
    else:
        print ("Information of the product with ID %d is as follows:" %p)
        print ("Product ID: %d, Product Name: %s, Quantity: %d, Price: %f" %(row[0], row[1], row[2], row[3]))
        pname=input("Enter new Product Name: ")
        qty=int(input("Enter new Quantity: "))
        price=float(input("Enter new Price: "))
        stmt.execute ("UPDATE products set prod_name='%s', quantity=%d, price=%f where prod_id=%d" %(pname, qty, price,p))
        print("Information of the Product with ID %d is updated." %p)
        #stmt.close()
        conn.commit()
        #conn.close()

def mysql_connect():
    conn=pymysql.connect(host="localhost", user="root", passwd="shree", db="shopping")
    stmt=conn.cursor()
    return [conn,stmt]

def mysql_disconnect(conn,stmt):
    stmt.close()
    conn.close()
    

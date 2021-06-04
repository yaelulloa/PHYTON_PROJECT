#!/usr/bin/env python3
import sys
import pymysql

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
    

def display_menu():
    print("The Product Table Maintenance ")
    print()
    print("COMMAND MENU")
    print("product - show a product info")
    print("show   - Show all products info")
    print("add    - insert a Product")
    print("update - update a Product")
    print("del    - Delete a product")
    print("exit   - Exit program")

def main():
    conn_list = mysql_connect()
    conn = conn_list[0]
    stmt = conn_list[1]
    
    display_menu()
    
    while True:
        print()
        command = input("Command: ").lower()
        if command == "show":
            show_products(conn,stmt)
        if command == "product":
            show_product(conn,stmt)
        elif command == "add":
            insert_products(conn,stmt)
        elif command == "update":
            update_products(conn,stmt)
        elif command == "del":
            delete_products(conn,stmt)
        elif command == "exit":
            mysql_disconnect(conn,stmt)
            print("Bye!")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()

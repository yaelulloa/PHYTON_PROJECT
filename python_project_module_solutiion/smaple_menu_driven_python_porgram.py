#!/usr/bin/env python3
import sys
import pymysql
from product_module import *

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

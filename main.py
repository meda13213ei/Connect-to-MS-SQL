import datetime
from prettytable import PrettyTable
import pypyodbc as odbc


def connecttodb(connection_strng):
    start_time = datetime.datetime.now()
    conn = odbc.connect(connection_strng)
    end_time = datetime.datetime.now()
    connection_time = end_time - start_time
    if conn.connected:
        print(f"Connected! ({connection_time} seconds)")
    elif conn.connection_timeout:
        print("Connection timed out! Please try again")
        return False


def queryexecution(connection_strng):
    x = PrettyTable()

    querymode = True
    while querymode:
        query = input("Enter the SQL Query you would like to execute:")
        if query != "Change DB":
            st = datetime.datetime.now()
            conn = odbc.connect(connection_strng)
            cursor = conn.cursor()
            cursor.execute(f"{query}")
            row = cursor.fetchone()
            while row:
                x.add_row([row[0], row[1], row[2], row[4], row[5]])
                row = cursor.fetchone()
            print(x)
            conn.close()
            print("")
            et = datetime.datetime.now()
            timetaken = et - st
            print(f"Connection_closed! {timetaken} seconds taken for Query")
            querymode = True
        if query == "Change DB":
            querymode = False


enter = True
while enter:
    driver_name = 'SQL SERVER'
    server_name = 'PC-35417'
    dbname = input("Enter the database you want to connect: ")
    database_name = dbname
    connection_string = f"DRIVER={{{driver_name}}};SERVER={server_name};DATABASE={database_name};Trust_Connection=yes;"
    connecttodb(connection_string)

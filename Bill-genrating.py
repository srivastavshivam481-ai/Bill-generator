import time as t
import mysql.connector


def shop2():
    con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pushkar@8840", #enter your password
    database="kishu1" #enter your database name
    )
    cur = con.cursor()
    Order_id=int(input("enter the order id: "))
    Product_Name=input("enter the product name: ")
    P_Price=float(input("enter the P_Price: "))
    Quantity=int(input("enter the Quantity: "))
    Amount=P_Price*Quantity
    sql = "INSERT INTO shop2 (Order_id,Product_name,P_Price,Quantity,Amount) VALUES (%s,%s,%s,%s,%s)"
    values = (Order_id,Product_Name,P_Price,Quantity,Amount)
    cur.execute(sql,values)
    con.commit()
    print("✅ Data successfully inserted into Products table!")

    amount=P_Price*Quantity
    name=str(Order_id)
    time=t.ctime()
    f = open(name + ".txt", "w")
    data=f.write(f'''
    Time: {time}
    --------------------
    order id: {Order_id}
    product name: {Product_Name}
    Quantity: {Quantity}
    ---------------------
    final amount: {amount}''')
    f.close()
    cur.close()
    con.close()
    
shop2()
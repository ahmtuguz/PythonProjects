import mysql.connector

def insertProduct(name,price,imageUrl,description):
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="node-app"
)
    cursor=connection.cursor()
    sql="INSERT INTO products(name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"
    values=(name,price,imageUrl,description)

    cursor.execute(sql,values)
    try:
         connection.commit()
         print(f"{cursor.rowcount} tane kayıt eklendi.")
         print(f"son eklenen kaydın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
         print("hata: ",err)
    finally:
         connection.close()
         print("database kapatıldı")        

def insertProducts(list):
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="node-app"
)
    cursor=connection.cursor()
    sql="INSERT INTO products(name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"
    values=(list)

    cursor.executemany(sql,values)
    try:
         connection.commit()
         print(f"{cursor.rowcount} tane kayıt eklendi.")
         print(f"son eklenen kaydın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
         print("hata: ",err)
    finally:
         connection.close()
         print("database kapatıldı") 

list=[]
while True:
    name=input("ürünün ismini giriniz:")
    price=float(input("ürünün fiyatını giriniz:"))
    imageUrl=input("ürünün resmini giriniz:")
    description=input("ürünün tanımını giriniz:")

    list.append((name,price,imageUrl,description))
    result=input("devam etmek istiyor musunuz (e/h)")
    if (result=="h"):
        print("kaydınız oluşturuluyor...")
        print(list)
        insertProducts(list)
        break

def getProducts():
     connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="node-app"
)
    cursor=connection.cursor()
    cursor.execute("SELECT *FROM products")
    result=cursor.fetchall()
    #result=cursor.fetchone()

    for x in result:
         print(x)
getProducts()
#insertProduct(name,price,imageUrl,description)




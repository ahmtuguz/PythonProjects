import mysql.connector
from datetime import datetime
from connection import connection

class Student:
    connection=connection
    cursor=connection.cursor()

    def __init__(self,studentNumber,name,surname,birthday,gender):
        self.studentNumber=studentNumber
        self.name=name
        self.surname=surname
        self.birthday=birthday
        self.gender=gender
    def saveStudent(self):
        sql="INSERT INTO school(studentNumber,name,surname,birthday,gender) VALUES (%s,%s,%s,%s,%s)"
        value=(self.studentNumber,self.name,self.surname,self.birthday,self.gender)
        Student.cursor.execute(sql,value)
        try:
         connection.commit()
         print(f"{Student.cursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
         print("hata: ",err)
        finally:
         connection.close()
         print("database kapatıldı")
    
    @staticmethod
    def saveStudents(students):
        sql="INSERT INTO school(studentNumber,name,surname,birthday,gender) VALUES (%s,%s,%s,%s,%s)"
        values=(students)
        Student.cursor.executemany(sql,values)
        try:
         connection.commit()
         print(f"{Student.cursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
         print("hata: ",err)
        finally:
         connection.close()
         print("database kapatıldı")    

    def getProducts():
        Student.cursor.execute("select count(*) from school")
        result=Student.cursor.fetchone()
        #for i in result:
        print(result)    

    def getProductsById(id):
        sql="SELECT * FROM school where id='%s'"
        param=(id,)
        Student.cursor.execute(sql,param)
        result=Student.cursor.fetchone()
        print(result)

    def getProductsInfo():
        sql="SELECT count(*) FROM school"
        sql="SELECT avg(studentNumber) FROM school"
        sql="SELECT sum(studentNumber) FROM school"
        sql="SELECT min(studentNumber) FROM school"
        Student.cursor.execute(sql)
        result=Student.cursor.fetchone()
        print(result)

    def updateProducts(id,name,surname):
        sql="update school set name=%s,surname=%s where id=%s"
        value=(name,surname,id)
        Student.cursor.execute(sql,value)
        try:
         connection.commit()
         print(f"{Student.cursor.rowcount} tane kayıt güncellendi.")
        except mysql.connector.Error as err:
         print("hata: ",err)
        finally:
         connection.close()
         print("database kapatıldı") 

    def deleteProducts(id):
        sql="delete from school where id=%s"
        value=(id,)
        Student.cursor.execute(sql,value)
        try:
         connection.commit()
         print(f"{Student.cursor.rowcount} tane kayıt silindi.")
        except mysql.connector.Error as err:
         print("hata: ",err)
        finally:
         connection.close()
         print("database kapatıldı")        
#ahmet=Student("901","can","uguz",datetime(2001,2,27),"E")
#ahmet.saveStudent()
# öğrenciler=[
#      ("201","ahmet","uguz",datetime(2001,2,27),"E"),
#      ("202","deniz","yücel",datetime(2002,7,17),"K"),
#      ("203","fatma","turgut",datetime(2003,5,7),"K"),
#      ("204","mehmet","şahin",datetime(2000,2,5),"E")
#  ]


#Student.saveStudents(öğrenciler) 
#Student.getProducts()
#Student.getProductsById(10)
#Student.getProductsInfo()
#Student.updateProducts(5,"mehmet","uguz")
Student.deleteProducts(5)
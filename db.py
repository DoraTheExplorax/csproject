import mysql.connector

class DB:
    def add_users(self, Lname,Fname,Add,Pass,ContactNumber,EmailId):
        conn = mysql.connector.connect(user='root',password='root',host='localhost',port='3306',database='ardinam')
        cursor = conn.cursor()
        query="INSERT INTO Users(LastName,FirstName,Address,Pass,ContactNumber,EmailId) VALUES ('{}','{}','{}','{}','{}','{}')".format(Lname,Fname,Add,Pass,ContactNumber,EmailId)
        cursor.execute(query)
        conn.commit()
    def fetch_data(self,query):
        conn = mysql.connector.connect(user='root',password='root',host='localhost',port='3306',database='ardinam')
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return  results

db=DB()
print(db.fetch_users(EmailId='98shim@gmail.com',Pass='root'))
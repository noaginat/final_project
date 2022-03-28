import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="anywhere1301", database="final_db")

mycursor = mydb.cursor()
mycursor.execute("DROP TABLE my_app_Type")


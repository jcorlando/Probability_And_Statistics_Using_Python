import mysql.connector

f = open("user.txt", "r")
userName = f.read()
f.close()

f = open("password.txt", "r")
passWord = f.read()
f.close()

f = open("database.txt", "r")
dataBase = f.read()
f.close()

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user=userName,
    password=passWord,
    database=dataBase
)

myCursor = mydb.cursor()

myCursor.execute("SELECT *\
                  FROM `<DATABASE>`.`List Order`")

myResult = myCursor.fetchall()

for x in myResult:
    index = x[:][0]
    ticker = x[:][1]
    print(index, ticker)

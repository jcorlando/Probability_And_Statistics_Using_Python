import mysql.connector
import time
import json
import requests
from datetime import timedelta
from datetime import datetime

start_time = time.monotonic()
print("\nStart Time of Program Execution  == ", datetime.now(), "\n")

f = open("user.txt", "r")
userName = f.read()
f.close()

f = open("password.txt", "r")
passWord = f.read()
f.close()

f = open("database.txt", "r")
dataBase = f.read()
f.close()

f = open("alphaVantageApiKey.txt", "r")
apiKey = f.read()
f.close()

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user=userName,
    password=passWord,
    database=dataBase
)

myCursor = mydb.cursor()
myCursor.execute("SELECT * FROM `" + dataBase + "`.`List Order`")
myResult = myCursor.fetchall()


for each in myResult:
    symbol = each[1]
    if symbol == "DOGE":
        url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=' +\
                                                                            symbol + '&market=USD&apikey=' + apiKey
    else:
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=' +\
                                                                            symbol + '&market=USD&apikey=' + apiKey
    receivedResponse = requests.get(url)
    assetDailyData = receivedResponse.json()
    writePath = "./timeSeries/" + symbol + ".json"
    with open(writePath, 'w') as writeFile:
        writeFile.write(json.dumps(assetDailyData))
    writeFile.close()
    print("Finished Gathering & Publishing Data For Asset  => ", symbol)
    time.sleep(14)

end_time = time.monotonic()
print("\nTime taken to execute program  == ", timedelta(seconds=end_time - start_time), "\n")

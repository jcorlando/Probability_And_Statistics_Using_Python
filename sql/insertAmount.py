

f = open("./amountOwned/fractionalAmount.dat", "r")
amountList = f.read()
f.close()
amountList = amountList.split("\n")

# Insert This Into
for amount in amountList:
    amountFloat = float(amount)

import gspread
import random
import time

sa = gspread.service_account(filename = r"C:\Users\User\Desktop\key1.json")

sh = sa.open("data")

wks = sh.worksheet("Sheet1")

print(wks.acell("A7").value)


while True:
    num = random.randint(0,5)

    wks.update("A3", num)

    time.sleep(5)
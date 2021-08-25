from customer import Customer
import random
import datetime

ATM = Customer(id)
count = 0
while(count < 3):
    userInput = int(input("Masukkan PIN anda:"))
    if userInput == ATM.get_custPin:
        print("Berhasil login")
        break
    count +=1
    if count == 3:
        print("Gagal login, silahkan restart program")
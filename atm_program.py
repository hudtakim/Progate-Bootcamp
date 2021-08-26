from customer import Customer
import random
import datetime

ATM = Customer(id)
while(True):
    userInput = int(input("Masukkan PIN anda:"))
    trial = 0
    while(trial < 2 and userInput != ATM.get_custPin):
        userInput = int(input("PIN salah, masukkan lagi:"))
        trial +=1
    
    if userInput == ATM.get_custPin:
        print("Berhasil masuk")
        break
    else:
        print("Anda melakukan kesalahan 3 kali, PIN anda terblokir")
        break
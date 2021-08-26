from atm_card import ATMCard
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

    if userInput != ATM.get_custPin:
        print("Anda melakukan kesalahan 3 kali, PIN anda terblokir")
        break
    
    print("Berhasil Masuk!!!")

    while(True):
        
        print("\n--------Selamat Datang di Mesin ATM---------")
        print("1. Cek saldo")
        print("2. Debet")
        print("3. Ganti PIN")
        print("4. Keluar")

        userInput = int(input("Pilih tindakan:"))
        if userInput == 1:
            print("Saldo anda: Rp.", ATM.get_custBalance)
        elif userInput == 2:
            print("Debet dipilih")
        elif userInput == 3:
            print("Ganti PIN dipilih")
        elif userInput == 4:
            print("Keluar dipilih")
        else:
            print("Input Invalid")

        break

    break
    
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
        exit()
    
    print("Berhasil Masuk!!!")

    while(True):
        
        print("\n--------Selamat Datang di Mesin ATM---------")
        print("1. Cek saldo")
        print("2. Debet")
        print("3. Deposit")
        print("4. Ganti PIN")
        print("5. Keluar")

        userInput = int(input("Pilih tindakan:"))
        if userInput == 1:
            print("Saldo anda: Rp.", ATM.get_custBalance)

        elif userInput == 2:
            nominal = int(input("Masukkan nominal debet:"))
            if ATM.custBalance > nominal:
                ATM.withdrawBalance(nominal)
                print("Sisa saldo: Rp.", ATM.get_custBalance)
            else:
                print("Saldo anda tidak mencukupi!")

        elif userInput == 3:
            nominal = int(input("Masukkan nominal deposit:"))
            ATM.depositBalance(nominal)
            print("Saldo anda menjadi: Rp.", ATM.get_custBalance)

        elif userInput == 4:
            verify = int(input("Masukkan PIN saat ini:"))
            trial = 0
            while verify != ATM.get_custPin and trial <2:
                verify = int(input("PIN salah!, coba masukkan lagi:"))
                trial += 1
                
            if verify != ATM.get_custPin:
                print("Anda melakukan kesalahan 3 kali, PIN anda terblokir")
                exit()

            newPin = int(input("Masukkan PIN baru:"))
            verify = int(input("Ulangi PIN baru:"))
            while verify != newPin:
                verify = int(input("PIN tidak cocok, ulangi PIN baru:"))
            
            ATM.updatePIN(newPin)
            print("PIN berhasil diganti")

        elif userInput == 5:
            print("--------Resi Transaksi-------")
            print("No. Rekord: ", random.randint(100000, 1000000))
            print("Tanggal: ", datetime.datetime.now())
            print("Saldo akhir: ", ATM.get_custBalance)
            print("Terima kasih telah menggunakan ATM Kami!")
            exit()

        else:
            print("Input Invalid, silahkan pilih sesuai nomor menu!")

    break
    
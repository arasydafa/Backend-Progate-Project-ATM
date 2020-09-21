import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
    id = int(input("Masukkan PIN Anda : "))123
    trial = 0

    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input("PIN Anda Salah, Silakan Masukkan PIN Yang Benar : "))

        trial += 1
        if trial == 3:
            print("PIN Anda Salah Sebanyak 3x. Terjadi Error. Silahkan Ambil Kartu ATM Anda dan Coba Lagi")
            exit()

    while True:
        print("Selamat Datang di Mesin ATM")
        print("\n1 - Cek Saldo \t 2 - Tarik \t 3 - Setor \t 4 - Ganti Pin \t 5 - Keluar ")
        selectmenu = int(input("\nSilakan Pilih Menu Yang Dibutuhkan : "))

        if selectmenu == 1:
            print("\nSaldo Anda Sekarang : Rp. " + str(atm.checkBalance()) + "\n" )

        elif selectmenu == 2:
            nominal = float(input("Masukkan Nominal Yang Ingin Di Tarik Tunai : "))
            verify_withdraw = input("Konfirmasi : Apakah Anda Akan Melakukan Tarik Tunai Dengan Nominal Tesebut ? Y/N " + str(nominal) + " ")
            if verify_withdraw == "y" or verify_withdray == "Y":
                print("Saldo Awal Anda : Rp. " + str(atm.checkBalance()) + "")
            else:
                break
            if nominal < atm.checkBalance():
                atm.withdrawBalance(nominal)
                print("Transaksi Berhasil!")
                print("Saldo Sisa : Rp. " + str(atm.checkBalance()) + "")
            else:
                print("Maaf. Saldo Anda Tidak Cukup Untuk Melakukan Transaksi!")
                print("Silakan Menambah Saldo")

        elif selectmenu == 3:
            nominal = float(input("Masukkan Nominal Yang Ingin Di Setor Tunai : "))
            verify_deposit = input("Konfirmasi : Apakah Anda Akan Melakukan Setor Tunai Dengan Nominal Tesebut ? Y/N " + str(nominal) + " ")
            if verify_deposit == "y" or verify_deposit == "Y":
                atm.depositBalance(nominal)
                print("Saldo Sisa : Rp." + str(atm.checkBalance()) + "\n" )
            else:
                break

        elif selectmenu == 4:
            verify_pin = int(input("Masukkan PIN Anda : "))
            while verify_pin != int(atm.checkPin()):
                print("PIN Anda Salah, Silakan Masukkan PIN Yang Benar : ")
            updated_pin = int(input("Silakan Masukkan PIN Yang Baru : "))
            print("PIN Anda Berhasil Diganti!")
            verify_newpin = int(input("Masukkan PIN Baru : "))
            if verify_newpin == updated_pin:
                print("PIN Telah Berhasil Diganti!")
            else:
                print("PIN Anda Salah, Silakan Masukkan PIN Yang Benar : ")

        elif selectmenu == 5:
            print("Resi Akan Tercetak Otomatis Saat Anda Keluar. \n Harap Simpan Resi \n Sebagai Bukti Transaksi.")
            print("No. Transaksi : ", random.randint(100000, 1000000))
            print("Tanggal : ", datetime.datetime.now())
            print("Saldo Terakhir : ", atm.checkBalance())
            print("Terima Kasih")
            print("Selamat Beraktivitas")
            exit()

        else:
            print("Terjadi Error. Maaf Menu Tidak Tersedia")
            print("Mohom Pilih Menu Yang Tertera Di Layar")
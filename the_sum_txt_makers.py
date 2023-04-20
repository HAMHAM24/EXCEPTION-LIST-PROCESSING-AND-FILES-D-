def txt_makers(a):
    with open("transaksi.txt", "w", encoding="utf-8") as file:
        file.write("\n|==>-------------------------------- KASIR --------------------------------<==|\n")
        file.write("|==========================| RESTORAN MURAH LANCAR |==========================|\n")
        file.write("|==>-----------------------------------------------------------------------<==|\n")
        file.write(f"|==> Total Harga = Rp. {a}")
        file.write("\n|==>-----------------------------------------------------------------------<==|\n")
        file.write("|==>----------------| Selamat Hari Raya Idul Fitri 1444 H |----------------<==|\n")
        file.write("|==>--------------------| Mohon Maaf Lahir dan Batin |---------------------<==|\n")
        file.write("|=============================================================================|\n")
        file.write("\n\t\t\t\t\t|<>|-- Source Code by.IP492473 --|<>|")
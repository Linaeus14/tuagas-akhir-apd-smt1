#nama program
print(
    ""
    "\n Program Pesanan Katering"
)

#deklarasi
lisadmin = {
    "user" : ["admin1"],
    "pass" : ["1111"]
}
liscostum = [[],[]]
lisidentitas = {
    "nama" : [],
    "no" : []
}
lismenu = {
    "tipe" : [
        "Nasi dengan Ayam goreng",
        "Nasi dengan Ikan Goreng",
        "Mi Goreng dengan Telur Goreng",
    ],
    "harga" : [
        15000,
        15000,
        14000
    ]
}
lispesan = {
    "pesanan" : [],
    "hargap" : [],
    "status" : [],
    "namap" : [],
    "nop" : [],
    "idp" : []
}
lispesancostum = {
    "pesanan" : [],
    "hargap" : [],
    "status" : []
}
counterakuncostumer = 0
countercustompesanan = []

def filterlis(x):
    for length in x:
        for index in x:
            if x.count(index) > 1:
                x.remove(index)
    return x
def daftar_pesanan(x):
    nu = -1
    print(
        ""
    )
    if x == "admin":
        topem = []
        for nama in lispesan["namap"]:
            topem.append(nama)
        topem = filterlis(topem)
        print(
            ""
            "\n DAFTAR PESANAN"
            "\n"
            "\n Total pesanan : " + str(sum(countercustompesanan)) +
            "\n Total pemesan : " + str(len(topem)) +
            "\n "
        )
        for nama in lispesan["namap"]:
            nu += 1
            print(
                f" {nu + 1}.", nama, "(", lispesan["nop"][nu],")", " id " + str(lispesan["idp"][nu]),
                "\n    Pesanan :", lispesan["pesanan"][nu],
                "\n    Harga total :", rp(lispesan["hargap"][nu]),
                "\n    Status : ", lispesan["status"][nu]
            )
    elif x == "costumer":
        print(
            ""
            "\n DAFTAR PESANAN"
        )
        for y in lispesancostum["pesanan"][idd-1]:
            nu += 1
            print(
                f" {nu + 1}.", "Pesanan :", lispesancostum["pesanan"][idd-1][nu],
                "\n    Harga total :", rp(lispesancostum["hargap"][idd-1][nu]),
                "\n    Status : ", lispesancostum["status"][idd-1][nu]
            )
    else:
        print(
            "daftar_pesanan() : argumen salah"
        )
def daftar_menu():
    nu = -1
    print(
        ""
        "\n MENU Katering"
    )
    for menu in lismenu["tipe"]:
        nu += 1
        print(
            f" {nu + 1}.", menu," : " , rp(lismenu["harga"][nu])
        )
def rp(x):
    return "Rp."+str(x)+".00"

#===================================================================================

#menu utama
loopmain = True
while loopmain:
    #Pilih tipe pengguna
    loop1 = True
    while loop1:
        login = str(input(
            " ========================= "
            "\n Masukan Tipe Pengguna"
            "\n 1. Admin"
            "\n 2. Costumer"
            "\n 3. Berhenti"
            "\n (angka saja, misal \"1\")"
            "\n "
            "\n > "
        ))

        #Tipe pengguna admin
        if login == "1":
            print(
                ""
                "\n Admin Login"
            )
            username = input(
                ""
                "\n Username : "
            )
            password = input(
                " Password : "
            )

            #cek username dan password
            if username in lisadmin["user"] and password in lisadmin["pass"]:
                print(
                    ""
                    "\n Telah masuk sebagai admin"
                )
                logintype = "admin"
                loop1 = False
            else:
                print(
                    ""
                    "\n username atau password salah!"
                    "\n"
                )

        #tipe pengguna costumer
        elif login == "2":
            logincostume = input(
                ""
                "\n Masuk sebagai costumer"
                "\n Pilih : "
                "\n 1. Login"
                "\n 2. Buat Akun"
                "\n > "
            )

            if logincostume == "1":
                print(
                ""
                "\n Costumer Login"
                )
                username = input(
                    ""
                    "\n Username : "
                )
                password = input(
                    " Password : "
                )

                #cek username dan password
                if username in liscostum[0] and password in liscostum[1]:
                    idd = liscostum[0].index(username) + 1
                    print(
                        ""
                        f"\n Telah masuk sebagai costumer dengan no id {idd}"
                    )
                    logintype = "costumer"
                    loop1 = False
                else:
                    print(
                        ""
                        "\n username atau password salah!"
                        "\n"
                    )
            
            if logincostume == "2":
                print(
                ""
                "\n Daftar sebagai Costumer"
                )
                nam = ""
                while nam == "":
                    nam = input(
                        ""
                        "\n Nama : "
                    )
                    if nam == "":
                        print(
                            ""
                            "\n Tidak boleh kosong, coba lagi!"
                        )
                nom = ""
                while nom == "":
                    nom = input(
                        " No Hp : +62 "
                    )
                    if nom == "":
                        print(
                            ""
                            "\n Tidak boleh kosong, coba lagi!"
                        )
                username = ""
                while username == "" or username in liscostum[0]:
                    username = input(
                        " Username : "
                    )
                    if username == "":
                        print(
                            ""
                            "\n Tidak boleh kosong, coba lagi!"
                        )
                    elif username in liscostum[0]:
                        print(
                            ""
                            "\n username sudah ada"
                        )
                password = ""
                while password == "":
                    password = input(
                        " Password : "
                    )
                    if password == "":
                        print(
                            ""
                            "\n Tidak boleh kosong, coba lagi!"
                        )
                lisidentitas["nama"].append(nam)
                lisidentitas["no"].append(nom)
                liscostum[0].append(username)
                liscostum[1].append(password)
                lispesancostum["pesanan"].append([])
                lispesancostum["hargap"].append([])
                lispesancostum["status"].append([])
                counterakuncostumer += 1
                print(
                    ""
                    "\n ==Daftar berhasil== "
                    f"\n no id : {counterakuncostumer}"
                )

        elif login == "3":
            logintype = ""
            loopmain = False
            loop1 = False

        else:
            print(
                " Input salah"
            )

#====================================================================
#menu kedua

    #admin
    if logintype == "admin":
        print(
        ""
        "\n Program Pesanan Katering"
        "\n Pengguna Admin"
        )
        loop1 = True
        while loop1:
            menuadmin = str(input(
                ""
                "\n Pilihan"
                "\n 1. Lihat pesanan"
                "\n 2. Ubah status pesanan"
                "\n 3. Lihat menu"
                "\n 4. Tambah menu"
                "\n 5. Ubah menu"
                "\n 6. Kembali"
                "\n (Masukan angka saja, misal \"1\")"
                "\n > "
            ))

            if menuadmin == "1":
                if len(lispesan["pesanan"]) != 0:
                    daftar_pesanan("admin")
                else:
                    print(
                        ""
                        "\n ==Tidak ada pesanan=="
                    )
                    
            elif menuadmin == "2":
                if len(lispesan["pesanan"]) != 0:
                    print(
                        ""
                        "\n Daftar Pesanan"
                    )
                    daftar_pesanan("admin")
                    editstatus = ""
                    while not(type(editstatus) == int):
                        editstatus = input(
                            ""
                            "\n Pilih pesanan di atas untuk di ubah status "
                            "\n (masukan angka saja, misal \"1\")"
                            "\n > "
                        )
                        try:
                           editstatus = int(editstatus)
                        except ValueError:
                            print(
                                "Input salah, coba lagi!"
                            )
                        if editstatus > len(lispesan["pesanan"]) or editstatus <= 0:
                            print(
                                ""
                                "\n Tidak ada pesanan dengan angka urut tersebut"
                            )
                            ubahm = str(ubahm)
                    ubahs = True
                    while ubahs:
                        status = str(input(
                            ""
                            "\n >  " + lispesan["namap"][editstatus-1] + " ( " + lispesan["nop"][editstatus-1] + " ) " + " id " + str(lispesan["idp"][editstatus-1]) +
                            "\n   " + lispesan["pesanan"][editstatus-1] + " dengan status " + lispesan["status"][editstatus-1] +

                            "\n Ubah status menjadi : "
                            "\n 1. Dalam proses pembuatan"
                            "\n 2. Selsai"
                            "\n (NOTE: Setelah di ubah \"Selsai\" tidak dapat di ubah kembali)"
                            "\n > "
                        ))
                        if status == "1":
                            lispesan["status"][editstatus-1] = "Dalam Proses Pembuatan"
                            idda = lispesan["idp"][editstatus-1]
                            lispesancostum["status"][idda - 1][countercustompesanan[idda - 1] - 1] = "Dalam Proses Pemmbuatan"
                            ubahs = False
                            print(
                                ""
                                "\n >  " + lispesan["namap"][editstatus-1] + " ( " + lispesan["nop"][editstatus-1] + " ) " + " id " + str(lispesan["idp"][editstatus-1]) +
                                "\n    " + lispesan["pesanan"][editstatus-1] +
                                "\n    Telah di ubah status menjadi : " + lispesan["status"][editstatus-1]
                            )
                        elif status == "2":
                            lispesan["status"][editstatus-1] = "Selsai"
                            idda = lispesan["idp"][editstatus-1]
                            lispesancostum["status"][idda - 1][countercustompesanan[idda - 1] - 1] = "Selsai"
                            ubahs = False
                            print(
                                ""
                                "\n >  " + lispesan["namap"][editstatus-1] + " ( " + lispesan["nop"][editstatus-1] + " ) " + " id " + str(lispesan["idp"][editstatus-1]) +
                                "\n    " + lispesan["pesanan"][editstatus-1] +
                                "\n    Telah di ubah status menjadi : " + lispesan["status"][editstatus-1]
                            )
                        else:
                            print(
                                "input salah, coba lagi!"
                            )
                else:
                    print(
                        ""
                        "\n ==Daftar Pesanan Kosong=="
                    )

            elif menuadmin == "3":
                daftar_menu()

            elif menuadmin == "4":
                newmenu = input(
                    ""
                    "\n Nama menu yang ingin di tambahkan : "
                    "\n > "
                )
                newmenuh = input(
                    ""
                    "\n >" + str(newmenu) +
                    "\n Harga menu yang di tambahkan : "
                    "\n (misal 50000)"
                    "\n > Rp."
                )
                lismenu["tipe"].append(newmenu)
                lismenu["harga"].append(newmenuh)
                print(
                    ""
                    "\n > " + str(newmenu) + " telah di tambahkan ke menu dengan harga " + rp(newmenuh) 
                )

            elif menuadmin == "5":
                daftar_menu()
                ubahm = ""
                while not(type(ubahm) == int):
                    ubahm = input(
                       ""
                        "\n Pilih menu untuk di ubah :"
                        "\n (angka saja misal \"1\")"
                        "\n > "
                    )
                    try:
                        ubahm = int(ubahm)
                    except ValueError:
                        print(
                            "Input salah, coba lagi!"
                        )
                    if ubahm > len(lismenu["tipe"]) or ubahm <= 0:
                        print(
                            ""
                            "\n Tidak ada pesanan dengan angka urut tersebut"
                        )
                        ubahm = str(ubahm)
                lismenu["tipe"][ubahm-1] = input(
                    ""
                    "\n >" + lismenu["tipe"][ubahm-1] +
                    "\n Ubah menu menjadi : "
                    "\n > "
                )
                lismenu["harga"][ubahm-1] = input(
                    ""
                    "\n > " + str(lismenu["harga"][ubahm-1]) +
                    "\n Ubah harga menjadi : "
                    "\n > "
                )
                print(
                    ""
                    "\n Menu telah di ubah menjadi:"
                    "\n >" + lismenu["tipe"][ubahm-1] + " dengan harga " + lismenu["harga"][ubahm-1]
                )

            elif menuadmin == "6":
                loop1 = False

            else:
                print(
                    "input salah, coba lagi!"
                )

    #===================================================================================================================

    #costumer
    elif logintype == "costumer":
        print(
        ""
        "\n Program Pesanan Katering"
        "\n Pengguna Costumer"
        )
        loop1 = True
        while loop1:
            menucostum = input(
                ""
                "\n Pilihan"
                "\n 1. Buat Pesanan"
                "\n 2. Edit pesanan"
                "\n 3. Hapus pesanan"
                "\n 4. Kembali"
                "\n "
                "\n > "
            )

            if menucostum == "1":
                daftar_menu()
                try :
                    count = countercustompesanan[idd-1]
                except IndexError:
                    count = 0
                pesanan = ""
                while not(type(pesanan) == int):
                    pesanan = input(
                        "\n Pilih pesanan : "
                        "\n (masukan angka saja, misal \"1\")"
                        "\n > "
                    )
                    try:
                        pesanan = int(pesanan)
                    except ValueError:
                        print(
                            "Input salah, coba lagi!"
                        )
                jml = ""
                while not(type(jml) == int):
                    jml = input(
                        ""
                        "\n " + lismenu["tipe"][pesanan-1] +
                        "\n Seberapa banyak :"
                        "\n > "
                    )
                    try:
                        jml = int(jml)
                    except ValueError:
                        print(
                            "Input salah, coba lagi!"
                        )
                pesananb = ""
                hargapb = 0
                pesananb += (" " + lismenu["tipe"][pesanan-1] + " sebanyak " + str(jml) + "\n    |")
                hargapb += lismenu["harga"][pesanan-1] * jml
                tambahan = True
                while tambahan:
                    tambah = input(
                        "\n Pesanan saat ini:"
                        "\n > " + str(pesananb) +
                        "\n    Seharga total :" + rp(str(hargapb)) +
                        "\n Tambah pesanan lagi? : "
                        "\n (masukan \"y\" atau \"t\" saja)"
                        "\n > "
                    )
                    if tambah == "y":
                        daftar_menu()
                        pesanan = ""
                        while not(type(pesanan) == int):
                            pesanan = input(
                                "\n Tambah pesanan : "
                                "\n (masukan angka saja, misal \"1\")"
                                "\n > "
                            )
                            try:
                                pesanan = int(pesanan)
                            except ValueError:
                                print(
                                    "Input salah, coba lagi!"
                                )
                        jml = ""
                        while not(type(jml) == int):
                            jml = input(
                                ""
                                "\n " + lismenu["tipe"][pesanan-1] +
                                "\n Seberapa banyak :"
                                "\n > "
                            )
                            try:
                                jml = int(jml)
                            except ValueError:
                                print(
                                    "Input salah, coba lagi!"
                                )
                        pesananb += (" " + lismenu["tipe"][pesanan-1] + " sebanyak " + str(jml) + "\n    |")
                        hargapb += lismenu["harga"][pesanan-1] * jml
                    elif tambah == "t":
                        print(
                            ""
                            "\n Pesanan telah di buat :"
                            "\n > " + str(pesananb) +
                            "\n    Seharga total :" + rp(str(hargapb))
                        )
                        lispesan["pesanan"].append(pesananb)
                        lispesan["hargap"].append(hargapb)
                        lispesan["status"].append("Dalam Antrian")
                        lispesan["namap"].append(lisidentitas["nama"][idd-1])
                        lispesan["nop"].append(lisidentitas["no"][idd-1])
                        lispesan["idp"].append(idd)
                        
                        lispesancostum["pesanan"][idd-1].append(pesananb)
                        lispesancostum["hargap"][idd-1].append(hargapb)
                        lispesancostum["status"][idd-1].append("Dalam Antrian")

                        count += 1
                        if count == 1:
                            countercustompesanan.append(count)
                        else:
                            countercustompesanan[idd-1] = count

                        tambahan = False
                    else:
                        print(
                            ""
                            "\n Input salah, coba lagi!"
                        )

            if menucostum == "2":
                if len(lispesan["pesanan"]) != 0:
                    daftar_pesanan("costumer")

                    editpesan = ""
                    while not(type(editpesan) == int):
                        editpesan = input(
                            ""
                            "\n Pilih pesanan di atas untuk di edit "
                            "\n (masukan angka saja, misal \"1\")"
                            "\n > "
                        )
                        try:
                            editpesan = int(editpesan)
                        except ValueError:
                            print(
                                "Input salah, coba lagi!"
                            )

                    loop2 = True
                    while loop2:
                        edit = input(
                            ""
                            "\n Pilih yang ingin di edit : "
                            "\n 1. Identitas"
                            "\n 2. Pesanan"
                            "\n (masukan angka saja, misal \"1\")"
                            "\n > "
                        )
                        if edit == "1":
                            loop2 = False
                            identitas = input(
                                "\n Identitas saat ini:"
                                "\n > " + lisidentitas["nama"][editpesan-1] + " (" + lisidentitas["no"][editpesan-1] + " )" +
                                "\n Ubah identitas menjadi : "
                                "\n"
                                "\n Nama : "
                                "\n > "
                            )
                            identitas1 = input(
                                ""
                                "\n No Hp : "
                                "\n > "
                            )
                            lisidentitas["nama"][editpesan-1] = identitas
                            lisidentitas["no"][editpesan-1] = identitas1
                            print(
                                ""
                                "\n Identitas telah di ubah menjadi : "
                                "\n >", lisidentitas["nama"][editpesan-1], "(", lisidentitas["no"][editpesan-1], ")"
                            )
                            

                        elif edit == "2":
                            loop2 = False
                            daftar_menu()
                            pesanan = input(
                                "\n Pesanan saat ini:"
                                "\n >", lispesan["pesanan"][editpesan-1],
                                "\n   Seharga:", lispesan["harga"][editpesan-1],
                                "\n Ubah pesanan menjadi : "
                                "\n (masukan angka saja, misal \"1\")"
                                "\n > "
                            )
                            jml = input(
                                ""
                                "\n Seberapa banyak :"
                                "\n >"
                            )
                            pesananb = ""
                            hargapb = 0
                            pesananb += " ", lismenu["tipe"][pesanan-1], "sebanyak", jml, "|"
                            hargapb += lismenu["tipe"][pesanan-1] * jml
                            lispesan["pesanan"][editpesan-1] = pesananb
                            lispesan["harga"][editpesan-1] = hargapb
                            tambahan = True
                            while tambahan:
                                tambah = input(
                                    "\n Pesanan saat ini:"
                                    "\n >", lispesan["pesanan"][editpesan-1],
                                    "\n   Seharga:", lispesan["harga"][editpesan-1],
                                    "\n tambah pesanan lagi? : "
                                    "\n (masukan \"y\" atau \"t\" saja)"
                                    "\n > "
                                )
                                if tambah == "y":
                                    daftar_menu()
                                    pesanan = input(
                                    "\n Tmbah pesanan : "
                                    "\n (masukan angka saja, misal \"1\")"
                                    "\n > "
                                    )
                                    jml = input(
                                        ""
                                        "\n Seberapa banyak :"
                                        "\n >"
                                    )
                                    pesananb += " ", lismenu["tipe"][pesanan-1], "sebanyak", jml, "|"
                                    hargapb += lismenu["tipe"][pesanan-1] * jml
                                    lispesan["pesanan"][editpesan-1] = pesananb
                                    lispesan["harga"][editpesan-1] = hargapb
                                    lispesancostum["pesanan"][idd-1][editpesan-1] = pesananb
                                    lispesancostum["hargap"][idd-1][editpesan-1] = hargapb
                                elif tambah == "t":
                                    print(
                                        ""
                                        "\n Pesanan telah di ubah menjadi :"
                                        "\n >", lispesan["pesanan"][editpesan-1]
                                    )
                                    tambahan = False
                                else:
                                    print(
                                        ""
                                        "\n Input salah, coba lagi!"
                                    )

                        else:
                            print(
                                ""
                                "\n Input salah, coba lagi!"
                            )
                else:
                    print(
                        ""
                        "\n ==Daftar Pesanan Kosong=="
                    )

            if menucostum == "4":
                loop1 = False
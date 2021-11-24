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
        
def rp(x):
    return "Rp."+str(x)+".00"
    
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
            "\n 0. Berhenti"
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
            loop2 = True
            while loop2:
                logincostume = input(
                    ""
                    "\n Masuk sebagai costumer"
                    "\n Pilih : "
                    "\n 1. Login"
                    "\n 2. Buat Akun"
                    "\n 0. Kembali"
                    "\n "
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
                        loop2 = False
                    else:
                        print(
                            ""
                            "\n username atau password salah!"
                            "\n"
                        )
                
                elif logincostume == "2":
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
                    while nom == "" or not (type(nom) == int):
                        nom = input(
                            " No Hp : +62 "
                        )
                        if nom == "":
                            print(
                                ""
                                "\n Tidak boleh kosong, coba lagi!"
                            )
                        else:
                            try:
                                nom = int(nom)
                            except ValueError:
                                print(
                                    ""
                                    "\n input bukan angka, coba lagi!"
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

                elif logincostume == "0":
                    loop2 = False

                else:
                    print(
                        ""
                        "\n input salah, coba lagi!"
                    )

        elif login == "0":
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
                "\n 6. Hapus menu"
                "\n 0. Kembali"
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

                    editstatus = ""
                    while not(type(editstatus) == int):
                        daftar_pesanan("admin")
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
                                "input bukan angka, coba lagi!"
                            )
                        if editstatus > len(lispesan["pesanan"]) or editstatus <= 0:
                            print(
                                ""
                                "\n Tidak ada pesanan dengan angka urut tersebut"
                            )
                            editstatus = ""
                        elif lispesan["status"][editstatus-1] == "Selsai":
                            print(
                                ""
                                "\n tidak dapat mengubah status pesanan yang sudah selsai!"
                            )
                            editstatus = ""

                    while True:
                        status = str(input(
                            ""
                            "\n >  " + lispesan["namap"][editstatus-1] + " ( " + str(lispesan["nop"][editstatus-1]) + " ) " + " id " + str(lispesan["idp"][editstatus-1]) +
                            "\n   " + lispesan["pesanan"][editstatus-1] + " dengan status " + lispesan["status"][editstatus-1] +

                            "\n Ubah status menjadi : "
                            "\n 1. Dalam Proses Pembuatan"
                            "\n 2. Selsai"
                            "\n (NOTE: Setelah di ubah \"Selsai\" / \"Dalam Proses Pembuatan\" tidak dapat di ubah kembali ke sebelumnya)"
                            "\n > "
                        ))
                        
                        idda = lispesan["idp"][editstatus-1]
                        stindex = lispesancostum["pesanan"][idda-1].index(lispesan["pesanan"][editstatus-1])

                        if status == "1":
                            lispesan["status"][editstatus-1] = "Dalam Proses Pembuatan"
                            lispesancostum["status"][idda - 1][stindex] = "Dalam Proses Pemmbuatan"
                            print(
                                ""
                                "\n >  " + lispesan["namap"][editstatus-1] + " ( " + str(lispesan["nop"][editstatus-1]) + " ) " + " id " + str(lispesan["idp"][editstatus-1]) +
                                "\n    " + lispesan["pesanan"][editstatus-1] +
                                "\n    Telah di ubah status menjadi : " + lispesan["status"][editstatus-1]
                            )
                            break

                        elif status == "2":
                            lispesan["status"][editstatus-1] = "Selsai"
                            lispesancostum["status"][idda - 1][stindex] = "Selsai"
                            print(
                                ""
                                "\n >  " + lispesan["namap"][editstatus-1] + " ( " + str(lispesan["nop"][editstatus-1]) + " ) " + " id " + str(lispesan["idp"][editstatus-1]) +
                                "\n    " + lispesan["pesanan"][editstatus-1] +
                                "\n    Telah di ubah status menjadi : " + lispesan["status"][editstatus-1]
                            )
                            break
                        
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
                if len(lismenu["tipe"]) != 0:
                    daftar_menu()
                else:
                    print(
                        ""
                        "\n ==Daftar Menu Kosong=="
                    )

            elif menuadmin == "4":
                newmenu = input(
                    ""
                    "\n Nama menu yang ingin di tambahkan : "
                    "\n > "
                )
                
                newmenuh = ""
                while not(type(newmenuh) == int):
                    newmenuh = input(
                        ""
                        "\n >" + str(newmenu) +
                        "\n Harga menu yang di tambahkan : "
                        "\n (misal 50000)"
                        "\n > Rp."
                    )
                    try:
                        newmenuh = int(newmenuh)
                    except ValueError:
                        print(
                            ""
                            "\n input bukan angka, coba lagi"
                        )

                lismenu["tipe"].append(newmenu)
                lismenu["harga"].append(newmenuh)
                print(
                    ""
                    "\n > " + str(newmenu) + " telah di tambahkan ke menu dengan harga " + rp(newmenuh) 
                )

            elif menuadmin == "5":
                ubahm = ""
                while not(type(ubahm) == int):
                    daftar_menu()
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
                            "input bukan angka, coba lagi!"
                        )
                    if ubahm > len(lismenu["tipe"]) or ubahm <= 0:
                        print(
                            ""
                            "\n Tidak ada pesanan dengan angka urut tersebut"
                        )
                        ubahm = ""

                lismenu["tipe"][ubahm-1] = input(
                    ""
                    "\n >" + lismenu["tipe"][ubahm-1] +
                    "\n Ubah menu menjadi : "
                    "\n > "
                )
                
                while True:
                    lismenu["harga"][ubahm-1] = input(
                        ""
                        "\n > " + rp(lismenu["harga"][ubahm-1]) +
                        "\n Ubah harga menjadi : "
                        "\n > "
                    )
                    try:
                        lismenu["harga"][ubahm-1] = int(lismenu["harga"][ubahm-1])
                        break
                    except ValueError:
                        print(
                            ""
                            "\n input bukan angka, coba lagi!"
                        )
                print(
                    ""
                    "\n Menu telah di ubah menjadi:"
                    "\n >" + lismenu["tipe"][ubahm-1] + " dengan harga " + rp(lismenu["harga"][ubahm-1])
                )

            elif menuadmin == "6":
                hapm = ""
                while not(type(hapm) == int):
                    daftar_menu()
                    hapm = input(
                       ""
                        "\n Pilih menu untuk di hapus :"
                        "\n (angka saja misal \"1\")"
                        "\n > "
                    )
                    try:
                        hapm = int(hapm)
                    except ValueError:
                        print(
                            "input bukan angka, coba lagi!"
                        )
                    if hapm > len(lismenu["tipe"]) or hapm <= 0:
                        print(
                            ""
                            "\n Tidak ada pesanan dengan angka urut tersebut"
                        )
                        hapm = ""

                confirmhapm = input(
                    ""
                    "\n " + lismenu["tipe"][hapm-1] +
                    "\n " + rp(lismenu["harga"][hapm-1]) +
                    "\n "
                    "\n Hapus menu di atas ? (y/t) : "
                    "\n (Note : Pesanan yang sebelumnya telah di buat pemesan dengan menu tersebut tidak akan hilang)"
                    "\n > "
                )

                if confirmhapm == "y":
                    del lismenu["tipe"][hapm-1]
                    del lismenu["harga"][hapm-1]
                    print(
                        ""
                        "\n Menu telah di hapus"
                    )
                elif confirmhapm == "t":
                    "back"
                else:
                    print(
                        ""
                        "\n input salah, coba lagi!"
                    )

            elif menuadmin == "0":
                loop1 = False

            else:
                print(
                    ""
                    "\n input salah, coba lagi!"
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
                "\n 1. Lihat Pesanan Yang Sudah Di Buat"
                "\n 2. Buat Pesanan"
                "\n 3. Edit pesanan"
                "\n 4. Hapus pesanan"
                "\n 0. Kembali"
                "\n "
                "\n > "
            )

            if menucostum == "1":
                if len(lispesancostum["pesanan"][idd-1]) != 0:
                    daftar_pesanan("costumer")
                else:
                    print(
                        ""
                        "\n ==Daftar pesanan kosong=="
                    )

            elif menucostum == "2":
                try :
                    count = countercustompesanan[idd-1]
                except IndexError:
                    count = 0

                pesanan = ""
                while not(type(pesanan) == int):
                    daftar_menu()
                    pesanan = input(
                        "\n Pilih pesanan : "
                        "\n (masukan angka saja, misal \"1\")"
                        "\n > "
                    )
                    try:
                        pesanan = int(pesanan)
                    except ValueError:
                        print(
                            "input bukan angka, coba lagi!"
                        )
                    if pesanan > len(lismenu["tipe"]) or pesanan <= 0:
                        print(
                            ""
                            "\n Tidak ada menu dengan nomor urut " + str(pesanan) + " , coba lagi!"
                        )
                        pesanan = ""

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
                            "input bukan angka, coba lagi!"
                        )
                    if jml <= 0:
                        print(
                            ""
                            "\n jumlah salah, mohon coba lagi!"
                        )
                        jml = ""

                pesananb = " " + lismenu["tipe"][pesanan-1] + " sebanyak " + str(jml) + "\n    |"
                hargapb = lismenu["harga"][pesanan-1] * jml
         
                while True:
                    tambah = input(
                        "\n Pesanan saat ini:"
                        "\n > " + str(pesananb) +
                        "\n    Seharga total :" + rp(str(hargapb)) +
                        "\n Tambah pesanan lagi? : "
                        "\n (masukan \"y\" atau \"t\" saja)"
                        "\n > "
                    )

                    if tambah == "y":
                        pesanan = ""
                        while not(type(pesanan) == int):
                            daftar_menu()
                            pesanan = input(
                                "\n Tambah pesanan : "
                                "\n (masukan angka saja, misal \"1\")"
                                "\n > "
                            )
                            try:
                                pesanan = int(pesanan)
                            except ValueError:
                                print(
                                    "input bukan angka, coba lagi!"
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
                                    "input bukan angka, coba lagi!"
                                )
                            if jml <= 0:
                                print(
                                    ""
                                    "\n jumlah salah, mohon coba lagi!"
                                )
                                jml = ""

                        pesananb += (" " + lismenu["tipe"][pesanan-1] + " sebanyak " + str(jml) + "\n    |")
                        hargapb += lismenu["harga"][pesanan-1] * jml

                    elif tambah == "t":
                        if pesananb in lispesancostum["pesanan"][idd-1]:
                            pke = lispesancostum["pesanan"][idd-1].count(pesananb) + 1
                            pluspes = "\n    |" + " ke 2" 
                            pesananb = pesananb + pluspes
                            if pesananb in lispesancostum["pesanan"][idd-1]:
                                z = 2
                                while pesananb in lispesancostum["pesanan"][idd-1]:
                                    z += 1
                                    pesananb = pesananb.rsplit(" ", 2)[0]
                                    pluspes = " ke " + str(z) 
                                    pesananb = pesananb + pluspes

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

                        print(
                            ""
                            "\n Pesanan telah di buat :"
                            "\n > " + str(pesananb) +
                            "\n    Seharga total :" + rp(str(hargapb))
                        )
                        break

                    else:
                        print(
                            ""
                            "\n Input salah, coba lagi!"
                        )

            elif menucostum == "3":
                if len(lispesancostum["pesanan"][idd-1]) != 0:
                    if not("Dalam Antrian" in lispesancostum["status"][idd-1]):
                        print(
                            ""
                            "\n Tidak ada pesanan yang dapat di ubah"
                        )

                    else:
                        editpesan = ""
                        while not(type(editpesan) == int):
                            daftar_pesanan("costumer")
                            editpesan = input(
                                ""
                                "\n Pilih pesanan di atas untuk di edit : "
                                "\n Note : hanya pesanan berstatus \"Dalam Antrian\" yang dapat di edit"
                                "\n (masukan angka saja, misal \"1\")"
                                "\n > "
                            )
                            try:
                                editpesan = int(editpesan)
                            except ValueError:
                                print(
                                    "input bukan angka, coba lagi!"
                                )
                            if editpesan > len(lispesan["pesanan"]) or editpesan <= 0:
                                print(
                                    ""
                                    "\n tidak ada pesanan dengan nomor urut \"" + str(editpesan) + " \""
                                )
                                editpesan = ""
                            elif lispesancostum["status"][idd-1][editpesan-1] != "Dalam Antrian":
                                print(
                                    ""
                                    "\n Hanya bisa mengubah pesanan yang dalam antrian dan belum Dalam Proses Pembuatan / Selsai!"
                                )
                                editpesan = ""

                    pesanan = ""
                    indexpara = lispesan["pesanan"][editpesan-1]
                    while not(type(pesanan) == int):
                        daftar_menu()
                        pesanan = input(
                            ""
                            "\n > " + lispesan["pesanan"][editpesan-1] +
                            "\n Ubah menjadi pilihan  : "
                            "\n (masukan angka saja, misal \"1\")"
                            "\n > "
                        )
                        try:
                            pesanan = int(pesanan)
                        except ValueError:
                            print(
                                "input bukan angka, coba lagi!"
                            )
                        if pesanan > len(lismenu["tipe"]) or pesanan <= 0:
                            print(
                                ""
                                "\n tidak ada pesanan dengan nomor urut \"" + str(pesanan) + " \""
                            )
                            pesanan = ""

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
                                "input bukan angka, coba lagi!"
                            )
                        if jml <= 0:
                            print(
                                ""
                                "\n jumlah salah, mohon coba lagi!"
                            )
                            jml = ""

                    pesananb = ""
                    hargapb = 0

                    pesananb += (" " + lismenu["tipe"][pesanan-1] + " sebanyak " + str(jml) + "\n    |")
                    hargapb += lismenu["harga"][pesanan-1] * jml
            
                    while True:
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
                                        "input bukan angka, coba lagi!"
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
                                        "input bukan angka, coba lagi!"
                                    )
                                if jml <= 0:
                                    print(
                                        ""
                                        "\n jumlah salah, mohon coba lagi!"
                                    )
                                    jml = ""

                            pesananb += (" " + lismenu["tipe"][pesanan-1] + " sebanyak " + str(jml) + "\n    |")
                            hargapb += lismenu["harga"][pesanan-1] * jml

                        elif tambah == "t":
                            if pesananb in lispesancostum["pesanan"][idd-1]:
                                pke = lispesancostum["pesanan"][idd-1].count(pesananb) + 1
                                pluspes = "\n    |" + " ke 2" 
                                pesananb = pesananb + pluspes
                                if pesananb in lispesancostum["pesanan"][idd-1]:
                                    z = 2
                                    while pesananb in lispesancostum["pesanan"][idd-1]:
                                        z += 1
                                        pesananb = pesananb.rsplit(" ", 2)[0]
                                        pluspes = " ke " + str(z) 
                                        pesananb = pesananb + pluspes

                            index = lispesan["pesanan"].index(indexpara)
                            lispesan["pesanan"][index] = pesananb
                            lispesan["hargap"][index] = hargapb
                            
                            lispesancostum["pesanan"][idd-1][editpesan-1] = pesananb
                            lispesancostum["hargap"][idd-1][editpesan-1] = hargapb

                            print(
                                ""
                                "\n Pesanan telah di ubah :"
                                "\n > " + str(pesananb) +
                                "\n    Seharga total :" + rp(str(hargapb))
                            )
                            break

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

            elif menucostum == "4":
                hapes = ""
                while not(type(hapes) == int):
                    daftar_pesanan("costumer")
                    hapes = input(
                        ""
                        "\n Pilih pesanan untuk di hapus : "
                        "\n Note : hanya pesanan berstatus \"Dalam Antrian\" yang dapat di hapus"
                        "\n (Angka urut saja, misal \"1\")"
                        "\n > "
                    )
                    try:
                        hapes = int(hapes)
                    except ValueError:
                        print(
                            ""
                            "\n input bukan angka, coba lagi!"
                        )
                    if hapes > len(lispesancostum["pesanan"][idd-1]) or hapes <= 0:
                        print(
                            ""
                            "\n tidak ada angka urut " + str(hapes) + ", coba lagi!"
                        )
                        hapes = ""
                    elif lispesancostum["status"][idd-1][hapes-1] != "Dalam Antrian":
                        print(
                            ""
                            "\n Hanya bisa menghapus pesanan yang Dalam Antrian dan belum Dalam Proses Pembuatan / Selsai!"
                        )
                        hapes = ""

                confirmhap = input(
                    ""
                    "\n " + lispesancostum["pesanan"][idd-1][hapes-1] +
                    "\n  " + str(lispesancostum["hargap"][idd-1][hapes-1]) +
                    "\n"
                    "\n Hapus pesanan di atas ? (y/t) : "
                    "\n > "
                )
                
                if confirmhap == "y":
                    indexpara = lispesan["pesanan"][hapes-1]
                    index = lispesan["pesanan"].index(indexpara)

                    del lispesan["pesanan"][index]
                    del lispesan["hargap"][index]
                    del lispesan["status"][index]
                    del lispesan["namap"][index]
                    del lispesan["nop"][index]
                    del lispesan["idp"][index]

                    del lispesancostum["pesanan"][idd-1][hapes-1]
                    del lispesancostum["hargap"][idd-1][hapes-1]
                    del lispesancostum["status"][idd-1][hapes-1]

                    countercustompesanan[idd-1] -= 1

                    print(
                        ""
                        "\n Pesanan telah di hapus"
                    )
                elif confirmhap == "t":
                    "back"
                else:
                    print(
                        ""
                        "\n input salah, coba lagi!"
                    )

            elif menucostum == "0":
                loop1 = False

            else:
                print(
                    ""
                    "\n input salah, coba lagi!"
                )
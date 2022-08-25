listBuku = [
    {'namabuku': 'Cinderela','jenis buku' : 'dongeng anak','stock': 3,'hargasewa': 2000},
    {'namabuku': 'Si Kancil','jenis buku' : 'dongeng anak','stock': 7,'hargasewa': 1500},
    {'namabuku': 'Bobo','jenis buku' : 'dongeng anak','stock': 4,'hargasewa': 3000}]

cart = []

def menampilkanDaftarBuku() :
    print('Daftar Buku\n')
    print('Index\t| Nama Buku  \t| Jenis Buku \t\t |Stock | Harga Sewa')
    for i in range(len(listBuku)) :
        print('{}\t| {}  \t| {}  \t | {}\t| {}'.format(i,listBuku[i]['namabuku'],listBuku[i]['jenis buku'],listBuku[i]['stock'],listBuku[i]['hargasewa']))

def MenambahBuku() :
    namaBuku = input('Masukkan Nama Buku : ')
    jenisBuku = input('Masukkan Jenis Buku : ')
    stockBuku = int(input('Masukkan Stock Buku : '))
    hargaBuku = int(input('Masukkan Sewa Buku : '))
    listBuku.append({
        'namabuku': namaBuku,
        'jenis buku':  jenisBuku, 
        'stock': stockBuku,
        'hargasewa': hargaBuku
    })
    menampilkanDaftarBuku()

def menghapusBuku() :
    menampilkanDaftarBuku()
    indexBuku = int(input('Masukkan index buku yang ingin dihapus : '))
    del listBuku[indexBuku]
    menampilkanDaftarBuku()

def menyewaBuku() :
    menampilkanDaftarBuku()
    while True :
        indexBuku = int(input('Masukkan Index buku yang ingin disewa : '))
        qtyBuah = int(input('Masukkan jumlah yang ingin disewa : '))
        if(qtyBuah > listBuku[indexBuku]['stock']) :
            print('Stock tidak cukup, stock {} tinggal {}'.format(listBuku[indexBuku]['namabuku'],listBuku[indexBuku]['stock']))
        else :
            cart.append({
                'namabuku': listBuku[indexBuku]['namabuku'], 
                'jenis buku':  listBuku[indexBuku]['jenis buku'], 
                'qty': qtyBuah, 
                'hargasewa': listBuku[indexBuku]['hargasewa'], 
                'index': indexBuku
            })
        print('Isi Cart :')
        print('Nama Buku\t| Qty\t| Harga Sewa')
        for item in cart :
            print('{}\t\t| {}\t| {}'.format(item['namabuku'], item['qty'], item['hargasewa']))
        checker = input('Mau sewa yang lain? (ya/tidak) = ')
        if(checker == 'tidak') :
            break

    print('Daftar Peminjaman Buku :')
    print('Nama Buku\t| Qty\t| Harga Sewa\t| Total Harga')
    totalHarga = 0
    for item in cart :
        print('{}\t| {}\t| {}\t| {}'.format(item['namabuku'], item['qty'], item['hargasewa'], item['qty'] * item['hargasewa']))
        totalHarga += item['qty'] * item['hargasewa']    
    while True :
        print('Total Yang Harus Dibayar = {}'.format(totalHarga))
        jmlUang = int(input('Masukkan jumlah uang : '))
        if(jmlUang > totalHarga) :
            kembali = jmlUang - totalHarga
            print('Terima kasih \n\nUang kembali anda : {}'.format(kembali))
            for item in cart :
                listBuku[item['index']]['stock'] -= item['qty']
            cart.clear()
            break
        elif(jmlUang == totalHarga) :
            print('Terima kasih')
            for item in cart :
                listBuku[item['index']]['stock'] -= item['qty']
            cart.clear()
            break
        else :
            kekurangan = totalHarga - jmlUang
            print('Uang anda kurang sebesar {}'.format(kekurangan))
while True :
    pilihanMenu = input('''
        ---------------Selamat Datang di Perpustakaan Desa--------------

        List Menu :
        1. Tampilkan Daftar Buku Perpustakaan
        2. Tambah Buku ke Perpustakaan
        3. Menghapus Buku dari Perpustakaan
        4. Meminjam Buku dari Perpustakaan
        5. Exit Program

        Masukkan angka Menu yang ingin dijalankan : ''')

    if(pilihanMenu == '1') :
        menampilkanDaftarBuku()
    elif(pilihanMenu == '2') :
        MenambahBuku()
    elif(pilihanMenu == '3') :
        menghapusBuku()
    elif(pilihanMenu == '4') :
       menyewaBuku()
    elif(pilihanMenu == '5') :
        break

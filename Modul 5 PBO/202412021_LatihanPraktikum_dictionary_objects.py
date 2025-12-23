class Produk:
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = harga

    def info(self):
        return f"{self.nama} - Rp {self.harga:,}"


# Membuat dictionary of objects Produk
katalog_produk = {
    "P001": Produk("P001", "Laptop", 8000000),
    "P002": Produk("P002", "Mouse", 150000),
    "P003": Produk("P003", "Keyboard", 300000)
}

print("=== Katalog Produk ===")
for kode, produk in katalog_produk.items():
    print(f"{kode}: {produk.info()}")


# ======================================
# a. Class Pelanggan
# ======================================
class Pelanggan:
    def __init__(self, id_pelanggan, nama, email):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.email = email

    def info(self):
        return f"ID: {self.id_pelanggan}, Nama: {self.nama}, Email: {self.email}"


# ======================================
# b. Dictionary objek Pelanggan
# ======================================
data_pelanggan = {
    "PL001": Pelanggan("PL001", "Andi", "andi@gmail.com"),
    "PL002": Pelanggan("PL002", "Siti", "siti@gmail.com"),
    "PL003": Pelanggan("PL003", "Budi", "budi@gmail.com")
}


# ======================================
# c. Fungsi tambah, hapus, dan cari pelanggan
# ======================================
def tambah_pelanggan(data, id_pelanggan, nama, email):
    if id_pelanggan in data:
        print("Pelanggan sudah ada.")
    else:
        data[id_pelanggan] = Pelanggan(id_pelanggan, nama, email)
        print("Pelanggan berhasil ditambahkan.")


def hapus_pelanggan(data, id_pelanggan):
    if id_pelanggan in data:
        del data[id_pelanggan]
        print("Pelanggan berhasil dihapus.")
    else:
        print("Pelanggan tidak ditemukan.")


def cari_pelanggan(data, id_pelanggan):
    if id_pelanggan in data:
        return data[id_pelanggan]
    else:
        return None


# ======================================
# d. Menampilkan seluruh daftar pelanggan
# ======================================
print("\n=== Uji Fungsi Pelanggan ===")

tambah_pelanggan(data_pelanggan, "PL004", "Rina", "rina@gmail.com")

pelanggan = cari_pelanggan(data_pelanggan, "PL002")
if pelanggan:
    print("Pelanggan ditemukan:", pelanggan.info())
else:
    print("Pelanggan tidak ditemukan.")

hapus_pelanggan(data_pelanggan, "PL001")

print("\n=== Daftar Seluruh Pelanggan ===")
for id_pel, pelanggan in data_pelanggan.items():
    print(f"{id_pel}: {pelanggan.info()}")

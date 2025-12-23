class Mahasiswa:
    def __init__(self, nama, nim, ipk):
        self.nama = nama
        self.nim = nim
        self.ipk = ipk

    def info(self):
        return f"{self.nama} (NIM: {self.nim}) - IPK: {self.ipk}"


# Membuat list of objects Mahasiswa
daftar_mahasiswa = [
    Mahasiswa("Ahmad", "IT001", 3.5),
    Mahasiswa("Budi", "IT002", 3.2),
    Mahasiswa("Citra", "IT003", 3.8)
]

# Mengakses list of objects Mahasiswa
print("=== Daftar Mahasiswa ===")
for mhs in daftar_mahasiswa:
    print(mhs.info())

# Filter berdasarkan IPK
print("\n=== Mahasiswa dengan IPK > 3.5 ===")
for mhs in daftar_mahasiswa:
    if mhs.ipk > 3.5:
        print(mhs.info())


# ======================================
# a. Class Buku
# ======================================
class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def info(self):
        return f"{self.judul} | Penulis: {self.penulis} | Tahun: {self.tahun}"


# ======================================
# b. List berisi 5 objek Buku
# ======================================
daftar_buku = [
    Buku("Laskar Pelangi", "Andrea Hirata", 2005),
    Buku("Sang Pemimpi", "Andrea Hirata", 2006),
    Buku("Negeri 5 Menara", "Ahmad Fuadi", 2009),
    Buku("Bumi", "Tere Liye", 2014),
    Buku("Dilan 1990", "Pidi Baiq", 2014)
]

print("\n=== Daftar Buku ===")
for buku in daftar_buku:
    print(buku.info())


# ======================================
# c. Fungsi mencari buku berdasarkan penulis
# ======================================
def cari_buku_berdasarkan_penulis(daftar, nama_penulis):
    hasil = []
    for buku in daftar:
        if buku.penulis.lower() == nama_penulis.lower():
            hasil.append(buku)
    return hasil


# ======================================
# d. Menampilkan hasil pencarian
# ======================================
penulis_dicari = "Andrea Hirata"
hasil_pencarian = cari_buku_berdasarkan_penulis(daftar_buku, penulis_dicari)

print(f"\n=== Hasil Pencarian Buku oleh {penulis_dicari} ===")
if hasil_pencarian:
    for buku in hasil_pencarian:
        print(buku.info())
else:
    print("Buku tidak ditemukan.")

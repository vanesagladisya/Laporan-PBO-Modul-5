class Produk:
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = harga

    def info(self):
        return f"{self.nama} - Rp {self.harga:,}"

# Membuat dictionary of objects
katalog_produk = {
    "P001": Produk("P001", "Laptop", 8000000),
    "P002": Produk("P002", "Mouse", 150000),
    "P003": Produk("P003", "Keyboard", 300000)
}

# Mengakses dictionary of objects
print("=== Katalog Produk ===")
for kode, produk in katalog_produk.items():
    print(f"{kode}: {produk.info()}")

# Mencari produk
cari_kode = "P002"
if cari_kode in katalog_produk:
    print(f"\nProduk ditemukan: {katalog_produk[cari_kode].info()}")

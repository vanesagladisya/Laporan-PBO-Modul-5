import tkinter as tk
from tkinter import messagebox, ttk

class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def to_dict(self):
        return {
            "judul": self.judul,
            "penulis": self.penulis,
            "tahun": self.tahun
        }

class AplikasiManajemenBuku:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Buku")
        self.root.geometry("600x400")

        # Collections: List untuk menyimpan objek buku
        self.daftar_buku = []

        # Frame untuk input
        frame_input = tk.Frame(root, padx=10, pady=10)
        frame_input.pack()

        # Widget input
        tk.Label(frame_input, text="Judul:").grid(row=0, column=0, sticky=tk.W)
        self.entry_judul = tk.Entry(frame_input, width=30)
        self.entry_judul.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Penulis:").grid(row=1, column=0, sticky=tk.W)
        self.entry_penulis = tk.Entry(frame_input, width=30)
        self.entry_penulis.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Tahun:").grid(row=2, column=0, sticky=tk.W)
        self.entry_tahun = tk.Entry(frame_input, width=30)
        self.entry_tahun.grid(row=2, column=1, padx=5, pady=5)

        # Frame untuk tombol
        frame_tombol = tk.Frame(root, padx=10, pady=10)
        frame_tombol.pack()

        tk.Button(frame_tombol, text="Tambah Buku", command=self.tambah_buku).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Hapus Buku", command=self.hapus_buku).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Cari Buku", command=self.cari_buku).pack(side=tk.LEFT, padx=5)

        # Treeview untuk menampilkan data
        frame_tabel = tk.Frame(root, padx=10, pady=10)
        frame_tabel.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(frame_tabel, columns=("Judul", "Penulis", "Tahun"), show="headings")
        self.tree.heading("Judul", text="Judul")
        self.tree.heading("Penulis", text="Penulis")
        self.tree.heading("Tahun", text="Tahun")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_tabel, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def tambah_buku(self):
        judul = self.entry_judul.get()
        penulis = self.entry_penulis.get()
        tahun = self.entry_tahun.get()

        if judul and penulis and tahun:
            # Membuat objek buku
            buku_baru = Buku(judul, penulis, tahun)

            # Menambahkan ke list
            self.daftar_buku.append(buku_baru)

            # Menambahkan ke treeview
            self.tree.insert("", tk.END, values=(judul, penulis, tahun))

            # Mengosongkan input
            self.entry_judul.delete(0, tk.END)
            self.entry_penulis.delete(0, tk.END)
            self.entry_tahun.delete(0, tk.END)

            messagebox.showinfo("Sukses", "Buku berhasil ditambahkan!")
        else:
            messagebox.showwarning("Peringatan", "Harap isi semua field!")

    def hapus_buku(self):
        selected_item = self.tree.selection()
        if selected_item:
            # Menghapus dari treeview
            item_data = self.tree.item(selected_item[0])
            judul = item_data['values'][0]

            # Menghapus dari list
            self.daftar_buku = [b for b in self.daftar_buku if b.judul != judul]

            self.tree.delete(selected_item[0])
            messagebox.showinfo("Sukses", "Buku berhasil dihapus!")
        else:
            messagebox.showwarning("Peringatan", "Pilih buku yang akan dihapus!")

    def cari_buku(self):
        pencarian = tk.simpledialog.askstring("Cari Buku", "Masukkan judul atau penulis:")
        if pencarian:
            hasil = []
            for buku in self.daftar_buku:
                if pencarian.lower() in buku.judul.lower() or pencarian.lower() in buku.penulis.lower():
                    hasil.append(buku)

            if hasil:
                pesan = "Buku ditemukan:\n"
                for buku in hasil:
                    pesan += f"{buku.judul} - {buku.penulis} ({buku.tahun})\n"
                messagebox.showinfo("Hasil Pencarian", pesan)
            else:
                messagebox.showinfo("Hasil Pencarian", "Tidak ditemukan buku yang sesuai.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiManajemenBuku(root)
    root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# =========================================
# 1. CLASS MAHASISWA
# =========================================
class Mahasiswa:
    def __init__(self, nim, nama, jurusan, ipk):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = ipk

    def info(self):
        return f"{self.nim} | {self.nama} | {self.jurusan} | IPK: {self.ipk}"

    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru


# =========================================
# 2 & 3. APLIKASI GUI
# =========================================
class AplikasiMahasiswa:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Manajemen Mahasiswa")
        self.root.geometry("900x550")

        # Dictionary mahasiswa (NIM sebagai key)
        self.data_mahasiswa = {}

        # =================================
        # FRAME INPUT
        # =================================
        frame_input = tk.LabelFrame(root, text="Input Data Mahasiswa", padx=10, pady=10)
        frame_input.pack(fill="x", padx=10, pady=5)

        tk.Label(frame_input, text="NIM").grid(row=0, column=0)
        tk.Label(frame_input, text="Nama").grid(row=0, column=2)
        tk.Label(frame_input, text="Jurusan").grid(row=1, column=0)
        tk.Label(frame_input, text="IPK").grid(row=1, column=2)

        self.entry_nim = tk.Entry(frame_input)
        self.entry_nama = tk.Entry(frame_input)
        self.entry_jurusan = tk.Entry(frame_input)
        self.entry_ipk = tk.Entry(frame_input)

        self.entry_nim.grid(row=0, column=1, padx=5)
        self.entry_nama.grid(row=0, column=3, padx=5)
        self.entry_jurusan.grid(row=1, column=1, padx=5)
        self.entry_ipk.grid(row=1, column=3, padx=5)

        # =================================
        # FRAME BUTTON CRUD
        # =================================
        frame_button = tk.Frame(root)
        frame_button.pack(pady=5)

        tk.Button(frame_button, text="Tambah", command=self.tambah).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_button, text="Update IPK", command=self.update_ipk).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_button, text="Hapus", command=self.hapus).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_button, text="Tampilkan Semua", command=self.tampilkan_semua).pack(side=tk.LEFT, padx=5)

        # =================================
        # SEARCH & FILTER
        # =================================
        frame_search = tk.LabelFrame(root, text="Cari & Filter", padx=10, pady=5)
        frame_search.pack(fill="x", padx=10, pady=5)

        self.entry_cari = tk.Entry(frame_search, width=30)
        self.entry_cari.pack(side=tk.LEFT, padx=5)

        tk.Button(frame_search, text="Cari (NIM/Nama)", command=self.cari).pack(side=tk.LEFT, padx=5)

        self.entry_filter = tk.Entry(frame_search, width=20)
        self.entry_filter.pack(side=tk.LEFT, padx=5)

        tk.Button(frame_search, text="Filter Jurusan", command=self.filter_jurusan).pack(side=tk.LEFT, padx=5)

        # =================================
        # TREEVIEW
        # =================================
        frame_table = tk.Frame(root)
        frame_table.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.tree = ttk.Treeview(frame_table, columns=("NIM", "Nama", "Jurusan", "IPK"), show="headings")
        self.tree.heading("NIM", text="NIM")
        self.tree.heading("Nama", text="Nama")
        self.tree.heading("Jurusan", text="Jurusan")
        self.tree.heading("IPK", text="IPK")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # =================================
        # FITUR TAMBAHAN
        # =================================
        frame_extra = tk.Frame(root)
        frame_extra.pack(pady=5)

        tk.Button(frame_extra, text="Rata-rata IPK", command=self.rata_ipk).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_extra, text="IPK Tertinggi", command=self.ipk_tertinggi).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_extra, text="Export ke File", command=self.export_file).pack(side=tk.LEFT, padx=5)

    # =================================
    # CRUD FUNCTIONS
    # =================================
    def tambah(self):
        try:
            nim = self.entry_nim.get()
            nama = self.entry_nama.get()
            jurusan = self.entry_jurusan.get()
            ipk = float(self.entry_ipk.get())

            if not nim or not nama or not jurusan:
                raise ValueError

            if nim in self.data_mahasiswa:
                messagebox.showerror("Error", "NIM sudah terdaftar!")
                return

            self.data_mahasiswa[nim] = Mahasiswa(nim, nama, jurusan, ipk)
            self.tampilkan_semua()
            self.clear_entry()
        except:
            messagebox.showerror("Error", "Input tidak valid!")

    def update_ipk(self):
        selected = self.tree.selection()
        if selected:
            nim = self.tree.item(selected[0])["values"][0]
            try:
                ipk_baru = float(self.entry_ipk.get())
                self.data_mahasiswa[nim].update_ipk(ipk_baru)
                self.tampilkan_semua()
            except:
                messagebox.showerror("Error", "IPK tidak valid!")

    def hapus(self):
        selected = self.tree.selection()
        if selected:
            nim = self.tree.item(selected[0])["values"][0]
            del self.data_mahasiswa[nim]
            self.tampilkan_semua()

    def tampilkan_semua(self):
        self.tree.delete(*self.tree.get_children())
        for mhs in self.data_mahasiswa.values():
            self.tree.insert("", tk.END, values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))

    # =================================
    # SEARCH & FILTER
    # =================================
    def cari(self):
        keyword = self.entry_cari.get().lower()
        self.tree.delete(*self.tree.get_children())
        for mhs in self.data_mahasiswa.values():
            if keyword in mhs.nim.lower() or keyword in mhs.nama.lower():
                self.tree.insert("", tk.END, values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))

    def filter_jurusan(self):
        jurusan = self.entry_filter.get().lower()
        self.tree.delete(*self.tree.get_children())
        for mhs in self.data_mahasiswa.values():
            if jurusan == mhs.jurusan.lower():
                self.tree.insert("", tk.END, values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))

    # =================================
    # FITUR TAMBAHAN
    # =================================
    def rata_ipk(self):
        if not self.data_mahasiswa:
            return
        rata = sum(m.ipk for m in self.data_mahasiswa.values()) / len(self.data_mahasiswa)
        messagebox.showinfo("Rata-rata IPK", f"Rata-rata IPK: {rata:.2f}")

    def ipk_tertinggi(self):
        if not self.data_mahasiswa:
            return
        terbaik = max(self.data_mahasiswa.values(), key=lambda m: m.ipk)
        messagebox.showinfo("IPK Tertinggi", terbaik.info())

    def export_file(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt")
        if file:
            with open(file, "w") as f:
                for mhs in self.data_mahasiswa.values():
                    f.write(mhs.info() + "\n")
            messagebox.showinfo("Sukses", "Data berhasil diekspor!")

    def clear_entry(self):
        self.entry_nim.delete(0, tk.END)
        self.entry_nama.delete(0, tk.END)
        self.entry_jurusan.delete(0, tk.END)
        self.entry_ipk.delete(0, tk.END)


# =========================================
# MAIN PROGRAM
# =========================================
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiMahasiswa(root)
    root.mainloop()

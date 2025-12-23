import tkinter as tk
from tkinter import messagebox, simpledialog

# Kelas Tugas
class Tugas:
    def __init__(self, nama, deskripsi, deadline, selesai=False):
        self.nama = nama
        self.deskripsi = deskripsi
        self.deadline = deadline
        self.selesai = selesai

    def __str__(self):
        status = "Selesai" if self.selesai else "Belum Selesai"
        return f"{self.nama} - {self.deskripsi} ({self.deadline}) - {status}"

# Kelas Aplikasi To-Do List
class AplikasiToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Tugas (To-Do List)")
        self.root.geometry("800x400")

        # List of objects
        self.daftar_tugas = []

        # Frame input
        frame_input = tk.Frame(root, padx=10, pady=10)
        frame_input.pack()

        tk.Label(frame_input, text="Nama Tugas:").grid(row=0, column=0, sticky=tk.W)
        self.entry_nama = tk.Entry(frame_input, width=30)
        self.entry_nama.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Deskripsi:").grid(row=1, column=0, sticky=tk.W)
        self.entry_deskripsi = tk.Entry(frame_input, width=30)
        self.entry_deskripsi.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Deadline:").grid(row=2, column=0, sticky=tk.W)
        self.entry_deadline = tk.Entry(frame_input, width=30)
        self.entry_deadline.grid(row=2, column=1, padx=5, pady=5)

        # Frame tombol
        frame_tombol = tk.Frame(root, padx=10, pady=10)
        frame_tombol.pack()

        tk.Button(frame_tombol, text="Tambah Tugas", command=self.tambah_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Hapus Tugas", command=self.hapus_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Edit Tugas", command=self.edit_tugas).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Tandai Selesai", command=self.tandai_selesai).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Cari Tugas", command=self.cari_tugas).pack(side=tk.LEFT, padx=5)

        # Listbox untuk menampilkan data
        frame_listbox = tk.Frame(root, padx=10, pady=10)
        frame_listbox.pack(fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(frame_listbox, width=100, height=15)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame_listbox, orient=tk.VERTICAL)
        scrollbar.config(command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

    def tambah_tugas(self):
        nama = self.entry_nama.get()
        deskripsi = self.entry_deskripsi.get()
        deadline = self.entry_deadline.get()

        if nama and deskripsi and deadline:
            tugas_baru = Tugas(nama, deskripsi, deadline)
            self.daftar_tugas.append(tugas_baru)
            self.listbox.insert(tk.END, str(tugas_baru))

            self.entry_nama.delete(0, tk.END)
            self.entry_deskripsi.delete(0, tk.END)
            self.entry_deadline.delete(0, tk.END)

            messagebox.showinfo("Sukses", "Tugas berhasil ditambahkan!")
        else:
            messagebox.showwarning("Peringatan", "Harap isi semua field!")

    def hapus_tugas(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.daftar_tugas[index]
            self.listbox.delete(index)
            messagebox.showinfo("Sukses", "Tugas berhasil dihapus!")
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang akan dihapus!")

    def edit_tugas(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            tugas = self.daftar_tugas[index]

            tugas.nama = simpledialog.askstring("Edit Tugas", "Nama Tugas:", initialvalue=tugas.nama)
            tugas.deskripsi = simpledialog.askstring("Edit Tugas", "Deskripsi:", initialvalue=tugas.deskripsi)
            tugas.deadline = simpledialog.askstring("Edit Tugas", "Deadline:", initialvalue=tugas.deadline)

            self.listbox.delete(index)
            self.listbox.insert(index, str(tugas))
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang akan diedit!")

    def tandai_selesai(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            tugas = self.daftar_tugas[index]
            tugas.selesai = True

            self.listbox.delete(index)
            self.listbox.insert(index, str(tugas))
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang akan ditandai selesai!")

    def cari_tugas(self):
        pencarian = simpledialog.askstring("Cari Tugas", "Masukkan nama atau deskripsi:")
        if pencarian:
            hasil = [t for t in self.daftar_tugas if pencarian.lower() in t.nama.lower() or pencarian.lower() in t.deskripsi.lower()]
            if hasil:
                pesan = "Tugas ditemukan:\n"
                for t in hasil:
                    pesan += str(t) + "\n"
                messagebox.showinfo("Hasil Pencarian", pesan)
            else:
                messagebox.showinfo("Hasil Pencarian", "Tidak ditemukan tugas yang sesuai.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiToDoList(root)
    root.mainloop()

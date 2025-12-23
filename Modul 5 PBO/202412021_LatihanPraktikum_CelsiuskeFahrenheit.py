import tkinter as tk
from tkinter import messagebox

# ================================
# (b) Gunakan class untuk mengorganisir komponen GUI
# ================================
class KonversiSuhu:
    def __init__(self, root):
        self.root = root
        self.root.title("Konversi Suhu")
        self.root.geometry("300x200")

        self.label = tk.Label(
            root,
            text="Konversi Celsius ke Fahrenheit",
            font=("Arial", 12)
        )
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=25)
        self.entry.pack(pady=5)

        self.btn_konversi = tk.Button(
            root,
            text="Konversi",
            command=self.konversi
        )
        self.btn_konversi.pack(pady=5)

        self.btn_hapus = tk.Button(
            root,
            text="Hapus",
            command=self.hapus
        )
        self.btn_hapus.pack(pady=5)

    # ================================
    # (c) Validasi input
    # ================================
    def konversi(self):
        try:
            celsius = float(self.entry.get())      # ← validasi: input harus angka
            fahrenheit = (celsius * 9 / 5) + 32
            messagebox.showinfo("Hasil", f"{celsius}°C = {fahrenheit:.2f}°F")
        except:
            messagebox.showerror("Error", "Masukkan angka yang valid")  # ← muncul jika input salah

    def hapus(self):
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = KonversiSuhu(root)
    root.mainloop()

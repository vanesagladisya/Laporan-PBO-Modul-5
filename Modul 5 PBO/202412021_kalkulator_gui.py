import tkinter as tk

class Kalkulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Sederhana")
        self.root.geometry("300x400")

        # Variabel untuk menyimpan input
        self.expression = ""

        # Text Display
        self.display = tk.Entry(root, font=("Arial", 18), bd=10, relief=tk.RIDGE, justify=tk.RIGHT)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Tombol-tombol kalkulator
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            if button == '=':
                tk.Button(root, text=button, font=("Arial", 14), width=8, height=2,
                          command=self.hitung).grid(row=row_val, column=col_val, padx=5, pady=5)
            elif button == 'C':
                tk.Button(root, text=button, font=("Arial", 14), width=8, height=2,
                          command=self.hapus).grid(row=row_val, column=col_val, padx=5, pady=5, columnspan=4, sticky="we")
            else:
                tk.Button(root, text=button, font=("Arial", 14), width=8, height=2,
                          command=lambda b=button: self.tekan_tombol(b)).grid(row=row_val, column=col_val, padx=5, pady=5)

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def tekan_tombol(self, nilai):
        self.expression += str(nilai)
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

    def hitung(self):
        try:
            hasil = eval(self.expression)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(hasil))
            self.expression = str(hasil)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            self.expression = ""

    def hapus(self):
        self.expression = ""
        self.display.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    kalkulator = Kalkulator(root)
    root.mainloop()

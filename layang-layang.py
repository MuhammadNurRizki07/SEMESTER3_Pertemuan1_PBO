import tkinter as tk
from tkinter import messagebox

def hitung_luas():
    try:
        diagonal1 = float(entry_diagonal1.get())
        diagonal2 = float(entry_diagonal2.get())
        if diagonal1 <= 0 or diagonal2 <= 0:
            raise ValueError("Diagonal harus lebih besar dari 0.")
        luas = (diagonal1 * diagonal2) / 2
        label_hasil.config(text=f"Luas: {luas}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def hitung_keliling():
    try:
        diagonal1 = float(entry_diagonal1.get())
        diagonal2 = float(entry_diagonal2.get())
        if diagonal1 <= 0 or diagonal2 <= 0:
            raise ValueError("Panjang sisi harus lebih besar dari 0.")
        keliling = 2 * (diagonal1 + diagonal2)
        label_hasil.config(text=f"Keliling: {keliling}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Membuat jendela
root = tk.Tk()
root.title("Kalkulator Layang-layang")
root.geometry("300x275")

# Label dan Entry untuk diagonal 1 dan diagonal 2
label_diagonal1 = tk.Label(root, text="Masukkan panjang diagonal 1:")
label_diagonal1.pack(pady=5)

entry_diagonal1 = tk.Entry(root)
entry_diagonal1.pack(pady=5)

label_diagonal2 = tk.Label(root, text="Masukkan panjang diagonal 2:")
label_diagonal2.pack(pady=5)

entry_diagonal2 = tk.Entry(root)
entry_diagonal2.pack(pady=5)

# Tombol untuk menghitung luas dan keliling
btn_luas = tk.Button(root, text="Hitung Luas", command=hitung_luas)
btn_luas.pack(pady=5)

btn_keliling = tk.Button(root, text="Hitung Keliling", command=hitung_keliling)
btn_keliling.pack(pady=5)

# Label hasil
label_hasil = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
label_hasil.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()

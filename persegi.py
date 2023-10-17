import tkinter as tk
from tkinter import messagebox

def hitung_luas():
    try:
        sisi = float(entry_sisi.get())
        if sisi <= 0:
            raise ValueError("Sisi harus lebih besar dari 0.")
        luas = sisi ** 2
        label_hasil.config(text=f"Luas: {luas}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def hitung_keliling():
    try:
        sisi = float(entry_sisi.get())
        if sisi <= 0:
            raise ValueError("Sisi harus lebih besar dari 0.")
        keliling = 4 * sisi
        label_hasil.config(text=f"Keliling: {keliling}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Membuat jendela
root = tk.Tk()
root.title("Kalkulator Persegi")
root.geometry("300x200")

# Label dan Entry untuk sisi
label_sisi = tk.Label(root, text="Masukkan panjang sisi:")
label_sisi.pack(pady=10)

entry_sisi = tk.Entry(root)
entry_sisi.pack(pady=5)

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

import tkinter as tk
from tkinter import messagebox
import math

def hitung_luas_lingkaran():
    try:
        jari_jari = float(entry_jari_jari.get())
        if jari_jari <= 0:
            raise ValueError("Jari-jari harus lebih besar dari 0.")
        luas = math.pi * (jari_jari ** 2)
        label_hasil_lingkaran.config(text=f"Luas: {luas}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def hitung_keliling_lingkaran():
    try:
        jari_jari = float(entry_jari_jari.get())
        if jari_jari <= 0:
            raise ValueError("Jari-jari harus lebih besar dari 0.")
        keliling = 2 * math.pi * jari_jari
        label_hasil_lingkaran.config(text=f"Keliling: {keliling}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Membuat jendela
root_lingkaran = tk.Tk()
root_lingkaran.title("Kalkulator Lingkaran")
root_lingkaran.geometry("300x250")

# Label dan Entry untuk jari-jari
label_jari_jari = tk.Label(root_lingkaran, text="Masukkan jari-jari:")
label_jari_jari.pack(pady=5)

entry_jari_jari = tk.Entry(root_lingkaran)
entry_jari_jari.pack(pady=5)

# Tombol untuk menghitung luas dan keliling
btn_luas_lingkaran = tk.Button(root_lingkaran, text="Hitung Luas", command=hitung_luas_lingkaran)
btn_luas_lingkaran.pack(pady=5)

btn_keliling_lingkaran = tk.Button(root_lingkaran, text="Hitung Keliling", command=hitung_keliling_lingkaran)
btn_keliling_lingkaran.pack(pady=5)

# Label hasil
label_hasil_lingkaran = tk.Label(root_lingkaran, text="", font=("Helvetica", 14, "bold"))
label_hasil_lingkaran.pack(pady=10)

# Menjalankan aplikasi
root_lingkaran.mainloop()

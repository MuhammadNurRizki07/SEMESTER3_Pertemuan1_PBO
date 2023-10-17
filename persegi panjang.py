import tkinter as tk
from tkinter import messagebox

def hitung_luas_persegi_panjang():
    try:
        panjang = float(entry_panjang.get())
        lebar = float(entry_lebar.get())
        if panjang <= 0 or lebar <= 0:
            raise ValueError("Panjang dan lebar harus lebih besar dari 0.")
        luas = panjang * lebar
        label_hasil_persegi_panjang.config(text=f"Luas: {luas}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def hitung_keliling_persegi_panjang():
    try:
        panjang = float(entry_panjang.get())
        lebar = float(entry_lebar.get())
        if panjang <= 0 or lebar <= 0:
            raise ValueError("Panjang dan lebar harus lebih besar dari 0.")
        keliling = 2 * (panjang + lebar)
        label_hasil_persegi_panjang.config(text=f"Keliling: {keliling}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Membuat jendela
root_persegi_panjang = tk.Tk()
root_persegi_panjang.title("Kalkulator Persegi Panjang")
root_persegi_panjang.geometry("300x400")

# Label dan Entry untuk panjang dan lebar
label_panjang = tk.Label(root_persegi_panjang, text="Masukkan panjang:")
label_panjang.pack(pady=5)

entry_panjang = tk.Entry(root_persegi_panjang)
entry_panjang.pack(pady=5)

label_lebar = tk.Label(root_persegi_panjang, text="Masukkan lebar:")
label_lebar.pack(pady=5)

entry_lebar = tk.Entry(root_persegi_panjang)
entry_lebar.pack(pady=5)

# Tombol untuk menghitung luas dan keliling
btn_luas_persegi_panjang = tk.Button(root_persegi_panjang, text="Hitung Luas", command=hitung_luas_persegi_panjang)
btn_luas_persegi_panjang.pack(pady=5)

btn_keliling_persegi_panjang = tk.Button(root_persegi_panjang, text="Hitung Keliling", command=hitung_keliling_persegi_panjang)
btn_keliling_persegi_panjang.pack(pady=5)

# Label hasil
label_hasil_persegi_panjang = tk.Label(root_persegi_panjang, text="", font=("Helvetica", 14, "bold"))
label_hasil_persegi_panjang.pack(pady=10)

# Menjalankan aplikasi
root_persegi_panjang.mainloop()

import tkinter as tk
from tkinter import messagebox

def hitung_luas_jajargenjang():
    try:
        alas = float(entry_alas.get())
        tinggi = float(entry_tinggi.get())
        if alas <= 0 or tinggi <= 0:
            raise ValueError("Alas dan tinggi harus lebih besar dari 0.")
        luas = alas * tinggi
        label_hasil_jajargenjang.config(text=f"Luas: {luas}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def hitung_keliling_jajargenjang():
    try:
        sisi1 = float(entry_sisi1.get())
        sisi2 = float(entry_sisi2.get())
        if sisi1 <= 0 or sisi2 <= 0:
            raise ValueError("Panjang sisi harus lebih besar dari 0.")
        keliling = 2 * (sisi1 + sisi2)
        label_hasil_jajargenjang.config(text=f"Keliling: {keliling}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Membuat jendela
root_jajargenjang = tk.Tk()
root_jajargenjang.title("Kalkulator Jajar Genjang")
root_jajargenjang.geometry("300x400")

# Label dan Entry untuk alas dan tinggi
label_alas = tk.Label(root_jajargenjang, text="Masukkan panjang alas:")
label_alas.pack(pady=5)

entry_alas = tk.Entry(root_jajargenjang)
entry_alas.pack(pady=5)

label_tinggi = tk.Label(root_jajargenjang, text="Masukkan tinggi:")
label_tinggi.pack(pady=5)

entry_tinggi = tk.Entry(root_jajargenjang)
entry_tinggi.pack(pady=5)

# Label dan Entry untuk sisi-sisi
label_sisi1 = tk.Label(root_jajargenjang, text="Masukkan panjang sisi 1:")
label_sisi1.pack(pady=5)

entry_sisi1 = tk.Entry(root_jajargenjang)
entry_sisi1.pack(pady=5)

label_sisi2 = tk.Label(root_jajargenjang, text="Masukkan panjang sisi 2:")
label_sisi2.pack(pady=5)

entry_sisi2 = tk.Entry(root_jajargenjang)
entry_sisi2.pack(pady=5)

# Tombol untuk menghitung luas dan keliling
btn_luas_jajargenjang = tk.Button(root_jajargenjang, text="Hitung Luas", command=hitung_luas_jajargenjang)
btn_luas_jajargenjang.pack(pady=5)

btn_keliling_jajargenjang = tk.Button(root_jajargenjang, text="Hitung Keliling", command=hitung_keliling_jajargenjang)
btn_keliling_jajargenjang.pack(pady=5)

# Label hasil
label_hasil_jajargenjang = tk.Label(root_jajargenjang, text="", font=("Helvetica", 14, "bold"))
label_hasil_jajargenjang.pack(pady=10)

# Menjalankan aplikasi
root_jajargenjang.mainloop()

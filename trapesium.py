import tkinter as tk
from tkinter import messagebox

def hitung_luas_trapesium():
    try:
        alas = float(entry_alas.get())
        atas = float(entry_atas.get())
        tinggi = float(entry_tinggi.get())
        if alas <= 0 or atas <= 0 or tinggi <= 0:
            raise ValueError("Alas, atas, dan tinggi harus lebih besar dari 0.")
        luas = 0.5 * (alas + atas) * tinggi
        label_hasil_trapesium.config(text=f"Luas: {luas}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def hitung_keliling_trapesium():
    try:
        sisi1 = float(entry_sisi1.get())
        sisi2 = float(entry_sisi2.get())
        sisi3 = float(entry_sisi3.get())
        sisi4 = float(entry_sisi4.get())
        if sisi1 <= 0 or sisi2 <= 0 or sisi3 <= 0 or sisi4 <= 0:
            raise ValueError("Panjang sisi harus lebih besar dari 0.")
        keliling = sisi1 + sisi2 + sisi3 + sisi4
        label_hasil_trapesium.config(text=f"Keliling: {keliling}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Membuat jendela
root_trapesium = tk.Tk()
root_trapesium.title("Kalkulator Trapesium")
root_trapesium.geometry("300x350")

# Label dan Entry untuk alas, atas, dan tinggi
label_alas = tk.Label(root_trapesium, text="Masukkan panjang alas:")
label_alas.pack(pady=5)

entry_alas = tk.Entry(root_trapesium)
entry_alas.pack(pady=5)

label_atas = tk.Label(root_trapesium, text="Masukkan panjang atas:")
label_atas.pack(pady=5)

entry_atas = tk.Entry(root_trapesium)
entry_atas.pack(pady=5)

label_tinggi = tk.Label(root_trapesium, text="Masukkan tinggi:")
label_tinggi.pack(pady=5)

entry_tinggi = tk.Entry(root_trapesium)
entry_tinggi.pack(pady=5)


# Membuat jendela
root_trapesium = tk.Tk()
root_trapesium.title("Kalkulator Trapesium")
root_trapesium.geometry("300x600")

# Label dan Entry untuk alas, atas, dan tinggi
label_alas = tk.Label(root_trapesium, text="Masukkan panjang alas:")
label_alas.pack(pady=5)

entry_alas = tk.Entry(root_trapesium)
entry_alas.pack(pady=5)

label_atas = tk.Label(root_trapesium, text="Masukkan panjang atas:")
label_atas.pack(pady=5)

entry_atas = tk.Entry(root_trapesium)
entry_atas.pack(pady=5)

label_tinggi = tk.Label(root_trapesium, text="Masukkan tinggi:")
label_tinggi.pack(pady=5)

entry_tinggi = tk.Entry(root_trapesium)
entry_tinggi.pack(pady=5)
btn_luas_trapesium = tk.Button(root_trapesium, text="Hitung Luas", command=hitung_luas_trapesium)
btn_luas_trapesium.pack(pady=5)

# Label dan Entry untuk sisi-sisi
label_sisi1 = tk.Label(root_trapesium, text="Masukkan panjang sisi 1:")
label_sisi1.pack(pady=5)

entry_sisi1 = tk.Entry(root_trapesium)
entry_sisi1.pack(pady=5)

label_sisi2 = tk.Label(root_trapesium, text="Masukkan panjang sisi 2:")
label_sisi2.pack(pady=5)

entry_sisi2 = tk.Entry(root_trapesium)
entry_sisi2.pack(pady=5)

label_sisi3 = tk.Label(root_trapesium, text="Masukkan panjang sisi 3:")
label_sisi3.pack(pady=5)

entry_sisi3 = tk.Entry(root_trapesium)
entry_sisi3.pack(pady=5)

label_sisi4 = tk.Label(root_trapesium, text="Masukkan panjang sisi 4:")
label_sisi4.pack(pady=5)

entry_sisi4 = tk.Entry(root_trapesium)
entry_sisi4.pack(pady=5)

# Tombol untuk menghitung luas dan keliling

btn_keliling_trapesium = tk.Button(root_trapesium, text="Hitung Keliling", command=hitung_keliling_trapesium)
btn_keliling_trapesium.pack(pady=5)

# Label hasil
label_hasil_trapesium = tk.Label(root_trapesium, text="", font=("Helvetica", 14, "bold"))
label_hasil_trapesium.pack(pady=10)

# Menjalankan aplikasi
root_trapesium.mainloop()

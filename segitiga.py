import tkinter as tk
from tkinter import messagebox

def hitung_luas_segitiga():
    try:
        alas = float(entry_alas.get())
        tinggi = float(entry_tinggi.get())
        if alas <= 0 or tinggi <= 0:
            raise ValueError("Alas dan tinggi harus lebih besar dari 0.")
        luas = 0.5 * alas * tinggi
        label_hasil_segitiga.config(text=f"Luas: {luas}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def hitung_keliling_segitiga():
    try:
        sisi1 = float(entry_sisi1.get())
        sisi2 = float(entry_sisi2.get())
        sisi3 = float(entry_sisi3.get())
        if sisi1 <= 0 or sisi2 <= 0 or sisi3 <= 0:
            raise ValueError("Panjang sisi harus lebih besar dari 0.")
        keliling = sisi1 + sisi2 + sisi3
        label_hasil_segitiga.config(text=f"Keliling: {keliling}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Membuat jendela
root_segitiga = tk.Tk()
root_segitiga.title("Kalkulator Segitiga")
root_segitiga.geometry("300x440")

# Label dan Entry untuk alas dan tinggi
label_alas = tk.Label(root_segitiga, text="Masukkan panjang alas:")
label_alas.pack(pady=5)

entry_alas = tk.Entry(root_segitiga)
entry_alas.pack(pady=5)

label_tinggi = tk.Label(root_segitiga, text="Masukkan tinggi:")
label_tinggi.pack(pady=5)

entry_tinggi = tk.Entry(root_segitiga)
entry_tinggi.pack(pady=5)

btn_luas_segitiga = tk.Button(root_segitiga, text="Hitung Luas", command=hitung_luas_segitiga)
btn_luas_segitiga.pack(pady=5)

# Label dan Entry untuk sisi-sisi
label_sisi1 = tk.Label(root_segitiga, text="Masukkan panjang sisi 1:")
label_sisi1.pack(pady=5)

entry_sisi1 = tk.Entry(root_segitiga)
entry_sisi1.pack(pady=5)

label_sisi2 = tk.Label(root_segitiga, text="Masukkan panjang sisi 2:")
label_sisi2.pack(pady=5)

entry_sisi2 = tk.Entry(root_segitiga)
entry_sisi2.pack(pady=5)

label_sisi3 = tk.Label(root_segitiga, text="Masukkan panjang sisi 3:")
label_sisi3.pack(pady=5)

entry_sisi3 = tk.Entry(root_segitiga)
entry_sisi3.pack(pady=5)

# Tombol untuk menghitung luas dan keliling

btn_keliling_segitiga = tk.Button(root_segitiga, text="Hitung Keliling", command=hitung_keliling_segitiga)
btn_keliling_segitiga.pack(pady=5)

# Label hasil
label_hasil_segitiga = tk.Label(root_segitiga, text="", font=("Helvetica", 14, "bold"))
label_hasil_segitiga.pack(pady=10)

# Menjalankan aplikasi
root_segitiga.mainloop()

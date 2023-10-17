import tkinter as tk
from tkinter import messagebox

def hitung_luas_belah_ketupat():
    try:
        diagonal1 = float(entry_diagonal1.get())
        diagonal2 = float(entry_diagonal2.get())
        if diagonal1 <= 0 or diagonal2 <= 0:
            raise ValueError("Diagonal harus lebih besar dari 0.")
        luas = 0.5 * diagonal1 * diagonal2
        label_hasil_belah_ketupat.config(text=f"Luas: {luas}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def hitung_keliling_belah_ketupat():
    try:
        diagonal1 = float(entry_diagonal1.get())
        if diagonal1 <= 0:
            raise ValueError("Sisi harus lebih besar dari 0.")
        keliling = 4 * diagonal1
        label_hasil_belah_ketupat.config(text=f"Keliling: {keliling}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Membuat jendela
root_belah_ketupat = tk.Tk()
root_belah_ketupat.title("Kalkulator Belah Ketupat")
root_belah_ketupat.geometry("300x250")

# Label dan Entry untuk diagonal 1 dan diagonal 2
label_diagonal1 = tk.Label(root_belah_ketupat, text="Masukkan panjang diagonal 1:")
label_diagonal1.pack(pady=5)

entry_diagonal1 = tk.Entry(root_belah_ketupat)
entry_diagonal1.pack(pady=5)

label_diagonal2 = tk.Label(root_belah_ketupat, text="Masukkan panjang diagonal 2:")
label_diagonal2.pack(pady=5)

entry_diagonal2 = tk.Entry(root_belah_ketupat)
entry_diagonal2.pack(pady=5)

# Tombol untuk menghitung luas dan keliling
btn_luas_belah_ketupat = tk.Button(root_belah_ketupat, text="Hitung Luas", command=hitung_luas_belah_ketupat)
btn_luas_belah_ketupat.pack(pady=5)

btn_keliling_belah_ketupat = tk.Button(root_belah_ketupat, text="Hitung Keliling", command=hitung_keliling_belah_ketupat)
btn_keliling_belah_ketupat.pack(pady=5)

# Label hasil
label_hasil_belah_ketupat = tk.Label(root_belah_ketupat, text="", font=("Helvetica", 14, "bold"))
label_hasil_belah_ketupat.pack(pady=10)

# Menjalankan aplikasi
root_belah_ketupat.mainloop()

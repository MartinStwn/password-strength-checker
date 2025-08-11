import tkinter as tk
from zxcvbn import zxcvbn

def check_password():
    password = entry.get()
    if not password:
        label_result.config(text="Masukkan password terlebih dahulu!")
        return
    results = zxcvbn(password)
    label_result.config(text=f"Skor (0-4): {results['score']}\nWaktu cracking: {results['crack_times_display']['offline_fast_hashing_1e10_per_second']}")

# Buat jendela utama
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x200")  # Ukuran jendela

# Tambah elemen UI
tk.Label(root, text="Masukkan password:").pack(pady=10)
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)
tk.Button(root, text="Cek Kekuatan", command=check_password).pack(pady=10)
label_result = tk.Label(root, text="", wraplength=250)
label_result.pack(pady=10)

# Jalankan aplikasi
root.mainloop()

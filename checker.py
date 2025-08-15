import tkinter as tk
from zxcvbn import zxcvbn
import math

def check_password():
    password = entry.get()
    if not password:
        label_result.config(text="Masukkan password terlebih dahulu!")
        return
    
    results = zxcvbn(password)
    guesses_log10 = results['guesses_log10']
    entropy = guesses_log10 / math.log10(2)  # Konversi ke log2 untuk entropi dalam bit
    percent = min(100, int((entropy / 100) * 100))
    if percent < 1:
        percent = 1
    
    label_result.config(
        text=f"Kekuatan: {percent}%\n"
             f"Entropy: {entropy:.2f} bit\n"
             f"Waktu cracking: {results['crack_times_display']['offline_fast_hashing_1e10_per_second']}"
    )

# Buat jendela utama
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("320x220")

tk.Label(root, text="Masukkan password:").pack(pady=10)
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)
tk.Button(root, text="Cek Kekuatan", command=check_password).pack(pady=10)
label_result = tk.Label(root, text="", wraplength=280, justify="left")
label_result.pack(pady=10)

root.mainloop()

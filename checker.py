import tkinter as tk
from zxcvbn import zxcvbn

def check_password():
    password = entry.get()
    results = zxcvbn(password)
    label_result.config(text=f"Skor (0-4): {results['score']}\nWaktu cracking: {results['crack_times_display']['offline_fast_hashing_1e10_per_second']}")

root = tk.Tk()
root.title("Password Strength Checker")
tk.Label(root, text="Masukkan password:").pack()
entry = tk.Entry(root, show="*")
entry.pack()
tk.Button(root, text="Cek", command=check_password).pack()
label_result = tk.Label(root, text="")
label_result.pack()
root.mainloop()

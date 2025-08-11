from zxcvbn import zxcvbn

password = input("Masukkan password: ")
results = zxcvbn(password)
print(f"Skor (0-4): {results['score']}")
print(f"Estimasi waktu cracking: {results['crack_times_display']['offline_fast_hashing_1e10_per_second']}")

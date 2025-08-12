# Password Strength Checker

Aplikasi untuk memeriksa kekuatan password menggunakan library `zxcvbn`. Mendukung antarmuka baris perintah (CLI) dan antarmuka grafis (GUI) dengan Tkinter.

## Tujuan
Aplikasi ini membantu pengguna mengevaluasi kekuatan password berdasarkan skor (0-4) dan estimasi waktu cracking, untuk meningkatkan kesadaran keamanan password.

## Fitur
- Memeriksa kekuatan password menggunakan `zxcvbn`.
- Menampilkan skor (0-4) dan estimasi waktu cracking.
- Antarmuka CLI untuk penggunaan sederhana.
- (Opsional) Antarmuka GUI dengan Tkinter untuk pengalaman interaktif.

## Prasyarat
- Python 3.11
- Library Python: `zxcvbn`, `bandit`
- Tkinter (`python3-tk`) untuk GUI
- Git untuk version control
- (Opsional) Draw.io untuk flowchart
- (Opsional) John the Ripper untuk simulasi cracking

## Instalasi
1. Clone repositori:
   ```bash
   git clone git@github.com:MartinStwn/password-strength-checker.git
   cd password_strength_checker

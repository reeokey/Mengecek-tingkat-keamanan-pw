import re # import modul regular expression untuk validasi pola

# fungsi untuk memeriksa tingkat keamanan kata sandi
def cek_kemanan_pw(password):
    
    panjang = len(password) >= 8
    # memeriksa panjang password minimal 8 karakter
    huruf_besar = bool(re.search(r'[A-Z]', password))
    # memeriksa huruf besar pada password
    huruf_kecil = bool(re.search(r'[a-z]', password))
    # memeriksa huruf kecil pada password
    angka = bool(re.search(r'\d', password))
    # memeriksa angka pada password
    simbol = bool(re.search(r'[!@#$%^&*(),."?{}|<>]', password))
    # memeriksa simbol pada password
    
    if panjang and huruf_besar and huruf_kecil and angka and simbol:
        return "Kuat"
    elif panjang and (huruf_besar or huruf_kecil) and angka:
        return "Tidak Terlalu Kuat"
    else:
        return "Lemah"
    
# fungsi untuk memeriksa format email user yang valid
def cek_keamanan_email(email):
    
    pola_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pola_email, email):
        return "Valid"
    else:
        return "Tidak Valid"

# menampilkan output code
print()
email_user = input("Masukkan Email Anda: ")
password_user = input("Masukkan Password Anda: ")
tingkat_keamanan_email = cek_keamanan_email(email_user)
tingkat_keamanan_password = cek_kemanan_pw(password_user)
print()
print(f"Email: {email_user} - Tingkat Keamanan: {tingkat_keamanan_email}")
print(f"Kata Sandi: {password_user} - Tingkat Keamanan: {tingkat_keamanan_password}")

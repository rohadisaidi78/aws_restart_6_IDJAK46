#Exercise1
print("Selamat Datang di Aplikasi Tebak Angka!")
print("Peraturannya sederhana. Saya akan menentukan sebuah angka dan Anda silakan menebak angka tersebut.")
import random
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Silakan tebak angka antara 1 dan 10: ")
    if int(guess) == number:
        print("Anda menebak angka {}. Tebakan Anda Benar! Anda Menang!".format(guess))
        isGuessRight = True
    else:
        print("Tebakan Anda {}. Maaf, masih salah. Silakan coba lagi.".format(guess))
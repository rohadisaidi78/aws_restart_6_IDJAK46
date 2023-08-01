#Excercise1
userReply = input("Apakah Anda ingin mengirimkan paket? (Pilih Ya atau Tidak) ")
if userReply == "Ya":
    print("Kami dapat membantu Anda mengirimkan paket!")
#Excercise2
else:
    print("Silakan kembali lagi kalau Anda ingin mengirimkan paket. Terima kasih.")
#Excercise3
userReply = input("Apakah Anda ingin membeli materai, membeli amplop atau ingin foto copy? (Pilih materai, amplop atau foto copy) ")
if userReply == "materai":
    print("Kami menyediakan beberapa desain materai yang bisa dipilih.")
elif userReply == "amplop":
    print("Kami menyediakan berbagai ukuran amplop yang bisa dipilih.")
elif userReply == "foto copy":
    copies = input("Mau rangkap berapa? (Pilih berapa rangkap) ")
    print("Ini hasilnya {} rangkap.".format(copies))
else:
    print("Terima kasih, silakan datang kembali.")
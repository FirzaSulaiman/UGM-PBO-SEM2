angka = int(input("Masukkan angka: "))

if angka <= 1:
    print(str(angka) + " bukan prima")
elif angka == 2:
    print(str(angka) + " angka prima")
elif angka % 2 == 0:
    print(str(angka) + " bukan prima")
else:
    is_prima = True
    i = 3
    while i <= int(angka**0.5) + 1:
        if angka % i == 0:
            is_prima = False
            break
        i += 2

    if is_prima:
        print(str(angka) + " merupakan angka prima")
    else:
        print(str(angka) + " bukan angka prima")

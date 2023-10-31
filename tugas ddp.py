print("tugas 1")
nama=["honda tiger","motor","200","hitam","2"]
nama.append("7jt")
nama.append("tiger 2000")
nama.insert(2,"honda")
print(nama)

print("tugas 2")
print ("""luas bangun datar
1.Persegi
2.Lingkaran
3.Segitiga""")
pilihan=int(input("masukkan pilihan :"))
match pilihan:
    case 1 :
        s=int(input("masukkan sisi :"))
        luas=s*s
    case 2 :
        r=int(input("masukkan jari-jari :"))
        luas=3.14*r*r
    case 3 :
        a=int(input("masukkan alas :"))
        t=int(input("masukkan tinggi :"))
        luas=1/2*a*t
    case _ :
        luas="invalid"
print(luas)
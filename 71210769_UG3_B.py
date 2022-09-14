rdata = int(input("Masukkan range data :"))

dikti = {}
for i in range(rdata):
    if i%2 == 0:
        if i != 0:
            faktor = 1
            for j in range(2,i+1):
                faktor = faktor * j
            dikti[i] = faktor
        else:
            dikti[i] = 1

        
print(dikti)

data = int(input("Data ditampilkan :"))

if data not in dikti:
    print("data tidak ditemukan")
else:
    print("Value dari",data, "adalah", dikti[data])
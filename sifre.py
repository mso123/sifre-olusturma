import random
uzunluk=input("uzunluk giriniz:")
semboller="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sifre=""
for a in range(int(uzunluk)): sifre += random.choice(semboller)
print(sifre)

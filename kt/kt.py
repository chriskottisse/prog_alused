import random

koneminut = input("Palun sisestage kõneminutihind: ")
konedkokku = input("Palun sisestage kõnede koguarv: ")
print(" ")

konekestused = []
konekestvus = random.randint(1, 1000)
kord = 1
while (kord <= int(konedkokku)):
    konekestused.append(konekestvus)
    kord += 1

kone_maksumus = int(koneminut) * int(float(konekestvus))
if konekestvus < 60:
    kone_maksumus = int(koneminut) * int(float(konekestvus))
    print("Kõne maksumus on: "+kone_maksumus)
elif konekestvus > 600:
    kone_maksumus = int(koneminut) * 10
    print("Kõne maksumus on: "+kone_maksumus)
elif konekestvus < 60 & konekestvus > 600:
    kone_maksumus = float(int(konekestvus) / 60) * int(float((koneminut))
    print("Kõne maksumus on: "+kone_maksumus)


kone = [0]
esimenekone = [konekestused[index] for index in kone]
print("Esimese kõne pikkus on "+str(esimenekone)+" sekundit.")

print("Kõne koguarv on: ")
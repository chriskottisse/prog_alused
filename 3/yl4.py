from random import randint
z = int(input("Mitu pöialpoissi tahab õunu? "))
i = 1
while i <= z:
    print(str(randint(1, 2)))
    i += 1

lumele = 14-i
print("Pöidlatele "+str(i))
print(str(lumele)+" õuna jäi Lumivalgekusele.")
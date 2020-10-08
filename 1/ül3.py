#alus = int(input("Sisesta astme alus: "))
#astendaja = int(input("Sisesta astendaja:"))
#vastus = int(alus) ** int(astendaja)
#print("Tulemus on" + str(vastus))

nimi = input("Sistestage oma nimi: ")
lubatudkiirus = input("Sistestage lubatud kiirus (kmh/h): ")
tegelikiirus = input("Sisestage tegelik kiirus: ")
trahv = ((tegelikiirus - lubatudkiirus) * 3)
trahv = min(190, trahv)

print(nimi + ", kiiruse ülteamise eest on trahv " + str(trahv) + " eurot.")
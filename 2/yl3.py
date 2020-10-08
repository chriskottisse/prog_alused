vanus = input("Sisestage oma vanus: ")
sugu = str(input("sisestage oma sugu: "))
treening = input("Sisestage oma treeningu tüüp: ")

meestepulss = 220-int(vanus)
naistepulss = 206-0.88*int(vanus)
tier1minmees = int(meestepulss)*0.5
tier1maxmees = int(meestepulss)*0.7
tier1minnaine = int(naistepulss)*0.5
tier1maxnaine = int(naistepulss)*0.7

if treening == 1 & sugu == m or M:
    print("Pulsisagedus peaks olema vahemikus ",tier1minmees," kuni ",tier1maxmees)
else:
    print("Pulsisagedus peaks olema vahemikus ",tier1minnaine," kuni ",tier1maxnaine)




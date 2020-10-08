ainepunkt = int(input("Sisestage ainepuktide määr: "))
apajakulu = int(26)
weeks = int(input("Sisestage nädalate arv: "))
weektime = ainepunkt * apajakulu / weeks
total = round(weektime, 1)
print("Eeldatav tunde nädalas: " , total , "h.")
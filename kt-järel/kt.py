import random
from random import randint

# sammude arvu sisestamine
sammu_pikkus_meetrites = int(float(input("Mitu meetrit on teie sammu pikkus?: ")))

# nädalas on 7 päeva
paevade_arv = 7

# sammude array
sammude_arv = []

# sammude genereerimine
sammud = [int(i) for i in sammude_arv]
for sammud in range(paevade_arv):
    sammude_arv.append(randint(5000, 15000))
kokku = 0

# päeva kilometraaži valem
def kilomeetrite_arv(sammude_arv, sammu_pikkus_meetrites):
    kilomeetri_arv = (random.choice(sammude_arv) * sammu_pikkus_meetrites)/1000
    if (kilomeetri_arv > 10000):
        return sammude_arv
    else:
        return kilomeetri_arv

# keskmine sammude arv
sammude_summa = sum(sammude_arv)
sammude_summa_2 = len(sammude_arv)
def keskmine_arv(sammude_summa, sammude_summa_2):
    keskmine = sammude_summa/sammude_summa_2
    return keskmine

# sisestatud päevas kilomeetri väljastamine
for paevade_arv in sammude_arv:
    kilomeetri_arv = kilomeetrite_arv(sammude_arv, sammu_pikkus_meetrites)
    print('Kilomeetri arv päaevas: ' +str(kilomeetri_arv))
    kokku += kilomeetri_arv

# kilomeetrite tulemus 7 päeva jooksul
print('Teie tulemus: Jalutasite ' + str(kokku) + ' kilomeetrit ' + str(7) + ' päeva jooksul kokku.')
# nädalas vajaliku kilomeetri väljastamise sõnum
if (keskmine_arv(sammude_summa, sammude_summa_2) < 10000):
    print('Keskmiselt on ' + str(round(keskmine_arv(sammude_summa, sammude_summa_2), 0)) + ' sammu päeavs mis ei ole piisav.')
else:
    print('Keskmiselt on ' + str(round(keskmine_arv(sammude_summa, sammude_summa_2), 0)) + ' sammu päeavs mis on piisav.')
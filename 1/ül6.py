inimesed = 69
bussikohad = 19
busse = inimesed / bussikohad
leftover = inimesed % bussikohad
buss = int(round(busse, 1))
print("Kulub" , buss , "bussi ja maha jääb" , leftover , "inimest.")
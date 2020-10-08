ring = int(input("Sisesta ringide arv: "))
ringi_number = 1
porgand = 0
while(ringi_number <= ring):
    #print(str(ringi_number) + ". ring")
    if(ringi_number%2==0):
    #    print("Said "+str(ringi_number)+" porgandeid.")
        porgand=porgand+ring
    ringi_number += 1
print("Hetkel on kokku "+str(porgand)+" porgandeid.")

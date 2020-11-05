fail = open("C:\\rebased.txt", encoding="UTF-8")
vastuvõetud = []
for rida in fail:
     vastuvõetud.append(int(rida))
fail.close()
aasta = int(input("Palun sisestage aasta: "))
print("Sel aastal oli vastuvõetuid: ")
if (aasta == 2011):
     print(vastuvõetud[0])
if (aasta == 2012):
     print(vastuvõetud[1])
if (aasta == 2013):
     print(vastuvõetud[2])
if (aasta == 2014):
     print(vastuvõetud[3])
if (aasta == 2015):
     print(vastuvõetud[4])
if (aasta == 2016):
     print(vastuvõetud[5])
if (aasta == 2017):
     print(vastuvõetud[6])
if (aasta == 2018):
     print(vastuvõetud[7])
if (aasta == 2019):
     print(vastuvõetud[8])
class Auto:
    def __init__(self, tipus, szin, ar):
        self.tipus = tipus
        self.szin = szin
        self.ar = ar

autok = []

for i in range(3):
    tipus = input("Add meg a típusát: ")
    szin = input("Add meg a színét: ")
    ar = int(input("Add meg az árát: "))
    autok.append(Auto(tipus, szin, ar))
    
legdragabb = autok[0]
for auto in autok:
    if auto.ar > legdragabb.ar:
        legdragabb = auto

fajl = open("autok.txt", "w", encoding="utf-8")
fajl.write(legdragabb.tipus + " típusú " + legdragabb.szin + " színű autó a legdrágább: " + str(legdragabb.ar) + " Ft")
fajl.close()

keresett = input("Keresett szín: ")
for auto in autok:
    if auto.szin == keresett:
        print(auto.tipus, auto.szin, auto.ar)

print("Autók összértéke:", sum(auto.ar for auto in autok))


# variable


aktion = input("Welche Aktion willt du? (+/-/*/:)")
print("Aktion ", aktion, " wird ausgrführt...")

zahl11 = input("Bitte erste zahl eingeben")
zahl22 = input("Bitte die 2 zahl eingeben")
zahl1 = int(zahl11)
zahl2 = int(zahl22)

# if(zahl1 == 0)
#     print("man darf nicht durch null rechnen")
#
# if(zahl2 == 0)
#     print("man darf nicht durch null rechnen")

if(aktion == "*"):
    print("Multiplikation ausgewählt.")
    ergebnis = zahl1*zahl2
    print("das ergebnis ist", ergebnis)
if(aktion == "+"):
    print("plus ausgewählt.")
    ergebnis = zahl1+zahl2
    print("das ergebnis ist", ergebnis)
if(aktion == "-"):
    print("Minus ausgewählt.")
    ergebnis = zahl1-zahl2
    print("das ergebnis ist", ergebnis)
if(aktion == ":"):
    print("division ausgewählt.")
    ergebnis = zahl1/zahl2
    print("das ergebnis ist", ergebnis)



#zahl2 = int(23)

#zahlA = "123"
#zahlB = "456"
#print(zahlA+zahlB)
#Ausgabe: 123456, weil es sich hier um einen STRING handelt!

#zahlC = 987

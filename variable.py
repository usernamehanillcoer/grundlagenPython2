# variable

a = 10
b = 20
 summe = a + b

 print("Summe von", a, " + ", b, " = ", summe)

aktion = input("Welche Aktion willt du? (+/-/*/:)")
print("Aktion ", aktion, " wird ausgrführt...")

zahl1 = print("Bitte erste zahl eingeben")
zahl2 = print("Bitte die 2 zahl eingeben")

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

#Töö "Vigade otsing -2" Sirakus
print("***NUMBER MÄNGU ***")
print()
#Seitsmes reas puudus sulg ja oli üleliigne. Ja puudus break
while 1:
    try:
        a=abs(int(input("Sisestage täisarv => ")))
        break
    except ValueError:
         print("See ei ole täisarv")
         break
#Ridadel 19, 20 ja 21 oli lisasumma võrdne
if a==0:
    print("Nulliga pole mõtet midagi teha")
else:
#
    print("Määrake, kui palju on paaris ja mitu paaritu numbrit")
    print()
    c=b=a
    paaris=0
    paaritu=0
    while b>0:
        if b%2==0:
            paaris+=1
        else:
            paaritu+=1
        b=b//10
    print("Isegi numbrid:", paaris)
    print("Kummalised numbrid:", paaritu)
    print()
#
    print("*Pöörake* sisestatud number ümber")
    print()
    b=0
    while a>0:
        number=a%10
        a=a//10
        b=b*10
        b+=number
    print("*Pööratud* number", b)
    print()
#
    print("Syracuse hüpoteesi testimine")
    print()
    if c%2==0:
        print("s on paarisarv. Jagage 2 -ga.")
    else:
        print("s on paaritu arv. Korrutage 3 -ga, lisage 1 ja jagage 2 -ga.")
    while c>1:
        if c%2:
            c=3*c+1
        c//=2
        print(c)
    print()
    print("Hüpotees on õige")
















print("***NUMBER MÄNGU ***")
print()
#Kaheksandal real puudus mitu silgu
while 1:
    try:
        a=abs(int(input("Sisestage täisarv => ")))
        break
    except ValueError:
         print("See ei ole täisarv")
         break
#Puudus mitu silgu ja katsekus break
if a==0:
    print("Nulliga pole mõtet midagi teha")
else:
#Üheksateistkümnendal ja kahekümnendal real peaks olema täpselt üleliigne, kahekümne esimesel peaks olema koolon ning kahekümne kolmandal ja kahekümne viiendal oli vaja plussid ümber korraldada
    print("Määrake, kui palju on paaris ja mitu paaritu numbrit")
    print()
    c=b=a
    paaris=0
    paaritu=0
    while b>0:
        if b%2==0:
            paaris+=1
        else:
            paaritu+=1
        b=b//10

    print("Isegi numbrid:", paaris)
    print("Kummalised numbrid:", paaritu)
    print()
#Kolmekümne neljandal puudus sulg ja kolmekümne kaheksandal oli vaja Pluss ümber korraldada
    print("*Pöörake* sisestatud number ümber")
    print()
    b=0
    while a>0:
        number=a%10
        a=a//10
        b=b*10
        b+=number
    print("*Pööratud* number", b)
    print()
#
    print("Syracuse hüpoteesi testimine")
    print()
    if c%2==0:
        print("s on paarisarv. Jagage 2 -ga.")
    else:
        print("s on paaritu arv. Korrutage 3 -ga, lisage 1 ja jagage 2 -ga.")
    while c>1:
        if c%2:
            c=3*c+1
        c//=2
        print(c)
    print()
    print("Hüpotees on õige")
from random import *
from datetime import *



#24




#23




#22




#21


#20







#19




#18




#17




#16






#15
katsed=0
while True:
    vastus=input("Osta elevant ära! Kirjuta 'elevant': ")
    katsed+=1

    if vastus.lower()== 'elevant':
        print(f"Õige! Ostsid elevanti ära {katsed} katsega.")
        break
    else:
        print("Vale vastus. Proovi uusti.")




#14 Korrutustabel
for j in range(1,11):
    for i in range(1, 11):
        print(f"{j*i:4}",end=" ")
    print()
    




#13 Ruutude ja kuupide tabel
print("arv ruut kuup")
print()

for i in range(1, 11):
    ruut=i**2
    kuup=i**3
    print(f"{i:2} {ruut:2} {kuup:3}")





#12 Pank
algsumma=float(input("Mis summa paneme panka?"))
alg=lõppsumma=algsumma
intress=randint(1,10)
print(f"Paned panka summa, mis võrdub {algsumma}. Intress on {intress}")
aastad=int(input("Mitmeks aastaks?"))
print("Aasta Algsumma Intress Aasta_lõpuks")
for i in range(1,aastad+1):
    intsumma=(algsumma*intress)/100
    lõppsumma=algsumma+intsumma
    print(f"{i} {algsumma} {intsumma} {lõppsumma}")
    algsumma=lõppsumma
print(f"Summa kokku: {lõppsumma} Eur")
print(f"Kasum: {lõppsumma-alg} Eur")






#11 Arvamismäng
number=randint(1,100)
katsed=3
while katsed>0:
    külaline=int(input("Arva ära arv vahemikus 1 kuni 100: "))
    if külaline==number:
        print("Palju õnne, arvasite numbri ära! ")
        break
    else:
        katsed -=1
        print(f"Vale! Teil on jäänud {katsed} katset. ")
        if katsed==0:
            print(f"Vabandust, olete andnud endast parima. Varjatud number oli {number}. ")
            veelkord=input("Kas sa tahad arvata? ").lower
            if veelkord.lower()=="ei":
                break
            else:
                katsed=3




#10 Viisikud
for arv in range(1, 101):
    if arv %5==0:
        print(arv)




#9 Pisike korrutustabel
korrutamine=["5"]
arv=["1", "2", "3", "4", "5", "6","7","8","9","10"]
for i in range(10):
    tulemus=int(arv[i])*5
    print(f"{arv[i]}*5={tulemus}")


korrutamine=5
for i in range(1,11):
    tulemus=(i)*5
    print(f"{i}*5={tulemus}")



#8 Paaris ja paaritu
paaris=0
paaritu=0
for i in range(1, 101):
    if i%2==0:
        print(f"{i}-paaris")
        paaris+=1
    else:
        print(f"{i}-paaritu")
        paaritu+=1

print(f"Paarisarvude arv: {paaris}")
print(f"Paaritute arvude arv: {paaritu}")


#7 Loto
from random import*

for i in range(5):
    number=randint(0,9)
    print(number, end="")
print()



#6 Tärnid





#5




#4




#3
k=0
while True:
    k+=1
    a=randint(1,50)
    b=randint(1,50)
    p=0
    while p!=3:
        p+=1
        v=int(input("Millega võrdub {0}+{1}".format(a,b)))
        if v==a+b:
            print("Tubli!")
            break
        else:
            print("Mõtle veel!")
    print("{0}+{1}={2}".format(a,b,a+b))

    if k==5:break





#2
summa=0
for i in range(10):
    arv=float(input("Sisesta arv: "))
    summa+=arv
print(summa)

summa=0
i=0
while True:
    i+=1
    arv=float(input("Sisesta arv: "))
    summa+=arv
    if i==10: break
print(summa)


#1
nimi=input("Mis on sinu nimi?").capitalize()
mitu=int(input("Mitu korda tervitada?"))
for i in range(1, mitu+1):
    print("Ole tervitatud, "+nimi+", "+str(i)+". korda.")




#Praktiline töö "Tsükkel"
#0
while True:
    v=input("Kas sul on trenn?").lower()
    if v=="jah": break

print("2. varindt -while tingimusega-")
v=""
while v!="jah":
    v=input("Kas sul on trenn?").lower()




paevad=["Esmaspäev", "Teisipäev", "Kolmapäev", "Neljapäev", "Reede", "Laupäev", "Pühapäev"]
trennid=["trenn on olemas", "trenn ei ole olemas", "trenn on olemas", "trenn ei ole olemas", "trenn on olemas", "trenn on olemas", "trenn ei ole olemas"]
for i in range(7):
    print(paevad[i]+"-"+trennid[i])





#3 Komm
while True:
    v=input("Tahan komme!").lower()
    if v=="komm": break

print("2. varindt -while tingimusega-")
v=""
while v!="komm":
    v=input("Tahan komme!").lower()




#2 Nädala päevad
paevad=["Esmaspäev", "Teisipäev", "Kolmapäev", "Neljapäev", "Reede", "Laupäev", "Pühapäev"]
tunnid=["8 tundi", "9 tundi", "8 tundi", "5 tundi", "6 tundi", "tunde pole", "tunde pole"]
for i in range(7):
    print(paevad[i]+"-"+tunnid[i])





#1 Poes korduslausega
arve_nr=datetime.now() #date.today()
print(arve_nr)
tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
summa=0
toodet=["Piim", "Leib", "Komm"] #index 0-1-2
for i in range(3): #i=0, i=1, i=2
    toode1=toodet[i]
    hind=randint(50,150)/100
    v=input("Toode:"+toode1+" Hind: "+str(hind)+"\nKas tahad osta?").lower()
    if v=="jah":
        mitu=int(input("Mitu?"))
        tsekk+=toode1+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
        summa+=mitu*hind

tsekk+="Kokku maksta: "+str(summa)
print(tsekk)
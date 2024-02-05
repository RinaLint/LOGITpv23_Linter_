#Variant 2


#5
n=int(input("sisesta number")) #numbrite päring
summa=0 #muutuv summa
korrutis=1 #muutuv toode
while n>0:
    praegune_number=n%10
    summa+=praegune_number  #kokkuvõte
    korrutis*=praegune_number #korrutada
    n=n//10
print("summa:", summa) #väljamakse summa
print("korrutis:", korrutis) #määra väljund


#4
n=int(input("Введите число:")) #numbrite päring
vastastikune_number=int(str(n)[::-1]) #pöörake numbrit
print(f"Обратное число: {vastastikune_number}") #järeldus





#3
#Juhusliku arvu importimine
from random import *
number=randint(1,100)
katsed=10
#Anname kasutajale 10 katset arvu ära arvata
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
#Kui kasutaja ei soovi otsustada, siis tsükkel katkeb. Kui ta tahab, katsed taastatakse 
            veelkord=input("Kas sa tahad arvata? ").lower()
            if veelkord.lower()=="ei":
                break
            else:
                katsed=10





#2
L=random
summ=0 #muutuja 0
print(f"Numbriseeria summa vahemikus 0 kuni {L} kaasa arvatud:")
summ+=i #loendage numbreid 0-st muutujani L
print("Numbrite summa 0 kuni L on: ", summ) #järeldus



#1 Jaanes
#Palume kasutajal sisestada arv vahemikus 1 kuni 9
n=int(input("Sisestage arv vahemikus 1 kuni 9: "))
#Funktsiooni print abil valime sümbolid 
for i in range(n):
    print("(\_/)", end=" ")
    if i<n-1:
        print(" ", end=" ")
print( )
#ja seejärel kontrollige muutujat. See jagab jänesed omavahel ära
for i in range(n):
        print("(o o)", end=" ")
        if i<n-1:
            print(" ", end=" ")
print( )
for i in range(n):
    print("/ | \*", end="")
    if i<n-1:
        print(" ", end=" ")
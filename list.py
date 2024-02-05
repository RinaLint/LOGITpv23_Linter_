nimed=["Mati","Kati"]
while True:
    valik=input("Andmete lisamine-add\nAndmete nätamine-show\nAndmete kustutamine-del\nJärjendi pööramine-rev\nAndmete kustutamine-clear\nAndmete sortimise-sort\nAndmete otsing-ots\n").lower()
    if valik=="add":
        valik=input("Kaslisame mitu inimest(mitu) või positsioonile (pos)\n").lower()
        if valik=="mitu":
            mitu=int(input("Mitu inimest lisamine? "))
            for i in range(mitu):
                nimi=input("Sisesta nimi: ").capitalize()
                nimed.append(nimi)
        else:
            indeks=int(input("Kuhu lisamine? "))
            nimi=input("Mis nimi: ").capitalize()
            nimed.insert(indeks,nimi)
    elif valik=="del":
        valik=input("Kas kustutamine nimi või indeksi järgi (ind)?")
        if valik=="nimi":
            nimi=input("Mis nimi on vaja kustutada?")
            kogus=nimed.count(nimi)
            if kogus>0:
                for i in range(kogus):
                    nimed.remove(nimi)
            else:
                print(f"Nimi {nimi} ei ole nimekirjas")
        else:
            indeks=int(input("Mis on järjekorranumber?"))
            nimed.pop(indeks-1)
    elif valik=="show":
        print(nimed)
    elif valik=="rev":
        nimed.reserve()
        print(nimed)
    elif valik=="sort":
        nimed.sort()
        print(nimed)
    elif valik=="clear":
        nimed.clear()
        print(nimed)
    elif valik=="ots":
        ind=-1
        nimi=input("Mis nime otsime? ")
        if nimed.count(nimi)>0:
            for nim in nimed:
                if nim==nimi:
                    ind=nimed.index(nimi,ind+1)
                    print(f"{nimi} on indeksiga {ind}")
        else:
            print(f"{nimi} ei ole nimekirjas")
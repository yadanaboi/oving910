# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 14:32:57 2021

@author: Yadana
"""

class Sporsmaal:
    def __init__(self, sporsmaal, svarAlternativer, korrekt_svar=0):
        self.sporsmaal = sporsmaal
        self.svarAlternativer = svarAlternativer
        self.korrekt_svar = korrekt_svar
        
    def __str__(self):
        resultat = self.sporsmaal + "\nSvaralternativer:\n"
        for index, verdi in enumerate(self.svarAlternativer):
            resultat += f"{index}: {verdi}\n"
        return resultat
    
    def sjekk_svar(self, svaret):
        if svaret == self.korrekt_svar:
            return True
        else:
            return False
    
    def korrekt_svar_tekst(self):
        return self.svarAlternativer[self.korrekt_svar]

class Spiller:
    def __init__(self, navn, svar="", poengsum=0):
        self.navn = navn
        self.poengsum = poengsum
        self.svar = svar
        
def spilleliste():
    print("temp")
        
def klasseManager(filnavn="sporsmaalsfil.txt"):
    with open (filnavn, "r", encoding="utf-8") as r:
        linjeleser = r.readlines()
        listami = []
        for linje in linjeleser:
            spørsmål = linje.split(":")
            alternativer = spørsmål[2].strip().strip("[]").split(", ")
            svar = int(spørsmål[1].strip())
            spørsmaul = spørsmål[0].strip()
            listami.append(Sporsmaal(spørsmaul, alternativer, svar))
        return listami




if __name__ == "__main__":
    klasseListe = klasseManager()

    antallSpillere = int(input("Antall spillere: "))

    navnliste = []
    for i in range(antallSpillere):
        navnliste.append(input(f"Spiller {i+1} navn: "))

    spillerListe = []
    for i in range(len(navnliste)):
        spillerListe.append(Spiller(navnliste[i]))

    for objekt in klasseListe:
        print(objekt.__str__())

        for i in range(antallSpillere):
            spillerListe[i].svar = int(input(f"{spillerListe[i].navn} svar: "))

        print("korrekt svar: " + objekt.korrekt_svar_tekst())
        print()

        for i in range(antallSpillere):
            if objekt.sjekk_svar(spillerListe[i].svar):
                print(f"spiller{i+1}: riktig")
                spillerListe[i].poengsum += 1
            else:
                print(f"spiller{i+1}: feil")

        print()

    for i in range(antallSpillere):
        print(f"{spillerListe[i].navn}: {spillerListe[i].poengsum} poeng")

    vinnerNavn = ""
    vinnerPoeng = 0

    for i in range(antallSpillere):
        if spillerListe[i].poengsum > vinnerPoeng:
            vinnerNavn = spillerListe[i].navn
            vinnerPoeng = spillerListe[i].poengsum

    print()
    print(f"Vinneren er: {vinnerNavn} med {vinnerPoeng} poeng.")
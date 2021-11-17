# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 09:23:12 2021

@author: Erlend Tøssebro
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
    player1 = 0
    player2 = 0
    
    for objekt in klasseListe:
        print(objekt.__str__())
        svar1 = int(input("Svar spiller 1: "))
        svar2 = int(input("Svar spiller 2: "))
        print("korrekt svar:" + objekt.korrekt_svar_tekst())
        if objekt.sjekk_svar(svar1):
            print("\nspiller1: riktig")
            player1 += 1
        else:
            print("\nspiller1: feil")
        
        if  objekt.sjekk_svar(svar2):
            print("spiller2: riktig")
            player2 += 1
        else:
            print("spiller2: feil")
    print(f"spiller1: {player1}" )
    print(f"spiller2: {player2}")
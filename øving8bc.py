# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 10:24:29 2021

@author: Yadana
"""

class A():
    def __init__(self, question, answer, alternatives):
        self.question = question
        self.answer = answer
        self.alternatives = alternatives
        
    def __str__(self):
        tekst = self.question + "\n"
        for altNummer, altTekst in enumerate(self.alternatives): #teller allternativene og legger til nr
            tekst +=f" {altNummer + 1} {altTekst} \n"
        return tekst
    
    def sjekk_svar(self, sjekk: int):
        return sjekk == self.answer

quiz = list()

quiz.append(A("Hvem er den mest kjente sjimpansen i Norge?", 2, ["Erik", "Julius", "Trym"]))
quiz.append(A("Hvor mange barnebarn har mormor fra Mormor og de 8 ungene?", 3, [2, 10, 8]))

for spm in quiz:
    print(spm)
    
    valg = int(input(f"ditt svar er (1-{len(spm.alternatives)}): ")) #skriver ut ditt svar og lengden av alternativene
    if spm.sjekk_svar(valg): 
        print("Gratulerer")
    else:
        print("Du må øve litt mer")
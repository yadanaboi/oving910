# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 15:16:05 2021

@author: Yadana
"""

import unittest
from oving_10e import Sporsmaal

class TestSporsmaal(unittest.TestCase):
    def test_sjekk_svar(self):
        sporsmaal1 = Sporsmaal(0, 4, 2) # lage instanse av klassen sporsmal
        sporsmaal1.sjekk_svar(2) # sjekke sjekksvar-metode
        self.assertEqual(sporsmaal1.korrekt_svar, 2) # sjekke at det korrekte svaret er altern. 2
        sporsmaal1.sjekk_svar(3)
    
    #def test_korrekt_svar_tekst(self):
        
        
if __name__ == "__main__":
    unittest.main()


# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 14:52:27 2021

@author: Yadana
"""

import unittest
from oving_10 import sjekk_svar(self)

class TestSporsmaal(unittest.TestCase):
    def test_sjekk_svar(self):
        self.assertFalse(sjekk_svar(0))
        self.assertFalse(sjekk_svar(2))
        self.assertFalse(sjekk_svar(1))


if __name__ == "__main__":
    unittest.main()        

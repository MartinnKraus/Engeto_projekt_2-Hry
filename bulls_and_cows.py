"""
bulls_and_cows.py: druhý projekt do Engeto Online Python Akademie, hra Bulls and cows
author: Martin Kraus
email: martinnkraus@gmail.com
discord: martin_64789
"""

import random

#random.seed(0)

def generuj_nahodne_unikatni():
    """
    Generuje náhodné 4místné číslo dle kritérií:
        -nezačíná na 0
        -Neobsahuje duplicitní cifry
    """
    dostupna_cisla = list(range(10))
    cislo_vystup = ""
    vybrane_cislo = random.randint(1, 9)
    cislo_vystup += str(vybrane_cislo)
    dostupna_cisla.remove(vybrane_cislo)
    for i in range(3):
        nah_index = random.randint(0, 9 - i)
        vybrane_cislo = dostupna_cisla[nah_index]   #Vyber číslo ze zbylých čísel
        cislo_vystup += str(vybrane_cislo)
        dostupna_cisla.remove(vybrane_cislo)
    return cislo_vystup

print(generuj_nahodne_unikatni())
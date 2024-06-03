"""
bulls_and_cows.py: druhý projekt do Engeto Online Python Akademie, hra Bulls and cows
author: Martin Kraus
email: martinnkraus@gmail.com
discord: martin_64789
"""

import random, time

random.seed(0)

def generuj_nahodne_unikatni() -> str:
    """
    Generuje náhodné 4místné číslo dle kritérií, kvůli kontrole v datovém formátu str:
        -nezačíná na 0
        -Neobsahuje duplicitní cifry
    """
    dostupna_cisla = list(range(10))
    cislo_vystup = ""
    vybrane_cislo = random.randint(1, 9)
    cislo_vystup += str(vybrane_cislo)
    dostupna_cisla.remove(vybrane_cislo)
    for i in range(3):
        nah_index = random.randint(0, 8 - i)
        vybrane_cislo = dostupna_cisla[nah_index]   #Vyber číslo ze zbylých čísel
        cislo_vystup += str(vybrane_cislo)
        dostupna_cisla.remove(vybrane_cislo)
    return cislo_vystup

def uvitani():
    print(
        """Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Rules for the number:
    - 4 digits number
    - Doesn't begin with zero
    - Only unique digits
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:"""
    )


def pocet_bulls_a_cows(cislo_vzor: str, cislo_hadane: str) -> list:
    """
    Vrací ve stringu počet bulls a počet cows
    """
    pocet_bulls = 0
    pocet_cows = 0
    for index, cislo in enumerate(cislo_hadane):
        if cislo_vzor[index] == cislo:
            pocet_bulls += 1
        elif cislo in cislo_vzor:
            pocet_cows += 1
    return(f"{pocet_bulls} {"bulls" if pocet_bulls != 1 else "bull"}, {pocet_cows} {"cows" if pocet_cows != 1 else "cow"}")

def obsahuje_duplicity(vstup: str) -> bool:
    """
    Kontrola, zda vstup od uživatele obsahuje duplicity
    """
    for znak in vstup:
        if vstup.count(znak)>1:
            return True
    else:
        return False    #pokud ani jeden znak není duplicitní


def obsahuje_neciselny_znak(vstup):
    """
    Vrací True, pokud vstup obsahuje nějaký nečíselný znak
    """
#Promyslet, zda je efektivní
    try:
        zkus_prevest = int(vstup)
    except:
        return True
    else:
        return False

def uzivatelsky_vstup_v_poradku(vstup: str) -> bool:
    """
    Zkontroluje vstup od uživatele, zda splňuje tyto požadavky:
        Je délky 4 znaků
        Cifry neobsahují duplicity
        Nezačíná nulou
        Obsahuje pouze číselné znaky
    """
    if len(vstup) != 4:
        print(f"Your input '{vstup}' isn't 4 digit number.\nEnter new number:")
        return False
    elif obsahuje_duplicity(vstup):
        print(f"Your input '{vstup}' doesn't contain unique digits.\nEnter new number:")
        return False
    elif vstup[0] == "0":
        print(f"Your input '{vstup}' begins with zero.\nEnter new number:")
        return False
    elif obsahuje_neciselny_znak(vstup):
        print(f"Your input '{vstup}' contains non-digit symbol.\nEnter new number:")
        return False
    else:
        return True

def slovni_vyhodnoceni(pokusu: int):
    """
    Vrátí slovní vyhodnocení na základě počtu pokusů k dohrání hry
    """
    if pokusu <= 4:
        return "amazing :-o"
    elif pokusu <= 7:
        return "average :-)"
    elif pokusu <= 11:
        return "not so good :-/"
    else:
        return "bad, you should train ;-)"

def main():
    #generuj náhodné číslo
    tajne_cislo = generuj_nahodne_unikatni()
    #uvítej uživatele
    uvitani()
    pocet_pokusu = 0
    while True:
        print("-" * 47)
        pocet_pokusu += 1
    #zadej cislo
        cislo_pokus = input(">>> ")
    #!!kontrola vstupu od uživatele
        if uzivatelsky_vstup_v_poradku(cislo_pokus):
            if cislo_pokus == tajne_cislo:
                print(f"Correct, you've guessed the right number in {pocet_pokusu} guesses!",
                      "-" * 47,
                      f"That's {slovni_vyhodnoceni(pocet_pokusu)}")
                break
            else:
                print(pocet_bulls_a_cows(tajne_cislo, cislo_pokus))

                #pocet_bulls_a_cows

    #vyhodnoť číslo, pokud se neshoduje, porovnej bulls and cows


if __name__ == "__main__":
    main()
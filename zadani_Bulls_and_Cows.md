Bulls & Cows
Tvým úkolem bude vytvořit program, který by simuloval hru Bulls and Cows. Po vypsání úvodního textu uživateli, může hádání tajného čtyřciferného čísla začít.

Program bude obsahovat:
Na úvod si svůj soubor popiš hlavičkou, ať se s tebou můžeme snadněji spojit:
Ukázka kódu1
ZKOPÍROVAT KÓD
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Petr Svetr
email: petr.svetr@gmail.com
discord: Petr Svetr#4490
"""

import ...
Program pozdraví užitele a vypíše úvodní text
Program dále vytvoří tajné 4místné číslo (číslice musí být unikátní a nesmí začínat 0)
Hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla, pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky
Program vyhodnotí tip uživatele
Program dále vypíše počet bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění), příp. cows/ cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění). Vrácené ohodnocení musí brát ohled na jednotné a množné číslo ve výstupu. Tedy 1 bull a 2 bulls (stejně pro cow/cows).
Úvodní text:
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------
Příklad hry s číslem 2017:
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------
>>> 1234
0 bulls, 2 cows
-----------------------------------------------
>>> 6147
1 bull, 1 cow
-----------------------------------------------
>>> 2417
3 bulls, 0 cows
-----------------------------------------------
>>> 2017
Correct, you've guessed the right number
in 4 guesses!
-----------------------------------------------
That's {amazing, average, not so good, ...}
Program toho může umět víc. Můžeš přidat například:

počítání času, za jak dlouho uživatel uhádne tajné číslo
uchovávat statistiky počtu odhadů jednotlivých her
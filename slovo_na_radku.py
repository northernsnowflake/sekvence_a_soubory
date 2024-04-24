"""
Stáhni si soubor index.dic se všemi českými slovy.

(Seznam slov vytvořil Petr Kolář a další a je poskytován pod licencí GNU GPL 2.)

Soubor není úplně „čistý“. Vytvoř seznam, kde budou opravdu jen slova:

Vytvoř prázdný seznam.
Projdi index.dic po řádcích a postupně přidávej slova do seznamu.
Na začátku souboru (řádek 0) je údaj s počtem řádků, ten neber jako slovo. (Jak při průchodu souborem – sekvencí – zjistíš číslo prvku?)

Některá slova obsahují další informace za znakem /. Tyto informace (i s lomítkem) ze slov odstraň. Bude se hodit umět slovo rozdělit podle /, viz tahák na seznamy.

Můžeš se rozhodnout odstranit i slova začínající velkým písmenem. (Většinou jde o vlastní jména a zkratky).
"""

with open('index.dic', encoding= 'utf-8') as soubor:
    seznam = []
    for radek in soubor:
        radek = radek.rstrip()
        if "/" in radek:
            pozice = radek.index("/")
            radek = radek[:pozice]
        if not radek[0].isupper():
            seznam.append(radek)
        #print(' ',radek)
    seznam.pop(0)

"""
Slova ze seznamu vytvořeného výše ulož do souboru slova.txt, 
kde bude na každém řádku jedno slovo."""

with open('slova.txt', encoding = 'utf-8',mode = 'w') as soubor2:
    for polozka in seznam:
        polozka = polozka.rstrip()
        print(polozka, file=soubor2) #zapiš do souboru slova.txt soubor2

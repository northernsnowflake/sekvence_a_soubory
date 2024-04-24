import random
"""
Karta pro nás v tomto projektu bude dvojice (hodnota, barva). 
Aby se karty dobře porovnávaly, hodnota bude vždy číslo: 2-10 budou karty s čísly, 11 kluk, 12 dáma, 13 král, 1 eso. Barva pak bude jeden z řetězců 'Sr', 'Pi', 'Ka', 'Kr'.

Následující funkce umí vytvořit balíček a popsat kartu trochu hezčím způsobem.
Zkopíruj si je a prostuduj.
"""
def vytvor_balicek():
    """Vrátí nový zamíchaný balíček karet."""
    karty = []
    for barva in 'Sr', 'Pi', 'Ka', 'Kr':
        for hodnota in range(1, 14):
            karta = hodnota, barva
            karty.append(karta)
    random.shuffle(karty)
    return karty


def popis_kartu(karta):
    """Popíše danou kartu; vrací řetězec jako "7♣", "A♠" nebo "Q♥"."""
    hodnota, barva = karta
    if hodnota == 11:
        popis_hodnoty = 'J'
    elif hodnota == 12:
        popis_hodnoty = 'Q'
    elif hodnota == 13:
        popis_hodnoty = 'K'
    elif hodnota == 1:
        popis_hodnoty = 'A'
    elif hodnota == 10:
        # Aby byly všechny hodnoty jednopísmenné,
        # a líp se to pak vypisovalo,
        # desítku označíme římským číslem.
        popis_hodnoty = 'X'
    else:
        popis_hodnoty = str(hodnota)

    if barva == 'Sr':
        popis_barvy = '♥'
    elif barva == 'Pi':
        popis_barvy = '♠'
    elif barva == 'Ka':
        popis_barvy = '♦'
    else:
        popis_barvy = '♣'

    return popis_hodnoty + popis_barvy

"""
# Napiš proceduru, která vytvoří balíček a „hezky“ vypíše 
# všechny karty v něm, každou na jeden řádek. Například:

# 9♠
# K♣
"""
# balicek = vytvor_balicek()
# for karta in balicek:
#     print(popis_kartu(karta))



"""
Napiš funkci porovnej_karty podle této hlavičky:

def porovnej_karty(karta_a, karta_b):
    # Porovná hodnoty dvou karet.
    # Vrací:
    # * 'A', je-li lepší karta_a,
    # * 'B', je-li lepší karta_b,
    # * None, mají-li stejnou hodnotu.
    
"""
def porovnej_karty(karta_a, karta_b):
    """Porovná hodnoty dvou karet.
    Vrací:
    * 'A', je-li lepší karta_a,
    * 'B', je-li lepší karta_b,
    * None, mají-li stejnou hodnotu.
    """
    if karta_a[0] > karta_b[0]:
        return 'A'

    elif karta_b[0] > karta_a[0]:
        return 'B'

    elif karta_a[0] == karta_b[0]:
        return None


"""
Stav hry bude trojice seznamů: balíček hráče A, balíček hráče B, 
a karty co jsou aktuálně na stole.

Následující funkce takový stav hry vytvoří.
"""

def rozdej_balicky():
    """Rozdá trojici balíčků: dva pro hráče a jeden pro "stůl"

    Připraví zamíchaný balíček všech karet.
    Balíček pro hráče A bude jeho první polovina; balíček pro hráče B druhá
    """
    balicek = vytvor_balicek()

    # "polovina" musí být celé číslo, protože pak jí číslujeme seznam.
    # Proto celočíselné dělení. Zbytek po dělení ignorujeme.
    polovina = len(balicek) // 2

    balicek_a = balicek[:polovina]
    balicek_b = balicek[polovina:]

    return balicek_a, balicek_b, []

#Úkol 6 - stav hry
# karty = []

# balicek_a,balicek_b,stul = rozdej_balicky()
# print('Hráč A', "", 'Hráč B'  )
# for i,j in zip(balicek_a,balicek_b):
#         print(popis_kartu(i), "    ", popis_kartu(j))
"""
Vytvoř funkci vyloz_karty, která dostane stav hry a simuluje jedno vyložení karet.

def vyloz_karty(balicky):
    Vyloží karty obou hráčů na stůl.

    "balicky" je trojice: balíček hráče A, balíček hráče B, karty na stole.

    Každý z hráčů vyloží poslední kartu svého balíčku na stůl.
    Nemá-li hráč co vyložit, nastane výjimka `SystemExit`.
    (To zjednodušuje zbytek hry.)

    Funkce vypisuje co dělá pomocí "print".
    (To taky zjednodušuje zbytek hry.)
    
    balicek_a, balicek_b, na_stole = balicky
    ...
Zkus:
Lízni poslední kartu balíčku A. To bude karta A.
Pokud to nešlo (balíček A byl prázdný):
Vyhoď výjimku SystemExit('Hráč B vyhrál')
Zkus:
Lízni poslední kartu balíčku B. To bude karta B.
Pokud to nešlo (balíček B byl prázdný):
Vyhoď výjimku SystemExit('Hráč A vyhrál')
Vypiš, že Hráč A hraje kartu A
Vypiš, že Hráč B hraje kartu B
Do karet na stole přidej kartu A
Do karet na stole přidej kartu B
(Výjimka SystemExit způsobí skončení programu bez chybové hlášky. 
Ta a výpisy pomocí print nejsou ve funkci která něco „počítá“ úplně „košer“,
 ale zjednoduší ti práci.)
"""

def vyloz_karty(balicky):
    """Vyloží karty obou hráčů na stůl.
    "balicky" je trojice: balíček hráče A, balíček hráče B, karty na stole.

    Každý z hráčů vyloží poslední kartu svého balíčku na stůl.
    Nemá-li hráč co vyložit, nastane výjimka `SystemExit`.
    (To zjednodušuje zbytek hry.)

    Funkce vypisuje co dělá pomocí "print".
    (To taky zjednodušuje zbytek hry.)
    """
    balicek_a, balicek_b, na_stole = balicky
    if balicek_a == None or balicek_b == None:
        return 'prázdný balíček'
    try:
        karta_A = balicek_a.pop()
    #karta_A = balicek_a[-1]
    #balicek_a.pop()
    except:
        if not balicek_a:
            raise SystemExit('Hráč B vyhrál')
    try:
        karta_B = balicek_b.pop()
        # karta_B = balicek_b[-1]
        # balicek_b.pop()
    except:
        if not balicek_b:
            raise SystemExit('Hráč A vyhrál')
    print(f'Hráč A hraje kartu {karta_A}')
    print(f'Hráč B hraje kartu {karta_B}')
    na_stole.append(karta_A)
    na_stole.append(karta_B)
    
    return print(f'na stole je', na_stole)

#Úkol 7 - vyloz_karty(balicky) a text níže
#balicek_a, balicek_b, na_stole = rozdej_balicky()
#balicky = balicek_a, balicek_b, na_stole
#vyloz_karty(balicky)



def valka():
    '''
    Rozdá balíčky, ozdnačí je jako balíček A, balíček B a karty na stole
    '''
    balicek_A, balicek_B, na_stole = rozdej_balicky()
    balicky = balicek_A, balicek_B, na_stole
    kolo = 0
    #karta_A, karta_B = vyloz_karty(balicky)
    while True:
        kolo = kolo + 1
        print('Kolo',kolo)
        #print('Na stole je právě',na_stole, 'karet')
        vyloz_karty(balicky)
        #print('právě vykládám {balicky}')
        #print('Z funkce valka vypisuji balicek na stole', na_stole)

        if na_stole[-2][0] == na_stole[-1][0]:
            print('Válka')
            vyloz_karty(balicky)
            #print('Z funkce valka vypisuji balicek na stole', na_stole)
            vyloz_karty(balicky)
            #print('Z funkce valka vypisuji balicek', na_stole)
            vyloz_karty(balicky)
            #print('Z funkce valka vypisuji balicek', na_stole)
            #vem_ze_stolu_k_hraci(balicek_A, balicek_B, na_stole)
            if na_stole[-1][0] > na_stole[-2][0]:
                print('B je vítěz války')
                vitez = 'B'
                na_stole.reverse()
                for kazda in na_stole:
                    balicek_B.insert(0,kazda)
                N = len(na_stole)
                print(f'Hráč {vitez} bere {N} karet')
                na_stole.clear()
                #print('Balíček B:', balicek_B)
                continue
            if na_stole[-1][0] < na_stole[-2][0]:
                print('A je vítěz války')
                vitez = 'A'
                na_stole.reverse()
                for kazda in na_stole:
                    balicek_A.insert(0,kazda)
                N = len(na_stole)
                print(f'Hráč {vitez} bere {N} karet')
                na_stole.clear()
                #print('Balíček A:', balicek_A)
                continue
        #print(na_stole[-2][0])
        #print(na_stole[-1][0])
        if na_stole[-1][0] > na_stole[-2][0]:
            print('B je vítěz')
            vitez = 'B'
            na_stole.reverse()
            for kazda in na_stole:
                balicek_B.insert(0,kazda)
            N = len(na_stole)
            print(f'Hráč {vitez} bere {N} karet')
            na_stole.clear()
            #print('Balíček B:', balicek_B)
        elif na_stole[-1][0] < na_stole[-2][0]:
            print('A je vítěz')
            vitez = 'A'
            na_stole.reverse()
            for kazda in na_stole:
                balicek_A.insert(0,kazda)
            N = len(na_stole)
            print(f'Hráč {vitez} bere {N} karet')
            na_stole.clear()
            #print('Balíček A:', balicek_A)
    #print(balicek_A)


    #print(balicek_A)
    #print(balicek_B)
    
# def vem_ze_stolu_k_hraci(balicek_A, balicek_B, na_stole):
#     if na_stole[-1][0] > na_stole[-2][0]:
#         print('B je vítěz války')
#         vitez = 'B'
#         na_stole.reverse()
#         for kazda in na_stole:
#             balicek_B.insert(0,kazda)
#         N = len(na_stole)
#         print(f'Hráč {vitez} bere {N} karet')
#         na_stole.clear()
#         pass
#         #print('Balíček B:', balicek_B)
#     if na_stole[-1][0] < na_stole[-2][0]:
#         print('A je vítěz války')
#         vitez = 'A'
#         na_stole.reverse()
#         for kazda in na_stole:
#             balicek_A.insert(0,kazda)
#         N = len(na_stole)
#         print(f'Hráč {vitez} bere {N} karet')
#         na_stole.clear()
#         pass
        #print('Balíček A:', balicek_A)
#valka()
#print(balicek_a, balicek_b, stul)

print(valka())
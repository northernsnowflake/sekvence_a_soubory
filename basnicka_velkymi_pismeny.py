
with open('basnicka.txt', encoding= 'utf-8') as soubor:
    for radek in soubor:
        radek = radek.rstrip() #zprava osekaný (nechci mít zprava prázdný znak)
        radek = radek.upper()
        print(' ',radek)#,end='')
    print()

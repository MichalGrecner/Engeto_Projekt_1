'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive                   
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

oddelovac = "------------------------------"

registrovani_uzivatele = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}

username = str(input("username: "))
password = str(input("password: "))

if username in registrovani_uzivatele and registrovani_uzivatele[username] == password:
    print(oddelovac)
    print(f"Vítej uživateli {username} v textovém analyzátoru")
    print(oddelovac)

else:
    print("špatné jméno/heslo, končím")
    quit()

status = 1
while status:
    vybrany_text_cislo = input("Zadej text k analýze v rozmezí 1 až 3: ")
    if vybrany_text_cislo.isnumeric() and int(vybrany_text_cislo) >= 1 and int(vybrany_text_cislo) <= 3 :
        vybrany_text_cislo = int(vybrany_text_cislo) -1
        status = 0
    else:
        print("Neplatný vstup!")




vycisteny_text = []
vycistene_slovo = str
for slovo in TEXTS[vybrany_text_cislo].split():
    vycistene_slovo = slovo.strip(".:;,")
    if vycistene_slovo.isalnum():
        vycisteny_text.append(vycistene_slovo)

print("vycisteny text: ", vycisteny_text)

# - počet slov,
print("počet slov: ", len(vycisteny_text))

# - počet slov začínajících velkým písmenem
pocet_slov_velke_pismeno = 0
for slovo_velke_pismeno in vycisteny_text:
    if slovo_velke_pismeno[0].isupper():
        pocet_slov_velke_pismeno += 1
print("Počet slov začínajících velkým písmenem: ", pocet_slov_velke_pismeno)

# - počet slov psaných velkými písmeny,
pocet_slov_velkymi_pismeny = 0
for slovo_velkymi_pismeny in vycisteny_text:
    if slovo_velkymi_pismeny.isupper():
        pocet_slov_velkymi_pismeny += 1
        #print(slovo_velkymi_pismeny)
print("Počet slov psané velkými písmeny: ", pocet_slov_velkymi_pismeny)

# - počet slov psaných malými písmeny,
pocet_slov_malymi_pismeny = 0
for slovo_malymi_pismeny in vycisteny_text:
    if slovo_malymi_pismeny.islower():
        pocet_slov_malymi_pismeny += 1

print("Počet slov psané malými písmeny: ", pocet_slov_malymi_pismeny)

# - počet čísel (ne cifer),
# - sumu všech čísel (ne cifer) v textu.
pocet_cisel = 0
suma_cisel = 0
for cislo in vycisteny_text:
    if cislo.isnumeric():
        pocet_cisel += 1
        suma_cisel += int(cislo)
print("Počet čísel: ", pocet_cisel)
print("Součet: ", suma_cisel)

# sloupcový graf
delky_slov = dict()
for slv in vycisteny_text:
    if len(slv) not in delky_slov.keys():
         delky_slov[len(slv)] = 1
    else:
         delky_slov[len(slv)] += 1

print(oddelovac)
print("""Délka |    Výskyt    | Počet""")
for radek in sorted(delky_slov.keys()):
    sloupec = "*" * delky_slov[radek]
    print(oddelovac,
    f"{radek:>6}|{sloupec:<14}|{delky_slov[radek]}",
    sep="\n")

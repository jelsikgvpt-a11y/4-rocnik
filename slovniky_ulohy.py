# ============================================================
#  SLOVNÍKY – ÚLOHY NA PRECVIČOVANIE
#  Každú úlohu rieš pod jej zadaním. Údaje sú pripravené.
# ============================================================


# ------------------------------------------------------------
# ÚROVEŇ 1 – ZÁKLADY
# ------------------------------------------------------------

# Úloha 1: Telefónny zoznam
# a) Pridaj kontakt "Mária" s číslom "0911 222 333".
# b) Zmeň Petrovo číslo na "0905 999 888".
# c) Vymaž kontakt "Ján".
# d) Vypýtaj si meno od používateľa (input) a vypíš jeho číslo,
#    alebo správu "Kontakt neexistuje" (použi get()).
kontakty = {"Peter": "0905 123 456", "Ján": "0918 654 321", "Eva": "0944 111 222"}
kontakty["Mária"] = "0911 222 333" #a
kontakty["Peter"] = "0905 999 888" #b
kontakty.clear("Ján") #c
vstup = kontakty.get(input("Zadaj mi meno")) #d
if vstup == None:
    print("Kontakt neexistuje")
else:
    print(vstup)

#slov["a"] = slov.get("a", 0) + 1

# Úloha 2: Nákupný košík
# Vypočítaj celkovú cenu nákupu (cena * množstvo pre každú položku).
# Vypíš aj každú položku v tvare: "rožok: 10 ks x 0.12 € = 1.20 €"
cennik = {"rožok": 0.12, "mlieko": 0.89, "maslo": 2.19, "syr": 1.75}
kosik = {"rožok": 10, "mlieko": 2, "syr": 1}

for polozka in kosik:
    print(polozka)
    print(kosik[polozka])
    if polozka in cennik:
        print(f"{polozka}: {kosik[polozka]} ks x {cennik[polozka]} = {cennik[polozka]* kosik[polozka]}")
        print ( polozka + " : " + kosik[polozka] + "ks x" + cennik[polozka] + " = " + str(cennik[polozka] * kosik[polozka]))
    

# Úloha 3: Najteplejší deň
# Nájdi deň s najvyššou a najnižšou teplotou a vypočítaj priemernú teplotu.
teploty = {"Po": 18.5, "Ut": 21.0, "St": 16.2, "Št": 23.4, "Pi": 19.8, "So": 25.1, "Ne": 22.3}



# Úloha 4: Prekladový slovník
# Prelož vetu slovo po slove. Ak slovo v slovníku nie je, nechaj ho v zátvorkách.
# Výsledok pre vetu nižšie: "cat eats (rybu)"
sk_en = {"mačka": "cat", "pes": "dog", "je": "eats", "mlieko": "milk", "a": "and"}
veta = "mačka je rybu"


# Úloha 5: Počet slov
# Spočítaj, koľkokrát sa v texte vyskytuje každé slovo (bez ohľadu na veľké/malé
# písmená). Vypíš 3 najčastejšie slová.
text = "Python je jazyk a Python je jednoduchý a Python sa učí dobre a rýchlo"
fr = open("nejaky.txt", "r", encoding= "utf-8")
text = fr.read()
slovnik = {}
print(text)
slova = text.split(" ")
print(slova)
for slovo in slova:
    slovnik
# ------------------------------------------------------------
# ÚROVEŇ 2 – KOMPREHENZIE
# ------------------------------------------------------------

# Úloha 6: Komprehenziou vytvor slovník, kde kľúče sú čísla 1–20
# a hodnoty sú "párne" alebo "nepárne".


# Úloha 7: Komprehenziou vytvor slovník len z tých miest,
# ktoré majú viac ako 50 000 obyvateľov.
obyvatelia = {"Martin": 52000, "Žilina": 80000, "Vrútky": 7000,
              "Ružomberok": 26000, "Bratislava": 475000, "Turany": 4500}


# Úloha 8: Zo zoznamu slov vytvor komprehenziou slovník
# slovo -> slovo napísané odzadu, ale len pre slová dlhšie ako 3 znaky.
slova = ["kajak", "les", "python", "oko", "slovník", "rotor", "ab"]


# Úloha 9: Pomocou komprehenzie zisti, ktoré slová zo zoznamu v úlohe 8
# sú palindrómy. Výsledok: slovník slovo -> True/False.


# Úloha 10: Zdražovanie
# Komprehenziou vytvor nový cenník, kde je každá cena zvýšená o 10 %
# a zaokrúhlená na 2 desatinné miesta. Použi `cennik` z úlohy 2.


# Úloha 11: Z dvoch zoznamov vytvor slovník (zip) a potom komprehenziou
# vytvor slovník len pre žiakov, ktorí majú známku lepšiu ako 3.
ziaci = ["Adam", "Beáta", "Cyril", "Dana", "Emil"]
znamky = [2, 4, 1, 3, 5]


# ------------------------------------------------------------
# ÚROVEŇ 3 – SLOVNÍKY SO ZOZNAMAMI
# ------------------------------------------------------------

# Úloha 12: Krúžky
# a) Vypíš, koľko žiakov je v každom krúžku.
# b) Pridaj žiaka "Tomáš" do krúžku "šach".
# c) Zisti, ktorí žiaci chodia do viacerých krúžkov.
# d) Vytvor "prevrátený" slovník: žiak -> zoznam jeho krúžkov.
kruzky = {
    "šach":       ["Adam", "Eva", "Filip"],
    "robotika":   ["Eva", "Juraj", "Adam", "Nina"],
    "basketbal":  ["Juraj", "Marek"],
    "divadlo":    ["Nina", "Eva"],
}


# Úloha 13: Zoskupenie čísel
# Rozdeľ čísla do slovníka podľa zvyšku po delení 3: {0: [...], 1: [...], 2: [...]}
# Vyrieš to raz cyklom a raz komprehenziou.
cisla = [4, 9, 12, 7, 15, 22, 3, 10, 8, 18, 5]


# Úloha 14: Športové výsledky
# Každý pretekár má zoznam časov (v sekundách) z niekoľkých pokusov.
# a) Pre každého nájdi najlepší (najmenší) čas.
# b) Zoraď pretekárov podľa najlepšieho času a vypíš poradie.
# c) Komprehenziou vytvor slovník pretekár -> počet pokusov pod 13 s.
casy = {
    "Lukáš":  [13.2, 12.8, 13.5],
    "Simona": [12.9, 12.6, 13.1, 12.7],
    "Oliver": [14.0, 13.7],
    "Kristína": [12.4, 13.3, 12.9],
}


# Úloha 15: Anagramy
# Zoskup slová, ktoré sú navzájom anagramami (majú rovnaké písmená).
# Tip: kľúčom môže byť "".join(sorted(slovo)).
# Očakávaný výsledok obsahuje napr. skupinu ['kot', 'tok', 'kto']
anag = ["kot", "rama", "tok", "mara", "sen", "kto", "nes", "arma", "les"]


# ------------------------------------------------------------
# ÚROVEŇ 4 – VNORENÉ ŠTRUKTÚRY
# ------------------------------------------------------------

# Úloha 16: Knižnica
# a) Vypíš všetky knihy, ktoré sú momentálne požičané.
# b) Vypíš knihy autora "Hviezdoslav".
# c) Vytvor slovník autor -> zoznam názvov jeho kníh.
# d) Vytvor slovník rok vydania -> počet kníh (pri dostupných knihách).
kniznica = {
    "K001": {"nazov": "Hájnikova žena", "autor": "Hviezdoslav", "rok": 1886, "pozicana": False},
    "K002": {"nazov": "Maryša",         "autor": "Mrštíkovci", "rok": 1894, "pozicana": True},
    "K003": {"nazov": "Ežo Vlkolinský", "autor": "Hviezdoslav", "rok": 1890, "pozicana": True},
    "K004": {"nazov": "Rysavá jalovica", "autor": "Timrava",   "rok": 1907, "pozicana": False},
    "K005": {"nazov": "Ťapákovci",      "autor": "Timrava",    "rok": 1914, "pozicana": False},
}


# Úloha 17: Hodnotenie tried
# a) Vypočítaj priemer každého žiaka zo všetkých predmetov.
# b) Vypočítaj priemer triedy v každom predmete.
# c) Nájdi najlepšieho žiaka (najnižší celkový priemer).
hodnotenie = {
    "Jana":  {"MAT": [1, 2, 1], "INF": [1, 1],    "SJL": [2, 3]},
    "Peter": {"MAT": [3, 3, 2], "INF": [2, 1, 2], "SJL": [3]},
    "Lucia": {"MAT": [2, 1],    "INF": [1, 2],    "SJL": [1, 1, 2]},
}


# Úloha 18: Sklad
# a) Vypočítaj celkovú hodnotu skladu (kusy * cena).
# b) Vypíš produkty, ktorých je menej ako 5 kusov (treba doobjednať).
# c) Vytvor slovník kategória -> celková hodnota tovaru v kategórii.
# d) Pridaj nový produkt do kategórie "doplnky".
sklad = {
    "elektronika": [
        {"produkt": "myš",       "kusy": 25, "cena": 12.90},
        {"produkt": "klávesnica", "kusy": 3,  "cena": 29.90},
        {"produkt": "monitor",   "kusy": 7,  "cena": 159.00},
    ],
    "kancelária": [
        {"produkt": "papier A4", "kusy": 40, "cena": 4.50},
        {"produkt": "zošívačka", "kusy": 2,  "cena": 8.20},
    ],
    "doplnky": [
        {"produkt": "podložka",  "kusy": 15, "cena": 6.00},
    ],
}


# Úloha 19: Rodokmeň
# Slovník hovorí, kto sú deti danej osoby.
# a) Vypíš všetky vnúčatá osoby "Anna".
# b) Napíš funkciu potomkovia(osoba), ktorá rekurzívne vráti zoznam
#    všetkých potomkov (deti, vnúčatá, pravnúčatá...).
deti = {
    "Anna":   ["Boris", "Cecília"],
    "Boris":  ["Dávid", "Ema"],
    "Cecília": ["Filip"],
    "Dávid":  ["Gabika"],
    "Ema":    [],
    "Filip":  [],
    "Gabika": [],
}


# Úloha 20: Mini-projekt – Kvíz
# Vytvor slovník otázok, kde kľúč je otázka a hodnota je slovník
# {"moznosti": [...], "spravna": "..."}.
# Program sa postupne pýta otázky, kontroluje odpovede a na konci vypíše
# počet bodov a zoznam otázok, v ktorých sa hráč pomýlil.

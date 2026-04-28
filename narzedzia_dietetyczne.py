import json
from datetime import datetime
def pobierz_mnoznik_pal(wybor_uzytkownika):
    slownik_pal = {1: 1.2, 2: 1.4, 3: 1.6, 4: 1.8, 5: 2.0}
    return slownik_pal.get(wybor_uzytkownika, 0.0)
    
def oblicz_zapotrzebowanie(plec, waga, wzrost, wiek, mnoznik_PAL):
    
    slownik_plec = {"m": "mezczyzna", "k": "kobieta"}
    pelna_plec = slownik_plec.get(plec, "")
    if pelna_plec == "mezczyzna":
        return ((10 * waga) + (6.25 * wzrost) + (5 * wiek) +5)*mnoznik_PAL
    elif pelna_plec == "kobieta":
        return ((10 * waga) + (6.25 * wzrost)+( 5* wiek) -161)*mnoznik_PAL
    else:
        return 0.0
    
def zliczaj_produkty(limit_kalorii):
    #Wczytywanie starych danych
    try:
        with open("dziennik.json", "r", encoding="utf-8") as plik:
                lista_produktow = json.load(plik)
    except (FileNotFoundError, json.JSONDecodeError):
        lista_produktow = []
    #Liczenie kalorii z wczytanych wczesniej produktow
    dzisiaj = datetime.now().strftime("%Y-%m-%d")
    kalorie_dzisiaj = 0
    for p in lista_produktow:
        if p["data"].startswith(dzisiaj):
            kalorie_dzisiaj += p["kalorie"]
    if kalorie_dzisiaj > limit_kalorii:
        print(f"Uwaga! Przekroczyłes limit kalorii.")
    while True: 
        nazwa_produktu = input("Podaj nazwe produktu(lub wpisz koniec):")
        if nazwa_produktu == "koniec":
                print("\nTwoje dzisiejsze menu:")
                for produkt in lista_produktow:
                    nazwa = produkt["nazwa"]
                    kcal = produkt["kalorie"]
                    if dzisiaj in produkt["data"]:
                        print(f"- {nazwa}: {kcal} kcal")
                print("Twoje kalorie wynoszą: ", kalorie_dzisiaj)
                break
        else:
            kalorie_produktu = pobierz_wartosc("Ile to miało kalorii? ")
            produkt = {
                "nazwa": nazwa_produktu, 
                "kalorie": kalorie_produktu,
                "data": datetime.now().isoformat()
            }
            lista_produktow.append(produkt)
            kalorie_dzisiaj += kalorie_produktu


            print(f"aktualnie zjedzone: {kalorie_dzisiaj} kcal.")
    with open("dziennik.json", "w", encoding="utf-8") as plik:
            json.dump(lista_produktow, plik, indent=4)
    print("Dane zapisane. Do nastepnego!")


def pobierz_wartosc(komunikat):
    while True:
        try:
            wartosc = float(input(komunikat))
            return wartosc
        except ValueError:
            print("To nie jest poprawna liczba!")

def pobierz_opcje(komunikat, dozwolone_opcje):
    while True:
        wybor = input(komunikat).lower().strip()
        if wybor in dozwolone_opcje:
            return wybor
        else:
            print(f"Błąd! Wybierz jedną z opcji: {dozwolone_opcje}")
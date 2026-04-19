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
    kalorie_uzytkownika = 0
    lista_produktow = []
    while True: 
        nazwa_produktu = input("Podaj nazwe produktu(lub wpisz koniec):")
        if nazwa_produktu != "koniec":
            kalorie_produktu = pobierz_wartosc("Ile to miało kalorii? ")
            kalorie_uzytkownika += kalorie_produktu

            lista_produktow.append(f"{nazwa_produktu}: {kalorie_produktu} kcal")
            print(f"Dodano {nazwa_produktu} do listy.")
            if kalorie_uzytkownika > limit_kalorii:
                print("Aktualnie masz zjedzone: ",kalorie_uzytkownika, "kalorii, przekroczyłeś limit!" )
            else:
                print("Aktualnie masz zjedzone: ",kalorie_uzytkownika)
        else:
            print("\nTwoje dzisiejsze menu:")
            with open("dziennik.txt", "a", encoding="utf-8") as plik:
                for produkt in lista_produktow:
                    print(f"- {produkt}")
                    plik.write(f"{produkt}\n")
                plik.write(f"Suma sesji: {kalorie_uzytkownika} kcal\n")
                plik.write("-" * 20 + "\n")
            print("Twoje kalorie wynoszą: ", kalorie_uzytkownika)
            break

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
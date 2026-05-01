import json
from datetime import datetime, timedelta

def uruchom_menu(zapotrzebowanie, lista_produktow, waga, plec, wzrost):
    while True:
        print("\n--- TWÓJ ASYSTENT DIETETYCZNY ---")
        print("1. Dodaj posiłek / Sprawdź kalorie")
        print("2. Pokaż raport z ostatnich 7 dni")
        print("3. Wyświetl moje parametry i cel")
        print("4. Zapisz i wyjdź")

        wybor = input("\nCo chcesz zrobić? (1-4): ")

        if wybor == "1":
            zliczaj_produkty(zapotrzebowanie, lista_produktow)

        elif wybor == "2":
            podsumowanie_tygodnia(lista_produktow)
        
        elif wybor == "3":
            print(f"\n[PROFIL] Cel: {zapotrzebowanie} kcal, plec: {plec}, waga: {waga}, wzrost: {wzrost}")
        
        elif wybor == "4":
            print("Kończymy program, do następnego!")
            break
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")


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
    
def zliczaj_produkty(limit_kalorii, lista_produktow):
    
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

def wczytaj_dane():
    try:
        with open("dziennik.json", "r", encoding="utf-8") as plik:
            dane = json.load(plik)
        return dane
    except (FileNotFoundError, json.JSONDecodeError):
        print("nie można wczytac pliku!")
        return []

def podsumowanie_tygodnia(lista_produktow):
    siedem_dni_temu = (datetime.now() - timedelta(days=7)).isoformat() #Data graniczna, sprzed 7 dni
    produkty_tydzien = [p for p in lista_produktow if p["data"] > siedem_dni_temu] #tylko dla produktow z ostatniego tygodnia

    if not produkty_tydzien: #zabezpieczenie, jesli brak produktow w ostatnim tygodniu
        print("Brak danych z ostatnich 7 dni.")
        return
    
    suma_kcal = sum(p["kalorie"] for p in produkty_tydzien)
    daty_z_wpisami = [p["data"][:10] for p in produkty_tydzien]
    unikalne_dni = set(daty_z_wpisami)

    srednia = suma_kcal/len(unikalne_dni)

    print ("\n" + "="*30)
    print("   RAPORT TYGODNIOWY")
    print("="*30)
    print(f"Liczba aktywnych dni: {len(unikalne_dni)}")
    print(f"Suma kalorii:         {suma_kcal} kcal")
    print(f"Średnia na dzień:      {round(srednia, 2)} kcal") # funkcja round usrednia do 2 miejsc po przecinku
    print("="*30 + "\n")
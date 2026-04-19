from narzedzia_dietetyczne import pobierz_mnoznik_pal, oblicz_zapotrzebowanie, zliczaj_produkty, pobierz_wartosc, pobierz_opcje

waga = pobierz_wartosc("Jaka jest twoja waga? ")
wiek = pobierz_wartosc("Jaki jest twój wiek? ")
wzrost = pobierz_wartosc("Jaki jest twój wzrost? ")
plec = pobierz_opcje("Podaj płeć (m/k): ", ["m", "k"])

opisy_pal = {
    1: "Brak aktywności (praca siedząca)",
    2: "Niska aktywność (spacery, lekki ruch)",
    3: "Średnia aktywność (trening 2-3 razy w tygodniu)",
    4: "Wysoka aktywność (ciężkie treningi 4-5 razy w tygodniu)",
    5: "Ekstremalna aktywność (sportowiec zawodowy)"
}
print("\nWybierz swoj poziom aktywnosci:")
for numer, opis in opisy_pal.items():
    print(f"{numer} - {opis}")
PAL = int(pobierz_opcje("\nPodaj cyfrę od 1 do 5: ", ["1", "2", "3", "4", "5"]))
mnoznik_PAL = pobierz_mnoznik_pal(PAL)
zapotrzebowanie_kaloryczne = oblicz_zapotrzebowanie(plec, waga, wzrost, wiek, mnoznik_PAL) 



if zapotrzebowanie_kaloryczne>0:
    print("Twoje zapotrzebowanie kaloryczne to:", zapotrzebowanie_kaloryczne)
    zliczaj_produkty(zapotrzebowanie_kaloryczne)
else:
    print("Nie udało sie obliczyć zapotrzebowania kalorycznego z powodu błędnych danych.")

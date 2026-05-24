# Koródi-Bálint Csilla Neptun kód: C80UIR

from abc import ABC, abstractmethod
from datetime import datetime


class Legitarsasag:
    def __init__(self,nev):
        self._nev=nev
        self._jaratok = []
        self._foglalasok = []

    @property
    def jaratok(self):
        return self._jaratok
    
    @property
    def foglalasok(self):
        return self._foglalasok

    def uj_jarat(self,jarat):
        self._jaratok.append(jarat)

    def uj_foglalas(self, foglalas):
        if foglalas.datum > datetime.now():
            self._foglalasok.append(foglalas)
            return foglalas.valasztott_jarat.jegyar_szamitas()   
        else:
            print("Nem lehet múltbeli időpontra jegyet foglalni.")
            return False

    def listazz_foglalasokat(self):
        print("\n=== AKTUÁLIS FOGLALÁSOK LISTÁJA ===")
        for jegy in self._foglalasok:
            print(
                    f"Utas {jegy.utas_neve}, Járat {jegy.valasztott_jarat.jaratszam},"
                    f"Ár: {jegy.valasztott_jarat.jegyar_szamitas()} Ft, Indulás: {jegy.datum}"
            )
        print("===================================\n")
    def lemond_foglalas(self, utas_neve):
        for jegy in self._foglalasok:
            if jegy.utas_neve == utas_neve:
                self._foglalasok.remove(jegy)
                print(f"Sikeresen lemondva: {utas_neve}, foglalása")
                return
        print(f"Nem található foglalás {utas_neve} névre!")

          

legitarsasag1=Legitarsasag("Repülő Felhő Légitársaság")


class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, tav_km, indulas):
        self._jaratszam = jaratszam
        self._celallomas = celallomas
        self._tav_km = tav_km
        self._indulas = indulas

    @property
    def jaratszam(self):
        return self._jaratszam
    
    @property
    def celallomas(self):
        return self._celallomas
    
    @property
    def tav_km(self):
        return self._tav_km

    @property
    def indulas(self):
        return self._indulas

    @abstractmethod
    def jegyar_szamitas(self):
        pass


class BelfoldiJarat(Jarat): 
    def __init__(self, jaratszam, celallomas, tav_km, indulas):
        super().__init__(jaratszam, celallomas, tav_km, indulas)

    def jegyar_szamitas(self):
        return self._tav_km * 10

class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, celallomas, tav_km, indulas):
        super().__init__(jaratszam, celallomas, tav_km, indulas)

    def jegyar_szamitas(self):
        return self._tav_km * 20


jarat1 = BelfoldiJarat("J001", "Budapest-Debrecen", 200, datetime(2026, 6, 15, 8, 00))
jarat2 = NemzetkoziJarat("J002", "Budapest-Róma", 800, datetime(2026, 7, 20, 10, 00))
jarat3 = NemzetkoziJarat("J003", "Budapest-Párizs", 1200, datetime(2026, 7, 13, 16, 00))

class Jegyfoglalas:
    def __init__(self, utas_neve, valasztott_jarat, datum):
        self._utas_neve = utas_neve
        self._valasztott_jarat = valasztott_jarat
        self._datum = datum

    @property
    def utas_neve(self):
        return self._utas_neve
    
    @property
    def valasztott_jarat(self):
        return self._valasztott_jarat
    
    @property
    def datum(self):
        return self._datum


Jegy1 = Jegyfoglalas("Kovács János", jarat1, jarat1.indulas)   
Jegy2 = Jegyfoglalas("Nagy Anna", jarat2, jarat2.indulas)
Jegy3 = Jegyfoglalas("Szabó Péter", jarat2, jarat2.indulas)
Jegy4 = Jegyfoglalas("Kiss Éva", jarat2, jarat2.indulas)
Jegy5 = Jegyfoglalas("Tóth Gábor", jarat3, jarat3.indulas)
Jegy6 = Jegyfoglalas("Molnár Júlianna", jarat3, jarat3.indulas)

legitarsasag1.uj_jarat(jarat1)
legitarsasag1.uj_jarat(jarat2)
legitarsasag1.uj_jarat(jarat3)

legitarsasag1.uj_foglalas(Jegy1)
legitarsasag1.uj_foglalas(Jegy2)
legitarsasag1.uj_foglalas(Jegy3)
legitarsasag1.uj_foglalas(Jegy4)
legitarsasag1.uj_foglalas(Jegy5)
legitarsasag1.uj_foglalas(Jegy6)

while True:
    print("\n--- Repülő Felhő Légitársaság Menü ---")
    print("1. Foglalások listázása")
    print("2. Jegy foglalása")
    print("3. Foglalás lemondása")
    print("4. Kilépés")
    
    beviteli_szoveg = input("Válassz egy menüpontot (1-4): ")

    try:
        valasztas = int(beviteli_szoveg)
    except ValueError:
        print("\nHiba: Kérjük, számot adj meg, ne betűket!")
        continue
    
    if valasztas == 1:
        legitarsasag1.listazz_foglalasokat()
        
        
    elif valasztas == 2:
        print("\n--- Új jegy foglalása ---")
        utas_neve = input("Add meg az utas nevét: ")
        
        print("\nElérhető járatok és indulási idők:")
        for jarat in legitarsasag1.jaratok:
            print(f"- {jarat.jaratszam}: {jarat.celallomas} | Indulás: {jarat.indulas} | Ár: {jarat.jegyar_szamitas()} Ft")
            
        valasztott_szam = input("\nAdd meg a választott járatszámot: ")
        
        kivallasztott_jarat = None
        for jarat in legitarsasag1.jaratok:
            if jarat.jaratszam == valasztott_szam:
                kivallasztott_jarat = jarat
                break
                
        if kivallasztott_jarat is None:
            print("\nHiba: Nem létezik ilyen járatszámmal járat!")
            continue
            
        uj_jegy = Jegyfoglalas(utas_neve, kivallasztott_jarat, kivallasztott_jarat.indulas)
        
        siker = legitarsasag1.uj_foglalas(uj_jegy)
        if siker:
            print(
                f"\nSikeres foglalás! Utas: {utas_neve}, Járat: {kivallasztott_jarat.jaratszam}, "
                f"Indulás: {kivallasztott_jarat.indulas}"
               )

    elif valasztas == 3:
        nev = input("Add meg a lemondani kívánt foglaláshoz tartozó utas nevét: ")
        legitarsasag1.lemond_foglalas(nev)
        
    elif valasztas == 4:
        print("Köszönjük, hogy a Repölő Felhő Légitársaságot választotta! Jó utat!")
        break
        
    else:
        print("Hibás választás! Kérjük, 1 és 4 közötti számot adj meg!")
    
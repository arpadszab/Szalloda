from abc import ABC, abstractmethod
from datetime import datetime

class Szoba(ABC):

    def __init__(self, ar, szobaszam):
        self.szoba_ar = ar
        self.szoba_szam = int(szobaszam)

    @abstractmethod
    def extrak(self):
        pass

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, wifi):
        super().__init__(ar = 10000, szobaszam = szobaszam)
        self.wifi = wifi

    def extrak(self):
        extrak = "Egyágyas szoba"
        if self.wifi:
             extrak += ", wifi"
        return extrak

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, jakuzzi):
        super().__init__(ar = 15000, szobaszam = szobaszam)
        self.jakuzzi = jakuzzi


    def extrak(self):
        extrak = "Kétágyas szoba"
        if self.jakuzzi:
            extrak += ", jakuzzi"
            return extrak
class Szalloda:

    def __init__(self, nev):
        self.szalloda_nev = nev
        self.szobak = []
        self.foglalasok = []

    def szoba_hozzaadasa(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        if datum < datetime.now():
            print("A foglalás dátuma nem lehet múltbéli.")
            return None

        for foglalas in self.foglalasok:
            if foglalas.szoba.szoba_szam == int(szobaszam) and foglalas.datum == datum:
                print("A szoba nem elérhető ezen a dátumon.")
                return None

        for szoba in self.szobak:
            if szoba.szoba_szam == int(szobaszam):
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                print("Foglalás sikeres")
                return None

        print("Nem található szoba ezen a számon.")

    def foglalas_lemondasa(self, szobaszam, datum):
        lefoglalt = False
        for foglalas in self.foglalasok:
            if foglalas.szoba.szoba_szam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                lefoglalt = True
                print("Foglalas sikeresen törölve.")
        if not lefoglalt:
            print("Nem található foglalás ezen a szobaszámon és dátumon.")


    def foglalasok_listazasa(self):
        print("Már lefoglalt szobák:")
        for foglalas in self.foglalasok:
            print(f"- Szobaszám:{foglalas.szoba.szoba_szam}, Dátum: {foglalas.datum}")

class Foglalas:

    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def ar_szamitas(self):
        return self.szoba.szoba_ar

def main():
    szalloda = Szalloda("Szunnyadó Kárpit")
    szalloda.szoba_hozzaadasa(EgyagyasSzoba(szobaszam=101, wifi=True)) #szoba1
    szalloda.szoba_hozzaadasa(EgyagyasSzoba(szobaszam=102, wifi=False)) #szoba2
    szalloda.szoba_hozzaadasa(KetagyasSzoba(szobaszam=203, jakuzzi=True)) #szoba3
    szalloda.foglalas(101, datetime(2024, 5, 17)) #foglalas1
    szalloda.foglalas(102, datetime(2024, 6, 30)) #foglalas2
    szalloda.foglalas(203, datetime(2024, 5, 24)) #foglalas3
    szalloda.foglalas(101, datetime(2024, 6, 9)) #foglalas4
    szalloda.foglalas(102, datetime(2024, 8, 2)) #foglalas5

    while True:
        print("\nVálasszon műveletet:")
        print("1. Foglalás")
        print("2. Foglalás törlése")
        print("3. Foglalások listázása")
        print("0. Kilépés")

        valasztas = input("Válaszás: ")

        if valasztas == "1":
            szobaszam = input("Adja meg a foglalni kívánt szoba számát: ")
            datum_forma = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN): ")
            datum = datetime.strptime(datum_forma, "%Y-%m-%d")
            szalloda.foglalas(szobaszam, datum)
        elif valasztas == "2":
            szobaszam = input("Adja meg a törölni kívánt foglalás szobaszámát: ")
            datum_forma = input("Adja meg a törölni kívánt foglalás dátumát (ÉÉÉÉ-HH-NN): ")
            datum = datetime.strptime(datum_forma, "%Y-%m-%d")
            szalloda.foglalas_lemondasa(szobaszam, datum)
        elif valasztas == "3":
            szalloda.foglalasok_listazasa()
        elif valasztas == "0":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    main()

# 1. Kas yra paprastieji (baziniai) duomenų tipai ir kam jie naudojami?
""" Tai pagrindiniai tipai: sveikieji (int), slankiojo kablelio (float), simboliai (char), tekstas (string), loginiai (bool). 
Jie naudojami duomenims saugoti ir su jais dirbti"""

# 2. Pateikite po vieną sveikojo skaičiaus ir slankiojo kablelio skaičiaus pavyzdį:
"""Sveikas skaičius: x = 10; Slankusis kablelis: y = 3.14"""

# 3. Kokiai informacijai saugoti naudojamas char tipas?
"""Char tipas naudojamas saugoti vieną simbolį, pavyzdžiui, raidę, skaičių ar specialų ženklą."""

# 4. Kuo string tipas skiriasi nuo char tipo?
"""String tipas saugo eilutę simbolių (teksto), o char saugo tik vieną simbolį."""

# 5. Kokias reikšmes gali turėti loginis (boolean) duomenų tipas?
"""Loginis (boolean) tipas gali turėti dvi reikšmes: True (tiesa) arba False (klaidinga)."""

# 6. Kokios yra pagrindinės aritmetinės operacijos? Parašykite bent 3 iš jų.
"""Pagrindinės aritmetinės operacijos yra: sudėtis (+), atimtis (-), daugyba (*), dalyba (/), liekana (%)."""

# 7.Parašykite pavyzdį, kur lyginimo operatorius „!=“ būtų true.
"""x = 5; y = 10; rezultatas = (x != y)  # rezultatas bus True, nes 5 nėra lygu 10"""

# 8. Ką daro loginis operatorius NOT (!) ir pateikite pavyzdį.
"""Loginis operatorius NOT (!) apverčia loginę reikšmę. Pavyzdys: x = True; rezultatas = not x  # rezultatas bus False"""

# 9. Kokie yra loginiai operatoriai ir kaip jie žymimi programavimo kalbose?
"""Loginiai operatoriai yra AND (ir), OR (arba), NOT (ne). Jie žymimi taip: AND - && arba 'and', OR - || arba 'or', 
NOT - ! arba 'not'."""

# 10. Paaiškinkite, kodėl programose svarbu atskirti skaičius su kableliu (float) nuo sveikųjų (int).
"""Skaičiai su kableliu (float) gali turėti dešimtaines dalis, o sveikieji (int) - ne. Tai svarbu, nes skirtingos operacijos ir
tikslumas gali priklausyti nuo duomenų tipo."""

# 11. Kuo skiriasi operatoriai „==“ ir „=“?
"""Operatorius „==“ yra lyginimo operatorius, kuris tikrina, ar dvi reikšmės yra lygios. Operatorius „=“ yra priskyrimo operatorius,
kuris priskiria reikšmę kintamajam."""

# 12. Kodėl tekstui saugoti neužtenka char tipo?
"""Char tipas saugo tik vieną simbolį, o tekstas dažnai susideda iš daugelio simbolių. Todėl tekstui saugoti naudojamas string tipas,
kuris gali talpinti ilgesnes simbolių sekas."""

# Užduotis: papildytas dėstytojos kodas:
"""Pabandykite patobulinti kodą ir pridėti: 
1. Dar 2 logines operacijas. 
2. Dar 2 formules stipendijoms gauti ir/arba jas pasikelti."""

from statistics import mean
from typing import List, Optional

class Student:
    """
    Klasė, aprašanti mokinį su paprastaisiais duomenų tipais:
    - Tekstas (vardas, klasė)
    - Loginiai duomenys (istojo ar ne)
    - Skaičiai (pažymiai ir jų vidurkis)
    """

    def __init__(self, vardas: str, klase: str, istojes: bool = True, pazymiai: Optional[List[int]] = None):
        self.vardas = vardas
        self.klase = klase
        self.istojes = istojes
        self.pazymiai = pazymiai if pazymiai is not None else []

    def prideti_pazymi(self, pazymys: int) -> None:
        """Prideda naują pažymį (1-10)."""
        if 1 <= pazymys <= 10:
            self.pazymiai.append(pazymys)
        else:
            raise ValueError("Pažymys turi būti nuo 1 iki 10!")

    def vidurkis(self) -> float:
        """Apskaičiuoja studento pažymių vidurkį."""
        return round(mean(self.pazymiai), 2) if self.pazymiai else 0.0

    def geriausias_pazymys(self) -> int:
        """Grąžina geriausią studento pažymį."""
        return max(self.pazymiai) if self.pazymiai else 0

    def ar_praejo(self) -> bool:
        """Patikrina, ar studentas išlaikė mokslus (vidurkis ≥ 4)."""
        return self.vidurkis() >= 4

    def stipendija(self) -> float:
        """
        Paprasta stipendijos formulė:
        - Jeigu vidurkis >= 8 → bazinė stipendija 100
        - Jeigu vidurkis >= 9 IR geriausias pažymys = 10 → padidinta stipendija 150
        - Jeigu vidurkis < 8, bet studentas vis tiek mokosi (istojo = True) → stipendija 50
        """
        if self.vidurkis() >= 9 and self.geriausias_pazymys() == 10:  # loginė AND operacija
            return 150
        elif self.vidurkis() >= 8:
            return 100
        elif self.vidurkis() >= 6 or self.istojes:  # loginė OR operacija
            return 50
        else:
            return 0

    def parodyti_pazymius(self) -> None:
        """Išveda visus studento pažymius."""
        if not self.pazymiai:
            print(f"{self.vardas} dar neturi pažymių.")
        else:
            print(f"{self.vardas} pažymiai: {', '.join(map(str, self.pazymiai))}")

    def __str__(self) -> str:
        statusas = "mokosi" if self.istojes else "baigęs"
        return f"{self.vardas}, {self.klase} — {statusas}, vidurkis: {self.vidurkis()}, stipendija: {self.stipendija()}"


# ==== Panaudojimo pavyzdžiai ====

s1 = Student("Aistė", "10A")
s2 = Student("Mantas", "12B", pazymiai=[8, 9, 7])
s3 = Student("Ernestas", "11C", pazymiai=[10, 9, 10])

for p in [10, 9, 8, 2]:
    s1.prideti_pazymi(p)

for student in [s1, s2, s3]:
    print(student)
    student.parodyti_pazymius()

    if student.ar_praejo():
        print(f"✅ {student.vardas} išlaikė mokslus.")
    else:
        print(f"❌ {student.vardas} neišlaikė mokslų.")

    print()  # tuščia eilutė, kad būtų aiškiau
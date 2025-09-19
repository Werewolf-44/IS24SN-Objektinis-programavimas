

# Importuojame reikalingas bibliotekas
from statistics import mean
from typing import List, Optional

# ==== Klasė Student ====
class Student:
    """
    Klasė, aprašanti mokinį su paprastaisiais duomenų tipais:
    - Tekstas (vardas, klasė)
    - Loginiai duomenys (istojo ar ne)
    - Skaičiai (pažymiai ir jų vidurkis)
    - Masyvai (pažymiai, kreditai, papildomi dalykai)
    """
    
    def __init__(self, vardas: str, klase: str, istojes: bool = True, 
                 pazymiai: Optional[List[int]] = None,
                 kreditai: Optional[List[int]] = None,           # PRIDĖTA
                 papildomi_dalykai: Optional[List[str]] = None): # PRIDĖTA
        self.vardas = vardas
        self.klase = klase
        self.istojes = istojes
        self.pazymiai = pazymiai if pazymiai is not None else []
        self.kreditai = kreditai if kreditai is not None else []              # PRIDĖTA
        self.papildomi_dalykai = papildomi_dalykai if papildomi_dalykai else []  # PRIDĖTA

    def prideti_pazymi(self, pazymys: int) -> None:
        if 1 <= pazymys <= 10:
            self.pazymiai.append(pazymys)
        else:
            raise ValueError("Pažymys turi būti nuo 1 iki 10!")

    def vidurkis(self) -> float:
        return round(mean(self.pazymiai), 2) if self.pazymiai else 0.0

    def geriausias_pazymys(self) -> int:
        return max(self.pazymiai) if self.pazymiai else 0

    def ar_praejo(self) -> bool:
        return self.vidurkis() >= 4

    # PRIDĖTA metodas kreditams
    def gauti_kreditus(self) -> int:
        """Susumuoja išlaikytus kreditus"""
        return sum(self.kreditai)

    # PRIDĖTA metodas papildomiems dalykams parodyti
    def parodyti_papildomus(self) -> None:
        if not self.papildomi_dalykai:
            print(f"{self.vardas} neturi papildomų dalykų.")
        else:
            print(f"{self.vardas} papildomi dalykai: {', '.join(self.papildomi_dalykai)}")

    def parodyti_pazymius(self) -> None:
        if not self.pazymiai:
            print(f"{self.vardas} dar neturi pažymių.")
        else:
            print(f"{self.vardas} pažymiai: {', '.join(map(str, self.pazymiai))}")

    def __str__(self) -> str:
        statusas = "mokosi" if self.istojes else "baigęs"
        return (f"{self.vardas}, {self.klase} — {statusas}, "
                f"vidurkis: {self.vidurkis()}, kreditai: {self.gauti_kreditus()}")  # PRIDĖTA

# ==== Sukuria studentus su papildomais duomenimis ====
s1 = Student("Aistė", "10A", kreditai=[5, 3, 2], papildomi_dalykai=["Dailė", "Muzika"])
s2 = Student("Mantas", "12B", pazymiai=[8, 9, 7], kreditai=[6, 4])
s3 = Student("Ieva", "11C", pazymiai=[5, 6], kreditai=[2, 3], papildomi_dalykai=["Sportas"])
s4 = Student("Jonas", "9D", kreditai=[1, 2, 2])
s5 = Student("Ona", "12A", pazymiai=[10, 10, 9], kreditai=[5, 5, 5])

# ==== Prideda papildomus pažymius ====
for p in [10, 9, 8]:
    s1.prideti_pazymi(p)

for p in [4, 6]:
    s3.prideti_pazymi(p)

for p in [7, 8, 5]:
    s4.prideti_pazymi(p)

# ==== Atspausdina studento informaciją ====
studentai = [s1, s2, s3, s4, s5]

print("=== Studentų informacija ===")
for student in studentai:
    print(student)
    student.parodyti_pazymius()
    student.parodyti_papildomus()  # PRIDĖTA
    print(f"✅ Kreditai: {student.gauti_kreditus()}")  # PRIDĖTA
    if student.ar_praejo():
        print(f"✅ {student.vardas} išlaikė mokslus.\n")
    else:
        print(f"❌ {student.vardas} neišlaikė mokslų.\n")

# ==== Surūšiuoja studentus pagal kreditus ====
studentai_su_kreditais = sorted(studentai, key=lambda x: x.gauti_kreditus(), reverse=True)
print("=== Studentai pagal kreditus (nuo daugiausiai) ===")
for student in studentai_su_kreditais:
    print(f"{student.vardas}: kreditai {student.gauti_kreditus()}")
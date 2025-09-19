# Atnaujinkite 6 užduoties kodą ir pabandykite pridėti sekančias operacijas su struktūrų masyvais:
# *Paieška
# *Rūšiavimas
# *Atnaujinimas

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
    """
    
    def __init__(self, vardas: str, klase: str, istojes: bool = True, pazymiai: Optional[List[int]] = None):
        self.vardas = vardas
        self.klase = klase
        self.istojes = istojes
        self.pazymiai = pazymiai if pazymiai is not None else []

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

    def parodyti_pazymius(self) -> None:
        if not self.pazymiai:
            print(f"{self.vardas} dar neturi pažymių.")
        else:
            print(f"{self.vardas} pažymiai: {', '.join(map(str, self.pazymiai))}")

    def __str__(self) -> str:
        statusas = "mokosi" if self.istojes else "baigęs"
        return f"{self.vardas}, {self.klase} — {statusas}, vidurkis: {self.vidurkis()}"

# ==== Sukuria 5 studentus su skirtingais pažymiais ====
s1 = Student("Aistė", "10A")
s2 = Student("Mantas", "12B", pazymiai=[8, 9, 7])
s3 = Student("Ieva", "11C", pazymiai=[5, 6])
s4 = Student("Jonas", "9D")
s5 = Student("Ona", "12A", pazymiai=[10, 10, 9])

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
    if student.ar_praejo():
        print(f"✅ {student.vardas} išlaikė mokslus.\n")
    else:
        print(f"❌ {student.vardas} neišlaikė mokslų.\n")

# ==== Surūšiuoja studentus pagal vidurkį nuo aukščiausio ====
studentai_su_vidurkiu = sorted(studentai, key=lambda x: x.vidurkis(), reverse=True)
print("=== Studentai pagal vidurkį (nuo aukščiausio) ===")
for student in studentai_su_vidurkiu:
    print(f"{student.vardas}: vidurkis {student.vidurkis()}")

# ==== Nustato, kuris studentas turi geriausią pažymį ====
geriausias_studentas = max(studentai, key=lambda x: x.geriausias_pazymys())
print(f"\n🎉 Geriausias pažymys priklauso: {geriausias_studentas.vardas} — {geriausias_studentas.geriausias_pazymys()}")

# PRIDĖTA  Operacijos su struktūrų masyvais

# Paieška pagal vardą
def ieskoti_studento(vardas: str, sarasas: List[Student]) -> Optional[Student]:
    """Grąžina studentą pagal vardą, jei rastas"""
    for st in sarasas:
        if st.vardas == vardas:
            return st
    return None

print("\n=== Paieška pagal vardą ===")
rez = ieskoti_studento("Mantas", studentai)
if rez:
    print(f"Rastas studentas: {rez}")
else:
    print("Tokio studento nėra.")

# Rūšiavimas pagal vardą
print("\n=== Studentai surikiuoti pagal vardą ===")
studentai_pagal_varda = sorted(studentai, key=lambda x: x.vardas)
for st in studentai_pagal_varda:
    print(st)

# Atnaujinimas (pakeisti klasę ir pridėti pažymį)
print("\n=== Atnaujinimas ===")
atnaujintas = ieskoti_studento("Ieva", studentai)
if atnaujintas:
    atnaujintas.klase = "12C"        # PRIDĖTA pakeičiam klasę
    atnaujintas.prideti_pazymi(9)    # PRIDĖTA pridedam naują pažymį
    print(f"Atnaujintas studentas: {atnaujintas}")
    atnaujintas.parodyti_pazymius()

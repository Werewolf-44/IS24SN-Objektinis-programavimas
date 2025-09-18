# Kas yra klasė ir kas yra objektas? Pateik pavyzdį iš pateikto kodo.
"""Klasė yra šablonas arba brėžinys. Objektas yra konkreti realizacija pagal klasės šabloną."""

# Kam reikalingas metodas __init__?
"""Metodas __init__ yra konstruktorius. Jo paskirtis yra inicijuoti naujai sukurtą objektą ir nustatyti jo pradines savybes.
*Sukuria ir nustato šias objekto savybes: self.vardas, self.klase, self.istojes, self.pazymiai.
*Leidžia perduoti reikšmes šioms savybėms kuriant objektą (Student("Aistė", "10A")).
*Nustato numatytąją reikšmę True savybei istojes.
*Užtikrina, kad pazymiai visada bus sąrašas (net jeigu jis nebuvo perduotas).:"""

# Ką daro metodas __str__ klasėje?
"""Metodas __str__ nustato, kaip objektas atrodys, kai jis bus konvertuojamas į eilutę (pvz., naudojant print()).:"""

# Kuo skiriasi sąlyga if nuo ciklo for? Pateik pavyzdį iš pateikto kodo.
"""If: Vykdoma vieną kartą - patikrina sąlygą ir vykdo kodą vieną kartą (jei sąlyga teisinga).
For: Kartojasi - eina per kiekvieną sąrašo elementą ir vykdo kodą kiekvienam elementui."""

# Kodėl prie kintamųjų klasėje rašome self.?
"""self yra nuoroda į patį objektą. Naudojant self, metodas gali pasiekti to objekto savybes ir kvieti kitus to objekto metodus. Taip pat, self leidžia išvengti vardų konfliktų tarp vietinių 
kintamųjų ir objekto savybių."""

# Praktiktinė užduotis. Sąlygos ir ciklai.

class Student:
    def __init__(self, vardas, klase, istojes=True, pazymiai=None):
        self.vardas = vardas
        self.klase = klase
        self.istojes = istojes
        self.pazymiai = pazymiai if pazymiai is not None else []

    def prideti_pazymi(self, pazymys):
        """Prideda naują pažymį prie studento sąrašo"""
        if 1 <= pazymys <= 10:
            self.pazymiai.append(pazymys)
        else:
            print("⚠️ Pažymys turi būti nuo 1 iki 10!")

    def vidurkis(self):
        """Apskaičiuoja studento pažymių vidurkį"""
        if self.pazymiai:
            return round(sum(self.pazymiai) / len(self.pazymiai), 2)
        return 0

    def ar_praejo(self):
        """Patikrina, ar studentas išlaikė mokslus pagal vidurkį"""
        if self.vidurkis() >= 4:
            return True
        return False

    def parodyti_pazymius(self):
        """Išveda visus studento pažymius naudojant ciklą"""
        if not self.pazymiai:
            print(f"{self.vardas} dar neturi pažymių.")
        else:
            print(f"{self.vardas} pažymiai:")
            for pazymys in self.pazymiai:
                print(" -", pazymys)

    # PRIDĖTA: Tikrina ar studentas turi neigiamų pažymių
    def ar_turi_neigiamu(self):
        """Tikrina ar studentas turi pažymių žemesnių už 4"""
        for pazymys in self.pazymiai:  # CIKLAS - einame per pažymius
            if pazymys < 4:            # SĄLYGA - jei pažymys mažesnis už 4
                return True
        return False

    def __str__(self):
        statusas = "mokosi" if self.istojes else "baigęs"
        return f"{self.vardas}, {self.klase} — {statusas}, vidurkis: {self.vidurkis()}"


# ==== Objekto kūrimo pavyzdžiai ====

s1 = Student("Aistė", "10A")
s2 = Student("Mantas", "12B", pazymiai=[8, 9, 7])
s3 = Student("Tomas", "9C", pazymiai=[10, 3, 5])  # Pridedam dar vieną studentą

# Pridedami keli pažymiai naudojant CIKLĄ
for p in [10, 9, 8, 2]:   # CIKLAS
    s1.prideti_pazymi(p)

# PRIDĖTA: Papildomas ciklas
print("Studentų pažymiai:")
for studentas in [s1, s2, s3]:  # CIKLAS - per visus studentus
    studentas.parodyti_pazymius()

# PRIDĖTA: Papildomas sąlygos tikrinimas
print("\nAr turi neigiamų pažymių?")
for studentas in [s1, s2, s3]:  # CIKLAS
    if studentas.ar_turi_neigiamu():  # SĄLYGA
        print(f"{studentas.vardas} - TAIP, turi neigiamų pažymių")
    else:
        print(f"{studentas.vardas} - NE, neturi neigiamų pažymių")

# Tikriname ar išlaikė mokslus
print("\nAr išlaikė mokslus?")
for student in [s1, s2, s3]:
    if student.ar_praejo():
        print(f"✅ {student.vardas} išlaikė mokslus.")
    else:
        print(f"❌ {student.vardas} neišlaikė mokslų.")
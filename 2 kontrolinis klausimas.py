# Antras kontrolinis klausimas. Kontrolinis darbas (kitai savaitei, po teorinės paskaitos). 
# Kaip objektas(objektai) yra susiję su klase(klasėmis). Atsakant į klausimą reiktų aiškinti apie klasės struktūrą(šabloną),
# galite remtis savo arba mano praktiniais pavyzdžiais

""" Atsakymas:
Objektas yra konkretus klasės egzempliorius. Klasė yra šablonas, o objektas yra pagal tą šabloną sukurtas konkretus "daiktas".
Objektas yra tiesiogiai susijęs su klase, nes jis yra sukurtas pagal tos klasės aprašą. Jis paveldi visą struktūrą (kokias savybes ir metodus turėti),
bet įgyja konkrečias, unikalias reikšmes. Be klasės apibrėžimo, objekto sukurti neįmanoma."""

# Kas yra klasė ir objektas?
"""
Klasė yra šablonas, brėžinys arba receptas. Ji apibrėžia, kokios savybės (duomenys) ir metodai (veiksmai) bus būdingi tam tikrai objektų grupei.
Objektas yra konkreti realizacija pagal klasės šabloną. Tai yra egzempliorius (instance), kuris jau turi konkrečias savybių reikšmes. """

# Kuo skiriasi klasės kintamieji (savybės) nuo metodų?
"""Klasės kintamieji (savybės) yra duomenys, kurie apibūdina objekto būseną arba charakteristikas.
Metodai yra funkcijos, kurios apibrėžia veiksmus arba elgesį, kuriuos objektas gali atlikti."""

# Kam naudojamas metodas __init__?
"""Metodas __init__ yra konstruktorius. Tai ypač svarbus metodas, kuris automatiškai iškviečiamas tik tada, kai kuriamas naujas objektas.
*Inicializuoti objektą.
*Nustatyti pradines objekto savybių reikšmes.
*Priimti argumentus objekto kūrimo metu ir priskirti juos savybėms.
"""

# Kam naudojamas metodas __str__?
""" Metodas __str__ nustato, kaip objektas atrodys, kai jis bus konvertuojamas į eilutę (string). Tai įvyksta, kai naudojate funkcijas print() arba str()."""

# Ką reiškia self.vardas, self.klase, self.istojes?
""" self yra nuoroda į patį objektą. Naudojant self, metodas gali pasiekti to objekto savybes ir kvieti kitus to objekto metodus.
*self.vardas, self.klase, self.istojes yra to objekto savybės.
*self.vardas reiškia: "objekto, kuris šiuo metu naudoja šį metodą, savybė vardas".
*Tai yra būdas išsaugoti duomenis konkrečiame objekte ir vėliau juos pasiekti."""

# Koks skirtumas tarp prideti_pazymi() ir vidurkis() metodų?
"""Abu yra metodai, bet jie atlieka skirtingus veiksmus su objekto būsena (jo duomenimis).
*prideti_pazymi(pazymys) yra modifikavimo metodas. Jis keičia objekto vidinę būseną - papildo sąrašą self.pazymiai nauju duomeniu.
*vidurkis() yra skaičiavimo metodas. Jis nekeičia objekto būsenos, o tik atsiima esamus duomenis (self.pazymiai), atlieka su jais skaičiavimus ir grąžina rezultatą."""

# Ką darys s2.baigti_mokslus()?
"""
Jūsų kode baigti_mokslus() metodas keičia savybės istojes reikšmę į False. Po s2.baigti_mokslus() iškvietimo, s2.istojes tampa False, o print(s2) rodo "baiges" vietoj "mokosi"."""

# Praktinė užduotis. Kintamieji ir metodai
class Student:  
    # Sukuriama klasė "Student", pagal kurią bus kuriami studentų objektai
   
    def __init__(self, vardas, klase, istojes=True, pazymiai=None):
        self.vardas = vardas
        self.klase = klase
        self.istojes = istojes
        self.pazymiai = pazymiai if pazymiai is not None else []
        
        # PRIDĖTI: Paprasti papildomi kintamieji
        self.grupe = None           # Kurioje grupėje mokosi (A, B, C)
        self.telefonas = ""         # Studento telefono numeris

    def prideti_pazymi(self, pazymys):
        """Prideda naują pažymį prie studento sąrašo"""
        if 1 <= pazymys <= 10:
            self.pazymiai.append(pazymys)
        else:
            print("Pažymys turi būti nuo 1 iki 10!")

    def vidurkis(self):
        """Gražina studento pažymių vidurkį"""
        if self.pazymiai:
            return round(sum(self.pazymiai) / len(self.pazymiai), 2)
        return 0

    def baigti_mokslus(self):
        """Studentas baigia mokslus"""
        self.istojes = False

    # PRIDĖTI: Paprastas metodas grupei priskirti
    def priskirti_grupe(self, grupes_raide):
        """Priskiria studentą grupei (A, B, C)"""
        if grupes_raide in ["A", "B", "C"]:
            self.grupe = grupes_raide
            print(f"{self.vardas} priskirtas į {grupes_raide} grupę")
        else:
            print("Grupė gali būti tik A, B arba C")

    # PRIDĖTI: Paprastas metodas telefono numeriui nustatyti
    def nustatyti_telefona(self, numeris):
        """Nustato studento telefono numerį"""
        if len(numeris) >= 8:
            self.telefonas = numeris
            print(f"{self.vardas} telefono numeris: {numeris}")
        else:
            print("Telefono numeris per trumpas")

    def __str__(self):
        statusas = "mokosi" if self.istojes else "baigęs"
        
        # Papildome informacija apie grupę ir telefoną
        grupes_info = f", grupė: {self.grupe}" if self.grupe else ""
        telefono_info = f", tel: {self.telefonas}" if self.telefonas else ""
        
        return f"{self.vardas}, {self.klase} — {statusas}, vidurkis: {self.vidurkis()}{grupes_info}{telefono_info}"


# ==== Objekto kūrimo ir naujų metodų testavimo pavyzdžiai ====

s1 = Student("Aistė", "10A")
s2 = Student("Mantas", "12B", pazymiai=[8, 9, 7])

s1.prideti_pazymi(10)
s1.prideti_pazymi(9)

print("Pradiniai duomenys:")
print(s1)
print(s2)

print("\nPriskiriame grupes:")
s1.priskirti_grupe("A")  # Aistė į A grupę
s2.priskirti_grupe("B")  # Mantas į B grupę
s1.priskirti_grupe("X")  # Neteisinga grupė - klaida

print("\nNustatome telefonus:")
s1.nustatyti_telefona("+37061234567")  # Teisingas numeris
s2.nustatyti_telefona("123")           # Per trumpas numeris - klaida

print("\nGalutinis studentų statusas:")
print(s1)
print(s2)
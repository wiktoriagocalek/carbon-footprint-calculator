class Material:
    def __init__(self, nazwa, masa_kg):
        self.nazwa = nazwa
        self.masa_kg = masa_kg

    def oblicz_slad_weglowy(self):
        return 0

    def __str__(self):
        return f"Nazwa materiału: {self.nazwa}, masa: {self.masa_kg} kg, ślad węglowy: {self.oblicz_slad_weglowy()}"

class Beton(Material):
    def __init__(self, nazwa, masa_kg):
        super().__init__(nazwa, masa_kg)
        self.wspolczynnik_emisji = 0.13

    def oblicz_slad_weglowy(self):
        return self.masa_kg * self.wspolczynnik_emisji

class Stal(Material):
    def __init__(self, nazwa, masa_kg):
        super().__init__(nazwa, masa_kg)
        self.wspolczynnik_emisji = 1.85

    def oblicz_slad_weglowy(self):
        return self.masa_kg * self.wspolczynnik_emisji

class Aluminium(Material):
    def __init__(self, nazwa, masa_kg):
        super().__init__(nazwa, masa_kg)
        self.wspolczynnik_emisji = 8.24

    def oblicz_slad_weglowy(self):
        return self.masa_kg * self.wspolczynnik_emisji

materialy_budowlane = []
typy_materialow = {"beton": Beton, "stal": Stal, "aluminium": Aluminium}

dalej = True
while dalej:
    wybor_material = input("Podaj typ materiału (Beton/Stal/Aluminium) albo 'koniec': ")
    if wybor_material.lower() == "koniec":
        dalej = False
    else:
        wybor_nazwa = input("Podaj nazwę materiału (np. beton z gliwic): ")
        wybor_masa = input("podaj masę materiału: ")
        nowy_material = typy_materialow[wybor_material.lower()](wybor_nazwa, float(wybor_masa))
        materialy_budowlane.append(nowy_material)

suma_slad_weglowy = sum([item.oblicz_slad_weglowy() for item in materialy_budowlane])
najgorsze_materialy = [item.nazwa for item in materialy_budowlane if item.oblicz_slad_weglowy() > 500]
posortowane_materialy = list(sorted(materialy_budowlane, key = lambda item: item.oblicz_slad_weglowy(), reverse = True))

print("Ślad węglowy wszystkich materiałów budowlanych wynosi " + str(suma_slad_weglowy))
print("Do najbardziej emisyjnych materiałów należą: " + str(najgorsze_materialy))
print("Materiały posortowane według emisyjności: ")
for item in posortowane_materialy:
    print(item)



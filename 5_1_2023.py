
# Vytvořte třídu Clovek s atributy pro uchování jména, věku a nálady
# Vytvořte metody pro změnu nálady
# Vytvořte metody pro zobrazení stavu člověka

class Clovek:

    def __init__(self, jmeno : str, vek : int, nalada : str):
        self.jmeno = jmeno
        self.vek = vek
        self.nalada = nalada

    def mej_se_fajn(self):
        self.nalada = "fajn"

    def mej_se_spatne(self):
        self.nalada = "špatně"

    def zobraz_stav(self):
        print(f"jméno: {self.jmeno} věk: {self.vek} nálada: {self.nalada}")


franta = Clovek("franta", 30, "dobře")
franta.zobraz_stav()
franta.mej_se_fajn()
franta.zobraz_stav()
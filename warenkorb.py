"""
Hier wird die Klasse Warenkorb mit ihren Methoden implementiert
"""

# pylint: disable = missing-function-docstring, missing-class-docstring

class Artikel:
    def __init__(self, name, preis=None):
        if preis is None:
            raise ValueError("Artikel ohne Preis sind nicht erlaubt")
        self.name = name
        self.preis = preis

class Warenkorb:
    def __init__(self):
        self.artikel = []
        self.rabattregeln = []

    def add_artikel(self, artikel):
        self.artikel.append(artikel)

    def add_rabattregel(self, rabattregel):
        self.rabattregeln.append(rabattregel)

    def get_summe(self):
        summe = sum(artikel.preis for artikel in self.artikel)
        for rabattregel in self.rabattregeln:
            summe = rabattregel.anwenden(summe)
        return summe

class Rabattregel:
    def __init__(self, rabatt):
        self.rabatt = rabatt

    def anwenden(self, summe):
        return summe * (1 - self.rabatt)

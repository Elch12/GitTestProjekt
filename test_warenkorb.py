
"""
Test für die Klasse Warenkorb werden hier implementiert
"""

# pylint: disable= redefined-outer-name, missing-function-docstring

import pytest
from warenkorb import Warenkorb, Artikel, Rabattregel

def test_artikel_preis():
    artikel = Artikel("Beispielartikel", 10.0)
    assert artikel.preis == 10.0

def test_warenkorb_hinzufuegen():
    warenkorb = Warenkorb()
    artikel = Artikel("Beispielartikel", 10.0)
    warenkorb.add_artikel(artikel)
    assert len(warenkorb.artikel) == 1

def test_warenkorb_summe_berechnen():
    warenkorb = Warenkorb()
    artikel1 = Artikel("Artikel1", 10.0)
    artikel2 = Artikel("Artikel2", 20.0)
    warenkorb.add_artikel(artikel1)
    warenkorb.add_artikel(artikel2)
    assert warenkorb.get_summe() == 30.0

def test_warenkorb_rabatt_anwenden():
    warenkorb = Warenkorb()
    artikel1 = Artikel("Artikel1", 10.0)
    artikel2 = Artikel("Artikel2", 20.0)
    warenkorb.add_artikel(artikel1)
    warenkorb.add_artikel(artikel2)

    rabattregel = Rabattregel(0.1)  # 10% Rabatt
    warenkorb.add_rabattregel(rabattregel)

    assert warenkorb.get_summe() == 27.0  # 10% Rabatt auf die Summe

def test_ausnahme_bei_artikel_ohne_preis():
    with pytest.raises(ValueError, match="Artikel ohne Preis sind nicht erlaubt"):
        artikel = Artikel("ArtikelOhnePreis")
        # Hier sollte eine ValueError-Ausnahme ausgelöst werden

# Weitere Tests für spezifischere Szenarien könnten hinzugefügt werden.

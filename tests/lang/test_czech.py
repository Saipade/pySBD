# -*- coding: utf-8 -*-
import pytest

GOLDEN_CZ_RULES_TEST_CASES = [
    ("Ahoj Světe. Jmenuji se Jonas.", [
        "Ahoj Světe.", 
        "Jmenuji se Jonas."]),
    ("Jak se jmenuješ? Jmenuji se Jonas.", [
        "Jak se jmenuješ", 
        "Jmenuji se Jonas."]),
    ("Tady to je! Našel jsem to.", ["Tady to je!",  "Našel jsem to."]),
    ("Jmenuji se Jonas E. Smith.", ["Jmenuji se Jonas E. Smith."]),
    ("Obraťte se prosím na s. 55.", ["Obraťte se prosím na s. 55."]),
    ("Byli Jane a spol. na večírku?", ["Byli Jane a spol. na večírku?"]),
    ("Uzavřeli dohodu s Pittem, Briggs & Co. v poledne.", ["Uzavřeli dohodu s Pittem, Briggs & Co. v poledne."]),
    ("Zeptáme se Jane a spol. Měli by to vědět.", [
        "Zeptáme se Jane a spol.", 
        "Měli by to vědět."]),
    ("Uzavřeli dohodu s Pittem, Briggs & Co. Včera to skončilo.", [
        "Uzavřeli dohodu s Pittem, Briggs & Co.", 
        "Včera to skončilo."])
]

@pytest.mark.parametrize('text,exptected_sents', GOLDEN_CZ_RULES_TEST_CASES)
def test_cz_sbd(cz_default_fixture, text, exptected_sents):
    """Czech language SBD tests"""
    segments = cz_default_fixture.segment(text)
    segments = [s.strip() for s in segments]
    assert segments == exptected_sents

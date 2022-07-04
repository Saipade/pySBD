# -*- coding: utf-8 -*-
import pytest

GOLDEN_PT_RULES_TEST_CASES = [
    
]

@pytest.mark.parametrize('text,exptected_sents', GOLDEN_PT_RULES_TEST_CASES)
def test_pt_sbd(pt_default_fixture, text, exptected_sents):
    """Portuguese language SBD tests"""
    segments = pt_default_fixture.segment(text)
    segments = [s.strip() for s in segments]
    assert segments == exptected_sents

from pubmedfetcher.fetcher import is_non_academic

def test_is_non_academic():
    assert is_non_academic("BioPharmaceuticals R&D, AstraZeneca") is True
    assert is_non_academic("Department of Surgery, Harvard Medical School") is False
    assert is_non_academic("Oncology R&D, Novartis") is True

from funcoes import email_valido, dividir

def test_email_valido():
    assert email_valido('exemplo@dominio.com') is True
    assert email_valido('exemplo.com') is False

def test_dividir():
    assert dividir(5, 0) is None
    assert dividir(4, 2) == 2
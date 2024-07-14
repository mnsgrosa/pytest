import pytest
from fatorial import fatorial

@pytest.mark.parametrize('n, esperado', [(1, 1), (0, 1), (5, 120), (6, 720)])
def test_fatorial(n, esperado):
    assert fatorial(n) == esperado


# @pytest.mark.parametrize('n', [-1, -2, -10])
# def test_fatorial_falha(n, esperado):
#     with pytest.raises(RecursionError):
#         fatorial(n)

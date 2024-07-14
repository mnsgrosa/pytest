import pytest
from classificacao import classifica_idade

@pytest.mark.parametrize('idade, categoria_esperada', [(10, 'crianca'), (12, 'adolescente'), (25, 'adulto'), (67, 'idoso')])
def test_classificacao(idade, categoria_esperada):
    assert classifica_idade(idade) == categoria_esperada
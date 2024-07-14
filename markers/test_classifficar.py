import pytest
from classificar_idade import classifica_idade

@pytest.mark.crianca
@pytest.mark.parametrize('idade, classificacao', [(10, 'crianca'), (8, 'crianca')])
def test_crianca(idade, classificacao):
    assert classifica_idade(idade) == classificacao

@pytest.mark.adolescente
@pytest.mark.parametrize('idade, classificacao', [(15, 'adolescente'), (17, 'adolescente')])
def test_adolescente(idade, classificacao):
    assert classifica_idade(idade) == classificacao

@pytest.mark.adulto
@pytest.mark.parametrize('idade, classificacao', [(21, 'adulto'), (37, 'adulto')])
def test_adolescente(idade, classificacao):
    assert classifica_idade(idade) == classificacao

@pytest.mark.idoso
@pytest.mark.parametrize('idade, classificacao', [(69, 'idoso'), (72, 'idoso')])
def test_adolescente(idade, classificacao):
    assert classifica_idade(idade) == classificacao
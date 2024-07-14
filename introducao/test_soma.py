import pytest
from typing import Union


def soma(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y

def soma_lista(x: list[Union[int, float]]):
    return sum(x)

def test_soma():
    assert soma(5, 3) == 8
    
def test_soma_lista():
    assert soma_lista([3, 4.5, 2]) == 9.5

import pytest
from decorator import pow, square


@pytest.mark.parametrize('a, b, c, answer', [
    (1, 2, 3, -1),
    (2, 1, 5, 16),
    ('Masha', 2, 'Masha', [])
])
def test_decPow(a, b, c, answer):
    @pow(power=a)
    def f3(x, y):
        if isinstance(x, (float, int)) and (y, (float, int)):
            return x - y
        return []
    assert f3(b, c) == answer



@pytest.mark.parametrize('a, b, answer', [
    (1, 2, 4),
    ('Masha', 'Masha', [])
])

def test_decSquare(a, b, answer):
    @square
    def f2(x, y):
        if isinstance(x, (float, int)) and (y, (float, int)):
            return x * y
        return []
    assert f2(a, b) == answer

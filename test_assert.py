import pytest

def test_check():
    var = 10
    assert var == 1
    assert var == 2
    for i in range(20):
        assert var == i

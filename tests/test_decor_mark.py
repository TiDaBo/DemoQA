import pytest


@pytest.mark.smoke
def test_decor_mark_1():
    assert True

@pytest.mark.regress
def test_decor_mark_2():
    assert True

@pytest.mark.regress
def test_decor_mark_3():
    assert True
@pytest.mark.regress
def test_decor_mark_4():
    assert True
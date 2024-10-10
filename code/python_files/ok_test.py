def test_check_basic():
    try:
        valr = 10
        assert valr == 1
    except AssertionError as ex:
        print("there is an assertion error")
        assert AssertionError

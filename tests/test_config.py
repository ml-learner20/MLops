import pytest

class NotInRange(Exception):
    def __init__(self,message="value is not in range"):
        self.message = message
        super().__init__(self.message)

def test_generic():
    a = 5
    with pytest.raises((NotInRange)):
        if a not in range(10,20):
            raise NotInRange

def test_something():
    a=2
    a=2
    assert True


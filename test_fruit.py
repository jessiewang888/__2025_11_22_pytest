import pytest
import random


@pytest.fixture
def random_small_int() -> int:
    return random.randint(0, 9999999999)
    ...

def test_big_int_bigger_than_small_int(random_small_int: int):
    BIG_INT = 9999999999

    assert BIG_INT > random_small_int
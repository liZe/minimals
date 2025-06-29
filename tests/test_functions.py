import pytest

from minimals import functions


@pytest.mark.parametrize("name", ("pykachu", "bulpyzarre"))
def test_hello(name):
    result = functions.hello(name)
    assert name in result
    assert "Hello" in result

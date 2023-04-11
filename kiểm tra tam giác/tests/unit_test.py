import pytest
from src.is_triangle import is_triangle
from unittest.mock import patch
import os

@pytest.mark.parametrize(
    "input,output",
    [
        ((3, 2, 1), False),
        ((1, 2, 3), False),
        ((1, 3, 2), False),
        ((4, 2, 5), True),
        ],
 )
def test_is_triangle(input, output):
    assert is_triangle(*input) == output
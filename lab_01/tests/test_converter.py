import subprocess
import sys

import pytest

from toolkit.converter import *
from toolkit.errors import *

def test_priority():
    assert convert(1000, "mm", 'm') == 1
    assert convert(1.5, "kg", 'g') == 1500
    assert convert(-273.15, "c", 'k') == 0


def test_unknown_unit():
    with pytest.raises(UnknownUnit):
        convert(123.16, "n", 'k')


def test_incompatible_units():
    with pytest.raises(IncompatibleUnits):
        convert(123.16, "kg", 'k')


def test_below_absolute_zero():
    with pytest.raises(BelowAbsoluteZero):
        convert(-1, "k", 'f')



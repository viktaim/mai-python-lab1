import subprocess
import sys

import pytest

from toolkit.converter import *
from toolkit.errors import *


def test_cli_success():
    result = subprocess.run(
        [sys.executable, "-m", "toolkit", "calc", "2+3*4"],
        capture_output=True, text=True,
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "14.0"


def test_cli_error():
    result = subprocess.run(
        [sys.executable, "-m", "toolkit", "calc", "10/0"],
        capture_output=True, text=True,
    )
    assert result.returncode == 2
    assert result.stderr.strip() != ""


def test_cli_success():
    result = subprocess.run(
        [sys.executable, "-m", "toolkit", "calc", "2+3*4"],
        capture_output=True, text=True,
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "14.0"
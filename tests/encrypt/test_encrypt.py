""" a"""
import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    """ a"""

    # Test for even key
    assert encrypt_message("message", 4) == "ega_ssem"

    # Test for odd key
    assert encrypt_message("message", 3) == "sem_egas"

    # Test for invalid key
    assert encrypt_message("message", -2) == "egassem"

    # Test for incorrect input type
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(5, 3)

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("trybe", 3.9)

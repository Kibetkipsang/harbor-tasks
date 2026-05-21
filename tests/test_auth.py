
import sys
import os


sys.path.append(os.path.abspath("environment/app"))

from auth import generate_token, verify_token


def test_token_valid():
    token = generate_token("alice")
    payload = verify_token(token)
    assert payload["username"] == "alice"


def test_multiple_validations():
    token = generate_token("bob")

    for _ in range(5):
        payload = verify_token(token)
        assert payload["username"] == "bob"


def test_token_structure():
    token = generate_token("charlie")
    assert isinstance(token, str)


def test_payload_contains_username():
    token = generate_token("david")
    payload = verify_token(token)
    assert "username" in payload


def test_consistency():
    token = generate_token("eve")
    p1 = verify_token(token)
    p2 = verify_token(token)
    assert p1 == p2
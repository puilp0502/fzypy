import pytest
from fzy import search, match_bytes, match, Choice


@pytest.fixture
def entries():
    entries = [
        "src/choices.c",
        "src/choices.h",
        "src/match.c",
        "src/match.h",
    ]
    return entries


def test_search(entries):
    search_result = search("s/c.c", entries)
    assert search_result == [
        ("src/choices.c", 2.82),
        ("src/match.c", 1.8399999999999999),
    ]


def test_choice_object(entries):
    choicer = Choice()
    for entry in entries:
        choicer.add(entry)

    search_result = choicer.search("s/c.c")
    assert search_result == [
        ("src/choices.c", 2.82),
        ("src/match.c", 1.8399999999999999),
    ]


def test_match():
    assert match("s/c", "src/choices.c") == 1.8400000000000007
    assert match_bytes(b"s/c", b"src/choices.c") == 1.8400000000000007

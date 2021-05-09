"""An utility module that provides simple search method.

This module provides a thin wrapper around the underlying
fzy.choices module. This module is provided only for user convenience;
users are encouraged to used fzy.choices module directly.
"""
from fzy import choices


def search(candidates, search):
    """Fuzzy search from provided `candidates` with query `search`.
    :param candidates: list (or iterable) of candidate strings
    :param search: search query
    :return: list of (candidate, score) tuples
    """
    choicer = choices.Choice()
    for candidate in candidates:
        choicer.add(candidate)
    return choicer.search(search)

"""An utility module that provides simple search method.

This module provides a thin wrapper around the underlying
fzy.choices module. This module is provided only for user convenience;
users are encouraged to used fzy.choices module directly.
"""
from fzy import choices


def search(search, candidates):
    """Fuzzy search from provided `candidates` with query `search`.
    :param search: search query
    :param candidates: list (or iterable) of candidate strings
    :return: list of (candidate, score) tuples
    """
    choicer = choices.Choice()
    for candidate in candidates:
        choicer.add(candidate)
    return choicer.search(search)

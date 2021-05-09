# distutils: sources = fzy/src/match.c
# distutils: include_dirs = fzy/src/

cimport fzy_match
import math


def match_bytes(const char* search, const char* candidate):
    """
    :param search: search query in utf-8 encoded bytes
    :param candidate: candidate string in utf-8 encoded bytes
    :return: similarity score.
    """
    if fzy_match.has_match(search, candidate):
        return fzy_match.match(search, candidate)
    else:
        return -1 * math.inf

def match(search, candidate):
    """Calculate similarity score between search query and candidate.
    :param search: search query in str
    :param candidate: candidate string in str
    :return: similarity score.
    """
    if not isinstance(search, str) or not isinstance(candidate, str):
        raise TypeError(
            "expected (str, str), got ({}, {})".format(type(search), type(candidate))
        )
    return match_bytes(search.encode("utf-8"), candidate.encode("utf-8"))
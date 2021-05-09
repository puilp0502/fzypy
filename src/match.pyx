# distutils: sources = fzy/src/match.c
# distutils: include_dirs = fzy/src/

cimport fzy_match
import math


def match(const char* search, const char* candidate):
    if fzy_match.has_match(search, candidate):
        return fzy_match.match(search, candidate)
    else:
        return -1* math.inf

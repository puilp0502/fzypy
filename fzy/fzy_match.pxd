cdef extern from "fzy/src/match.h":
    ctypedef double score_t
    bint has_match(const char *needle, const char *haystack);
    score_t match(const char *needle, const char *haystack);

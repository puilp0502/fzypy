from fzy_match cimport score_t
from fzy_options cimport options_t

cdef extern from "choices.h":
    cdef struct scored_result:
        pass
    ctypedef struct choices_t:
        pass
    void choices_init(choices_t *c, options_t *options)
    void choices_destroy(choices_t *c)
    void choices_add(choices_t *c, const char *choice)
    size_t choices_available(choices_t *c)
    void choices_search(choices_t *c, const char *search)
    const char *choices_get(choices_t *c, size_t n)
    score_t choices_getscore(choices_t *c, size_t n)
    void choices_prev(choices_t *c)
    void choices_next(choices_t *c)

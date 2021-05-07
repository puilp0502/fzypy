# distutils: sources = fzy/src/choices.c fzy/src/options.c fzy/src/match.c
# distutils: include_dirs = fzy/src/

from libc.stdlib cimport malloc
cimport fzy_choices
cimport fzy_options

cdef class Choice:
    cdef fzy_choices.choices_t _choices_t
    cdef fzy_options.options_t _options_t

    def __cinit__(self):
        pass
    
    def __init__(self):
        fzy_options.options_init(&self._options_t)
        fzy_choices.choices_init(&self._choices_t, &self._options_t)

    def __dealloc__(self):
        fzy_choices.choices_destroy(&self._choices_t)

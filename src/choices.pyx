# distutils: sources = fzy/src/choices.c fzy/src/options.c fzy/src/match.c
# distutils: include_dirs = fzy/src/

cimport fzy_choices
cimport fzy_options


cdef class Choice:
    cdef fzy_choices.choices_t _choices_t
    cdef fzy_options.options_t _options_t
    cdef list _strings

    def __cinit__(self):
        pass
    
    def __init__(self):
        fzy_options.options_init(&self._options_t)
        fzy_choices.choices_init(&self._choices_t, &self._options_t)
        self._strings = []

    def _add(self, const char* choice):
        fzy_choices.choices_add(&self._choices_t, choice)

    def _search(self, const char* search):
        fzy_choices.choices_search(&self._choices_t, search)

    def _get_results(self):
        results = []
        cdef size_t i = 0
        cdef size_t choices_available = 0
        choices_available = fzy_choices.choices_available(&self._choices_t)
        while i < choices_available:
            results.append((
                fzy_choices.choices_get(&self._choices_t, i),
                fzy_choices.choices_getscore(&self._choices_t, i)
            ))
            i += 1
        return results

    def add(self, choice):
        if not isinstance(choice, str):
            raise TypeError("expected str, got {}".format(type(choice)))
        encoded = choice.encode("utf-8")
        self._strings.append(encoded)  # Increase refcount to prevent GC
        self._add(encoded)

    def search(self, search):
        if not isinstance(search, str):
            raise TypeError("expected str, got {}".format(type(search)))
        self._search(search.encode("utf-8"))
        results = self._get_results()
        decoded_results = [(v[0].decode("utf-8"), v[1]) for v in results]
        return decoded_results

    def __dealloc__(self):
        fzy_choices.choices_destroy(&self._choices_t)

cdef extern from "options.h":
    ctypedef struct options_t:
        int benchmark
        const char *filter
        const char *init_search
        const char *tty_filename
        int show_scores
        unsigned int num_lines
        unsigned int scrolloff
        const char *prompt
        unsigned int workers
        char input_delimiter
        int show_info

    void options_init(options_t *options)
    void options_parse(options_t *options, int argc, char *argv[])
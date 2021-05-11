from fzy import search


def test_korean():
    assert search("국장사업", ["국가 장학금 지급 사업", "한국장학재단"]) == [
        ("국가 장학금 지급 사업", 8.820000000000004),
    ]


def test_french():
    # This was in fzy's test set for segfault regression
    test_string = "Edmund Husserl - Méditations cartésiennes - Introduction a la phénoménologie.pdf"
    assert search("e", [test_string]) == [(test_string, 0.48499999999999965)]

import psutil
from fzy import Choice


def test_large_input():
    c = Choice()
    for i in range(100000):
        c.add(str(i))
    results = c.search("12")
    # Must match `seq 0 99999 | grep '.*1.*2.*' | wc -l`
    assert len(results) == 8146


def test_repeated_run():
    proc = psutil.Process()  # self
    iter_count = 50
    test_large_input()
    t1_mem_usage = proc.memory_info().rss
    for _ in range(iter_count):
        test_large_input()
    t2_mem_usage = proc.memory_info().rss
    assert (
        t2_mem_usage <= 2 * t1_mem_usage
    ), "Memory usage increased more than 2 times after {} iterations".format(iter_count)

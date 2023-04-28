from src.pre_built.counter import count_ocurrences

path = "data/jobs.csv"
word_jobs = "jobs"
word_python = "python"


def test_counter():
    assert count_ocurrences(path, word_jobs) == 306
    assert count_ocurrences(path, word_python) == 1639

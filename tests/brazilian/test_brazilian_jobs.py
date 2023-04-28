from src.pre_built.brazilian_jobs import read_brazilian_file

path = "tests/mocks/brazilians_jobs.csv"


def test_brazilian_jobs():
    for key_words in read_brazilian_file(path):
        assert "title" in key_words
        assert "salary" in key_words
        assert "type" in key_words

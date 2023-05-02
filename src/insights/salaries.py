from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)
    return max([
        int(max_salary["max_salary"])
        for max_salary in jobs
        if max_salary["max_salary"].isdigit()
    ])


def get_min_salary(path: str) -> int:
    jobs = read(path)
    return min([
        int(min_salary["min_salary"])
        for min_salary in jobs
        if min_salary["min_salary"].isdigit()
    ])


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        if (
            "min_salary" and "max_salary" not in job
            or type(
                job["min_salary"] and job["max_salary"] and salary)
                is not int and not str
            or int(job["min_salary"]) > int(job["max_salary"])
        ):
            raise bool
        return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])
    except (ValueError, KeyError, TypeError):
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError

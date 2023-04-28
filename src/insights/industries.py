from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs = read(path)
    set_industry = set()
    for industry in jobs:
        if industry["industry"] != "":
            set_industry.add(industry["industry"])
    return set_industry


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [indust for indust in jobs if indust["industry"] == industry]

from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    jobs_types = set()
    for job in jobs_list:
        jobs_types.add(job["job_type"])
    return jobs_types


def filter_by_job_type(jobs, job_type):
    jobs_filtered = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_filtered.append(job)
    return jobs_filtered


def get_unique_industries(path):
    jobs_list = read(path)
    industries = set()
    for job in jobs_list:
        if job["industry"] != "":
            industries.add(job["industry"])
    return industries


def filter_by_industry(jobs, industry):
    jobs_filtered = []
    for job in jobs:
        if job["industry"] == industry:
            jobs_filtered.append(job)
    return jobs_filtered


def get_max_salary(path):
    jobs_list = read(path)
    salaries = set()
    for job in jobs_list:
        if job["max_salary"].isnumeric():
            salaries.add(int(job["max_salary"]))
    return max(salaries)


def get_min_salary(path):
    jobs_list = read(path)
    salaries = set()
    for job in jobs_list:
        if job["min_salary"].isnumeric():
            salaries.add(int(job["min_salary"]))
    return min(salaries)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Não foi encontrado o salário mínimo ou o salário máximo")
    elif type(job["min_salary"]) != int or type(job["max_salary"]) != int or type(salary) != int:
        raise ValueError("Valores não são inteiros")
    elif(job["max_salary"] < job["min_salary"]):
        raise ValueError("o min_salary é maior que o max_salary")

    if job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else: 
        return False


def filter_by_salary_range(jobs, salary):
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
    return []

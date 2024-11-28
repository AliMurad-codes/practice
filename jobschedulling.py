class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit


def job_scheduling(jobs, max_slots):
    jobs.sort(key=lambda x: x.profit, reverse=True)

    result = [None] * max_slots
    slot = [False] * max_slots

    for job in jobs:
        for j in range(min(max_slots - 1, job.deadline - 1), -1, -1):
            if not slot[j]:
                slot[j] = True
                result[j] = job.job_id
                break

    return [job_id for job_id in result if job_id is not None]

jobs = [
    Job('Job1', 2, 100),
    Job('Job2', 1, 19),
    Job('Job3', 2, 27),
    Job('Job4', 1, 25),
    Job('Job5', 3, 15)
]
max_slots = 5
scheduled_jobs = job_scheduling(jobs, max_slots)
print("Scheduled jobs:", scheduled_jobs)

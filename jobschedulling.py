class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit


def job_scheduling(jobs, max_slots):
    # Sort jobs based on decreasing order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Initialize result and slot arrays
    result = [None] * max_slots
    slot = [False] * max_slots

    # Iterate through all given jobs
    for job in jobs:
        # Find a free slot for this job (we start from the last possible slot)
        for j in range(min(max_slots - 1, job.deadline - 1), -1, -1):
            if not slot[j]:
                slot[j] = True
                result[j] = job.job_id
                break

    # Filter out None values and return scheduled job ids
    return [job_id for job_id in result if job_id is not None]


# Example usage
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

# Job Scheduler (Python)

This is a simple Python-based job scheduler that allows users to schedule tasks:

- Hourly at a specific minute
- Daily at a specific time
- weekly on a specific day and time

All task outputs are logged into a text file (job_log.txt) instead of printed on the console.

---

## Features

- Schedule multiple jobs in one run
- Menu-based interface (loop) for choosing job type
- Supports:
  - Hourly scheduling (e.g., every hour at :15)
  - Daily scheduling (e.g., every day at 18:00)
  - Weekly scheduling (e.g., every Monday at 09:00)
- Output written to job_log.txt with timestamps

---

##  Requirements

- Python 3.x
- schedule library

Install required package:

```bash
pip install schedule

## How to RUN
python scheduler.py

## Output
Output is saved to job_log.txt like this"

Hello world - 2025-06-05 18:45:03

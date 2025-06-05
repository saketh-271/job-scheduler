import time
import threading
from datetime import datetime
def job(message):
    with open("job_log.txt", "a") as f:
        log_message = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n"
        print(log_message.strip())
        f.write(log_message)
def hourly_job(minute, message):
    while True:
        now = datetime.now()
        if now.minute == minute:
            job(message)
            time.sleep(60)
        time.sleep(1)
def daily_job(hour, minute, message):
    while True:
        now = datetime.now()
        if now.hour == hour and now.minute == minute:
            job(message)
            time.sleep(60)
        time.sleep(1)
def weekly_job(day, hour, minute, message):
    day = day.lower()
    while True:
        now = datetime.now()
        if now.strftime("%A").lower() == day and now.hour == hour and now.minute == minute:
            job(message)
            time.sleep(60)
        time.sleep(1)
def main():
    print("Custom Job Scheduler\n")
    threads = []
    while True:
        print("Choose schedule type:")
        print("1. Hourly")
        print("2. Daily")
        print("3. Weekly")
        print("4. Exit")
        choice = input("Enter option number (1/2/3/4): ")
        if choice == "1":
            minute = int(input("Enter minute (0–59): "))
            message = input("Enter job message: ")
            t = threading.Thread(target=hourly_job, args=(minute, message))
            t.start()
            threads.append(t)
            print("Hourly job scheduled!\n")
        elif choice == "2":
            time_str = input("Enter time in HH:MM format(24-hour): ")
            hour, minute = map(int, time_str.split(":"))
            message = input("Enter job message: ")
            t = threading.Thread(target=daily_job, args=(hour, minute, message))
            t.start()
            threads.append(t)
            print("Daily job scheduled!\n")
        elif choice == "3":
            day = input("Enter day : ").strip().lower()
            time_str = input("Enter time in HH:MM format: ")
            hour, minute = map(int, time_str.split(":"))
            message = input("Enter job message: ")
            t = threading.Thread(target=weekly_job, args=(day, hour, minute, message))
            t.start()
            threads.append(t)
            print("Weekly job scheduled!\n")
        elif choice == "4":
            print("Exiting menu... Scheduled jobs will continue running.\n")
            break
        else:
            print("Invalid choice. Try again.\n")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Scheduler stopped manually.")
if __name__ == "__main__":
    main()

import schedule
import time
from datetime import datetime

def job():
    with open("job_log.txt", "a") as file:
        file.write(f"Hello World - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

def schedule_job():
    print("\nChoose schedule type:")
    print("1. Hourly")
    print("2. Daily")
    print("3. Weekly")
    choice = input("Enter option number (1/2/3 or q to quit): ").strip()

    if choice == "1":
        minute = input("Enter minute (0–59): ").strip()
        try:
            minute = int(minute)
            if 0 <= minute <= 59:
                schedule.every().hour.at(f":{minute:02d}").do(job)
                print("Hourly job scheduled.")
            else:
                print("Invalid minute.")
        except:
            print("Invalid input.")
    
    elif choice == "2":
        time_of_day = input("Enter time (HH:MM in 24-hr format): ").strip()
        schedule.every().day.at(time_of_day).do(job)
        print("Daily job scheduled.")

    elif choice == "3":
        day = input("Enter day of week (e.g., monday): ").strip().lower()
        time_of_day = input("Enter time (HH:MM in 24-hr format): ").strip()
        schedule.every()._getattribute_(day).at(time_of_day).do(job)
        print("Weekly job scheduled.")
    
    elif choice.lower() == "q":
        print("Exiting scheduler setup.")
        return False

    else:
        print("Invalid option.")
    
    return True

def main():
    print("=== Job Scheduler ===")
    while True:
        should_continue = schedule_job()
        if not should_continue:
            break

    print("Job(s) scheduled! Logs will be written to job_log.txt")
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nScheduler stopped.")

if __name__ == "__main__":
    main()
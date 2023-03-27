from salary_calculator import calculateMonth

def main():
    # Prompt user for input
    workdays = int(input("Enter the number of workdays: "))
    overtime_hours = int(input("Enter the number of overtime hours: "))
    late_days = int(input("Enter the number of late days: "))

    # Calculate monthly compensation
    monthly_compensation = calculateMonth(workdays, overtime_hours, late_days)

    # Print result
    print(f"The monthly compensation is {monthly_compensation} baht.")

if __name__ == '__main__':
    main()

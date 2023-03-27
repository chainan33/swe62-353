from salary_calculator import calculateMonth

def main():
    # input
    workdays = int(input("Enter the number of workdays: "))
    overtime_hours = int(input("Enter the number of overtime hours: "))
    late_days = int(input("Enter the number of late days: "))

    monthly_compensation = calculateMonth(workdays, overtime_hours, late_days)
    #แสดงผล
    print(f"The monthly compensation is {monthly_compensation} baht.")

if __name__ == '__main__':
    main()
